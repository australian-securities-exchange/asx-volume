
volData = [20255479,10917563,14103186,27241123,8163199]
mean = 16136110
sd = 6858918.825634781

from math import sqrt

#Mean and Standard Deviation Function
#[mean,sd] = dataMean(data)
#
#Inputs:
#-volume data array with 1(?) year of data
#
#Outputs:
#-mean of data
#-standard deviation
#-current standard deviation from mean
#-statistically relevancy

def dataMean(data):
	sum = 0
	inner_sum = 0
	
	for i in range(0,len(data)):
		sum = sum + data[i]
	
	mean = int(sum/len(data))
	#print(len(data))
	#print(mean)
	
	for i in range(0,len(data)):
		interior = abs(data[i]-mean)
		inner_sum = inner_sum + interior**2
	sd = sqrt(inner_sum/len(data))
	
	return mean, sd

#Current Deviation Function
#[numSD] = currentDayDeviation(data,mean,sd)
#
#Inputs:
#-volume data array with 1(?) year of data
#-mean calculated from previous function
#-deviation calculated from previous function
#
#Outputs:
#-number of standard deviations the current volume is from the mean over time period

def currentDayDeviation(data, mean, sd):
	numSD = (data[-1]-mean)/sd
	return numSD

