#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:58:41 2018

@author: Radek Duchoň
"""
#Vrati vstupni polozku item, pokud tato polozka muze byt prvkem mnoziny v Pythonu, v opacnem pripade frozenset(item)
def can_be_a_set_member_or_frozenset(item):
    """Funkce pro overeni, zda muze byt 'item' prvkem mnoziny, vrati parametr item jako frozenset, pokud 'item' nemuze byt prvkem mnoziny, jinak vrati 'item'
    Args: item
    return: frozenset(item) || item"""
    #Pokud neni promenna hashovatelna, nemuze byt polozkou seznamu
    try:
        hash(item)
    except TypeError:
        return frozenset(item)

    return item


assert can_be_a_set_member_or_frozenset(1) == 1
assert can_be_a_set_member_or_frozenset((1,2)) == (1,2)
assert can_be_a_set_member_or_frozenset([1,2]) == frozenset([1,2])
    
#Vraci potencni mnozinu prvku
def all_subsets(lst):
    """Vraci list s potencni mnozinou prvku z prvku ze seznamu v argumentu
    Args: seznam s prvky
    return: seznam s potencni mnozinou"""
    k = [[]] #deklarace seznamu s prvni polozkou (prazdnou mnozinou)
    #Pridani dalsich polozek seznamu
    for l in lst:
        for m in k:
            if [l] == m: break
            k.append(m+[l])
    
    return k
    

assert all_subsets(['a', 'b', 'c']) == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    
#Vraci porencni mnozinu s/bez prazdne mnoziny dle parametru exclude_empty
def all_subsets_excl_empty(*lst, exclude_empty = True):    
    """Vraci list s potencni mnozinou prvku seznamu z prvku v seznamu v argumentu, volitelne beu prazdne mnoziny
    Args: volitelny pocet parametru jako prvku, volitelny parametr exclude_empty
    return: list s potencni mnozinou s nebo bez prazdne mnoziny dle volitelneho parametru exclude_empty"""
    k = [[]]#deklarace seznamu s prvni polozkou (prazdnou mnozinou)
    #Pridani dalsich polozek seznamu
    for l in lst:
        for m in k:
            if [l] == m: break
            k.append(m+[l])
    #Vyrazeni prazdne mnoziny ze seznamu, pokud je exclude_empty True
    if exclude_empty:
        k.pop(0)

    return k


assert all_subsets_excl_empty('a', 'b', 'c') == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty = True) == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty = False) == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
