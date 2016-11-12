import pickle
from multiprocessing import Pool
from mcmc import Walker
from chi2 import likelihood_func_LambdaCDM, likelihood_func_wCDM
import sys
N_WALKERS = 20


def single_thread_wCDM(p):
    ind = p
    walker = Walker(pars_range=[[0.0, 1.0], [-2.0, 0.5]],
                    likelihood_func=likelihood_func_wCDM,
                    step_box_length=[0.05, 0.2], begin_step=2000)
    pars_on_chains = []
    likelihoods_on_chains = []

    # print("walker {} of wCDM".format(ind), end="\n", file = )

    p, l = walker.begin_walk()
    pars_on_chains.append(p)
    likelihoods_on_chains.append(l)

    print "walker {} finished, saving result".format(ind)

    pickle.dump(pars_on_chains,
                open('wCDM_pars_on_chains_{}.pydata'.format(ind), 'wb'))
    pickle.dump(likelihoods_on_chains,
                open('wCDM_likelihood_on_chains_{}.pydata'.format(ind), 'wb'))

    return


def single_thread_LambdaCDM(p):

    ind = p
    walker = Walker(pars_range=[[-0.5, 2.0], [-0.5, 2.0]],
                    likelihood_func=likelihood_func_LambdaCDM,
                    step_box_length=[0.05, 0.1], begin_step=2000)
    pars_on_chains = []
    likelihoods_on_chains = []

    # print "walker {} of LambdaCDM".format(ind)
    p, l = walker.begin_walk()
    pars_on_chains.append(p)
    likelihoods_on_chains.append(l)
    print "walker {} finished, saving result".format(ind)
    pickle.dump(pars_on_chains,
                open('LambdaCDM_pars_on_chains_{}.pydata'.format(ind), 'wb'))
    pickle.dump(likelihoods_on_chains,
                open('LambdaCDM_likelihood_on_chains_{}.pydata'.format(ind),
                     'wb'))
    return

if __name__ == "__main__":

    try:
        N_WALKERS = int(sys.argv[1])
    except:
        pass

    threads1 = Pool(N_WALKERS)
    threads1.map(single_thread_wCDM, range(N_WALKERS))
    threads1.close()
    threads1.join()

    threads2 = Pool(N_WALKERS)
    threads2.map(single_thread_LambdaCDM, range(N_WALKERS))
    threads2.close()
    threads2.join()

