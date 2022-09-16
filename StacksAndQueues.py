'''
#Matching delimiters using Stacks
#LIFO: Last In First Out

def checkDelimitersMatch(n):
    n = list(n)
    stackList = []
    symbolsOpen = ['[', '(', '{']
    symbolsClose = [']', ')', '}']
    if len(n) > 0:
        for x in n:
            if x in symbolsOpen:
                stackList.append(x)
            elif x in symbolsClose:
                if symbolsClose.index(x) != symbolsOpen.index(stackList[-1]):
                    print("The expression doesn't have symbols in order.")
                    break
                else:
                    stackList.pop()
        if (len(stackList)==0):
            print("Your expression has symbols in order.")
        else:
            print("The expression doesn't have symbols in order.")
    else:
        print("Your expression list is empty.")
expression = '[{(5+x)-{(y+z)}}]'
checkDelimitersMatch(expression)

'''
'''
#Queues
#FIFO: First In First Out

def deque(n):

    lengthN = len(n)
    if(lengthN > 0):
        answer = n[0]
        for x in range(0,lengthN):
            n[x] = n[(x +1) % lengthN]
        n[lengthN-1] = None
        print(n)
        return answer
    else:
        print('List is empty')
print(deque([1]))

'''


