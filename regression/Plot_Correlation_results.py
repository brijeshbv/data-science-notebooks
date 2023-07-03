
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

Results = np.load("R_(1measurement)_normalized_NoGap[202,202,79].matData_small.csv.npy");
x_total  = 202;
y_total  = 202;

data_IDs = Results[:,:,0];
np.savetxt("Best_IDs.dat", data_IDs);

data_Corr = Results[:,:,1];
np.savetxt("Best_r_value.dat", data_Corr);

# Melanin in living epidermis

data_mel = Results[:,:,4]*100.0;

mel_xy_out_fig_file = "Melanin.png";
mel_xy_out_data_file = "Melanin.dat";

fig_mel = plt.figure(figsize=(8,7));
ax_mel = fig_mel.add_subplot(111);
plot_mel = ax_mel.imshow(data_mel, extent=(0,x_total,0,y_total), cmap='jet');
ax_mel.set_ylabel(r'$Width, \mu m$', fontsize=20);
ax_mel.set_xlabel(r'$Length, \mu m$', fontsize=20);
ax_mel.yaxis.set_ticks_position('left');
ax_mel.xaxis.set_ticks_position('bottom');
ax_mel.tick_params(axis='both',reset=False,which='both',length=8,width=2,labelsize=20);
ax_mel.set_title('Melanin, XY', fontsize=20);
plot_mel.set_clim(vmin=0, vmax=25.0);
cbar_mel = fig_mel.colorbar(plot_mel, fraction=0.046, pad=0.04);
cbar_mel.set_label('Melanin, a.u.',size=20);
cbar_mel.ax.tick_params(labelsize=14) ;
plt.show();
fig_mel.savefig(mel_xy_out_fig_file, bbox_inches='tight');
np.savetxt(mel_xy_out_data_file, data_mel);

# Blood in DBN

data_blood_BlDBN = Results[:,:,9]*100.0;

blood_BlDBN_xy_out_fig_file = "Blood_BlDBN.png";
blood_BlDBN_xy_out_data_file = "Blood_BlDBN.dat";

fig_blood_BlDBN = plt.figure(figsize=(8,7));
ax_blood_BlDBN = fig_blood_BlDBN.add_subplot(111);
plot_blood_BlDBN = ax_blood_BlDBN.imshow(data_blood_BlDBN, extent=(0,x_total,0,y_total), cmap='jet');
ax_blood_BlDBN.set_ylabel(r'$Width, \mu m$', fontsize=20);
ax_blood_BlDBN.set_xlabel(r'$Length, \mu m$', fontsize=20);
ax_blood_BlDBN.yaxis.set_ticks_position('left');
ax_blood_BlDBN.xaxis.set_ticks_position('bottom');
ax_blood_BlDBN.tick_params(axis='both',reset=False,which='both',length=8,width=2,labelsize=20);
ax_blood_BlDBN.set_title('Blood BlDBN, XY', fontsize=20);
plot_blood_BlDBN.set_clim(vmin=0, vmax=50.0);
cbar_blood_BlDBN = fig_blood_BlDBN.colorbar(plot_blood_BlDBN, fraction=0.046, pad=0.04);
cbar_blood_BlDBN.set_label('Blood BlDBN, a.u.',size=20);
cbar_blood_BlDBN.ax.tick_params(labelsize=14) ;
plt.show();
fig_blood_BlDBN.savefig(blood_BlDBN_xy_out_fig_file, bbox_inches='tight');
np.savetxt(blood_BlDBN_xy_out_data_file, data_blood_BlDBN);

# Blood Saturation in DBN

data_blood_BlSDBN = Results[:,:,10];

blood_BlSDBN_xy_out_fig_file = "Blood_BlSDBN.png";
blood_BlSDBN_xy_out_data_file = "Blood_BlSDBN.dat";

fig_blood_BlSDBN = plt.figure(figsize=(8,7));
ax_blood_BlSDBN = fig_blood_BlSDBN.add_subplot(111);
plot_blood_BlSDBN = ax_blood_BlSDBN.imshow(data_blood_BlSDBN, extent=(0,x_total,0,y_total), cmap='jet');
ax_blood_BlSDBN.set_ylabel(r'$Width, \mu m$', fontsize=20);
ax_blood_BlSDBN.set_xlabel(r'$Length, \mu m$', fontsize=20);
ax_blood_BlSDBN.yaxis.set_ticks_position('left');
ax_blood_BlSDBN.xaxis.set_ticks_position('bottom');
ax_blood_BlSDBN.tick_params(axis='both',reset=False,which='both',length=8,width=2,labelsize=20);
ax_blood_BlSDBN.set_title('Oxygen Saturation BlSDBN, XY', fontsize=20);
plot_blood_BlSDBN.set_clim(vmin=0, vmax=1.0);
cbar_blood_BlSDBN = fig_blood_BlSDBN.colorbar(plot_blood_BlSDBN, fraction=0.046, pad=0.04);
cbar_blood_BlSDBN.set_label('Oxygen Saturation BlSDBN, a.u.',size=20);
cbar_blood_BlSDBN.ax.tick_params(labelsize=14) ;
plt.show();
fig_blood_BlSDBN.savefig(blood_BlSDBN_xy_out_fig_file, bbox_inches='tight');
np.savetxt(blood_BlSDBN_xy_out_data_file, data_blood_BlSDBN);