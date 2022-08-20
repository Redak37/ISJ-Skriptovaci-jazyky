#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5.4.2018

@author: Radek Duchoň
"""

def first_nonrepeating(string):
    """
    Funkce hledající první neopakující se znak v řetězci.
    Args:   string - řetězec, ve kterém se vyhledává
    return: První neopakující se znak, nebo None, pokud nebyl nalezen, či byl neplatný vstup
    """
    if type(string) is not str: return None

    for x in range(len(string)):
        if string[x] != '\t' and string[x] != ' ':
            for y in range(len(string)):
                if string[x] == string[y]:
                    if x != y: break
                    elif y == len(string) - 1: return string[x]
                elif y == len(string) - 1: return string[x]

    return None

def combine2(a, b, zn):
    """
    Funkce provádějící určitou operaci mezi danými argumenty
    Args:   a - číslo v operaci
            b - číslo v operaci
            zn - číslo od 0 do 3 určující operaci
    return: výsledek dané operace mezi dvěmi čísly
    """
    if not a or not b: return None
    if zn == 0: return a + b
    if zn == 1: return a - b
    if zn == 2: return a * b
    if zn == 3 and b != 0: return a / b
    return None

def combine4(lst, sol):
    """
    Funkce hledající všechny způsoby, jak získat dané řešení ze zadaných kladných čísel a znamének +-*/
    Args:   lst - seznam čtyř čísel
            sol - hledaný výsledek
    return: seznam všech možných způsobů, jak získat pomocí základních operací a čtyř čísel daný výsledek
    """
    if len(lst) != 4: return None
    zn = ['+', '-', '*', '/']
    zn1 = 0
    zn2 = 0
    zn3 = -1
    out = []
    for i in range(64):
        zn3 += 1
        if zn3 == 4:
            zn2 += 1
            zn3 = 0
        if zn2 == 4:
            zn1 += 1
            zn2 = 0

        for v in range(4):
            c1 = lst[v]
            for x in range(4):
                if x == v: continue
                c2 = lst[x]
                for y in range(4):
                    if y == x or y == v: continue
                    c3 = lst[y]
                    for z in range (4):
                        if z == y or z == x or z == v: continue
                        c4 = lst[z]
                        if combine2(combine2(combine2(c1, c2, zn1), c3, zn2), c4, zn3) == sol:
                            out.append('(('+str(c1)+str(zn[zn1])+str(c2)+')'+str(zn[zn2])+str(c3)+')'+str(zn[zn3])+str(c4))

                        if combine2(combine2(c1, combine2(c2, c3, zn2), zn1), c4, zn3) == sol:
                            out.append('('+str(c1)+str(zn[zn1])+'('+str(c2)+str(zn[zn2])+str(c3)+'))'+str(zn[zn3])+str(c4))

                        if combine2(c1, combine2(c2, combine2(c3, c4, zn3), zn2), zn1) == sol:
                            out.append(str(c1)+str(zn[zn1])+'('+str(c2)+str(zn[zn2])+'('+str(c3)+str(zn[zn3])+str(c4)+'))')

                        if combine2(c1, combine2(combine2(c2, c3, zn2), c4, zn3), zn1) == sol:
                            out.append(str(c1)+str(zn[zn1])+'(('+str(c2)+str(zn[zn2])+str(c3)+')'+str(zn[zn3])+str(c4)+')')

                        if combine2(combine2(c1, c2, zn[zn1]), combine2(c3, c4, zn[zn3]), zn2) == sol:
                            out.append('('+str(c1)+str(zn[zn1])+str(c2)+')'+str(zn[2])+'('+str(c3)+str(zn[zn3])+str(c4)+')')
    return(list(set(out)))
