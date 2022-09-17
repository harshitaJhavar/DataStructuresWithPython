#Mean
import statistics
print(statistics.mean([2,4]))
print(statistics.mode([2,3]))
print(statistics.median([3,4,5,6,7]))
print(statistics.quantiles([2,4,6]))
x=[24,36,42,23,65]
xBar = sum(x[0:len(x)])/ len(x)
varianceX = sum([(x[i]-xBar)**2 for i in range(0,len(x))]) / (len(x)-1)
print(varianceX)
print(statistics.variance(x))



