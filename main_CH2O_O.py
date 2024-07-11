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

Temperature_list = np.arange(250,700,10).tolist() + np.arange(700,5000,100).tolist() # K
Pressure_list = [[1.0], ['[atm]']] # Torr will be converted into atm internally

channels = ['P1->P2'] # channel-specific rate constants of interest



pertubation_percent = 0.1 # percentage of perturbation
nominal_MESS_input_path = os.getcwd() + '/K_R3/'
nominal_MESS_input = 'ch2o+o2.inp'
#nominal_MESS_input = 'combined.inp'

#nominal_MESS_input = 'ho2+ho2_Lei.inp'


model = MSI.PAPR_MESS(nominal_MESS_input_path, nominal_MESS_input,
                                    {'B1_Energy_1': [Temperature_list, Pressure_list, 0.00]},
                                    {'P1_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                      'P1_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                      'P1_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                      'P2_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                      'P2_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                      'P2_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],


                                      'B1_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                      'B1_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                      'B1_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                      'B1_HinderRotor_1':[Temperature_list, Pressure_list, pertubation_percent],
                                      'B1_ImaginaryFrequency_1': [Temperature_list, Pressure_list, pertubation_percent],

                                      },
                                     channels, abstraction=True)

# fit rate constants
n_P = 1  # number of pressure polynominals
n_T = 5 # number of temperature polynominals
same_line_result = True
aggregated_sens = False
model.Run() # execute PAPR-MESS perturbations
model.fit_Cheb_rates(n_P, n_T, P_min=0.0001, P_max=10.0, T_min=200.0, T_max=3000.0, same_line_result=same_line_result) # fit rate constants into Chebyshev expressions
model.Cheb_sens_coeff(same_line_result=same_line_result, aggregated_sens=aggregated_sens) # calculate sensitivity coefficients


# for debugging, fitting rate constants for a given trail
# target_dir = '/home/leil/MSI/PAPR-MESS_calculation/h+ho2=hooh/calculation_5/'
# model.fit_Cheb_rates(n_P, n_T, target_dir=target_dir)
# model.Cheb_sens_coeff()
