#!/bin/python3
import matplotlib.pyplot as plt

#====================================================================================================

def getDataFromFile(fileName):

    crossSections    = []
    masses           = []
    widths           = []

    with open(fileName) as f:
        for line in f:
            if line.startswith("#"):
                continue

            strippedLine = line.strip("\n")
            parts   = strippedLine.split()
            mass    = float(parts[1])
            # convert to fb
            xsec    = float(parts[2]) * 1000.
            width   = float(parts[3])

            masses           += [mass]
            crossSections    += [xsec]
            widths           += [width]

    return (masses, crossSections, widths)

#====================================================================================================

def main():

    f_Z      = "data/results_schan_ZGamma.txt"
    f_W      = "data/results_schan_W.txt"
    f_VBF_ll = "data/results_VBF_ll.txt"
    f_VBF_WW = "data/results_debug.txt"

    m_schan_Z, xs_schan_Z, w_schan_Z = getDataFromFile(f_Z)
    m_schan_W, xs_schan_W, w_schan_W = getDataFromFile(f_W)
    m_VBF_ll, xs_VBF_ll, w_VBF_ll = getDataFromFile(f_VBF_ll)
    m_VBF_WW, xs_VBF_WW, w_VBF_WW = getDataFromFile(f_VBF_WW)

    # cross section plot
    fig, axis = plt.subplots(figsize = (10, 10))
    plt.plot(m_schan_Z, xs_schan_Z, c = "b", label="$pp \\to\ Z/\gamma^* \\to\ H_L^{++} H_L^{--}$", linestyle = "", marker = 'o')
    plt.plot(m_schan_W, xs_schan_W, c = "r", label="$pp \\to\ W^{\pm} \\to\ H_L^{\pm\pm}H_L^{\mp}$", linestyle = "", marker = 'o')
    plt.plot(m_VBF_ll,  xs_VBF_ll,  c = "g", label="$pp \\to\ H_R^{\pm\pm}(\\to\ \ell^\pm\ell^\pm$) jj", linestyle = "", marker = 'o')
    #plt.plot(m_VBF_WW,  xs_VBF_WW,  c = "m", label="$pp \\to\ H^{\pm\pm}(\\to\ W^\pm W^\pm \\to\ \ell^\pm\ell^\pm\\nu_\ell\\nu_\ell$) jj", linestyle = "", marker = 'o')

    plt.yscale('log')

    #axis.set_xlabel("Cross section [pb]", fontsize = 20)
    axis.set_ylabel("Madgraph cross section [fb]", fontsize = 20)
    axis.set_xlabel("$M(H^{\pm\pm})$ [GeV]", fontsize = 20)

    plt.legend(loc = 'upper right', fontsize = 15)

    tickSize = 14
    for tick in axis.xaxis.get_major_ticks():
        tick.label.set_fontsize(tickSize)

    for tick in axis.yaxis.get_major_ticks():
        tick.label.set_fontsize(tickSize)

    fig.savefig("cross_sections_vs_mass.pdf")

    # width plot
    fig_width, axis_width = plt.subplots(figsize = (10, 10))
    plt.plot(m_schan_Z, w_schan_Z, c = "b", label="$pp \\to\ Z/\gamma^* \\to\ H_L^{++} H_L^{--}$", linestyle = "", marker = 'o')
    plt.plot(m_schan_W, w_schan_W, c = "r", label="$pp \\to\ W^{\pm} \\to\ H_L^{\pm\pm}H_L^{\mp}$", linestyle = "", marker = 'o')
    plt.plot(m_VBF_ll,  w_VBF_ll,  c = "g", label="$pp \\to\ H_R^{\pm\pm}(\\to\ \ell^\pm\ell^\pm$) jj", linestyle = "", marker = 'o')
    #plt.plot(m_VBF_WW,  w_VBF_WW,  c = "m", label="$pp \\to\ H^{\pm\pm}(\\to\ W^\pm W^\pm \\to\ \ell^\pm\ell^\pm\\nu_\ell\\nu_\ell$) jj", linestyle = "", marker = 'o')

    plt.yscale('log')

    axis_width.set_ylabel("$H^{\pm\pm}$ width [GeV]", fontsize = 20)
    axis_width.set_xlabel("$M(H^{\pm\pm})$ [GeV]", fontsize = 20)

    plt.legend(loc = 'upper left', fontsize = 15)

    tickSize = 14
    for tick in axis_width.xaxis.get_major_ticks():
        tick.label.set_fontsize(tickSize)

    for tick in axis_width.yaxis.get_major_ticks():
        tick.label.set_fontsize(tickSize)

    fig_width.savefig("width_vs_mass.pdf")

#====================================================================================================

if __name__ == "__main__":
    main()
