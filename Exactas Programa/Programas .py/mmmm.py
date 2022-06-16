# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:52:43 2018

@author: Kalexa
"""

"""

La clase "Ccy" se puede usar para definir value monetarios en varias monedas. 
Una instancia de Ccy tiene los atributos de cadena 'unit' (por ejemplo, 'CHF',
 'CAD' od 'EUR' y el 'value' como un float.
Un objeto de moneda consta de un value y la unit correspondiente.



"""

    

class Ccy:

    currencies =  {'CHF': 1.0821202355817312, 
                   'CAD': 1.488609845538393, 
                   'GBP': 0.8916546282920325, 
                   'JPY': 114.38826536281809, 
                   'EUR': 1.0, 
                   'USD': 1.11123458162018}
    
    def __init__(self, value, unit="EUR"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return "{0:5.2f}".format(self.value) + " " + self.unit

    def changeTo(self, new_unit):
        """
        Un objeto Ccy se transforma de la unidad "self.unit" a "new_unit"
        """
        self.value = (self.value / Ccy.currencies[self.unit] * Ccy.currencies[new_unit])
        self.unit = new_unit
        
    def __add__(self, other):
        """
        Define el operador '+'.
        Si otro es un objeto CCy, los valores de la moneda
        se agregan y el resultado será la unidad de
        yo. Si otro es un int o un float, otro lo hará
        ser tratado como un valor en euros. 
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit]) 
        return Ccy(x + self.value, self.unit)


    def __iadd__(self, other):
        """
        Similar a __add__
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit])
        self.value += x
        return self

    def __radd__(self, other):
        res = self + other
        if self.unit != "EUR":
            res.changeTo("EUR")
        return res

    # __sub__, __isub__ y __rsub__ se puede definir analogue

x = Ccy(10,"USD")
y = Ccy(11)
z = Ccy(12.34, "JPY")
z = 7.8 + x + y + 255 + z
print(z)

lst = [Ccy(10,"USD"), Ccy(11), Ccy(12.34, "JPY"), Ccy(12.34, "CAD")]

z = sum(lst)

print(z)
