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
temperature_list = np.arange(290,700,10).tolist() + np.arange(700,3100,100).tolist() # K

#temperature_list = [296,370,407,474,513,539,577,700,810,906,1050,1200,1350,1525,1700,1950,2250,2600,3000] # K



#temperature_list = np.arange(300,700,10).tolist()

pressure_list = [[.1,.3,.5,.7,.9,1,1.5,2,2.5,3,3.5,4], ['[atm]']] # Torr will be converted into atm internally



channels = ['W1->R',
             'W1->P1',
             'W1->P2',
             'W1->P3', 
             'W1->P4',
             'W1->P5',
              'W1->P6',
              'W1->P7',

              'R->P1',
              'R->P2',
              'R->P3',
              'R->P4',
              'R->P5',
              'R->P6',
              #'R->P7', # this reaction is the abtraction reaction FAKE->

              'P1->P2',
              'P1->P3',
              'P1->P4',
              'P1->P5',
              'P1->P6',
              'P1->P7',

              'P2->P3',
              'P2->P4',
              'P2->P5',
              'P2->P6',
              'P2->P7',

              'P3->P4', 
              'P3->P5', 
              'P3->P6', 
              'P3->P7',

              'P4->P5',
              'P4->P6',
              'P4->P7',

              'P5->P6',
              'P5->P7',

              'P6->P7'
              ]


channels = ['W1->R',
             'W1->P1',
             'W1->P2',
             'W1->P3', 
             'W1->P4',
             'W1->P5',
              'W1->P6',
              'P7->W1',

              'R->P1',
              'R->P2',
              'R->P3',
              'R->P4',
              'R->P5',
              'R->P6',
              'P7->R', # this reaction is the abtraction reaction

              'P1->P2',
              'P1->P3',
              'P1->P4',
              'P1->P5',
              'P1->P6',
              'P7->P1',

              'P2->P3',
              'P2->P4',
              'P2->P5',
              'P2->P6',
              'P7->P2',

              'P3->P4', 
              'P3->P5', 
              'P3->P6', 
              'P7->P3',

              'P4->P5',
              'P4->P6',
              'P7->P4', 

              'P5->P6',
              'P7->P5',

              'P7->P6'
              ]



pertubation_percent = 0.1 # percentage of perturbation
#pertubation_percent = 0.1
nominal_MESS_input_path = os.getcwd() + '/ch3+oh/'
nominal_MESS_input = 'ch4o.inp'

model = MSI.PAPR_MESS(nominal_MESS_input_path, nominal_MESS_input,
                                        {'W1_Energy_1':[temperature_list, pressure_list, 0.00]},
                                        { 'colrel_FactorOne': [temperature_list, pressure_list, pertubation_percent],
                                           'colrel_PowerOne': [temperature_list, pressure_list, pertubation_percent],
                                           'colrel_Epsilons': [temperature_list, pressure_list, pertubation_percent],
                                           'colrel_Sigmas': [temperature_list, pressure_list, pertubation_percent],
                                            'W1_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                          'W1_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                          'W1_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                          'R_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                          'R_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                          'R_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],


                                           'B1_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],

                                           'B2_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],


                                           'B3_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                           'B3_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                           'B3_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],


                                             'B4_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                             'B4_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                             'B4_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],


                                             'B5_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                             'B5_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                             'B5_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],


                                             'B6_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                           
                                             'B7_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],

                                             'B8_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                             'B8_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                             'B8_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                           'P1_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                           'P1_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                           'P1_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],


                                           'P2_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                           'P2_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                           'P2_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],



                                           'P3_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                           'P3_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                           'P3_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],


                                           'P4_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                           'P4_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                           'P4_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],



                                           'P5_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                           'P5_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                           'P5_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],



                                           'P6_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                           'P6_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                           'P6_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                           'P7_Energy_1':[temperature_list, pressure_list, pertubation_percent * 349.759],
                                           'P7_Frequencies_1':[temperature_list, pressure_list, pertubation_percent],
                                           'P7_SymmetryFactor_1':[temperature_list, pressure_list, pertubation_percent],

                                         },
                                        channels)

# fit rate constants
n_P = 4 # number of pressure polynominals
n_T = 8 # number of temperature polynominals
same_line_result = True
model.Run() # execute PAPR-MESS perturbations
model.fit_Cheb_rates(n_P, n_T, P_min=0.0001, P_max=10, T_min=200, T_max=3000,same_line_result=same_line_result) # fit rate constants into Chebyshev expressions
model.Cheb_sens_coeff(same_line_result=same_line_result) # calculate sensitivity coefficients


# for debugging, fitting rate constants for a given trail
# target_dir = '/home/leil/MSI/PAPR-MESS_calculation/h+ho2=hooh/calculation_5/'
# model.fit_Cheb_rates(n_P, n_T, target_dir=target_dir)
# model.Cheb_sens_coeff()
