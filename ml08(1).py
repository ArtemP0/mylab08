from array import*
import random

N = int(input("Введыть число N: "))

A = array("i", [random.randint(0,N) for _ in range(4)])
B = array("i", [random.randint(0,N) for _ in range(18)])
print(f"масив А : {A} ")
print(f"масив B : {B} ")

C = array("i")
for x in B:
  if x not in A:
    C.append(x)
print(f"масив C : {C} ")