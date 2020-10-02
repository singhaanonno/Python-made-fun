# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 00:12:54 2020

@author: Anonno
"""


import goslate

goslateobj=goslate.Goslate()
translatedtext=goslateobj.translate('I am a boy. I have a girlfriend and her name is arpita. ','bn')
print(translatedtext)