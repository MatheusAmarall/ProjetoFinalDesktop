from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QToolButton, QVBoxLayout,
    QWidget, QMessageBox)
from infra.entities.pedido import Pedido
from infra.entities.item import Item
from infra.repository.item_repository import ItemRepository
from infra.repository.pedido_repository import PedidoRepository
from datetime import datetime

class NovoPedido(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1124, 689)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setStyleSheet(u"background-color:#222;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:#222;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_13)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(307, 10, 16, 16))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setStyleSheet(u"image: url(images/bugui.png);\n"
"")
        self.label.setPixmap(QPixmap(u"buguii.png"))
        self.label.setScaledContents(True)
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(296, 10, 16, 16))
        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 16, 16))
        self.label_7 = QLabel(self.frame_13)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 0, 50, 50))
        self.label_7.setMaximumSize(QSize(50, 50))
        self.label_7.setPixmap(QPixmap(u"images/bugui.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(False)
        self.label_7.setMargin(0)
        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 0, 221, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setStyleSheet(u"color: #c77f14;\n"
"font-size: 40px;")

        self.verticalLayout_3.addWidget(self.frame_13)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 50))
        self.label_5.setStyleSheet(u"font-size: 40px;\n"
"color: #fcba03;")

        self.verticalLayout_2.addWidget(self.label_5)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 20))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.txt_nome = QLineEdit(self.frame_7)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(500, 20, 211, 20))
        self.cb_ham = QComboBox(self.frame_7)
        self.cb_ham.addItem("")
        self.cb_ham.addItem("")
        self.cb_ham.addItem("")
        self.cb_ham.addItem("")
        self.cb_ham.setObjectName(u"cb_ham")
        self.cb_ham.setGeometry(QRect(500, 50, 211, 22))
        self.cb_bebida = QComboBox(self.frame_7)
        self.cb_bebida.addItem("")
        self.cb_bebida.addItem("")
        self.cb_bebida.addItem("")
        self.cb_bebida.addItem("")
        self.cb_bebida.setObjectName(u"cb_bebida")
        self.cb_bebida.setGeometry(QRect(500, 80, 211, 22))
        self.cb_acompanha = QComboBox(self.frame_7)
        self.cb_acompanha.addItem("")
        self.cb_acompanha.addItem("")
        self.cb_acompanha.addItem("")
        self.cb_acompanha.addItem("")
        self.cb_acompanha.setObjectName(u"cb_acompanha")
        self.cb_acompanha.setGeometry(QRect(500, 110, 211, 22))
        self.btn_voltar = QToolButton(self.frame_7)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setGeometry(QRect(20, 290, 75, 23))
        self.btn_voltar.setStyleSheet(u"QToolButton{\n"
" \n"
"  border: none;\n"
"  border-radius: 4px;\n"
"  cursor: pointer; \n"
"}\n"
"\n"
"button:hover {\n"
"  background-color: #45a049;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btn_cadastrar = QPushButton(self.frame_7)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(1020, 290, 75, 23))
        self.sp_qtd = QSpinBox(self.frame_7)
        self.sp_qtd.setObjectName(u"sp_qtd")
        self.sp_qtd.setGeometry(QRect(651, 150, 61, 22))
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(500, 150, 141, 20))
        self.btn_excluir = QPushButton(self.frame_7)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setGeometry(QRect(490, 290, 75, 23))

        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setStyleSheet(u"background-color:#222;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.frame_8)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setStyleSheet(u"\n"
"background-color:#222;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #c77f14;\n"
"font-size: 15px;")

        self.verticalLayout.addWidget(self.label_4)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.verticalLayout_4.addWidget(self.frame_8)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.btn_cadastrar.clicked.connect(self.salvar_pedido)
        self.btn_voltar.clicked.connect(self.limpar_campos)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_3.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PalhoBurger", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Monte seu combo:</p></body></html>", None))
        self.cb_ham.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE SEU HAMBURGUER", None))
        self.cb_ham.setItemText(1, QCoreApplication.translate("MainWindow", u"X-Salada", None))
        self.cb_ham.setItemText(2, QCoreApplication.translate("MainWindow", u"X-cora\u00e7\u00e3o", None))
        self.cb_ham.setItemText(3, QCoreApplication.translate("MainWindow", u"X-PalhoBurger", None))

        self.cb_bebida.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE SUA BEBIDA", None))
        self.cb_bebida.setItemText(1, QCoreApplication.translate("MainWindow", u"Agua", None))
        self.cb_bebida.setItemText(2, QCoreApplication.translate("MainWindow", u"Coca cola", None))
        self.cb_bebida.setItemText(3, QCoreApplication.translate("MainWindow", u"Pepsi", None))

        self.cb_acompanha.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE SEU ACOMPANHAMENTO", None))
        self.cb_acompanha.setItemText(1, QCoreApplication.translate("MainWindow", u"Batata frita", None))
        self.cb_acompanha.setItemText(2, QCoreApplication.translate("MainWindow", u"Aneis de cebola", None))
        self.cb_acompanha.setItemText(3, QCoreApplication.translate("MainWindow", u"Nuggets", None))

        self.btn_voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"SELECIONE A QUANTIDADE", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">PalhoBurger \u00a9 2023</span></p></body></html>", None))
    # retranslateUi



    def salvar_pedido(self):
        print("asdsad")
        # dbPedido = PedidoRepository()
        # dbItem = ItemRepository()
        #
        # pedido = Pedido(
        #     cliente=self.txt_nome.text(),
        #     data=datetime.now()
        # )
        #
        # if self.btn_cadastrar.text() == 'CADASTRAR':
        #     retornoPedido = dbPedido.insert(pedido)
        #
        #     item = Item(
        #         descricao=self.cb_ham.currentText(),
        #         quantidade=self.sp_qtd.text(),
        #         id_pedido=pedido.id
        #     )
        #
        #     retornoItem = dbItem.insert(item)
        #     if retornoPedido == 'OK' and retornoItem == 'OK':
        #         msg = QMessageBox()
        #         msg.setIcon(QMessageBox.Information)
        #         msg.setWindowTitle('Cadastro realizado')
        #         msg.setText('Cadastro realizado com sucesso')
        #         msg.exec()
        #
        #         self.limpar_campos()
        #     else:
        #         msg = QMessageBox()
        #         msg.setIcon(QMessageBox.Critical)
        #         msg.setWindowTitle('Erro ao cadastrar')
        #         msg.setText(f'Erro ao cadastrar o cliente, verifique os dados')
        #         msg.exec()
        # elif self.btn_cadastrar.text() == 'ATUALIZAR':
        #     print("atualizar")
        #     # retorno = db.update(cliente)
        #     #
        #     # if retorno == 'OK':
        #     #     msg = QMessageBox()
        #     #     msg.setIcon(QMessageBox.Information)
        #     #     msg.setWindowTitle('Atualizar')
        #     #     msg.setText('Usuario editado com sucesso')
        #     #     msg.exec()
        #     #
        #     #     self.limpar_campos()

    def limpar_campos(self):
        print("limpou")
        # for widget in self.widgetDados.children():
        #     if isinstance(widget, QLineEdit):
        #         widget.setText("")
        #     elif isinstance(widget, QComboBox):
        #         widget.setCurrentIndex(0)
        #
        # for widget in self.widgetEndereco.children():
        #     if isinstance(widget, QLineEdit):
        #         widget.setText("")
        #
        # self.btn_salvar.setText('Salvar')
        # self.btn_remover.setVisible(False)
        # self.txt_cpf.setReadOnly(False)

    # def home(self):
    #     self.parent().show()
    #     self.close()

