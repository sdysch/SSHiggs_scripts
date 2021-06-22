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

    f_Z      = "cross_section_top.txt"
    f_W      = "cross_section_top.txt"
    f_VBF_ll = "cross_section_top.txt"
    f_VBF_WW = "cross_section_top.txt"

    crossSections_schan_Z, crossSectionsUnc_schan_Z = getDataFromFile(f_Z)
    crossSections_schan_W, crossSectionsUnc_schan_W = getDataFromFile(f_W)
    crossSections_schan_VBF_ll, crossSectionsUnc_schan_VBF_ll = getDataFromFile(f_VBF_ll)
    crossSections_schan_VBF_WW, crossSectionsUnc_schan_VBF_WW = getDataFromFile(f_VBF_WW)

    # sanity check that all lists have the same length

    lists = [masses]
    lists += [crossSections_schan_Z, crossSectionsUnc_schan_Z]
    lists += [crossSections_schan_W, crossSectionsUnc_schan_W]
    lists += [crossSections_schan_VBF_ll, crossSectionsUnc_schan_VBF_ll]
    lists += [crossSections_schan_VBF_WW, crossSectionsUnc_schan_VBF_WW]

    it = iter(lists)
    length = len(next(it))
    if not all(len(l) == length for l in it):
        print("Not all lists have the same dimensions, please check!")
        exit(1)

    # plot
    fig, axis = plt.subplots(figsize = (20, 8))
    plt.errorbar(masses, crossSections_schan_Z, yerr = crossSectionsUnc_schan_Z, c = "b", label="$pp \\to\ Z/\gamma^* \\to\ H^{++} H^{--}$", linestyle = "", marker = 'o')
    plt.errorbar(masses, crossSections_schan_W, yerr = crossSectionsUnc_schan_W, c = "r", label="$pp \\to\ W^{\pm} \\to\ H^{\pm\pm}H^{\mp}$", linestyle = "", marker = 'o')
    plt.errorbar(masses, crossSections_schan_VBF_ll, yerr = crossSectionsUnc_schan_VBF_ll, c = "g", label="$pp \\to\ H^{\pm\pm}(\\to\ \ell^\pm\ell^\pm$) jj", linestyle = "", marker = 'o')
    plt.errorbar(masses, crossSections_schan_VBF_WW, yerr = crossSectionsUnc_schan_VBF_WW, c = "m", label="$pp \\to\ H^{\pm\pm}(\\to\ W^\pm W^\pm \\to\ \ell^\pm\ell^\pm\\nu_\ell\\nu_\ell$) jj", linestyle = "", marker = 'o')

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
