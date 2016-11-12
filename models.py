"""
    cosmic models: 
    
    mag_th: the relation between lunimosity distance and apparent magnitude
    H0, speed of light, and the absolute magnitude (assuming a constant
     luminosity of SNeIa)
    are all included in the parameter M, which is linear and will be
    marginalized in the fitting process
    
    LambdaCDM_dL: the relation between redshift z and the luminosity distance,
     assuming equation of state parameter w = -1
    
    wCDM_dL: the relation between redshift z and the luminosity distance,
     assuming a flat universe with OmegaM + OmegaLambda = 1
"""
import numpy as np
# from scipy.special import hyp2f1
from scipy.integrate import quad


def models():

    def mag_th(dL_func, p, z, M):
        dL = dL_func(p, z)
        return 5 * np.log10(dL) + M

    yield mag_th

    def LambdaCDM_dL(p, z):

        OmegaM, OmegaLambda = p
        Omegak = 1. - OmegaM - OmegaLambda
        
        # dC: line-of-sight co-moving distance
        dC = quad(lambda x: 1./ np.sqrt(OmegaM*(1.+x)**3 +
                                        Omegak*(1.+x)**2 + OmegaLambda),0, z)[0]

        # dM: transverse co-mving distance
        if Omegak > 0:
            dM = 1./np.sqrt(Omegak) * np.sinh(np.sqrt(Omegak) * dC)
        elif Omegak == 0:
            dM = dC
        else:
            dM = 1./np.sqrt(-Omegak) * np.sin(np.sqrt(-Omegak) * dC)
        
        return dM*(1+z)

    yield LambdaCDM_dL

    def wCDM_dL(p, z):
        # Omegak = 0, w=w0+wa(z/(1+z))
        # OmegaM, w0, wa= p
        OmegaM, w0= p
        # def w(zz):
        # return w0 + wa*(zz/(1.+zz))
        
        OmegaDE = 1. - OmegaM
        # DE_timedependence =
        #  np.exp(quad(lambda zz: 3.*(1+w(zz))/(1.+zz), 0, z)[0])

        dC = quad(lambda x: 1./np.sqrt(OmegaM*(1.+x)**3 +
                                       OmegaDE * (1.+x)**(3.*(1.+w0))), 0, z)[0]
        # def _integrate(om, ol, w, zz):
        #     hy1 = 0.5
        #     hy2 = -1./6/w
        #     hy3 = 1.-1./6/w
        #     hy4 = -ol*(1+zz)**(3*w)/om
        #     form = np.sqrt(om + ol*(1+zz)**(3*w))
        #     return -2*(1+zz)*form/np.sqrt(om)/np.sqrt((1+zz)**3)/form * \
        #            hyp2f1(hy1,hy2,hy3,hy4)
        # dC = _integrate(OmegaM, OmegaDE, w0, z)
        #  - _integrate(OmegaM, OmegaDE, w0, 0)

        return dC*(1+z)
        
    yield wCDM_dL

# the best fitting parameter from Union 2 paper
literature_LambdaCDM_par = [0.282, 0.722]
literature_wCDM_par = [0.281, -1.011]







