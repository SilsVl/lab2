divisibleByTwo = []
divisibleByThree = []
divisibleByFive = []
listNumbers = []
def listSorting(listNumbers):
    listNumbers = input('Enter numbers: ').split()
    for i in listNumbers:
      if int(i)%2 == 0:
        divisibleByTwo.append(i)
      if int(i)%3 == 0:
        divisibleByThree.append(i)
      if int(i)%5 == 0:
        divisibleByFive.append(i)
    print (divisibleByTwo, divisibleByThree, divisibleByFive)
    
listSorting(listNumbers)
