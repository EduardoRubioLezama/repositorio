#*-* encoding: utf-8 *-*

#!/usr/bin/env python
#
# https://www.spoj.pl/problems/FCTRL
#

# El algoritmo GetZeros corre en tiempo 2 lg (5,x) , con esta pequeña 
# modificacion el algoritmo corre en tiempo lg (5,x) que para ejemplares
# amplios nos ahorramos un poco de tiempo de ejcucion
def modf_GetZeros(number):
  zeros = 0
  potencia = 1
  while True:
    parte_entera = number / (5**potencia)

    zeros += parte_entera
    potencia += 1
    if (parte_entera < 1):
      break
  return zeros    
      
def GetZeros(number):
  zeros = 0
  value = 5
  counter = 0

  while value <= number:
    value *= 5
    counter += 1

  for i in xrange(1, counter+1):
    zeros += number / (5 ** i)

  return zeros


if __name__ == '__main__':
  num = int(raw_input())
  numbers = []
  results = []

  for i in xrange(num):
    numbers.append(int(raw_input()))

  for i in numbers:
    results.append(modf_GetZeros(i))

  print '\n'.join([str(result) for result in results])
  
