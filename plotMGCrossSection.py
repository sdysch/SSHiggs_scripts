#!/bin/python3
import matplotlib.pyplot as plt

# FIXME write parser of html files from MG?
masses = [100, 200, 300, 400, 500, 600, 700, 800]

# in pb
crossSections_schan_Z    = [0.6524, 0.2167, 0.1149, 0.08092, 0.06834, 0.06076, 0.05154, 0.03723]
crossSectionsUnc_schan_Z =  [0.0013, 0.00059, 0.00025, 0.00018,0.00015, 0.00014, 0.00015, 6.4E-05]

crossSections_schan_W = [0.001246, 0.001959, 0.002191, 0.002109, 0.001876, 0.001602, 0.001329, 0.001079]

if (len(crossSections_schan_Z) != len(masses)):
    print("Invalid masses/crossSections dimensions. Please check!")
    exit(1)

if (len(crossSections_schan_W) != len(masses)):
    print("Invalid masses/crossSections dimensions. Please check!")
    exit(1)

# plot!
fig, axis = plt.subplots(figsize = (20, 8))
#plt.plot(masses, crossSections_schan, c = "b", label="s channel", linestyle = "", marker = 'o')
plt.errorbar(masses, crossSections_schan_Z, yerr = crossSectionsUnc_schan_Z, c = "b", label="s channel, $Z/\gamma^*$", linestyle = "", marker = 'o')
plt.plot(masses, crossSections_schan_W, c = "r", label="s channel, $W^{\pm}$", linestyle = "", marker = 'o')

plt.yscale('log')

#axis.set_xlabel("Cross section [pb]", fontsize = 20)
axis.set_ylabel("Madgraph cross section [pb]", fontsize = 20)
axis.set_xlabel("$M(H^{++}_{L})$ [GeV]", fontsize = 20)

plt.legend(loc = 'upper right', fontsize = 15)

tickSize = 14
for tick in axis.xaxis.get_major_ticks():
    tick.label.set_fontsize(tickSize)

for tick in axis.yaxis.get_major_ticks():
    tick.label.set_fontsize(tickSize)

plt.show()
plotSave = "cross_sections_vs_mass.pdf"
fig.savefig(plotSave)
print("Created {plot}".format(plot=plotSave))
