#%%
import pandas as pd
import numpy as np
import csv
from __future__ import division
from __future__ import print_function
import matplotlib.pyplot as plt

#%%

eigenV = pd.read_csv('/home/jmp/MSI_Theory/CH2O_decomp/eVal.csv')
eigenVB = pd.read_csv('/home/jmp/MSI_Theory/CH2O_decomp/eValB.csv')
eigenVB1 = pd.read_csv('/home/jmp/MSI_Theory/CH2O_decomp/eValB1.csv')
paper = pd.read_csv('/home/jmp/MSI_Theory/CH2O_decomp/Faraday_F4_noO2.csv')
#print(eigenV)
#eigenV1 = pd.read_csv('MSI_Theory/CH2O_decomp/eVal.csv')
# #%%
# spoop = eigenV.shape
# print(spoop)
# print(spoop[1])
# print(range(spoop[1]))
# print(len(spoop))
# #%%
# print(eigenV.columns)
# #%%
# print(eigenV.QpF)
# print(eigenV.QpF[1])
#%%
print(paper.columns)
#%%
#set up comparisons between 2 runs

Temps = eigenV.Temperature
#print(Temps)
Vals1 = eigenV.EpF*eigenV.F
Vals2 = eigenV.EpF_1*eigenV.F
Vals3 = eigenV.EpF_2*eigenV.F
Vals4 = eigenV.EpF_3*eigenV.F
Vals5 = eigenV.EpF_4*eigenV.F
Vals6 = eigenV.EpF_5*eigenV.F
Vals7 = eigenV.EpF_6*eigenV.F
#print(eigenV.EpF,Vals1)
TempsB = eigenVB.Temperature
ValsB_1 = eigenVB.EpF*eigenVB.F
ValsB_2 = eigenVB.EpF_1*eigenVB.F
ValsB_3 = eigenVB.EpF_2*eigenVB.F
ValsB_4 = eigenVB.EpF_3*eigenVB.F
ValsB_5 = eigenVB.EpF_4*eigenVB.F
ValsB_6 = eigenVB.EpF_5*eigenVB.F
ValsB_7 = eigenVB.EpF_6*eigenVB.F

TempsB1 = eigenVB1.Temperature
ValsB1_1 = eigenVB1.EpF*eigenVB1.F
ValsB1_2 = eigenVB1.EpF_1*eigenVB1.F
ValsB1_3 = eigenVB1.EpF_2*eigenVB1.F
ValsB1_4 = eigenVB1.EpF_3*eigenVB1.F
ValsB1_5 = eigenVB1.EpF_4*eigenVB1.F
ValsB1_6 = eigenVB1.EpF_5*eigenVB1.F
ValsB1_7 = eigenVB1.EpF_6*eigenVB1.F
#%%
plt.figure()
plt.plot(Temps,Vals1,color='blue')
plt.yscale("log")
plt.plot(Temps,Vals2,color='red')
plt.plot(Temps,Vals3,color='black')
plt.plot(Temps,Vals4,color='green')
plt.plot(Temps,Vals5,color='orange')
plt.plot(Temps,Vals6,color='purple')
plt.plot(Temps,Vals7,color='turquoise')

# plt.plot(paper.T1,paper.L1,color='blue',linestyle='dotted')
# plt.plot(paper.T2,paper.L2,color='red',linestyle='dotted')
# plt.plot(paper.T3,paper.L3,color='black',linestyle='dotted')
# plt.plot(paper.T4,paper.L4,color='green',linestyle='dotted')
# #plt.show

# plt.figure()
plt.plot(TempsB,ValsB_1,color='blue',linestyle='dashed')
plt.yscale("log")
plt.plot(TempsB,ValsB_2,color='red',linestyle='dashed')
plt.plot(TempsB,ValsB_3,color='black',linestyle='dashed')
plt.plot(TempsB,ValsB_4,color='green',linestyle='dashed')
plt.plot(TempsB,ValsB_5,color='orange',linestyle='dashed')
plt.plot(TempsB,ValsB_6,color='purple',linestyle='dashed')
plt.plot(TempsB,ValsB_7,color='turquoise',linestyle='dashed')

plt.plot(TempsB1,ValsB1_1,color='blue',linestyle='dotted',marker='.')
plt.yscale("log")
plt.plot(TempsB1,ValsB1_2,color='red',linestyle='dotted',marker='.')
plt.plot(TempsB1,ValsB1_3,color='black',linestyle='dotted',marker='.')
plt.plot(TempsB1,ValsB1_4,color='green',linestyle='dotted',marker='.')
plt.plot(TempsB1,ValsB1_5,color='orange',linestyle='dotted',marker='.')
plt.plot(TempsB1,ValsB1_6,color='purple',linestyle='dotted',marker='.')
plt.plot(TempsB1,ValsB1_7,color='turquoise',linestyle='dotted',marker='.')

# plt.show
#%%
# for i in range(spoop[0]):
#     for j in range(spoop[1]):
#         print(eigenV[i,j])


#%%
# Tlo=EigenV.Temperature[0::3]
# Tatm=EigenV.Temperature[1::3]
# Thi=EigenV.Temperature[2::3]

# L1lo = EigenV.EpF[0::3]*EigenV.F[0::3]
# L2lo = EigenV.EpF_1[0::3]*EigenV.F[0::3]
# L3lo = EigenV.EpF_2[0::3]*EigenV.F[0::3]
# L4lo = EigenV.EpF_3[0::3]*EigenV.F[0::3]
# L5lo = EigenV.EpF_4[0::3]*EigenV.F[0::3]
# L6lo = EigenV.EpF_5[0::3]*EigenV.F[0::3]
# L7lo = EigenV.EpF_6[0::3]*EigenV.F[0::3]

# L1atm = EigenV.EpF[1::3]*EigenV.F[1::3]
# L2atm = EigenV.EpF_1[1::3]*EigenV.F[1::3]
# L3atm = EigenV.EpF_2[1::3]*EigenV.F[1::3]
# L4atm = EigenV.EpF_3[1::3]*EigenV.F[1::3]
# L5atm = EigenV.EpF_4[1::3]*EigenV.F[1::3]
# L6atm = EigenV.EpF_5[1::3]*EigenV.F[1::3]
# L7atm = EigenV.EpF_6[1::3]*EigenV.F[1::3]

# L1hi = EigenV.EpF[2::3]*EigenV.F[2::3]
# L2hi = EigenV.EpF_1[2::3]*EigenV.F[2::3]
# L3hi = EigenV.EpF_2[2::3]*EigenV.F[2::3]
# L4hi = EigenV.EpF_3[2::3]*EigenV.F[2::3]
# L5hi = EigenV.EpF_4[2::3]*EigenV.F[2::3]
# L6hi = EigenV.EpF_5[2::3]*EigenV.F[2::3]
# L7hi = EigenV.EpF_6[2::3]*EigenV.F[2::3]

#%%
# plt.figure()
# plt.plot(Temps,Vals1,color='blue')
# plt.yscale("log")
# plt.plot(Temps,Vals2,color='red')
# plt.plot(Temps,Vals3,color='black')
# plt.plot(Temps,Vals4,color='green')
# plt.plot(Tatm,L1atm,color='blue',linestyle='dashed')
# plt.plot(Tatm,L2atm,color='red',linestyle='dashed')
# plt.plot(Tatm,L3atm,color='black',linestyle='dashed')
# plt.plot(Tatm,L4atm,color='green',linestyle='dashed')

#%%
# plt.plot(Tlo,L1lo,color='blue')
# plt.yscale("log")
# plt.plot(Tlo,L2lo,color='red')
# plt.plot(Tlo,L3lo,color='black')
# plt.plot(Tlo,L4lo,color='green')
# # plt.plot(Tlo,L5lo,color='orange')
# # plt.plot(Tlo,L6lo,color='purple')
# # plt.plot(Tlo,L7lo,color='cyan')
# plt.plot(Tatm,L1atm,color='blue',linestyle='dashed')
# plt.plot(Tatm,L2atm,color='red',linestyle='dashed')
# plt.plot(Tatm,L3atm,color='black',linestyle='dashed')
# plt.plot(Tatm,L4atm,color='green',linestyle='dashed')
# # plt.plot(Tatm,L5atm,color='orange',linestyle='dashed')
# # plt.plot(Tatm,L6atm,color='purple',linestyle='dashed')
# # plt.plot(Tatm,L7atm,color='cyan',linestyle='dashed')
# plt.plot(Thi,L1hi,color='blue',linestyle='dotted')
# plt.plot(Thi,L2hi,color='red',linestyle='dotted')
# plt.plot(Thi,L3hi,color='black',linestyle='dotted')
# plt.plot(Thi,L4hi,color='green',linestyle='dotted')
# # plt.plot(Thi,L5hi,color='orange',linestyle='dotted')
# # plt.plot(Thi,L6hi,color='purple',linestyle='dotted')
# # plt.plot(Thi,L7hi,color='cyan',linestyle='dotted')