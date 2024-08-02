from pylab import *

aw = 2 
fs = 18 
lw = 3
font = {'size'   : fs}
matplotlib.rc('font', **font)
matplotlib.rc('axes' , linewidth=aw)
def set_fig_properties(ax_list):
    tl = 8
    tw = 2
    tlm = 4
    for ax in ax_list:
        ax.tick_params(which='major', length=tl, width=tw)
        ax.tick_params(which='minor', length=tlm, width=tw)
        ax.tick_params(which='both', axis='both', direction='out', right=False, top=False)
        
"""
Please check https://gpumd.org/gpumd/output_files/thermo_out.html

If the simulation box is orthogonal, there are 12 columns in this output 
file, each containing the values of a quantity at increasing time points:
    
column   1 2 3 4  5  6  7   8   9   10 11 12
quantity T K U Px Py Pz Pyz Pxz Pxy Lx Ly Lz"""

thermo_raw = np.loadtxt("thermo.out")

lx = thermo_raw[:, 9]
px = thermo_raw[:, 3]
strainx = lx / lx[0] -1 #definition of engineering strain
stressx = px * -1 #unit in GPa

figure(figsize=(10, 6.2))
set_fig_properties([gca()])
plot(strainx, stressx, lw=2)
xlabel(r'Strain')
ylabel(r'Stress (GPa)')
savefig("graphene_tension.png", bbox_inches='tight')