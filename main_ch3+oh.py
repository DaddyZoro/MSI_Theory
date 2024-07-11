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

#temperature_list = np.arange(200,700,10).tolist() + np.arange(700,3100,100).tolist() # K
temperature_list = np.arange(290,700,10).tolist() + np.arange(700,2800,100).tolist() # K

temperature_list = [296,370,407,474,513,539,577,700,810,906,1050,1200,1350,1525,1700,1950,2250,2600,3000] # K



#temperature_list = np.arange(300,700,10).tolist()

pressure_list = [[1,4], ['[atm]']] # Torr will be converted into atm internally

channels = ['W1->R',
            'W1->P1',
            'W1->P2', 'P2->W1',
            'W1->P3' , 'P3->W1',
            'W1->P4',
            'W1->P5',
             'W1-P6',
             'R->P1',
             'R->P2', 'P2->R',
             'R->P3','P3->R',
             'R->P4',
             'R->P5',
             'R->P6',
             'P1->P2', 'P2->P1',
             'P1->P3','P3->P1',
             'P1->P4',
             'P1->P5',
             'P1->P6',
             'P2->P3','P3->P2',
             'P2->P4','P4->P2',
             'P2->P5','P5->P2',
             'P2->P6', 'P6->P2',
             'P3->P4', 'P4->P3',
             'P3->P5', 'P5->P3',
             'P3->P6', 'P6->P3',
             'P4->P5',
             'P4->P6',
             'P5->P6']
            
pertubation_percent = 0.05 # percentage of perturbation
pertubation_percent = 0.1
nominal_MESS_input_path = os.getcwd() + '/Jasper/'
nominal_MESS_input = 'ch3ar.inp'

model = MSI.PAPR_MESS(nominal_MESS_input_path, nominal_MESS_input,
                                        {'W1_Energy_1':[temperature_list, pressure_list, 0.00]},
                                        { 'W1_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                          # 'W1_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                          # 'W1_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],
                                          #'W1_HinderRotor_1':[temperature_list, pressure_list, pertubation_percent],
                                          # 'B1_NejScale_1':[temperature_list, pressure_list, pertubation_percent],
                                          # 'B1_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                          # 'B2_NejScale_1':[temperature_list, pressure_list, pertubation_percent],
                                          # 'B2_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                          # 'B3_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                          # 'B3_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                          # 'B3_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],
                                         # 'B5_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         # 'B5_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                         # 'B5_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],
                                         # # 'B6_NejScale_1':[temperature_list, pressure_list, pertubation_percent],
                                         # # 'B6_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         #'B7_NejScale_1':[temperature_list, pressure_list, pertubation_percent],
                                         #'B7_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         # 'B3_VariationalEnergy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         # 'B3_VariationalFrequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                         # 'B3_ImaginaryFrequency_1':[temperature_list, pressure_list, pertubation_percent],
                                         # 'B4_VariationalEnergy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                         # 'B4_VariationalFrequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                         # 'B4_ImaginaryFrequency_1':[temperature_list, pressure_list, pertubation_percent],
                                         },
                                        channels)

# fit rate constants
n_P = 2  # number of pressure polynominals
n_T = 6 # number of temperature polynominals
same_line_result = True
model.Run() # execute PAPR-MESS perturbations
model.fit_Cheb_rates(n_P, n_T, P_min=0.0001, P_max=100, T_min=200, T_max=3000) # fit rate constants into Chebyshev expressions
model.Cheb_sens_coeff(same_line_result=same_line_result) # calculate sensitivity coefficients


# for debugging, fitting rate constants for a given trail
# target_dir = '/home/leil/MSI/PAPR-MESS_calculation/h+ho2=hooh/calculation_5/'
# model.fit_Cheb_rates(n_P, n_T, target_dir=target_dir)
# model.Cheb_sens_coeff()
