import numpy as np

# Read Values from csv into 2 Lists: X & Y
def ols(file):
    X = []
    Y = []
    csv = np.genfromtxt(file, delimiter=",")
    X = csv[:,1]
    Y = csv[:,2]
    X[np.isnan(X)]=0
    Y[np.isnan(Y)]=0
    # Mean x & y
    x_mean = np.mean(X)
    y_mean = np.mean(Y)
    # Calculate Intercept & Slope
    sum1 = 0
    sum2 = 0
    for x,y in zip(X,Y):
        sum1 += ((x - x_mean)*(y - y_mean))
        sum2 += ((x - x_mean)**2)
    slope = (sum1/sum2)
    intercept = y_mean - (slope*x_mean)
    # Calculate variance
    # sum3 = 0
    # for x,y in zip(X,Y):
    #     sum3 += (y - ((intercept + slope*x)**2))
    # variance = (sum1 / (len(X)-2))
    print ("Slope: ", slope)
    print ("Intercept: ", intercept)
    #print ("Variance:", variance)


ols('question_2.csv')
