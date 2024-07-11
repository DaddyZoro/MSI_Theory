# -*- coding: utf-8 -*-
"""

Pipeline for PAPR-MESS MSI code.

@author: Rodger E. Cornell
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

Temperature_list = np.arange(200,700,10).tolist() + np.arange(700,3100,100).tolist() # K
Pressure_list = [[0.1,0.2154,0.4641,1.0,2.154,4.641,10.,65], ['[atm]']] # Torr will be converted into atm internally

channels = ['P1->W1','R1->P1'] # channel-specific rate constants of interest (trans-HONO->NO+OH,NO2+H->NO+OH)

pertubation_percent = 0.1 # percentage of perturbation
pertubation_percent = 0.05 # percentage of perturbation

nominal_MESS_input_path = os.getcwd() + '/hono/'
nominal_MESS_input = 'hono.inp'

model = MSI.PAPR_MESS(nominal_MESS_input_path, nominal_MESS_input,
                                    {'W1_Energy_1': [Temperature_list, Pressure_list, 0.00]},
                                    {'colrel_FactorOne': [Temperature_list, Pressure_list, pertubation_percent],
                                    'colrel_PowerOne': [Temperature_list, Pressure_list, pertubation_percent],
                                     'colrel_Epsilons': [Temperature_list, Pressure_list, pertubation_percent],
                                     'colrel_Sigmas': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'W2a_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    # 'W2a_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'W2a_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'W2b_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    # 'W2b_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'W2b_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'W3_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    # 'W3_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'W3_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B3_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B3_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B3_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    # 'B4_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B4_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B4_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    # 'B5_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B5_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B5_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    # 'B6_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B6_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B6_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    # 'B6_ImaginaryFrequency_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B7_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B7_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    
                                    'W1_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    'W1_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'W1_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],                                                                
                                    'W3_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    'W3_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'W3_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent], 
                                    
                                    'R1_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'R1_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'R1_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                    'P1_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'P1_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'P1_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    
                                    'B1_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'B1_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'B1_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    'B1_ImaginaryFrequency_1': [Temperature_list, Pressure_list, pertubation_percent],

                                    'B2_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'B2_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'B2_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    
                                    'B3_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'B3_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'B3_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    
                                    'B4_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    'B4_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                  'B4_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                    
                                    # 'B9_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B9_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'B9_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                    # 'P1_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'P1_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'P1_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                    # 'P3_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'P3_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'P3_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                    # 'P4_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'P4_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'P4_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                    # 'P5_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'P5_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    # 'P5_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],                                    

                                    },
                                    channels)

# fit rate constants
n_P = 4  # number of pressure polynominals
n_T = 10  # number of temperature polynominals
same_line_result = True
model.Run() # execute PAPR-MESS perturbations
model.fit_Cheb_rates(n_P, n_T, P_min=0.0001, P_max=100.0, T_min=200.0, T_max=3000.0, same_line_result=same_line_result) # fit rate constants into Chebyshev expressions
model.Cheb_sens_coeff(same_line_result=same_line_result) # calculate sensitivity coefficients


# for debugging, fitting rate constants for a given trail
# target_dir = '/home/leil/MSI/PAPR-MESS_calculation/h+ho2=hooh/calculation_5/'
# model.fit_Cheb_rates(n_P, n_T, target_dir=target_dir)
# model.Cheb_sens_coeff()
