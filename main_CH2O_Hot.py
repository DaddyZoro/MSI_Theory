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

# Temperature_list = np.arange(250,700,10).tolist() + np.arange(700,5000,100).tolist() # K
Temperature_list=[290,300,310] 
Pressure_list = [[1.], ['[atm]']] # Torr will be converted into atm internally

channels = [#'W0->W1','W1->W0',
#'W0->W2','W2->W0', 
#'W0->W3','W3->W0' ,
#'W0->W4','W4->W0', 
#'W0->W5c','W5c->W0', 
#'W0->W5t','W5t->W0', 
#'W0->S1','S1->W0',
#'W0->P1','P1->W0', 
#'W0->P2','P2->W0',
#'W0->Pescape','Pescape->W0',
#'W0->P2143','P2143->W0',
#'W0->P2141','P2141->W0',
#'W0->P41','P41->W0',


#'W1->W2','W2->W1',
#'W1->W3','W3->W1', 
#'W1->W4','W4->W1' , 
#'W1->W5c','W5c->W1', 
#'W1->W5t','W5t->W1',
#'W1->S1','S1->W1',
#'W1->P1','P1->W1', 
#'W1->P2','P2->W1',
#'W1->Pescape','Pescape->W1',
#'W1->P2143','P2143->W1',
#'W1->P2141','P2141->W1',
#'W1->P41','P41->W1',

#'W2->W3','W3->W2', 
#'W2->W4','W4->W2', 
#'W2->W5c','W5c->W2', 
#'W2->W5t','W5t->W2', 
#'W2->S1','S1->W2',
#'W2->P1','P1->W2', 
#'W2->P2','P2->W2',
#'W2->Pescape','Pescape->W2',
#'W2->P2143','P2143->W2',
#'W2->P2141','P2141->W2',
#'W2->P41','P41->W2',

#'W3->W4','W4->W3', 
#'W3->W5c','W5c->W3', 
#'W3->W5t','W5t->W3', 
#'W3->S1','S1->W3',
#'W3->P1','P1->W3', 
#'W3->P2','P2->W3',
#'W3->Pescape','Pescape->W3',
#'W3->P2143','P2143->W3',
#'W3->P2141','P2141->W3',
#'W3->P41','P41->W3',


'W4->W5c','W5c->W4', 
'W4->W5t','W5t->W4',
'W4->S1','S1->W4',
'W4->P1','P1->W4',
'W4->P2','P2->W4',
'W4->Pescape','Pescape->W4',
'W4->P2143','P2143->W4',
'W4->P2141','P2141->W4',
'W4->P41','P41->W4',

'W5c->W5t','W5t->W5c', 
#'W5c->S1','S1->W5c',
'W5c->P1','P1->W5c', 
'W5c->P2','P2->W5c',
'W5c->Pescape','Pescape->W5c',
#'W5c->P2143','P2143->W5c',
#'W5c->P2141','P2141->W5c',
#'W5c->P41','P41->W5c',

#'W5t->S1','S1->W5t',
'W5t->P1','P1->W5t', 
'W5t->P2','P2->W5t',
#'W5t->Pescape','Pescape->W5c',
#'W5t->P2143','P2143->W5t',
#'W5t->P2141','P2141->W5t',
#'W5t->P41','P41->W5t',

#'S1->P1','P1->S1', 
#'S1->P2','P2->S1',
#'S1->Pescape','Pescape->S1',
#'S1->P2143','P2143->S1',
#'S1->P2141','P2141->S1',
#'S1->P41','P41->S1',

'P1->P2','P2->P1',
'P1->Pescape','Pescape->P1',
'P1->P2143','P2143->P1',
'P1->P2141','P2141->P1',
'P1->P41','P41->P1'


] # channel-specific rate constants of interest


# w4

#channels = ['W0->W1','W0->W2', 'WO->W3', 'W0->W4', 'W0->W5c', 'W0->W5t', 'W0->P1', 'W0->P2',
#'W1->W2', 'W1->W3', 'W1->W4', 'W1->W5c', 'W1->W5t', 'W1->P1', 'W1->P2',
#'W2->W3', 'W2->W4', 'W2->W5c', 'W2->W5t', 'W2->P1', 'W2->P2',
#'W3->W4', 'W3->W5c', 'W3->W5t', 'W3->P1', 'W3->P2',
#'W4->W5c', 'W4->W5t', 'W4->P1', 'W4->P2',
#'W5c->W5t', 'W5c->P1', 'W5c->P2',
#'W5t->P1', 'W5t->P2',
#'P1->P2']



pertubation_percent = 0.1 # percentage of perturbation
nominal_MESS_input_path = os.getcwd() + '/CH2O_Hot/'
nominal_MESS_input = 'CH2O_Hot_All.inp'
#nominal_MESS_input = 'combined.inp'

#nominal_MESS_input = 'ho2+ho2_Lei.inp'


model = MSI.PAPR_MESS(nominal_MESS_input_path, nominal_MESS_input,
                                    {'W0_Energy_1': [Temperature_list, Pressure_list, 0.00]},
                                    {'colrel_FactorOne': [Temperature_list, Pressure_list, pertubation_percent],
                                     'colrel_FactorTwo': [Temperature_list, Pressure_list, pertubation_percent],
                                      'colrel_PowerOne': [Temperature_list, Pressure_list, pertubation_percent],
                                      'colrel_PowerTwo': [Temperature_list, Pressure_list, pertubation_percent],

                                      'colrel_Epsilons': [Temperature_list, Pressure_list, pertubation_percent],
                                      'colrel_Sigmas': [Temperature_list, Pressure_list, pertubation_percent],
                                      'colrel_FractionOne': [Temperature_list, Pressure_list, pertubation_percent],

                                     'W0_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'W0_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'W0_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     
                                     'W1_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'W1_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'W1_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],

                                     'W2_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'W2_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'W2_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],

                                     'W3_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'W3_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'W3_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],


                                     'W4_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'W4_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'W4_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],

                                     'W5c_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'W5c_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'W5c_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],

                                     'W5t_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'W5t_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'W5t_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],

                                     'S1_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'S1_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'S1_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],

                                     'P1_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'P1_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'P1_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                     'P2_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'P2_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'P2_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                     'Pescape_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'Pescape_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'Pescape_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],

                                     'P2143_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'P2143_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'P2143_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],

                                     'P2141_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'P2141_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'P2141_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent], 

                                     'P41_Energy_1': [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'P41_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'P41_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],                                                                         

                                      'B0_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                      'B0_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                      'B0_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                      'B1_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B1_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                      'B1_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                     'B2_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B2_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B2_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                     'B3_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B3_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B3_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                     'B4_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B4_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     #'B4_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                     'B5_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B5_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     #'B5_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                     'B6t_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B6t_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B6t_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'B6t_ImaginaryFrequency_1': [Temperature_list, Pressure_list, pertubation_percent],


                                     'B6c_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B6c_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     #'B6c_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],




                                     'B7_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B7_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B7_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],


                                     'B8_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B8_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B8_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],




                                     'B9_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B9_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B9_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],



                                     'B10_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B10_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B10_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],



                                     'B11_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B11_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B11_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],


                                     'B12_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B12_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B12_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'B12_ImaginaryFrequency_1': [Temperature_list, Pressure_list, pertubation_percent],


                                     'B13_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B13_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B13_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'B13_ImaginaryFrequency_1': [Temperature_list, Pressure_list, pertubation_percent],


                                     'B14_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B14_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B14_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'B14_ImaginaryFrequency_1': [Temperature_list, Pressure_list, pertubation_percent],


                                     'B15_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B15_Frequencies_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B15_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],
                                     'B15_ImaginaryFrequency_1': [Temperature_list, Pressure_list, pertubation_percent],

# The escape (rxn w/ O2) and the pphoton excitiation states

                                     'B16_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B16_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                     'B17_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B17_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                     'B18_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B18_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                     'B19_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B19_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                     'B20_SymmetryFactor_1': [Temperature_list, Pressure_list, pertubation_percent],
                                     'B20_Energy_1' : [Temperature_list, Pressure_list, pertubation_percent * 349.759],

                                                                        

                                    },
                                    channels)

# fit rate constants
n_P = 4  # number of pressure polynominals
n_T = 13 # number of temperature polynominals
same_line_result = True
model.Run() # execute PAPR-MESS perturbations
model.fit_Cheb_rates(n_P, n_T, P_min=.01, P_max=10.0, T_min=250.0, T_max=5000.0, same_line_result=same_line_result) # fit rate constants into Chebyshev expressions
model.Cheb_sens_coeff(same_line_result=same_line_result) # calculate sensitivity coefficients


# for debugging, fitting rate constants for a given trail
# target_dir = '/home/leil/MSI/PAPR-MESS_calculation/h+ho2=hooh/calculation_5/'
# model.fit_Cheb_rates(n_P, n_T, target_dir=target_dir)
# model.Cheb_sens_coeff()
