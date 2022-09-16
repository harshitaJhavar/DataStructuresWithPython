'''
####### Factorial of a number#######

class Factorial:
    def __init__(self, number):
        self.number = number

    def findFactorial(self):
        if (self.number==0):
            return 1
        else:
            result = self.number * Factorial(self.number-1).findFactorial()
            return result
def main():
    x = Factorial(6)
    print(x.findFactorial())

if __name__== "__main__":
    main()
'''
'''
# 0,1,1,2,3,5....
def Fabonacci(n):
    if(n<=1):
        return n
    else:
        return Fabonacci(n-1) + Fabonacci(n-2)

length=10
series=[]
for i in range(0,length):
    series.append(Fabonacci(i))

print(series)
'''
'''
#Find sum of sequence recursively

def SumOfSequence(n):
    if len(n) >0:
        return n[-1] + SumOfSequence(n[0:(len(n)-1)])
    else:
        return 0

n = [2,5,3,6,8]
print(SumOfSequence(n))

'''
'''
#Reversing a list

def reverseList(n, start, stop):
    l = len(n)
    if start >= stop:
        return None
    else:
        n[stop], n[start] = n[start], n[stop]
        reverseList(n, start+1, stop-1)
        return n
n = [2,5,3,3,2,4,5,6]
print(reverseList(n, 0, (len(n)-1)))
'''



































