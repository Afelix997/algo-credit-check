from multiprocessing.connection import answer_challenge

def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
def credit_check(str):
    total1=0
    total2=0
    rev_1= list(str[-1::-2])
    rev_2= list(str[-2::-2])
    multiplied = [2*int(number)  for number in rev_2]
    rev_2_fixed=[]
    for value in multiplied:
        if value > 9:
           value= getSum(value)
        rev_2_fixed.append(value)
    for val in rev_1:
        total1 = total1 + int(val)
    for val in rev_2_fixed:
        total2 = total2 + int(val)
    if (total1+total2) % 10 == 0:
        return "The number is valid!"
    else:
        return "The number is invalid!"    

    return answer




