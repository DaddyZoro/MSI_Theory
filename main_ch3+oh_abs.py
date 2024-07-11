# -*- coding: utf-8 -*-
"""

Pipeline for PAPR-MESS MSI code.

@author: Jonathan Pankauski
Based on code written by Lei Lei
"""

import postprocessor as MSI
import os, io, sys
import numpy as np
sys.path.append("/home/jmp/MSI_Theory/")

# Initialize MSI.PAPR_MESS:
# -- the first arguement is the file path for the nominal PAPR-MESS input files
# -- the second arguement is the name for the unperturbed (nominal) input file
# -- the third arguement is a dictionary specifying the nominal condition (to allow optimization starting from nonzero perturbations),
#    the value specifies temperature list, pressure list, and nominal perturbation
# -- the fourth arguement is a dictionary with elements specifying the perturbations (sensitivity analysis are based on the nominal conditions defined above),
#    the keys specify names of perturbation runs and values specify temperature, pressure, and perturbation
# -  the fifth arguement is a list indicating the channels of interest

# energies in cm-1

Temperature_list = np.arange(200,700,10).tolist() + np.arange(700,3000,50).tolist() # K
Pressure_list = [[1.], ['[atm]']] # Torr will be converted into atm internally

channels = ['R->P8',]  # channel-specific rate constants of interest

pertubation_percent = 0.05 # percentage of perturbation
#pertubation_percent = 0.1 # percentage of perturbation

nominal_MESS_input_path = os.getcwd() + '/ch3+oh/'
nominal_MESS_input = 'CH3+OHtripletabs.inp'

model = MSI.PAPR_MESS(nominal_MESS_input_path, nominal_MESS_input,
                                    {'R_Energy_1': [Temperature_list, Pressure_list, 0.00]},
                                    {'R_Energy_1': [Temperature_list, Pressure_list, pertubation_percent* 349.759],
                                     'R_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'R_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],

                                     'P8_Energy_1': [Temperature_list, Pressure_list, pertubation_percent* 349.759],
                                     'P8_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'P8_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],

                                     'B1_VariationalEnergy_1': [Temperature_list, Pressure_list, pertubation_percent* 349.759],
                                     'B1_VariationalSymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B1_VariationalFrequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B1_ImaginaryFrequency_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B1_VariationalHinderRotor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                    },
                                    channels,abstraction=True)

# fit rate constants
n_P = 1 # number of pressure polynominals
n_T = 15 # number of temperature polynominals
model.Run() # execute PAPR-MESS perturbations
same_line_result = True
#aggregated_sens = False
model.fit_Cheb_rates(n_P, n_T, P_min=0.01, P_max=10, T_min=200, T_max=3000, same_line_result=same_line_result) # fit rate constants into Chebyshev expressions
model.Cheb_sens_coeff(same_line_result=same_line_result) # calculate sensitivity coefficients

# for debugging, fitting rate constants for a given trail
# target_dir = '/home/leil/MSI/PAPR-MESS_calculation/h+ho2=hooh/calculation_5/'
# model.fit_Cheb_rates(n_P, n_T, target_dir=target_dir)
# model.Cheb_sens_coeff()