
from PyQt5.QtGui import QClipboard
from PyQt5.QtWidgets import QApplication


class PromoCode:
    def __init__(self, codelist):
        self.promo_codes = ['50%OFF','PLSCODE','DISCOUNTPLS']
        codelist.addItems(self.promo_codes)

    @staticmethod
    def clipboard(value):
        print(value)




