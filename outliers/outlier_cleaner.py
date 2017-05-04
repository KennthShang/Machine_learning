#!/usr/bin/python
import numpy as np


def outlierCleaner(predictions, ages, net_worths):
	"""
		Clean away the 10% of points that have the largest
		residual errors (difference between the prediction
		and the actual net worth).

		Return a list of tuples named cleaned_data where 
		each tuple is of the form (age, net_worth, error).
	"""
	cleaned_data = []

	error = list( (net_worths - predictions)**2) ## use square
	data = zip(ages, net_worths, error)
	sorted_data = sorted(data, key=lambda tup: tup[2]) ## tup[2] is error
	cleaned_data = sorted_data[:81]  # get the first 81 with least square errors
	
	
	
	return cleaned_data

