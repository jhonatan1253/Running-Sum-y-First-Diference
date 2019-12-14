# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:45:48 2019

@author: Usuario
"""

import numpy as np
import signals as sigs
import pylab as plt

##### Señal ruido_1KHz  ##### 
a1=sigs.ruido_1KHz
plt.plot(a1, 'y')
plt.plot(a1, 'b.')
plt.title(" Señal original (ruido_1KHz)")
##### Señal ruido_100Hz  ##### 
a2=sigs.ruido_100Hz
plt.plot(a2, 'y')
plt.plot(a2, 'b.')
plt.title(" Señal original (ruido_100Hz)")
##### Señal ruido_extra_100Hz   ##### 
a3=sigs.ruido_extra_100Hz
plt.plot(a3, 'y')
plt.plot(a3, 'b.')
plt.title(" Señal original (ruido_extra_100Hz)")
##### Señal ecg_100Hz  ##### 
a4=sigs.ecg_100Hz
plt.plot(a4, 'y')
plt.plot(a4, 'b.')
plt.title(" Señal original (ecg_100Hz)")
##### Señal airflow_calibrated_100Hz   ##### 
a5=sigs.airflow_calibrated_100Hz
plt.plot(a5, 'y')
plt.plot(a5, 'b.')
plt.title(" Señal original (airflow_calibrated_100Hz)")
##### Señal airflow_100Hz   ##### 
a6=sigs.airflow_100Hz
plt.plot(a6, 'y')
plt.plot(a6, 'b.')
plt.title(" Señal original (airflow_100Hz)")


#################################################################################################################
#################################################################################################################
####### first difference######

######################################## formula:    y[n]=x[n]-x[n-1]        ###############
##### Señal ruido_1KHz  ##### 

def dff(a1):
    y1=[]
    for i in range(0, len(a1)):
        v=a1[i]-a1[i-1]
        y1.append(v)
        print(y1)
        plt.title(" first difference en señal (ruido_1KHz)")
        plt.plot(y1, 'b')
        
dff(a1)

##### Señal ruido_100Hz  #####

def dff(a2):
    y2=[]
    for i in range(0, len(a2)):
        v=a2[i]-a2[i-1]
        y2.append(v)
        print(y2)
        plt.title(" first difference en señal (ruido_100Hz)")
        plt.plot(y2, 'b')

dff(a2)


##### Señal ruido_extra_100Hz   ##### 

def dff(a3):
    y3=[]
    for i in range(0, len(a3)):
        v=a3[i]-a3[i-1]
        y3.append(v)
        print(y3)
        plt.title(" first difference en señal (ruido_extra_100Hz)")
        plt.plot(y3, 'b')

dff(a3)

##### Señal ecg_100Hz  #####
def dff(a4):
    y4=[]
    for i in range(0, len(a4)):
        v=a4[i]-a4[i-1]
        y4.append(v)
        print(y4)
        plt.title(" first difference en señal (ecg_100Hz)")
        plt.plot(y4, 'b')

dff(a4)
##### Señal airflow_calibrated_100Hz   #####
def dff(a5):
    y5=[]
    for i in range(0, len(a5)):
        v=a5[i]-a5[i-1]
        y5.append(v)
        print(y5)
        plt.title(" first difference en señal (airflow_calibrated_100Hz)")
        plt.plot(y5, 'b')

dff(a5)
##### Señal airflow_100Hz   #####

def dff(a6):
    y6=[]
    for i in range(0, len(a6)):
        v=a6[i]-a6[i-1]
        y6.append(v)
        print(y6)
        plt.title(" first difference en señal (airflow_100Hz)")
        plt.plot(y6, 'b')

dff(a6)

 #################################################################################################################
#################################################################################################################
####### Running Sum  ######
 
 
######################################## formula:    y[n]=x[n]+y[n-1]      ###############
##### Señal ruido_1KHz  ##### 

def ds(a1):
    y7=[0]
    for i in range(1, len(a1)):
        v=a1[i]+y7[i-1]
        y7.append(v)
        print(y7)
        plt.title(" Running Sum en señal (ruido_1KHz)")
        plt.plot(y7, 'r')
        
ds(a1)

##### Señal ruido_100Hz  #####
def ds(a2):
    y8=[0]
    for i in range(1, len(a2)):
        v=a2[i]+y8[i-1]
        y8.append(v)
        print(y8)
        plt.title(" Running Sum en señal (ruido_100Hz)")
        plt.plot(y8, 'r')
        
ds(a2)
##### Señal ruido_extra_100Hz   ##### 
def ds(a3):
    y9=[0]
    for i in range(1, len(a3)):
        v=a3[i]+y9[i-1]
        y9.append(v)
        print(y9)
        plt.title(" Running Sum en señal (ruido_extra_100Hz)")
        plt.plot(y9, 'r')
        
ds(a3)
##### Señal ecg_100Hz  #####
def ds(a4):
    y10=[0]
    for i in range(1, len(a4)):
        v=a4[i]+y10[i-1]
        y10.append(v)
        print(y10)
        plt.title(" Running Sum en señal (ecg_100Hz)")
        plt.plot(y10, 'r')
        
ds(a4)
##### Señal airflow_calibrated_100Hz   #####
def ds(a5):
    y11=[0]
    for i in range(1, len(a5)):
        v=a5[i]+y11[i-1]
        y11.append(v)
        print(y11)
        plt.title(" Running Sum en señal (airflow_calibrated_100Hz)")
        plt.plot(y11, 'r')
        
ds(a5)
##### Señal airflow_100Hz   #####
def ds(a6):
    y12=[0]
    for i in range(1, len(a6)):
        v=a6[i]+y12[i-1]
        y12.append(v)
        print(y12)
        plt.title(" Running Sum en señal (airflow_100Hz)")
        plt.plot(y12, 'r')
ds(a6)