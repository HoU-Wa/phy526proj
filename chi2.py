"""
    the likelihood function of the two models L~exp(-chi2/2)
    
"""
import numpy as np
from models import models

mag_th, LambdaCDM_dL, wCDM_dL = [item for item in models()]


def chi2s():

    global redshift, magnitude, mag_error

    idx = np.array(redshift).argsort()
    redshift = np.array(redshift)[idx]
    magnitude = np.array(magnitude)[idx]
    mag_error = np.array(mag_error)[idx]

    def likelihood_func_LambdaCDM(p):
        OmegaM, OmegaLambda = p
        chi2 = 0.
        # marginalize M

        M = sum(
            np.array([(mag - mag_th(LambdaCDM_dL, [OmegaM, OmegaLambda], z,
                                    0.)) / mag_e ** 2
                      for z, mag, mag_e in zip(redshift, magnitude, mag_error)])
            / sum([1. / mag_e ** 2 for mag_e in mag_error])
        )

        for z, mag, mag_e in zip(redshift, magnitude, mag_error):
            magth = mag_th(LambdaCDM_dL, [OmegaM, OmegaLambda], z, M)
            chi2 += (mag - magth)**2 / mag_e ** 2

        return -chi2 / 2.

    yield likelihood_func_LambdaCDM

    def likelihood_func_wCDM(p):
        OmegaM, w = p
        chi2 = 0.
        # marginalize M
        M = sum(
            np.array([(mag - mag_th(wCDM_dL, [OmegaM, w], z, 0.)) / mag_e ** 2
                      for z, mag, mag_e in zip(redshift, magnitude, mag_error)])
            / sum([1. / mag_e ** 2 for mag_e in mag_error])
        )
        for z, mag, mag_e in zip(redshift, magnitude, mag_error):
            magth = mag_th(wCDM_dL, [OmegaM, w], z, M)
            chi2 += (mag - magth)**2 / mag_e ** 2

        return -chi2 / 2.
    yield likelihood_func_wCDM

likelihood_func_LambdaCDM, likelihood_func_wCDM = [item for item in chi2s()]