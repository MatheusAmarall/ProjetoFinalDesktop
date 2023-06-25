from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget, QAbstractItemView)
from infra.entities.pedido import Pedido
from infra.entities.item import Item
from infra.repository.item_repository import ItemRepository
from infra.repository.pedido_repository import PedidoRepository
from infra.configs.connection import DBConnectionHandler
from view.novopedido import NovoPedido

class Home(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(941, 693)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.mainWindow = MainWindow
        conn = DBConnectionHandler()

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color:#222;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:#222;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_13)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_13)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setStyleSheet(u"image: url(images/bugui.png);\n"
"")
        self.label.setPixmap(QPixmap(u"images/bugui.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #c77f14;\n"
"font-size: 40px;")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(467, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_novo = QToolButton(self.frame_13)
        self.btn_novo.setObjectName(u"btn_novo")
        self.btn_novo.setStyleSheet(u"QToolButton {\n"
"    background-color: transparent;\n"
"    color: #fcba03;\n"
"    font-size: 15px;\n"
"    border: none;\n"
"	cursor: pointer;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    color: #fdcf4f;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_novo)


        self.horizontalLayout_2.addWidget(self.frame_13)


        self.verticalLayout_5.addWidget(self.frame)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size: 40px;\n"
"color: #fcba03;")

        self.verticalLayout_2.addWidget(self.label_5)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_9)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tb_pedidos = QTableWidget(self.frame_6)
        self.tb_pedidos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_pedidos.verticalHeader().setVisible(False)
        self.tb_pedidos.setSelectionBehavior(QAbstractItemView.SelectRows)
        if (self.tb_pedidos.columnCount() < 4):
            self.tb_pedidos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_pedidos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_pedidos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_pedidos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_pedidos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_pedidos.setObjectName(u"tb_pedidos")
        self.tb_pedidos.setMaximumSize(QSize(16777215, 200))
        self.tb_pedidos.setWordWrap(True)
        self.tb_pedidos.setCornerButtonEnabled(True)
        self.tb_pedidos.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_pedidos.horizontalHeader().setDefaultSectionSize(200)
        self.tb_pedidos.horizontalHeader().setHighlightSections(True)
        self.tb_pedidos.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_pedidos.horizontalHeader().setStretchLastSection(True)
        self.tb_pedidos.verticalHeader().setCascadingSectionResizes(False)
        self.tb_pedidos.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.tb_pedidos)


        self.verticalLayout_10.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color:#222;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.frame_8)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 100))
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


        self.verticalLayout_10.addWidget(self.frame_8)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.btn_novo.clicked.connect(self.novo_pedido)
        self.tb_pedidos.cellDoubleClicked.connect(self.visulizar_pedido)
        self.popula_tabela_pedidos()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PalhoBurger", None))
        self.btn_novo.setText(QCoreApplication.translate("MainWindow", u"NOVO PEDIDO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;\">Pedidos feitos:</span></p></body></html>", None))
        ___qtablewidgetitem = self.tb_pedidos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tb_pedidos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None));
        ___qtablewidgetitem2 = self.tb_pedidos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem3 = self.tb_pedidos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">PalhoBurger \u00a9 2023</span></p></body></html>", None))
    # retranslateUi

    def novo_pedido(self):
        self.window = QMainWindow()
        self.ui = NovoPedido()
        self.ui.setupUi(self.window)
        self.window.show()
        self.mainWindow.hide()

    def visulizar_pedido(self, row):
        dbPedido = PedidoRepository()
        pedido = dbPedido.select(self.tb_pedidos.item(row, 0).text())
        dbItem = ItemRepository()
        item = dbItem.select(pedido.id)

        self.window = QMainWindow()
        self.ui = NovoPedido()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.popula_visualizacao(item, pedido)
        self.mainWindow.hide()

    def popula_tabela_pedidos(self):
        self.tb_pedidos.setRowCount(0)
        db = PedidoRepository()
        lista_pedidos = db.select_all()
        self.tb_pedidos.setRowCount(len(lista_pedidos))

        for linha, pedido in enumerate(lista_pedidos):
            valores_pedido = [pedido.id, pedido.numero, pedido.cliente, pedido.data]
            for coluna, valor in enumerate(valores_pedido):
                self.tb_pedidos.setItem(linha, coluna, QTableWidgetItem(str(valor)))

