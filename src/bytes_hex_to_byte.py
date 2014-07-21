#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

In Python, How to convert hex string to bytes?

En Python, ¿Cómo convertir un string hexadecimal a bytes?
'''

#create a string with hexadecimal data
s = '48656c6c6f20576f726c64'
print(s)

#this class method returns a bytes object, decoding the given string object.
#the string must contain two hexadecimal digits per byte.
b = bytes.fromhex(s)
print(b)
