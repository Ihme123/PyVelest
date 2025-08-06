#!/usr/bin/env python

from numpy import loadtxt
from os import path

# Read the parameter file
par_file = path.join('par','par.dat')
input_par = loadtxt(par_file,comments='#',dtype=str,delimiter=':')
input_dic = {}

for i in input_par:
    input_dic[i[0].strip()] = i[1].strip()

print("Parameter dictionary:")
for key, value in input_dic.items():
    print(f"{key}: {value}")

print("\nChecking specific parameters:")
print(f"nsinv: {input_dic.get('nsinv', 'NOT FOUND')}")
print(f"nshcor: {input_dic.get('nshcor', 'NOT FOUND')}")
print(f"nshfix: {input_dic.get('nshfix', 'NOT FOUND')}")
print(f"iuseelev: {input_dic.get('iuseelev', 'NOT FOUND')}")
print(f"iusestacorr: {input_dic.get('iusestacorr', 'NOT FOUND')}")

# Test the line processing
l7 = '*** nsinv   nshcor   nshfix     iuseelev    iusestacorr'
l = l7.split()
l = l[1:]
print(f"\nLine 7 split: {l}")
print("Values from dictionary:")
for v in l:
    print(f"{v}: {input_dic.get(v, 'NOT FOUND')}")

result = "    ".join([input_dic.get(v, '0') for v in l])
print(f"\nFinal result: {result}") 