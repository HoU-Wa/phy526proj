import numpy as np
import matplotlib.pyplot as plt

from models import literature_LambdaCDM_par, literature_wCDM_par
from chi2 import likelihood_func_LambdaCDM, likelihood_func_wCDM

LambdaCDM_Omega_M = np.linspace(0.1, 0.45, 128)
LambdaCDM_Omega_Lambda = np.linspace(0.5, 1, 128)
wCDM_Omega_M = np.linspace(0.15, 0.4, 128)
wCDM_w = np.linspace(-1.3, -0.7, 128)

fig, axisArr = plt.subplots(2, 2)

ax1, ax2 = axisArr[0]
ax1.set_xlim(0.1, 0.45)
ax2.set_xlim(0.5, 1)
ax3, ax4 = axisArr[1]
ax3.set_xlim(0.15, .4)
ax4.set_xlim(-1.25, -0.8)

data1 = np.array([likelihood_func_LambdaCDM([om, literature_LambdaCDM_par[1]])
                  for om in LambdaCDM_Omega_M])
data2 = np.array([likelihood_func_LambdaCDM([literature_LambdaCDM_par[0], ol])
                  for ol in LambdaCDM_Omega_Lambda])
data3 = np.array([likelihood_func_wCDM([om, literature_wCDM_par[1]])
                  for om in wCDM_Omega_M])
data4 = np.array([likelihood_func_wCDM([literature_wCDM_par[0], w])
                  for w in wCDM_w])

data1 = np.exp(data1 - max(data1))
data2 = np.exp(data2 - max(data2))
data3 = np.exp(data3 - max(data3))
data4 = np.exp(data4 - max(data4))


def region(_ax, data, x):

    ind = data.argsort()
    data = data[ind][::-1]
    x = x[ind][::-1]

    _all = sum(data)
    part = 0.0

    x_best = x[0]
    l1 = []
    l3 = []
    l5 = []
    lll = []
    flag1 = True
    flag2 = True
    for ind, d in enumerate(data):
        part += d
        if (part/_all > 0.683) & flag1:
            l1 = x[ind:ind+3]
            flag1 = False

        if (part/_all > 0.954) & flag2:
            l3 = x[ind:ind+3]
            flag2 = False

        if part/_all > 0.997:
            l5 = x[ind:ind+3]
            break

    for ll in [l1, l3, l5]:
        for _l in ll[1:]:
            if (_l-x_best) * (ll[0]-x_best) < 0:
                lll.append([ll[0], _l])
                break

    for _l in lll:
        _ax.plot([_l[0], _l[0]], [0, 1], 'k--')
        _ax.plot([_l[1], _l[1]], [0, 1], 'k--')

    return lll, x_best


ax1.plot(LambdaCDM_Omega_M, data1, "k")
ax2.plot(LambdaCDM_Omega_Lambda, data2, "k")
ax3.plot(wCDM_Omega_M, data3, "k")
ax4.plot(wCDM_w, data4, "k")

l, x0 = region(ax1, data1, LambdaCDM_Omega_M)
ax1.set_title(r"${\Omega_M=%.2f_{%.2f%.2f}^{+%.2f+%.2f}}"
              r"\ (\Omega_\Lambda=%.2f)$"%
              (x0, min(l[0]-x0), min(l[1]-x0), max(l[0]-x0),
               max(l[1]-x0), literature_LambdaCDM_par[1]))
ax1.set_xticks([0.1, 0.2, 0.3, 0.4])

l, x0 = region(ax2, data2, LambdaCDM_Omega_Lambda)
ax2.set_title(r"${\Omega_\Lambda=%.2f_{%.2f%.2f}^{+%.2f+%.2f}}"
              r"\ (\Omega_M=%.2f)$"%
              (x0, min(l[0]-x0), min(l[1]-x0), max(l[0]-x0),
               max(l[1]-x0), literature_LambdaCDM_par[0]))
l, x0 = region(ax3, data3, wCDM_Omega_M)

ax3.set_title(r"${\Omega_M=%.2f_{%.2f%.2f}^{+%.2f+%.2f}}\ (w=%.2f)$"%
              (x0, min(l[0]-x0), min(l[1]-x0), max(l[0]-x0),
               max(l[1]-x0), literature_wCDM_par[1]))
l, x0 = region(ax4, data4, wCDM_w)

ax4.set_title(r"${w=%.2f_{%.2f%.2f}^{+%.2f+%.2f}}\ (\Omega_M=%.2f)$"%
              (x0, min(l[0]-x0), min(l[1]-x0), max(l[0]-x0),
               max(l[1]-x0), literature_wCDM_par[0]))

for ax in [ax1, ax2,ax3,ax4]:
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
    plt.setp(ax.yaxis.get_majorticklabels(), rotation=45)
plt.subplots_adjust(hspace=.5)

fig.savefig('one_par.pdf')