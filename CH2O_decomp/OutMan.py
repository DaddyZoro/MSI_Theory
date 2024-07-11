#%%
import sys
import os
import io
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import pandas as pd

#%%
# #sys.argv practice
# print sys.argv
# print(len(sys.argv))

# for i in range(5):
#     print(sys.argv[i])
#     print('length of '+sys.argv[i]+' is '+str(len(sys.argv[i])))

# test = np.array(sys.argv[1])
# print(test)
# #print(len(test))

#%%
# os.system('mess CH2O_decomp.inp')

#%%
# fhand = io.open('CH2O_decomp.out')
# fgrand = fhand.readlines()
# fhand.close
# cleaner_file='rates.txt'
# cleaner_out=open(cleaner_file,'w')

# wells = 7
# products = 2
# barriers = 17
# pressures = 1
# temperatures = 23
# start = wells+products+barriers+4*3+7
# end = start+(2+(1+pressures)*(wells+products+4))*temperatures
# # R1 = [4,9]
# # R2 = [4,8]

# for i,grand in enumerate(fgrand):
#         fgrand[i] = fgrand[i].replace('***',"000").replace('From\To','F\T    ').replace('Temperature = ','').replace('High Pressure Rate Coefficients','HPRC').replace('Pressure = ','     ').replace('K',' ')
#         if i > start and i < end: #and i % 5:
#             cleaner_out.write(fgrand[i])        

# df = pd.read_fwf(cleaner_file)
# df.to_csv('rates.csv')
# # os.remove(cleaner_file)

# rates = pd.read_csv('/home/jmp/MSI_Theory/CH2O_decomp/rates.csv')

# # # arrays for python2
# # T_list = np.array(rates['500'][14::28],float)
# # R1 = np.array(rates['Unnamed: 9'][21::28],float)
# # R2 = np.array(rates['Unnamed: 8'][21::28],float) 

# # arrays for python3 
# T_list = np.array(rates['500'][11::23],float)
# R1 = np.array(rates['Unnamed: 9'][17::23],float)
# R2 = np.array(rates['Unnamed: 8'][17::23],float)

# plt.figure(1)
# plt.plot(T_list,R1,color='blue')
# plt.plot(T_list,R2,color='red')
# plt.yscale("log")
# plt.xlabel('Temperature (K)')
# plt.ylabel('k (s$^{-1}$)')

# plt.savefig('rates.pdf')
# plt.savefig('rates.png')
# plt.savefig('rates.svg')

#%%
fudd = open('eVal.out')
crimes = fudd.readlines()
fudd.close
cleaned_file='eigens.txt'
cleaned_out=open(cleaned_file,'w')

for i,crime in enumerate(crimes):
    crime = crime.replace(',',' ').replace('*',' ').replace('/','p').replace('\t',' ')
    if i == 4 or i > 5:
        cleaned_out.write(crime)
    # if i == 4:
    #     crime=crime.replace('*',' ').replace('/','p').replace(' ','').replace('pF','pF,')

width = [13]*18
print(width)
df = pd.read_fwf('eigens.txt',widths=width)
# df = pd.read_csv(cleaned_file)
# print(df)
df.to_csv('eigens.csv')
# os.remove(cleaned_file)

eigenV = pd.read_csv('/home/jmp/MSI_Theory/CH2O_decomp/eigens.csv')

Temps = eigenV['Temperature']

Vals1 = eigenV['EpF']*eigenV['F']
Vals2 = eigenV['EpF.1']*eigenV['F']
Vals3 = eigenV['EpF.2']*eigenV['F']
Vals4 = eigenV['EpF.3']*eigenV['F']
Vals5 = eigenV['EpF.4']*eigenV['F']
Vals6 = eigenV['EpF.5']*eigenV['F']
Vals7 = eigenV['EpF.6']*eigenV['F']


plt.figure(2)
plt.plot(Temps,Vals1,color='blue')
plt.yscale("log")
plt.plot(Temps,Vals2,color='red')
plt.plot(Temps,Vals3,color='black')
plt.plot(Temps,Vals4,color='green')
plt.plot(Temps,Vals5,color='orange')
plt.plot(Temps,Vals6,color='purple')
plt.plot(Temps,Vals7,color='turquoise')
plt.xlabel('Temperature (K)')
plt.ylabel('Eigenvalues (s$^{-1}$)')

plt.savefig('eigens.pdf')
plt.savefig('eigens.png')
plt.savefig('eigens.svg')

