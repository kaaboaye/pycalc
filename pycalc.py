#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

## FUNCTIONS

def e(x): # notacja wykłądnicza
    return pow(10, x)

def s(x): # silnia
    o = 1
    for i in range(1, x + 1):
        o *= i
    return o

def sn(n, k): # symbol newtona
    return s(n)/(s(k)*s(n-k))

def C(k, n): # kombinacja
    return sn(n, k)

def W(k, n): # Wariacja z powtórzeniami
    return pow(n, k)

def V(k, n): # Wariacja bez powtórzeń
    return s(n)/s(n-k)

## CONSOLE

def console():
    try:
        while True:
            output = ""
            ans = 0

            while True:
                inp = input("> ")
                if len(inp) > 0:
                    break

            if inp[0] == "=":
                inp = inp.replace("=", "")
                ans = eval(inp)
                print(ans)
            else:
                exec(inp)

    except EOFError:
        end()
    except KeyboardInterrupt:
        end()
    except:
        print("Niepoprawne dane wejściowe")
        print(sys.exc_info())
        console()

def end():
    print("\nZakończono")
    quit()

console()
