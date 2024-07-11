# -*- coding: utf-8 -*-

"""



Pipeline for PAPR-MESS MSI code.



@author: Lei Lei

"""



#from tkinter import E

import postprocessor as MSI

import os

import numpy as np



# Initialize MSI.PAPR_MESS:

# -- the first arguement is the file path for the nominal PAPR-MESS input files

# -- the second arguement is the name for the unperturbed (nominal) input file

# -- the third arguement is a dictionary specifying the nominal condition (to allow optimization starting from nonzero perturbations),

#    the value specifies temperature list, pressure list, and nominal perturbation

# -- the fourth arguement is a dictionary with elements specifying the perturbations (sensitivity analysis are based on the nominal conditions defined above),

#    the keys specify names of perturbation runs and values specify temperature, pressure, and perturbation

# -  the fifth arguement is a list indicating the channels of interest



# energies in cm-1



temperature_list = np.arange(300,700,10).tolist() + np.arange(700,3100,100).tolist() # K

# temperature_list = np.arange(200,400,200).tolist() 

#pressure_list = [[0.001, 0.01, 0.1, 1., 10.], ['[atm]']] # Torr will be converted into atm internally
temperature_list = [200,250,300,350,400,450,500,550,600,650]
pressure_list = [[ 1.], ['[atm]']] # Torr will be converted into atm internally



channels = [#'W1->W2a','W1->W2b','W1->W3a','W1->W3b','W1->W4','W1->W5',

            #'W1->P1','W1->P2','W1->P3','W1->P4',

            #'W2a->W2b','W2a->W3a','W2a->W3b','W2a->W4','W2a->W5','W2a->P1','W2a->P2','W2a->P3','W2a->P4',

            # 'W2b->W3a','W2b->W3b','W2b->W4','W2b->W5', 'W2b->P1','W2b->P2','W2b->P3','W2b->P4',

            # 'W3a->W3b','W3a->W4','W3a->W5','W3a->P1','W3a->P2','W3a->P3','W3a->P4',

            # 'W3b->W4','W3b->W5','W3b->P1','W3b->P2','W3b->P3','W3b->P4',

            'P1->P2','P1->P3','P1->P4',

            'P2->P3','P2->P4',

            'P4->P3',] # channel-specific rate constants of interest



pertubation_percent = 0.1 #0.05  # 0.05 # percentage of perturbation

nominal_MESS_input_path = os.getcwd() + '/test_for_rodger/'

nominal_MESS_input = 'nh2no.inp'



model = MSI.PAPR_MESS(nominal_MESS_input_path, nominal_MESS_input,

                                        {'W1_Energy_1':[temperature_list, pressure_list, 0.00]},

                                        {'W1_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],

                                         'W1_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'W1_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                      

                                         # 'W2a_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],

                                         # 'W2a_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'W2a_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'W2b_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],

                                         # 'W2b_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'W2b_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'W3a_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],

                                         # 'W3a_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'W3a_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'W3b_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],

                                         # 'W3b_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'W3b_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],
                                       
                                         # 'B7_NejScale_1':[temperature_list, pressure_list, pertubation_percent],                     #### Nej.dat  VRC-TST

                                         # 'B7_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],

                                         # 'B7_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent], ###should consider the Symmetry Factor or not?

                                         # 'B12_NejScale_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B12_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],

                                         # 'B12_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B13_NejScale_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B13_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],

                                         # 'B13_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B8_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],          #####TST  

                                         # 'B8_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B8_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B8_ImaginaryFrequency_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B9_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],          

                                         # 'B9_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B9_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B9_ImaginaryFrequency_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B10_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],           

                                         # 'B10_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B10_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B10_ImaginaryFrequency_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B11_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],           

                                         # 'B11_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B11_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B11_ImaginaryFrequency_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B16_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],           

                                         # 'B16_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],

                                         # 'B16_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                      #   'B16_ImaginaryFrequency_1':[temperature_list, pressure_list, pertubation_percent], ## End

                                         },

                                        channels)



# fit rate constants

n_P = 1  # number of pressure polynominals

n_T = 8 # number of temperature polynominals

model.Run() # execute PAPR-MESS perturbations

model.fit_Cheb_rates(n_P, n_T, P_min=0.0001, P_max=100, T_min=200, T_max=3000) # fit rate constants into Chebyshev expressions

model.Cheb_sens_coeff() # calculate sensitivity coefficients





# for debugging, fitting rate constants for a given trail

# target_dir = '/home/leil/MSI/PAPR-MESS_calculation/h+ho2=hooh/calculation_5/'

# model.fit_Cheb_rates(n_P, n_T, target_dir=target_dir)

# model.Cheb_sens_coeff()

