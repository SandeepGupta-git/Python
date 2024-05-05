## Example-1
def helloWorld() :
    msg = 'Heloo Python Worls'
    print(msg)
helloWorld()
## Example-2
def printDays():
    days = ['SUN','MON','TUE']
    for i in days:
        print(i)
printDays()
## Example-3
def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()
    
smallest = None
itervar = [1,2,3]
print("Before:", smallest)
if smallest is None or itervar < smallest:
        smallest = itervar
        print("Loop:", itervar, smallest)