import numpy as np
from corner import corner
from chi2 import likelihood_func_LambdaCDM, likelihood_func_wCDM

LambdaCDM_Omega_M = np.linspace(0.0, 0.5, 30)
LambdaCDM_Omega_Lambda = np.linspace(0.4, 1.1, 30)
wCDM_Omega_M = np.linspace(0.0, 0.5, 30)
wCDM_w = np.linspace(-1.75, -0.5, 30)


def draw(par1, par2, lf, figurename, range, labels):
    pos = []
    likelihoods = []
    for om in par1:
        for ol in par2:
            pos.append([om, ol])
            likelihoods.append(lf([om, ol]))

    pos = np.array(pos)
    likelihoods = np.exp(np.array(likelihoods) - max(likelihoods))

    figure = corner(pos,bins=30, range=range, weights=likelihoods,
                    show_titles=True, levels=(0.68, 0.95, 0.99),
                    labels=labels )
    figure.savefig(figurename)

draw(LambdaCDM_Omega_M, LambdaCDM_Omega_Lambda,
     likelihood_func_LambdaCDM, "2par_l.pdf", range=[[0.0,0.5],[0.4,1.1]],
     labels=[r"$\Omega_M$", r"$\Omega_\Lambda$"])
draw(wCDM_Omega_M, wCDM_w, likelihood_func_wCDM,
     "2par_w.pdf", range=[[0.0, 0.5],[-1.75, -0.5]],
     labels=[r"$\Omega_M$",r"$w$"])