# -*- coding: utf-8 -*-
"""

Pipeline for PAPR-MESS MSI code.

@author: Lei Lei
"""

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

temperature_list = np.arange(200,700,10).tolist() + np.arange(700,3100,100).tolist() # K
#pressure_list = [[0.001, 0.01, 0.1, 1., 10.], ['[atm]']] # Torr will be converted into atm internally
pressure_list = [[.1,.5,1,2,3,5], ['[atm]']] # Torr will be converted into atm internally


channels = ['W2->P1', 'W2->P2', 'P1->P2'] # channel-specific rate constants of interest

pertubation_percent = 0.05 # percentage of perturbation
pertubation_percent = 0.1 # percentage of perturbation

nominal_MESS_input_path = os.getcwd() + '/hoco/'
nominal_MESS_input = 'meqz.inp'

model = MSI.PAPR_MESS(nominal_MESS_input_path, nominal_MESS_input,
                                        {'W1_Energy_1':[temperature_list, pressure_list, 0.00]},
                                        {'W1_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         'W1_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                         'W1_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         'W2_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         'W2_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                         'W2_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         'W3_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         'W3_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                         'W3_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         'B1_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         'B1_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                         'B1_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         'B2_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         'B2_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                         'B2_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],
                                         'B2_ImaginaryFrequency_1':[temperature_list, pressure_list, pertubation_percent],

                                         'B3_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         'B3_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                         'B3_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],
                                         'B3_ImaginaryFrequency_1':[temperature_list, pressure_list, pertubation_percent],


                                         'P1_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         'P1_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                         'P1_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         'P2_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         'P2_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                         'P2_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],
                                         'colrel_FactorOne': [temperature_list, pressure_list, pertubation_percent],
                                         'colrel_PowerOne': [temperature_list, pressure_list, pertubation_percent],
                                         'colrel_Epsilons': [temperature_list, pressure_list, pertubation_percent],
                                         'colrel_Sigmas': [temperature_list, pressure_list, pertubation_percent],

                 
                                         },
                                        channels)

# fit rate constants
n_P = 3 # number of pressure polynominals
n_T = 7 # number of temperature polynominals
model.Run() # execute PAPR-MESS perturbations
same_line_result = True
model.fit_Cheb_rates(n_P, n_T, P_min=0.0001, P_max=100, T_min=200, T_max=3000, same_line_result=same_line_result) # fit rate constants into Chebyshev expressions
model.Cheb_sens_coeff(same_line_result=same_line_result) # calculate sensitivity coefficients


# for debugging, fitting rate constants for a given trail
# target_dir = '/home/leil/MSI/PAPR-MESS_calculation/h+ho2=hooh/calculation_5/'
# model.fit_Cheb_rates(n_P, n_T, target_dir=target_dir)
# model.Cheb_sens_coeff()
