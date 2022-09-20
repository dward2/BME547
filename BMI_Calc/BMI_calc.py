#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:52:46 2022

@author: dylancai
"""

def data_input():
    height_raw = input("Enter height followed by spacebar and then in or m: ")
    weight_raw = input("Enter weight followed by spacebar and then lb or kg: ")
    weight_data = weight_raw.split(" ")
    weight = float(weight_data[0])
    weight_units = weight_data[1]
    weight_new = 0
    if weight_units == "lb":
        weight_new = weight / 2.205
    height_data = height_raw.split(" ")
    height = float(height_data[0])
    height_units = height_data[1]
    height_new = 0
    if height_units == "in":
        height_new = height * .0254
    print ("The height entered was {} m".format(height_new))
    print ("The weight entered was {} kg".format(weight_new))
    return weight_new, height_new

def BMI_calc(w, h):
    BMI = w / (h*h)
    print("BMI = ")
    print(BMI)
    return BMI


def check_BMI(bmi):
    if bmi > 30.0:
        print("you are obese")
        
    elif 25 < bmi < 29.9:
        print("you are overweight")
        
    elif 18.5 < bmi < 24.9:
        print("you are healthy")
        
    else:
        print("you are underweight")
    
