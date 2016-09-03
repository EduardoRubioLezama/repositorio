#!/usr/bin/env python
#
# Can extend to unique words, duplicate words etc.
#

import sys

def duplicateWords (lista):
  conjunto = set()
  duplicadas = 0
  for i in range (len(lista)):
    conjunto.add(lista[i])
  duplicadas = len(lista) - len(conjunto)
  return duplicadas  


def IsUnique(string):
  d = {}
  for char in string:
    if char in d:
      return False
    else:
      d[char] = True
  return True

# Como lo sugiere el codigo inicial, hacemos que en vez de determinar si una palabra tiene letras unicas, un texto determine si tiene palabras 
# con letras unicas
def giveUnique (texto):
  lista = []
  for i in range (len (texto)):
    if IsUnique(texto[i]):
      lista.insert(len(lista),texto[i])
  return lista       

if __name__ == '__main__':
  
  f = open(sys.argv[1])

  l = f.read().split()

  print (giveUnique (l))
  print (duplicateWords(l))
