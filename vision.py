import pickle
import numpy as np
# from getdist import plots, MCSamples
from corner import corner

N_WALKERS = 20
tail = 700

pars_on_chains = []
for i in xrange(N_WALKERS):
    try:
        pars_on_chains += pickle.load(
                open('./pydata/LambdaCDM_pars_on_chains_{}.pydata'.format(i)
                     ,'rb'))
    except:
        continue

data = np.array(sum([p[-tail:] for p in pars_on_chains], []))
figure = corner(data,bins=50, smooth=True,
                show_titles=True, levels=(0.68, 0.95, 0.99),
                labels=[r"$\Omega_M$",r"$\Omega_\Lambda$"])
figure.savefig('mcmc_l.pdf')

# names = [r"\Omega_M", r"\Omega_\Lambda"]
# labels = names
#
# samples = MCSamples(samples=data, names = names, labels = labels)
# g = plots.getSubplotPlotter()
# samples.updateSettings({'contours': [0.683, 0.9545, 0.9973]})
# g.settings.num_plot_contours = 3
# g.triangle_plot([samples], filled=True)
# # g.fig.axes[0].plot([0.27, 0.27], [0, 1.5], '--', color="#1F618D")
# # g.fig.axes[1].plot([0.7311, 0.7311], [0, 1.5], '--', color="#1F618D")
#
# # g.fig.axes[0].plot([0.15, 0.15], [0, 1.5], '--', color="#1F618D")
# # g.fig.axes[0].plot([0.39, 0.39], [0, 1.5], '--', color="#1F618D")
# # g.fig.axes[1].plot([0.93, 0.93], [0, 1.5] , '--', color="#1F618D")
# # g.fig.axes[1].plot([0.53, 0.53], [0, 1.5] , '--', color="#1F618D")
# # g.fig.axes[2].text(0.07, 1, r"$\Omega_M=0.27\pm0.12$", fontsize=8)
# # g.fig.axes[2].text(0.07, 0.9, r"$\Omega_\Lambda=0.73\pm0.20$", fontsize=8)
# # g.fig.axes[1].plot([0.53, 0.53], [0, 1.5] , '--', color="#1F618D")
# g.fig.savefig('figure1.png')

pars_on_chains = []
for i in xrange(N_WALKERS):
    try:
        pars_on_chains += (pickle.load(
                open('wCDM_pars_on_chains_{}.pydata'.format(i),'rb')))[-tail:]
    except:
        continue
pars_on_chains = sum([p[-tail:] for p in pars_on_chains], [])

figure = corner(pars_on_chains,bins=50, smooth=True,
                show_titles=True, levels=(0.68, 0.95, 0.99),
                labels=[r"$\Omega_M$",r"$w$"] )
figure.savefig('mcmc_w.pdf')
#
# ndim = 2
# nsamp = len(pars_on_chains)
#
# names = [r"\Omega_M", r"w"]
# labels = names
#
# samples = MCSamples(samples=data,names=names, labels = labels)
# # samples2 = MCSamples(samples=samps2,names = names, labels = labels)
#
# g = plots.getSubplotPlotter()
# samples.updateSettings({'contours': [0.683, 0.954, 0.997]})
# g.settings.num_plot_contours = 3
# g.triangle_plot([samples], filled=True)

# g.fig.axes[0].plot([0.29, 0.29], [0, 1.5], '--', color="#1F618D")
# g.fig.axes[1].plot([-1.02, -1.02], [0, 1.5], '--', color="#1F618D")
# g.fig.axes[2].scatter([0.29], [-1.02], marker='+', color="black")
# g.fig.axes[0].plot([0.18, 0.18], [0, 1.5], '--', color="#1F618D")
# g.fig.axes[0].plot([0.36, 0.36], [0, 1.5], '--', color="#1F618D")
# g.fig.axes[1].plot([-1.3, -1.3], [0, 1.5] , '--', color="#1F618D")
# g.fig.axes[1].plot([-0.81, -0.81], [0, 1.5] , '--', color="#1F618D")
# # g.fig.axes[1].plot([0.53, 0.53], [0, 1.5] , '--', color="#1F618D")
# g.fig.axes[2].text(0., -1.3, r"$\Omega_M=0.29_{-0.11}^{+0.07}$", fontsize=8)
# g.fig.axes[2].text(0., -1.45, r"$w=-1.02^{+0.21}_{-0.28}$", fontsize=8)
# g.fig.savefig('figure2.png')


#
# likelihood_on_chains = []
# pars_on_chains = []
# tail = 200
# for i in xrange(N_WALKERS):
#     try:
#         likelihood_on_chains += (pickle.load(
#                 open('LambdaCDM_likelihood_on_chains_{}.pydata'.format(i),'rb')))
#         pars_on_chains += (pickle.load(
#             open('LambdaCDM_pars_on_chains_{}.pydata'.format(i), 'rb')))
#     except:
#         continue
#
# for lc, pc in [zip(likelihood_on_chains, pars_on_chains)[0]]:
#
#     pc1 = [p[0] for p in pc]
#     pc2 = [p[1] for p in pc]
#
#     lc = np.array(lc)
#     lc = lc - max(lc)
#
#     plt.plot(range(len(pc1)), pc1, color='blue', linewidth=0.5)
#     plt.plot(range(len(pc1)), pc2, color='red', linewidth=0.5)
#
# plt.show()