#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 29.4.2018

@author: Radek Duchoň
"""


class TooManyCallsError(Exception):
    """
    Vyjimka mnoha volani
    """
    pass


def limit_calls(max_calls = 2, error_message_tail = 'called too often'):
    """
    Dekorator pro omezeni poctu volani funkce
    Args:   max_calls - maximalni pocet volani funkce - impicitne 2
            error_message_tail - konec chybove zpravy - implicitne 'called too often'
    """
    def decorate(func):
        """Dekorator funkce"""
        
        def wrapper(*args, **kwargs):
            """Limitace dekoratoru"""
            wrapper.calls += 1
            
            if wrapper.calls > max_calls:
                specific_error_message = "function \"" + str(func.__name__) + "\" - " + error_message_tail
                raise TooManyCallsError(specific_error_message)
            
            return func(*args, **kwargs)
        
        wrapper.calls = 0
        return wrapper
    
    return decorate


def ordered_merge(*args, selector = [], **kwargs):
    """
    Funkce tridici iterovatelne objekty dle selectoru
    Args:   *args - libovolny pocet iterovatelnych objektu
            selector - parametr udavajici jak utridit prvky
    return: ret - setrizeny list prvku
    """
    ret = []
    arg = []
    
    for a in args:
        arg.append(list(a))
        
    for num in selector:
        ret.append(arg[num][0])
        arg[num].pop(0)
            
    return ret

print(list(ordered_merge('abcde', [1, 2, 3], (3.0, 3.14, 3.141), range(11, 44, 11))))

class Log():
    """
    Trida pro vytvoreni logu do souboru
    """ 
    def __init__(self, filename):
        """
        Inicializace logu
        """
        self.output=open(filename, "w")
        
    def __enter__(self):
        """
        Spusteni logu
        """
        self.output.write("Begin\n")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Ukoncnei logu
        """
        self.output.write("End\n")
        self.output.close()
        
    def logging(self, log):
        """
        Zapis (logovani)
        """
        self.output.write(log + "\n")
