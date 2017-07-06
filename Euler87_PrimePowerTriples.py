"""
Euler87_Prime power triples
Problem 87
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube,
and prime fourth power?

print(math.ceil((5*10**7)**(1/4))) #--> 85
print(math.ceil((5*10**7)**(1/3))) #-->369
print(math.ceil((5*10**7)**(1/2))) #-->7072
"""
import math 
def is_prime(x):
    for i in range(2,math.floor(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

def list_primes(max):
    primes=[]; 
    j=2
    while j<=max:
        if is_prime(j):
            primes.append(j);
        j+=1
    #print(list(primes));
    #print("have assembled a list of the",len(primes),"primes below",max);
    return list(primes);

primes=list_primes(7070) #-->has length 908, of which the largest in 7069
p2=[]
p3=[]
p4=[]
#primes[22]=83    
#primes[72]=367 
for p in primes:
    p2.append(p**2)
for b in range(73):
    p3.append(primes[b]**3) 
for a in range(23):
    p4.append(primes[a]**4)
  
#print(len(p2)) #-->908, of which 7069 is the largest base
#print(len(p3)) #-->73, of which 367 is the largest base
#print(len(p4)) #-->23, of which 83 is the largest base

tots=[]
for x in p2:
    for y in p3:
        for z in p4:
            if x+y+z<50000000:
                tots.append(x+y+z)
#print(len(tots)) #-->1139575
print(len(set(tots)))  #-->  1097343 CORRECT
