#!/usr/local/bin/python3

import sys 
sys.path.append("../../correction/TP1")
import energyrequirement
if __name__ == '__main__':
	print(energyrequirement.dailyEnergyRequirement(input("Gender :") ,int(input("BodyWeight :")) ,int(input("Height :")) ,int(input("Age :")), input("Sport :")))