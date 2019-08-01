

def insertt(num, numb, shift):

  numb = int(numb, 2) << shift
  num = int(num, 2) | numb
  print(bin(num))
 

 
a = '10000000000'
b = '10011'
c = 2
insertt(a, b, c)
