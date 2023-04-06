# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:58:46 2019

@author: ali
"""
#designerden .ui tasarımını değiştirdiğinde çalıştırılır

from PyQt5 import uic


with open('yeristasyonu.py', 'w', encoding="utf-8") as fout:
  uic.compileUi('yeristasyonu.ui', fout)