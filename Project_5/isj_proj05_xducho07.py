#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5.4.2018

@author: Radek Duchoň
"""
#Třída Polynomial pro polynomy
class Polynomial(object):
    """
    Třída Polynomial pro práci s polynomy a jejich inicializací
    """
    #Inicializace polynomu
    def __init__(self, *num, **keys):
        """
        Metoda třídy Polynomial pro inicializaci polynomu
        Args:   self - samotný polynom
                *num - hodnoty při zadání N-ticí nebo listem
                **keys - dict pro způsob zadání x1=, x2=...
        """
        #Kontrola a převedení zadaných argumentů do jednoho listu
        if len(keys) == 0:
            if isinstance(num[0], list): self.list = num[0]
            else: self.list = list(num)
        else:
            self.list = []
            for x in keys:
                turn = int(x[1:len(x)])
                if keys[x] != 0:
                    while turn >= len(self.list):
                        self.list.append(0)
                    self.list[turn]=int(keys[x])
    #Metoda popisující výpis polynomu
    def __str__(self):
        """
        Metoda třídy Polynomial pro výpis
        Args:   self - samotný polynom
        return: vrátí polynom ve formě určené k výpisu
        """
        #Proměnné pro výstup, znaménko a pozici listu, se kterou se bude zrovna pracovat
        out = ""
        Mark = ""
        koef = len(self.list)
        for x in self.list[::-1]:
            koef -= 1
            #Není potřeba vypisovat nulové členy
            if x != 0:
                #Zadání znaménka pro výpis, krom první vypisované části polynomu a změna znaménka části polynomu
                if x > 0:
                    if out != "":
                        Mark = " + "
                else:
                    Mark = " - "
                    x = -x
                #Aby se nevypisovali nepotřebné jedničky    
                if x == 1:
                    x = ""
                #Zápis polynomu do výpisu
                if koef > 1:
                    out += str(Mark)+str(x)+"x^"+str(koef)
                if koef == 1:
                    out += str(Mark)+str(x)+"x"
                if koef == 0:
                    if x == "": x = 1
                    out += str(Mark)+str(x)
        if out == "": out = "0"
        return out
    #Porovnání rovnosti polynomů
    def __eq__(self, other):
        """
        Metoda třídy Polynomial pro porovnání
        Args:   self - samotný polynom
                other - další polynom
        return: vrátí True || False
        """
        return self.list == other.list
    #Sčítání polynomů
    def __add__(self, other):
        """
        Metoda třídy Polynomial pro sčítání polynomů
        Args:   self - samotný polynom
                other - další polynom
        """
        #Vytvoří se nový prázdný polynom, zvětší se na velikost většího z dvou polynomů a zapíší se do něj sečtené hodnoty z daných indexů
        out = Polynomial(0)
        while len(self.list) >= len(out.list): out.list.append(0)
        while len(self.list) >= len(out.list): out.list.append(0)
        for x in range(len(self.list)):
            out.list[x] = self.list[x]
        for x in range(len(other.list)):
            out.list[x] += other.list[x]
        return out
    #Mocnina polynomu
    def __pow__(self, pow):
        """
        Metoda třídy Polynomial pro umocnňování
        Args:   self - samotný polynom
                pow - mocnitel
        return: vrací umocněný polynom
        """
        #Vytvoření dvou polynomů pro výpočty a jejich rozšíření na možnou budoucí velikost
        out = Polynomial(0)
        count = Polynomial(0) 
        for x in range(len(self.list) * pow):
            out.list.append(0)
            count.list.append(0)
        for x in range(len(self.list)): out.list[x] = self.list[x]
        #přepsání návratové hodnoy do průběžného count a jeho vynulování pro další výpočet
        for z in range(pow - 1):
            for x in range(len(out.list)):
                count.list[x] = out.list[x]
                out.list[x] = 0
            for x in range(len(self.list)):
                for y in range(len(count.list)):
                    if x+y < pow * len(self.list):
                        out.list[x+y] += self.list[x] * count.list[y]
        #První mocnina = přepis sebe sama
        if pow == 1:
            for x in range(len(self.list)):
                out.list[x] = self.list[x]
        return out
    #Derivace polynomu
    def derivative(self):
        """
        Metoda třídy Polynomial pro derivaci
        Args:   self - sasmotný polynom
        return: vrací zderivovaný polynom
        """
        #Vytvoření novéoh polynomu pro návrat, přepis vstupního polynomu dle vzorce derivace
        out = Polynomial(0)
        for x in range(len(self.list) - 1):
            out.list.append(0)
        for x in range(len(self.list) - 1):
            out.list[x] = self.list[x + 1] * (x + 1)
        return out
    #Výpočet hodnoty polynomu pro zadané x, případně rozdíl dvou hodnot pro polynom
    def at_value(self, *num):
        """
        Metoda třídy Polynomial pro výpočet hodnoty polynomu v bodě a rozdílu dvou hodnot v bodě
        Args:   self - samotný polynom
                *num - hodnota/hodnoty v bodě
        return: vrací hodnotu polynomu v bodě, nebo rozdíl hodnot, pokud byly zadány 2 body
        """
        #Dvě hodnoty pro až 2 hodnoty polynomu
        out = 0
        count = 0
        #Výpočet out
        for x in range(len(self.list)):
            pls = self.list[x]
            for y in range(x):
                pls *= num[0]
            out += pls
        #Případný výpočet count
        if len(num) == 2:
            for x in range(len(self.list)):
                pls = self.list[x]
                for y in range(x):
                    pls *= num[1]
                count += pls
        #Odečtení hodnot, pokud nebyla zadána druhá hodnota, převrácení výslekdu na správné znaménko
        out = count - out
        if len(num) == 1: out = -out
        return out


#Testy
def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
