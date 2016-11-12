import numpy as np
from sne_data import redshift, mag_error
from models import models, literature_LambdaCDM_par, literature_wCDM_par

benchmark = False
# use the "benchmark"
if benchmark:
    literature_wCDM_par = [0.3, -1.]

mag_th_func, LambdaCDM_dL, wCDM_dL = [item for item in models()]

delta = 0.000000001

# the fisher matrix is diagonal
LambdaCDM_f11 = 0
LambdaCDM_f12 = 0
LambdaCDM_f13 = 0
LambdaCDM_f22 = 0
LambdaCDM_f23 = 0
LambdaCDM_f33 = 0

wCDM_f11 = 0
wCDM_f12 = 0
wCDM_f13 = 0
wCDM_f22 = 0
wCDM_f23 = 0


for z, mag_e in zip(redshift, mag_error):

    lambdaCDM_mth = mag_th_func(LambdaCDM_dL, literature_LambdaCDM_par, z, 0)
    wCDM_mth = mag_th_func(wCDM_dL, literature_wCDM_par, z, 0)
    # shift the pars a little bit to find the partial derivative

    LambdaCDM_partial1 = delta * literature_LambdaCDM_par[0]
    LambdaCDM_par_partial1 = \
        [literature_LambdaCDM_par[0]+LambdaCDM_partial1,
         literature_LambdaCDM_par[1]]

    LambdaCDM_partial2 = delta * literature_LambdaCDM_par[1]
    LambdaCDM_par_partial2 = \
        [literature_LambdaCDM_par[0],
         literature_LambdaCDM_par[1]+ LambdaCDM_partial2]

    wCDM_partial1 = delta * literature_wCDM_par[0]
    wCDM_par_partial1 = [literature_wCDM_par[0]+wCDM_partial1,
                         literature_wCDM_par[1]]

    wCDM_partial2 = delta * literature_wCDM_par[1]
    wCDM_par_partial2 = [literature_wCDM_par[0],
                         literature_wCDM_par[1]+wCDM_partial2]

    LambdaCDM_partial_m_partial_p1 = \
        (mag_th_func(LambdaCDM_dL, LambdaCDM_par_partial1, z, 0) -
         lambdaCDM_mth) / LambdaCDM_partial1
    LambdaCDM_partial_m_partial_p2 = \
        (mag_th_func(LambdaCDM_dL, LambdaCDM_par_partial2, z, 0) -
         lambdaCDM_mth) / LambdaCDM_partial2

    wCDM_partial_m_partial_p1 = \
        (mag_th_func(wCDM_dL, wCDM_par_partial1, z, 0) - wCDM_mth) \
        / wCDM_partial1
    wCDM_partial_m_partial_p2 = \
        (mag_th_func(wCDM_dL, wCDM_par_partial2, z, 0) - wCDM_mth) \
        / wCDM_partial2

    LambdaCDM_f11 += 1. / mag_e**2 * LambdaCDM_partial_m_partial_p1**2
    LambdaCDM_f12 += 1. / mag_e**2 * LambdaCDM_partial_m_partial_p1 * \
                     LambdaCDM_partial_m_partial_p2
    LambdaCDM_f13 += 1. / mag_e**2 * LambdaCDM_partial_m_partial_p1
    LambdaCDM_f23 += 1. / mag_e ** 2 * LambdaCDM_partial_m_partial_p2
    LambdaCDM_f22 += 1. / mag_e**2 * LambdaCDM_partial_m_partial_p2**2
    LambdaCDM_f33 += 1. / mag_e ** 2

    wCDM_f11 += 1. / mag_e**2 * wCDM_partial_m_partial_p1**2
    wCDM_f12 += 1. / mag_e**2 * wCDM_partial_m_partial_p1 * \
                     wCDM_partial_m_partial_p2
    wCDM_f13 += 1. / mag_e**2 * wCDM_partial_m_partial_p1
    wCDM_f23 += 1. / mag_e**2 * wCDM_partial_m_partial_p2
    wCDM_f22 += 1. / mag_e ** 2 * wCDM_partial_m_partial_p2 ** 2

wCDM_f33 = LambdaCDM_f33
LambdaCDM_F = \
    np.mat([[LambdaCDM_f11, LambdaCDM_f12, LambdaCDM_f13],
            [LambdaCDM_f12, LambdaCDM_f22, LambdaCDM_f23],
           [LambdaCDM_f13, LambdaCDM_f23, LambdaCDM_f33]])

wCDM_F = \
    np.mat([[wCDM_f11, wCDM_f12, wCDM_f13],
            [wCDM_f12, wCDM_f22, wCDM_f23],
           [wCDM_f13, wCDM_f23, wCDM_f33]])

print "------------------the Fisher Matrix:------------------"
print "-----------wCDM-----------"
print wCDM_F
print "inversion:"
print wCDM_F.I
print "\n"
print "--------LambdaCDM---------"
print LambdaCDM_F
print "inversion:"
print LambdaCDM_F.I

#print "-----------Marginalized results: "
# print "LambdaCDM: sigma_{Omaga_M} is larger than %f"% \
#       np.sqrt(LambdaCDM_F.I[0,0])
# print "LambdaCDM: sigma_{Omaga_Lambda} is larger than %f"% \
#       np.sqrt(LambdaCDM_F.I[1,1])
# print "LambdaCDM: sigma_M is larger than %f"% np.sqrt(LambdaCDM_F.I[2,2])
# print "inversion:"
# print wCDM_F.I
#
# print "wCDM: sigma_{Omaga_M} is larger than %f"% np.sqrt(wCDM_F.I[0,0])
# print "wCDM: simga_w is larger than %f"% np.sqrt(wCDM_F.I[1,1])
#
# print "wCDM: simga_M is larger than %f"% np.sqrt(wCDM_F.I[2,2])
# print "\n"
# #print "\n"
# print "-----------Unmarginalized results: "
# # print "LambdaCDM: sigma_{Omaga_M} is larger than %f"%\
# #       np.sqrt(1./LambdaCDM_F[0,0])
# # print "LambdaCDM: sigma_{Omaga_Lambda} is larger than %f"% \
# #       np.sqrt(1./LambdaCDM_F[1,1])
# # print "LambdaCDM: sigma_M is larger than %f"% np.sqrt(1./LambdaCDM_F[2,2])
# # print "\n"
# print "wCDM: sigma_{Omaga_M} is larger than %f"% np.sqrt(1./wCDM_F[0,0])
# print "wCDM: simga_w is larger than %f"% np.sqrt(1./wCDM_F[1,1])
# print "wCDM: simga_M is larger than %f"% np.sqrt(1./wCDM_F[2,2])
#

# wCDM_Omega_M = np.linspace(0, 1., 10)
# wCDM_w = np.linspace(-2, 0, 10)
#
# wCDM_F_fixM = np.mat([[wCDM_f11, wCDM_f12],
#                     [wCDM_f12, wCDM_f22]])
#
# wCDM_F_marM = np.mat([[wCDM_F.I[0,0], float(wCDM_F.I[0,1])],
#                      [wCDM_F.I[1,0], wCDM_F.I[1,1]]]).I
# print wCDM_F_fixM
# print "\n"
# print wCDM_F_marM
