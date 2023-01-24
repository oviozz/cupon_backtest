
from PyQt5 import QtCore, QtGui, QtWidgets
from nagivation import ScreenNavigate
from account_check import SignUp, Login
from product_apply import Product
from promoCodes import PromoCode
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pre_loginscreen = QtWidgets.QTabWidget(self.centralwidget)
        self.pre_loginscreen.setGeometry(QtCore.QRect(-20, -30, 1141, 681))
        self.pre_loginscreen.setTabPosition(QtWidgets.QTabWidget.South)
        self.pre_loginscreen.setObjectName("pre_loginscreen")
        self.signup = QtWidgets.QWidget()
        self.signup.setObjectName("signup")
        self.title = QtWidgets.QLabel(self.signup)
        self.title.setGeometry(QtCore.QRect(340, 50, 461, 81))
        self.title.setStyleSheet("font: 50pt \"Arial\";")
        self.title.setObjectName("title")
        self.madeby = QtWidgets.QLabel(self.signup)
        self.madeby.setGeometry(QtCore.QRect(420, 110, 251, 41))
        self.madeby.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.madeby.setObjectName("madeby")
        self.signup_title = QtWidgets.QLabel(self.signup)
        self.signup_title.setGeometry(QtCore.QRect(430, 200, 301, 71))
        self.signup_title.setStyleSheet("font: 75 40pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(130, 119, 255);\n"
"border-radius: 10px;")
        self.signup_title.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_title.setObjectName("signup_title")
        self.sign_up_username = QtWidgets.QLineEdit(self.signup)
        self.sign_up_username.setGeometry(QtCore.QRect(400, 300, 371, 41))
        self.sign_up_username.setObjectName("sign_up_username")
        self.sign_up_password = QtWidgets.QLineEdit(self.signup)
        self.sign_up_password.setGeometry(QtCore.QRect(400, 370, 371, 41))
        self.sign_up_password.setObjectName("sign_up_login")
        self.signup_submit = QtWidgets.QPushButton(self.signup)
        self.signup_submit.setGeometry(QtCore.QRect(400, 440, 361, 41))
        self.signup_submit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.signup_submit.setObjectName("signup_submit")
        self.pre_loginscreen.addTab(self.signup, "")
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.madeby1 = QtWidgets.QLabel(self.login)
        self.madeby1.setGeometry(QtCore.QRect(420, 110, 251, 41))
        self.madeby1.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.madeby1.setObjectName("madeby1")
        self.title1 = QtWidgets.QLabel(self.login)
        self.title1.setGeometry(QtCore.QRect(340, 50, 461, 81))
        self.title1.setStyleSheet("font: 50pt \"Arial\";")
        self.title1.setObjectName("title1")
        self.signup_title_2 = QtWidgets.QLabel(self.login)
        self.signup_title_2.setGeometry(QtCore.QRect(430, 200, 301, 71))
        self.signup_title_2.setStyleSheet("font: 75 40pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(130, 119, 255);\n"
"border-radius: 10px;")
        self.signup_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_title_2.setObjectName("signup_title_2")
        self.login_username = QtWidgets.QLineEdit(self.login)
        self.login_username.setGeometry(QtCore.QRect(400, 300, 371, 41))
        self.login_username.setObjectName("login_username")
        self.login_password = QtWidgets.QLineEdit(self.login)
        self.login_password.setGeometry(QtCore.QRect(400, 370, 371, 41))
        self.login_password.setObjectName("login_password")
        self.login_submit = QtWidgets.QPushButton(self.login)
        self.login_submit.setGeometry(QtCore.QRect(400, 440, 361, 41))
        self.login_submit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.login_submit.setObjectName("login_submit")

        self.signup_screen = QtWidgets.QLineEdit(self.login)
        self.signup_screen.setGeometry(QtCore.QRect(90, 70, 141, 41))
        self.signup_screen.setObjectName("login_username")
        self.signup_screen = QtWidgets.QLineEdit(self.login)
        self.signup_screen.setGeometry(QtCore.QRect(90, 70, 141, 41))
        self.signup_screen.setObjectName("login_password")
        self.signup_screen = QtWidgets.QPushButton(self.login)
        self.signup_screen.setGeometry(QtCore.QRect(90, 70, 141, 41))
        self.signup_screen.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.signup_screen.setObjectName("signup_screen")



        self.pre_loginscreen.addTab(self.login, "")
        self.product = QtWidgets.QWidget()
        self.product.setObjectName("product")
        self.product_title = QtWidgets.QLabel(self.product)
        self.product_title.setGeometry(QtCore.QRect(16, 20, 1121, 71))
        self.product_title.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(158, 151, 255);")
        self.product_title.setAlignment(QtCore.Qt.AlignCenter)
        self.product_title.setObjectName("product_title")
        self.promocode_btn = QtWidgets.QPushButton(self.product)
        self.promocode_btn.setGeometry(QtCore.QRect(140, 40, 121, 31))
        self.promocode_btn.setObjectName("promocode_btn")

        self.product_btn = QtWidgets.QPushButton(self.product)
        self.product_btn.setGeometry(QtCore.QRect(350, 40, 121, 31))
        self.product_btn.setObjectName("product_btn")

        self.checkout_btn = QtWidgets.QPushButton(self.product)
        self.checkout_btn.setGeometry(QtCore.QRect(860, 40, 121, 31))
        self.checkout_btn.setObjectName("checkout_btn")
        self.checkout_screen = QtWidgets.QTabWidget(self.product)
        self.checkout_screen.setGeometry(QtCore.QRect(10, 80, 1131, 611))
        self.checkout_screen.setTabPosition(QtWidgets.QTabWidget.South)
        self.checkout_screen.setObjectName("checkout_screen")
        self.product_lists_screen = QtWidgets.QWidget()
        self.product_lists_screen.setObjectName("product_lists_screen")
        self.listWidget = QtWidgets.QListWidget(self.product_lists_screen)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 1121, 581))
        self.listWidget.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"border: none;")
        self.listWidget.setIconSize(QtCore.QSize(200, 200))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shirt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)

        item1 = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brown_pants.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item1.setIcon(icon)

        item2 = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bluejacket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item2.setIcon(icon)

        self.listWidget.addItem(item)
        self.listWidget.addItem(item1)
        self.listWidget.addItem(item2)

        self.checkout_screen.addTab(self.product_lists_screen, "")
        self.promo_code_screen = QtWidgets.QWidget()
        self.promo_code_screen.setObjectName("promo_code_screen")
        self.promo_codes_lists = QtWidgets.QListWidget(self.promo_code_screen)
        self.promo_codes_lists.setGeometry(QtCore.QRect(420, 30, 311, 461))
        self.promo_codes_lists.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.promo_codes_lists.setObjectName("promo_codes_lists")
        self.label = QtWidgets.QLabel(self.promo_code_screen)
        self.label.setGeometry(QtCore.QRect(420, 500, 311, 20))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.checkout_screen.addTab(self.promo_code_screen, "")
        self.checkout_tab = QtWidgets.QWidget()
        self.checkout_tab.setObjectName("self.checkout_tab")
        self.product_image = QtWidgets.QLabel(self.checkout_tab)
        self.product_image.setGeometry(QtCore.QRect(190, 60, 281, 301))
        self.product_image.setText("")
        self.product_image.setPixmap(QtGui.QPixmap("../../../Downloads/shirt.png"))
        self.product_image.setScaledContents(True)
        self.product_image.setObjectName("product_image")
        self.product_title_checkout = QtWidgets.QLabel(self.checkout_tab)
        self.product_title_checkout.setGeometry(QtCore.QRect(470, 70, 571, 51))
        self.product_title_checkout.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.product_title_checkout.setObjectName("product_title_checkout")
        self.product_price = QtWidgets.QLabel(self.checkout_tab)
        self.product_price.setGeometry(QtCore.QRect(470, 120, 291, 61))
        self.product_price.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.product_price.setObjectName("product_price")
        self.product_coupon_code = QtWidgets.QLineEdit(self.checkout_tab)
        self.product_coupon_code.setGeometry(QtCore.QRect(460, 190, 201, 31))
        self.product_coupon_code.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.product_coupon_code.setObjectName("product_coupon_code")
        self.cupon_code_tbn = QtWidgets.QPushButton(self.checkout_tab)
        self.cupon_code_tbn.setGeometry(QtCore.QRect(690, 190, 81, 31))
        self.cupon_code_tbn.setObjectName("cupon_code_tbn")
        self.product_checkout = QtWidgets.QPushButton(self.checkout_tab)
        self.product_checkout.setGeometry(QtCore.QRect(470, 270, 291, 61))
        self.product_checkout.setStyleSheet("background-color: rgb(111, 107, 180);\n"
"color: rgb(255, 255, 255);\n"
"font: 30pt \"MS Shell Dlg 2\";")
        self.product_checkout.setObjectName("product_checkout")
        self.background_checkout = QtWidgets.QLabel(self.checkout_tab)
        self.background_checkout.setGeometry(QtCore.QRect(240, 50, 691, 421))
        self.background_checkout.setStyleSheet("background-color: rgb(146, 140, 236);\n"
"border-radius: 30px;")
        self.background_checkout.setText("")
        self.background_checkout.setObjectName("background_checkout")
        self.background_checkout.raise_()
        self.product_image.raise_()
        self.product_title_checkout.raise_()
        self.product_price.raise_()
        self.product_coupon_code.raise_()
        self.cupon_code_tbn.raise_()
        self.product_checkout.raise_()
        self.checkout_screen.addTab(self.checkout_tab, "")
        self.pre_loginscreen.addTab(self.product, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pre_loginscreen.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.signup_submit.clicked.connect(self.create_account)
        self.login_submit.clicked.connect(self.login_account)
        self.signup_screen.clicked.connect(lambda x: ScreenNavigate().screen_change(self.pre_loginscreen, 0))
        self.promocode_btn.clicked.connect(lambda x: ScreenNavigate().screen_change(self.checkout_screen, 1))
        self.checkout_btn.clicked.connect(lambda x: ScreenNavigate().screen_change(self.checkout_screen, 2))
        self.product_btn.clicked.connect(lambda x: ScreenNavigate().screen_change(self.checkout_screen, 0))

        self.listWidget.itemClicked.connect(self.item_clicked)
        PromoCode(self.promo_codes_lists)


        self.promo_codes_lists.itemDoubleClicked.connect(lambda x: PromoCode.clipboard(x.text()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "DISCOUNTER"))
        self.madeby.setText(_translate("MainWindow", "Made by: GUNTAAS"))
        self.signup_title.setText(_translate("MainWindow", "SIGNUP"))
        self.sign_up_username.setPlaceholderText(_translate("MainWindow", "USERNAME"))
        self.sign_up_password.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.signup_submit.setText(_translate("MainWindow", "SIGNUP"))
        self.pre_loginscreen.setTabText(self.pre_loginscreen.indexOf(self.signup), _translate("MainWindow", "Tab 1"))
        self.madeby1.setText(_translate("MainWindow", "Made by: GUNTAAS"))
        self.title1.setText(_translate("MainWindow", "DISCOUNTER"))
        self.signup_title_2.setText(_translate("MainWindow", "LOGIN"))
        self.login_username.setPlaceholderText(_translate("MainWindow", "USERNAME"))
        self.login_password.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.login_submit.setText(_translate("MainWindow", "SUBMIT"))
        self.signup_screen.setText('SignUp')
        self.pre_loginscreen.setTabText(self.pre_loginscreen.indexOf(self.login), _translate("MainWindow", "Tab 2"))
        self.product_title.setText(_translate("MainWindow", "Products"))
        self.promocode_btn.setText(_translate("MainWindow", "PROMO-CODES"))
        self.product_btn.setText('PRODUCTS')
        self.checkout_btn.setText(_translate("MainWindow", "CHECKOUT"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Blue Color Shirt"))

        item1 = self.listWidget.item(1)
        item1.setText(_translate("MainWindow", "Brown Color Pants"))

        item2 = self.listWidget.item(2)
        item2.setText(_translate("MainWindow", "Blue Color Jacket"))

        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.checkout_screen.setTabText(self.checkout_screen.indexOf(self.product_lists_screen), _translate("MainWindow", "Tab 1"))
        self.label.setText(_translate("MainWindow", "Double click on the item to copy the promo code"))
        self.checkout_screen.setTabText(self.checkout_screen.indexOf(self.promo_code_screen), _translate("MainWindow", "Tab 2"))
        self.product_title_checkout.setText(_translate("MainWindow", "NO ITEM SELECTED"))
        self.product_price.setText(_translate("MainWindow", "Price: $Nan"))
        self.product_coupon_code.setPlaceholderText(_translate("MainWindow", "Apply Coupon Code"))
        self.cupon_code_tbn.setText(_translate("MainWindow", "Apply"))
        self.product_checkout.setText(_translate("MainWindow", "CHECK OUT"))
        self.checkout_screen.setTabText(self.checkout_screen.indexOf(self.checkout_tab), _translate("MainWindow", "Page"))
        self.pre_loginscreen.setTabText(self.pre_loginscreen.indexOf(self.product), _translate("MainWindow", "Page"))


    def create_account(self):
        SignUp().create_account(self.sign_up_username.text(), self.sign_up_password.text(), self.pre_loginscreen)


    def login_account(self):
        Login().read_account(self.login_username, self.login_password, self.pre_loginscreen)


    def item_clicked(self,item_num):
        Product.product_checkout(self.checkout_screen, item_num, self.product_title_checkout, self.product_price, random.randint(15,30), self.product_image)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
