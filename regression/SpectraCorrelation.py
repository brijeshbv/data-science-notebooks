
# -*- coding: utf-8 -*-
"""
This file is part of the Hyperspectral GPU-accelerated Monte Carlo model for light transport in scattering medium:

www.lighttransport.net

This source code and examples are licensed under the terms of the BSD 2-clause "Simplified" License, as follows :

Copyright (c) 2010-2022, Alexander Doronin and others
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""

from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import sys

#dataset_path = sys.argv[1];
#folder = sys.argv[2];
#filename = sys.argv[3];

dataset_path = "MC_Modeled_spectra.csv";
folder = "Data_Mike";
filename = "R_(1measurement)_normalized_NoGap[202,202,79].mat";

folder = folder + "/";
data_file_to_load = folder + filename;
Results_file = folder + filename + dataset_path;

def compute_r2(y_true, y_predicted):
    sse = sum((y_true - y_predicted)**2)
    tse = (len(y_true) - 1) * np.var(y_true, ddof=1)
    r2_score = 1 - (sse / tse)
    return r2_score, sse, tse
    
    
# initializing the titles and rows list
fields = []
rows = []
total_rows = 0

with open(dataset_path) as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    
    # extracting field names through first row
    fields = next(csvreader)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(np.array([float(i) for i in row]))
 
    # get total number of rows
    total_rows = csvreader.line_num
    print("Total no. of rows: %d"%(total_rows))
    

# printing the field names
#print('Field names are:' + ', '.join(field for field in fields))
     
lambda_val = np.arange(510, 905, 5);
Hyperspectra_data = loadmat(data_file_to_load)['R1'];
(x_total, y_total, wavelenght) = Hyperspectra_data.shape;
print("Hyperspectral data: x_total", x_total, "y_total", y_total, "wavelenth",wavelenght);

lambda_val_resized = np.arange(510, 720, 10);
Hyperspectra_data_resized = Hyperspectra_data[:,:, 0:42:2]; # Get from 510 to 720 nm with 10nm step size

Results = np.zeros(shape=(x_total,y_total,11));

# fields
dSC_field = 1;
dLE_field = 4;
Mel_field = 5;
Mel_blend_field = 6;
BlPD_field = 11;
BlSPD_field = 12;

H20DBN_field = 25;
BlDBN_field = 26;
BlSDBN_field = 27;

current_pos = 1;
for xpos in range(0, x_total):
    for ypos in range(0, y_total):
        t = time.time()
        spectra_measured = Hyperspectra_data_resized[xpos, ypos,:];

        best_spectra = [];
        best_ID = 1;
        best_r_value = 0;
               
        for row in rows:
            spectra_modelled = row[46:67];
            r_value, sse, tse = compute_r2(spectra_modelled, spectra_measured) # <-- GOOD & FAST!
            if (r_value > best_r_value):
                 best_r_value = r_value;
                 best_spectra = spectra_modelled;
                 best_ID = row[0];
       
        elapsed = time.time() - t;        
        best_ID  = int(best_ID);         
        Results[xpos, ypos, 0] = best_ID;
        Results[xpos, ypos, 1] = best_r_value;

        Results[xpos, ypos, 2] = rows[best_ID][dSC_field];  
        Results[xpos, ypos, 3] = rows[best_ID][dLE_field]; 
        Results[xpos, ypos, 4] = rows[best_ID][Mel_field]; 
        Results[xpos, ypos, 5] = rows[best_ID][Mel_blend_field]; 
        Results[xpos, ypos, 6] = rows[best_ID][BlPD_field]; 
        Results[xpos, ypos, 7] = rows[best_ID][BlSPD_field];
 
        Results[xpos, ypos, 8] = rows[best_ID][H20DBN_field]; 
        Results[xpos, ypos, 9] = rows[best_ID][BlDBN_field]; 
        Results[xpos, ypos, 10] = rows[best_ID][BlSDBN_field]; 

        current_pos +=1;
        total_data_points = x_total*y_total;
        fraction_complete = (current_pos / total_data_points);
        has_been_running_for = elapsed*current_pos / 60;
        total_time = elapsed*total_data_points / 60;
        expected_time = (total_time - has_been_running_for);
        print("Completed fraction: ", fraction_complete, " Total time [min]: ", total_time, " Has been running for [min]: ", has_been_running_for, " Finishing in [min]: ", expected_time);

np.save(Results_file, Results);
print("Results have benn saved!");
