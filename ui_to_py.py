# -*- coding: utf-8 -*-

#designerden .ui tasarımını değiştirdiğinde çalıştırılır.
#çalıştırmadan değiştirdiğiniz dosya ya göre, open ve uic.compileUi() deki isimleri değiştirdiğiniz.

from PyQt5 import uic

with open("dosya'nın adı", 'w', encoding="utf-8") as fout:
  uic.compileUi("dosya'nın adı", fout)
