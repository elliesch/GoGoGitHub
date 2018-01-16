import numpy as np 

def multiply_by_5(input_number):
	new_number = input_number * 5

	return new_number

def spherical2cartesian(ra, dec, distance):
	x = distance * np.cos(dec) * np.cos(ra)
	y = distance * np.cos(dec) * np.sin(ra)
	z = distance * np.sin(dec)

	return x,y,z