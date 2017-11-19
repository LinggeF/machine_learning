import random


def dot_product(a1, a2):
    a=0
    for i in range(0,len(a1),1):
        a+=a1[i]*a2[i];
    return a

a1=[1,2,3]
a2=[2,4,6]
print(dot_product(a1,a2))