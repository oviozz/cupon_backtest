
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from nagivation import ScreenNavigate

class Product:
    img_url = {
        'Blue Color Shirt': 'shirt.png',
        'Brown Color Pants': 'brown_pants.png',
        'Blue Color Jacket': 'bluejacket.png'
    }
    @staticmethod
    def product_checkout(switch, product, checkout_tite, price_text, price_cost, product_image):

        image = Product.img_url[product.text()]

        checkout_tite.setText(product.text())
        price_text.setText(f'Price: ${price_cost}')
        ScreenNavigate.screen_change(switch, 2)

        product_image.setPixmap(QtGui.QPixmap(f"{image}"))


