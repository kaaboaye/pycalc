#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exc_info
from math import *

## FUNCTIONS

def e(x): # Notacja wykłądnicza
    return pow(10, x)

def s(x): # Silnia
    o = 1
    for i in range(1, x + 1):
        o *= i
    return int(o)

def sn(n, k): # Symbol Newtona
    return int(s(n)/(s(k)*s(n-k)))

def C(k, n): # Kombinacja bez powtórzeń
    return int(sn(n, k))

def W(k, n): # Wariacja z powtórzeniami
    return int(pow(n, k))

def V(k, n): # Wariacja bez powtórzeń
    return int(s(n)/s(n-k))

## CONSTANT

G = 6.674083131313131 * e(-11) # Stała grawitacji

## CONSOLE

def console():
    try:
        while True:
            while True:
                inp = input("> ")
                if len(inp) > 0:
                    break

            if inp[0] == "`":
                inp = inp.replace("`", "")
                exec(inp)
            else:
                ans = eval(inp)
                print(ans)

    except EOFError:
        end()
    except KeyboardInterrupt:
        end()
    except:
        print("Niepoprawne dane wejściowe:")
        print("    " + str(exc_info()[1]))
        console()

def end():
    print("\nZakończono")
    quit()


## EXECUTE

ans = 0
console()
