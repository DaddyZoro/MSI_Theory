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

temperature_list = np.arange(200,700,10).tolist() + np.arange(700,3100,100).tolist() # K
pressure_list = [[.1,3], ['[atm]']] # Torr, will be converted into atm internally
pertubation_percent = 0.05 # percentage of perturbation
pertubation_percent = 0.01 # percentage of perturbation

channels = ['P1->P2'] # channel-specific rate constants of interest
nominal_MESS_input_path = os.getcwd() + '/ch4+oh/'
nominal_MESS_input = 'ch4oh.inp'

# channels = ['P2->P1'] # channel-specific rate constants of interest
# nominal_MESS_input_path = os.getcwd() + '/h2+o2/excited_state/'
# nominal_MESS_input = 'H2+O2=HO2+H.inp'

model = MSI.PAPR_MESS(nominal_MESS_input_path, nominal_MESS_input,
                                        {'B1_Energy_1':[temperature_list, pressure_list, 0.00]},
                                        {'B1_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                          #'B1_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                          #'B1_SymmetryFactor_1': [temperature_list, pressure_list, pertubation_percent],

                                         # 'B2_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                        #  'B2_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                        #  'B2_SymmetryFactor_1': [temperature_list, pressure_list, pertubation_percent],
                                       #   'B2_ImaginaryFrequency_1': [temperature_list, pressure_list, pertubation_percent],


                                       # 'P1_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                      #  'P1_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                        #'P1_SymmetryFactor_1': [temperature_list, pressure_list, pertubation_percent],

                                       #'P2_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                       #'P2_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                       #'P2_SymmetryFactor_1': [temperature_list, pressure_list, pertubation_percent]
                                       },
                                        channels#, abstraction=True
                                        )

# fit rate constants
model.Run() # execute PAPR-MESS perturbations
# model.fit_Arr_perturbed_rates() # fit rate constants into Chebyshev expressions
# model.Arr_sens_coeff() # calculate sensitivity coefficients

n_P = 1
n_T = 7
same_line_result = True
aggregated_sens = False
model.fit_Cheb_rates(n_P=n_P, n_T=n_T, P_min=0.0001, P_max=10, T_min=200.0, T_max=3000.0, same_line_result=same_line_result)
model.Cheb_sens_coeff(same_line_result=same_line_result, aggregated_sens=aggregated_sens)

# for debugging, fitting rate constants for a given trail
# target_dir = '/home/leil/MSI/PAPR-MESS_calculation/h+ho2=hooh/calculation_5/'
# model.fit_Cheb_rates(n_P, n_T, target_dir=target_dir)
# model.Cheb_sens_coeff()
