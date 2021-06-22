#!/bin/python3
import matplotlib.pyplot as plt

#====================================================================================================

def getDataFromFile(fileName):

    crossSections    = []
    crossSectionsUnc = []

    with open(fileName) as f:
        for line in f:
            if line.startswith("#"):
                continue

            strippedLine = line.strip("\n")
            parts   = strippedLine.split(" ")
            xsec    = float(parts[2])
            xsecUnc = float(parts[3])

            crossSections    += [xsec]
            crossSectionsUnc += [xsecUnc]

    return (crossSections, crossSectionsUnc)

#====================================================================================================

def main():
    #FIXME hardcoded, these parameters are not written in txt file from MG
    masses = [100, 200, 300, 400, 500, 600, 700, 800]

    f_Z = "cross_section_top.txt"
    f_W = "cross_section_top.txt"

    crossSections_schan_Z, crossSectionsUnc_schan_Z = getDataFromFile(f_Z)
    crossSections_schan_W, crossSectionsUnc_schan_W = getDataFromFile(f_W)

    # sanity check that all lists have the same length

    lists = [masses]
    lists += [crossSections_schan_Z, crossSectionsUnc_schan_Z]
    lists += [crossSections_schan_W, crossSectionsUnc_schan_W]

    it = iter(lists)
    length = len(next(it))
    if not all(len(l) == length for l in it):
        print("Not all lists have the same dimensions, please check!")
        exit(1)

    # plot
    fig, axis = plt.subplots(figsize = (20, 8))
    plt.errorbar(masses, crossSections_schan_Z, yerr = crossSectionsUnc_schan_Z, c = "b", label="s channel, $Z/\gamma^*$", linestyle = "", marker = 'o')
    plt.errorbar(masses, crossSections_schan_W, yerr = crossSectionsUnc_schan_W, c = "r", label="s channel, $W^{\pm}$", linestyle = "", marker = 'o')

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

#====================================================================================================

if __name__ == "__main__":
    main()
