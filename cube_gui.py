from PyQt5 import QtWidgets, QtGui, QtCore
from rubik_cube import Rubik_cube

class MovieSplashScreen(QtWidgets.QSplashScreen):
    def __init__(self,pathToGIF):
        self.movie = QtGui.QMovie(pathToGIF)
        self.movie.setScaledSize(QtCore.QSize(512,512))
        self.movie.jumpToFrame(0)
        pixmap = QtGui.QPixmap(self.movie.frameRect().size())
        QtWidgets.QSplashScreen.__init__(self,pixmap)
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self,event):
        self.movie.start()

    def hideEvent(self, event):
        self.movie.stop()

    def paintEvent(self,event):
        painter = QtGui.QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0,0,pixmap)

class CubeWindow(QtWidgets.QWidget, Rubik_cube):
    def __init__(self):
        QtWidgets.QWidget.__init__(self,parent=None)
        pal = self.palette()
        pal.setColor(
            QtGui.QPalette.Normal,QtGui.QPalette.Window,
            QtGui.QColor("#224443")
        )
        self.setPalette(pal)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        """ cube's front buttons """
        self.button_f1 = QtWidgets.QPushButton("")
        self.button_f2 = QtWidgets.QPushButton("")
        self.button_f3 = QtWidgets.QPushButton("")
        self.button_f4 = QtWidgets.QPushButton("")
        self.button_f5 = QtWidgets.QPushButton("")
        self.button_f6 = QtWidgets.QPushButton("")
        self.button_f7 = QtWidgets.QPushButton("")
        self.button_f8 = QtWidgets.QPushButton("")
        self.button_f9 = QtWidgets.QPushButton("")
        self.button_f1.setFixedSize(57,57)
        self.button_f2.setFixedSize(57,57)
        self.button_f3.setFixedSize(57,57)
        self.button_f4.setFixedSize(57,57)
        self.button_f5.setFixedSize(57,57)
        self.button_f6.setFixedSize(57,57)
        self.button_f7.setFixedSize(57,57)
        self.button_f8.setFixedSize(57,57)
        self.button_f9.setFixedSize(57,57)
        self.button_f1.setCheckable(True)
        self.button_f2.setCheckable(True)
        self.button_f3.setCheckable(True)
        self.button_f4.setCheckable(True)
        self.button_f5.setCheckable(True)
        self.button_f6.setCheckable(True)
        self.button_f7.setCheckable(True)
        self.button_f8.setCheckable(True)
        self.button_f9.setCheckable(True)
        group_fg = QtWidgets.QGridLayout()
        group_fg.addWidget(self.button_f1,0,0)
        group_fg.addWidget(self.button_f2,0,1)
        group_fg.addWidget(self.button_f3,0,2)
        group_fg.addWidget(self.button_f4,1,0)
        group_fg.addWidget(self.button_f5,1,1)
        group_fg.addWidget(self.button_f6,1,2)
        group_fg.addWidget(self.button_f7,2,0)
        group_fg.addWidget(self.button_f8,2,1)
        group_fg.addWidget(self.button_f9,2,2)
        group_fg.setSpacing(0)
        group_fg.setObjectName("front")
        """ cube's left labels """
        self.label_l1 = QtWidgets.QLabel("")
        self.label_l2 = QtWidgets.QLabel("")
        self.label_l3 = QtWidgets.QLabel("")
        self.label_l4 = QtWidgets.QLabel("")
        self.label_l5 = QtWidgets.QLabel("")
        self.label_l6 = QtWidgets.QLabel("")
        self.label_l7 = QtWidgets.QLabel("")
        self.label_l8 = QtWidgets.QLabel("")
        self.label_l9 = QtWidgets.QLabel("")
        self.label_l1.setFixedSize(30,30)
        self.label_l2.setFixedSize(30,30)
        self.label_l3.setFixedSize(30,30)
        self.label_l4.setFixedSize(30,30)
        self.label_l5.setFixedSize(30,30)
        self.label_l6.setFixedSize(30,30)
        self.label_l7.setFixedSize(30,30)
        self.label_l8.setFixedSize(30,30)
        self.label_l9.setFixedSize(30,30)
        group_lg = QtWidgets.QGridLayout()
        group_lg.addWidget(self.label_l1,0,0)
        group_lg.addWidget(self.label_l2,0,1)
        group_lg.addWidget(self.label_l3,0,2)
        group_lg.addWidget(self.label_l4,1,0)
        group_lg.addWidget(self.label_l5,1,1)
        group_lg.addWidget(self.label_l6,1,2)
        group_lg.addWidget(self.label_l7,2,0)
        group_lg.addWidget(self.label_l8,2,1)
        group_lg.addWidget(self.label_l9,2,2)
        group_lg.setSpacing(0)
        group_lg.setObjectName("left")
        """ cube's right labels """
        self.label_r1 = QtWidgets.QLabel("")
        self.label_r2 = QtWidgets.QLabel("")
        self.label_r3 = QtWidgets.QLabel("")
        self.label_r4 = QtWidgets.QLabel("")
        self.label_r5 = QtWidgets.QLabel("")
        self.label_r6 = QtWidgets.QLabel("")
        self.label_r7 = QtWidgets.QLabel("")
        self.label_r8 = QtWidgets.QLabel("")
        self.label_r9 = QtWidgets.QLabel("")
        self.label_r1.setFixedSize(30,30)
        self.label_r2.setFixedSize(30,30)
        self.label_r3.setFixedSize(30,30)
        self.label_r4.setFixedSize(30,30)
        self.label_r5.setFixedSize(30,30)
        self.label_r6.setFixedSize(30,30)
        self.label_r7.setFixedSize(30,30)
        self.label_r8.setFixedSize(30,30)
        self.label_r9.setFixedSize(30,30)
        group_rg = QtWidgets.QGridLayout()
        group_rg.addWidget(self.label_r1,0,0)
        group_rg.addWidget(self.label_r2,0,1)
        group_rg.addWidget(self.label_r3,0,2)
        group_rg.addWidget(self.label_r4,1,0)
        group_rg.addWidget(self.label_r5,1,1)
        group_rg.addWidget(self.label_r6,1,2)
        group_rg.addWidget(self.label_r7,2,0)
        group_rg.addWidget(self.label_r8,2,1)
        group_rg.addWidget(self.label_r9,2,2)
        group_rg.setSpacing(0)
        group_rg.setObjectName("right")
        """ cube's top labels """
        self.label_t1 = QtWidgets.QLabel("")
        self.label_t2 = QtWidgets.QLabel("")
        self.label_t3 = QtWidgets.QLabel("")
        self.label_t4 = QtWidgets.QLabel("")
        self.label_t5 = QtWidgets.QLabel("")
        self.label_t6 = QtWidgets.QLabel("")
        self.label_t7 = QtWidgets.QLabel("")
        self.label_t8 = QtWidgets.QLabel("")
        self.label_t9 = QtWidgets.QLabel("")
        self.label_t1.setFixedSize(30,30)
        self.label_t2.setFixedSize(30,30)
        self.label_t3.setFixedSize(30,30)
        self.label_t4.setFixedSize(30,30)
        self.label_t5.setFixedSize(30,30)
        self.label_t6.setFixedSize(30,30)
        self.label_t7.setFixedSize(30,30)
        self.label_t8.setFixedSize(30,30)
        self.label_t9.setFixedSize(30,30)
        group_tg = QtWidgets.QGridLayout()
        group_tg.addWidget(self.label_t1,0,0)
        group_tg.addWidget(self.label_t2,0,1)
        group_tg.addWidget(self.label_t3,0,2)
        group_tg.addWidget(self.label_t4,1,0)
        group_tg.addWidget(self.label_t5,1,1)
        group_tg.addWidget(self.label_t6,1,2)
        group_tg.addWidget(self.label_t7,2,0)
        group_tg.addWidget(self.label_t8,2,1)
        group_tg.addWidget(self.label_t9,2,2)
        group_tg.setSpacing(0)
        group_tg.setObjectName("top")
        """ cube's bot labels """
        self.label_b1 = QtWidgets.QLabel("")
        self.label_b2 = QtWidgets.QLabel("")
        self.label_b3 = QtWidgets.QLabel("")
        self.label_b4 = QtWidgets.QLabel("")
        self.label_b5 = QtWidgets.QLabel("")
        self.label_b6 = QtWidgets.QLabel("")
        self.label_b7 = QtWidgets.QLabel("")
        self.label_b8 = QtWidgets.QLabel("")
        self.label_b9 = QtWidgets.QLabel("")
        self.label_b1.setFixedSize(30,30)
        self.label_b2.setFixedSize(30,30)
        self.label_b3.setFixedSize(30,30)
        self.label_b4.setFixedSize(30,30)
        self.label_b5.setFixedSize(30,30)
        self.label_b6.setFixedSize(30,30)
        self.label_b7.setFixedSize(30,30)
        self.label_b8.setFixedSize(30,30)
        self.label_b9.setFixedSize(30,30)
        group_bg = QtWidgets.QGridLayout()
        group_bg.addWidget(self.label_b1,0,0)
        group_bg.addWidget(self.label_b2,0,1)
        group_bg.addWidget(self.label_b3,0,2)
        group_bg.addWidget(self.label_b4,1,0)
        group_bg.addWidget(self.label_b5,1,1)
        group_bg.addWidget(self.label_b6,1,2)
        group_bg.addWidget(self.label_b7,2,0)
        group_bg.addWidget(self.label_b8,2,1)
        group_bg.addWidget(self.label_b9,2,2)
        group_bg.setSpacing(0)
        group_bg.setObjectName("bot")
        """ cube's back labels """
        self.label_bc1 = QtWidgets.QLabel("")
        self.label_bc2 = QtWidgets.QLabel("")
        self.label_bc3 = QtWidgets.QLabel("")
        self.label_bc4 = QtWidgets.QLabel("")
        self.label_bc5 = QtWidgets.QLabel("")
        self.label_bc6 = QtWidgets.QLabel("")
        self.label_bc7 = QtWidgets.QLabel("")
        self.label_bc8 = QtWidgets.QLabel("")
        self.label_bc9 = QtWidgets.QLabel("")
        self.label_bc1.setFixedSize(30,30)
        self.label_bc2.setFixedSize(30,30)
        self.label_bc3.setFixedSize(30,30)
        self.label_bc4.setFixedSize(30,30)
        self.label_bc5.setFixedSize(30,30)
        self.label_bc6.setFixedSize(30,30)
        self.label_bc7.setFixedSize(30,30)
        self.label_bc8.setFixedSize(30,30)
        self.label_bc9.setFixedSize(30,30)
        group_bcg = QtWidgets.QGridLayout()
        group_bcg.addWidget(self.label_bc1,0,0)
        group_bcg.addWidget(self.label_bc2,0,1)
        group_bcg.addWidget(self.label_bc3,0,2)
        group_bcg.addWidget(self.label_bc4,1,0)
        group_bcg.addWidget(self.label_bc5,1,1)
        group_bcg.addWidget(self.label_bc6,1,2)
        group_bcg.addWidget(self.label_bc7,2,0)
        group_bcg.addWidget(self.label_bc8,2,1)
        group_bcg.addWidget(self.label_bc9,2,2)
        group_bcg.setSpacing(0)
        group_bcg.setObjectName("back")
        """ arrows """
        self.up_but = QtWidgets.QPushButton("")
        self.down_but = QtWidgets.QPushButton("")
        self.left_but = QtWidgets.QPushButton("")
        self.right_but = QtWidgets.QPushButton("")
        self.around_but = QtWidgets.QPushButton("")
        self.reverse_but = QtWidgets.QPushButton("")
        self.up_but.setFixedSize(30,30)
        self.down_but.setFixedSize(30,30)
        self.left_but.setFixedSize(30,30)
        self.right_but.setFixedSize(30,30)
        self.around_but.setFixedSize(30,30)
        self.reverse_but.setFixedSize(30,30)
        self.up_but.setIcon(QtGui.QIcon("media\\up.png"))
        self.down_but.setIcon(QtGui.QIcon("media\\down.png"))
        self.left_but.setIcon(QtGui.QIcon("media\\left.png"))
        self.right_but.setIcon(QtGui.QIcon("media\\right.png"))
        self.around_but.setIcon(QtGui.QIcon("media\\around"))
        self.reverse_but.setIcon(QtGui.QIcon("media\\reverse"))
        self.up_but.setIconSize(QtCore.QSize(30,30))
        self.down_but.setIconSize(QtCore.QSize(30,30))
        self.left_but.setIconSize(QtCore.QSize(30,30))
        self.right_but.setIconSize(QtCore.QSize(30,30))
        self.around_but.setIconSize(QtCore.QSize(30,30))
        self.reverse_but.setIconSize(QtCore.QSize(30,30))
        group_cb = QtWidgets.QGridLayout()
        group_cb.addWidget(self.up_but,0,0)
        group_cb.addWidget(self.down_but,0,2)
        group_cb.addWidget(self.left_but,1,0)
        group_cb.addWidget(self.right_but,1,2)
        group_cb.addWidget(self.reverse_but,2,0)
        group_cb.addWidget(self.around_but,2,2)
        group_cb.setObjectName("control_buttons")
        """ control edges buttons """
        self.button_lc1 = QtWidgets.QPushButton("")
        self.button_lc2 = QtWidgets.QPushButton("")
        self.button_lc3 = QtWidgets.QPushButton("")
        self.button_rc1 = QtWidgets.QPushButton("")
        self.button_rc2 = QtWidgets.QPushButton("")
        self.button_rc3 = QtWidgets.QPushButton("")
        self.button_tc1 = QtWidgets.QPushButton("")
        self.button_tc2 = QtWidgets.QPushButton("")
        self.button_tc3 = QtWidgets.QPushButton("")
        self.button_bc1 = QtWidgets.QPushButton("")
        self.button_bc2 = QtWidgets.QPushButton("")
        self.button_bc3 = QtWidgets.QPushButton("")
        self.button_lc1.setFixedSize(30,30)
        self.button_lc2.setFixedSize(30,30)
        self.button_lc3.setFixedSize(30,30)
        self.button_rc1.setFixedSize(30,30)
        self.button_rc2.setFixedSize(30,30)
        self.button_rc3.setFixedSize(30,30)
        self.button_tc1.setFixedSize(30,30)
        self.button_tc2.setFixedSize(30,30)
        self.button_tc3.setFixedSize(30,30)
        self.button_bc1.setFixedSize(30,30)
        self.button_bc2.setFixedSize(30,30)
        self.button_bc3.setFixedSize(30,30)
        self.button_lc1.setIcon(QtGui.QIcon("media\\left.png"))
        self.button_lc2.setIcon(QtGui.QIcon("media\\left.png"))
        self.button_lc3.setIcon(QtGui.QIcon("media\\left.png"))
        self.button_rc1.setIcon(QtGui.QIcon("media\\right.png"))
        self.button_rc2.setIcon(QtGui.QIcon("media\\right.png"))
        self.button_rc3.setIcon(QtGui.QIcon("media\\right.png"))
        self.button_tc1.setIcon(QtGui.QIcon("media\\up.png"))
        self.button_tc2.setIcon(QtGui.QIcon("media\\up.png"))
        self.button_tc3.setIcon(QtGui.QIcon("media\\up.png"))
        self.button_bc1.setIcon(QtGui.QIcon("media\\down.png"))
        self.button_bc2.setIcon(QtGui.QIcon("media\\down.png"))
        self.button_bc3.setIcon(QtGui.QIcon("media\\down.png"))
        self.button_lc1.setIconSize(QtCore.QSize(30,30))
        self.button_lc2.setIconSize(QtCore.QSize(30,30))
        self.button_lc3.setIconSize(QtCore.QSize(30,30))
        self.button_rc1.setIconSize(QtCore.QSize(30,30))
        self.button_rc2.setIconSize(QtCore.QSize(30,30))
        self.button_rc3.setIconSize(QtCore.QSize(30,30))
        self.button_tc1.setIconSize(QtCore.QSize(30,30))
        self.button_tc2.setIconSize(QtCore.QSize(30,30))
        self.button_tc3.setIconSize(QtCore.QSize(30,30))
        self.button_bc1.setIconSize(QtCore.QSize(30,30))
        self.button_bc2.setIconSize(QtCore.QSize(30,30))
        self.button_bc3.setIconSize(QtCore.QSize(30,30))
        self.button_lc1.setEnabled(False)
        self.button_lc2.setEnabled(False)
        self.button_lc3.setEnabled(False)
        self.button_rc1.setEnabled(False)
        self.button_rc2.setEnabled(False)
        self.button_rc3.setEnabled(False)
        self.button_tc1.setEnabled(False)
        self.button_tc2.setEnabled(False)
        self.button_tc3.setEnabled(False)
        self.button_bc1.setEnabled(False)
        self.button_bc2.setEnabled(False)
        self.button_bc3.setEnabled(False)

        """ self.undo_but = QtWidgets.QPushButton("Undo")
        self.redo_but = QtWidgets.QPushButton("Redo")
        self.undo_but.setStyleSheet("background: #b01030; font: bold;")
        self.redo_but.setStyleSheet("background: #b01030; font: bold;")
        self.undo_but.setFixedSize(30,30)
        self.redo_but.setFixedSize(30,30) """
        
        robut = QtWidgets.QPushButton("MIX")
        robut.setStyleSheet("background: #b01030; font: bold;")
        robut.setFixedSize(70,30)
        robut.setToolTip("Press to random mix cube")
        robut.setToolTipDuration(-1)
        ebut = QtWidgets.QPushButton("EXIT")
        ebut.setStyleSheet("background: #b01030; font: bold;")
        ebut.setFixedSize(70,30)
        ebut.setToolTip("Press EXIT to close game")
        ebut.setToolTipDuration(-1)

        """ r_u_grid = QtWidgets.QGridLayout()
        r_u_grid.addWidget(robut,0,0)
        r_u_grid.addWidget(self.redo_but,1,0)
        r_u_grid.addWidget(self.undo_but,1,1)
        self.count = -1 """

        self.group_grid = QtWidgets.QGridLayout()
        self.group_grid.addLayout(group_fg,1,1,alignment = QtCore.Qt.AlignCenter)
        self.group_grid.addLayout(group_lg,1,0,alignment = QtCore.Qt.AlignRight)
        self.group_grid.addLayout(group_rg,1,2,alignment = QtCore.Qt.AlignLeft)
        self.group_grid.addLayout(group_tg,0,1,alignment = QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.group_grid.addLayout(group_bg,2,1,alignment = QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.group_grid.addLayout(group_bcg,0,2,alignment = QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
        self.group_grid.addLayout(group_cb,2,0)
        self.group_grid.addWidget(robut,0,0,alignment = QtCore.Qt.AlignHCenter)
        #self.group_grid.addLayout(r_u_grid,0,0)
        self.group_grid.addWidget(ebut,2,2,alignment = QtCore.Qt.AlignCenter)
        self.group_grid.setRowMinimumHeight(0,171)
        self.group_grid.setRowMinimumHeight(1,171)
        self.group_grid.setRowMinimumHeight(2,171)
        self.group_grid.setColumnMinimumWidth(0,171)
        self.group_grid.setColumnMinimumWidth(1,171)
        self.group_grid.setColumnMinimumWidth(2,171)
        self.setStyleSheet("QPushButton {background: #487054;}")
        self.coloring()
        #self.group_grid.setSpacing(0)
        self.setLayout(self.group_grid)
        #self.children = self.group_grid.findChildren(QtWidgets.QGridLayout,QtCore.QRegExp('\w'))
        self.setCursor(QtGui.QCursor(QtGui.QPixmap("media\\cursor.png"),0,0))
        self.up_but.clicked.connect(self.to_up)
        self.down_but.clicked.connect(self.to_down)
        self.left_but.clicked.connect(self.to_left)
        self.right_but.clicked.connect(self.to_right)
        self.around_but.clicked.connect(self.to_around)
        self.reverse_but.clicked.connect(self.to_reverse)
        self.button_f1.toggled.connect(self.f1_activated)
        self.button_f2.toggled.connect(self.f2_activated)
        self.button_f3.toggled.connect(self.f3_activated)
        self.button_f4.toggled.connect(self.f4_activated)
        self.button_f5.toggled.connect(self.f5_activated)
        self.button_f6.toggled.connect(self.f6_activated)
        self.button_f7.toggled.connect(self.f7_activated)
        self.button_f8.toggled.connect(self.f8_activated)
        self.button_f9.toggled.connect(self.f9_activated)
        self.button_lc1.clicked.connect(self.top_to_left)
        self.button_lc2.clicked.connect(self.mid_to_left)
        self.button_lc3.clicked.connect(self.bot_to_left)
        self.button_rc1.clicked.connect(self.top_to_right)
        self.button_rc2.clicked.connect(self.mid_to_right)
        self.button_rc3.clicked.connect(self.bot_to_right)
        self.button_tc1.clicked.connect(self.left_to_up)
        self.button_tc2.clicked.connect(self.center_to_up)
        self.button_tc3.clicked.connect(self.right_to_up)
        self.button_bc1.clicked.connect(self.left_to_down)
        self.button_bc2.clicked.connect(self.center_to_down)
        self.button_bc3.clicked.connect(self.right_to_down)
        robut.clicked.connect(self.mix_it_randomize)
        """ self.undo_but.clicked.connect(self.undo)
        self.redo_but.clicked.connect(self.redo) """
        ebut.clicked.connect(QtWidgets.qApp.quit)

    def coloring(self):
        colors = {
            'b':'blue','g':'green',
            'y':'yellow','w':'white',
            'r':'red','o':'orange',
        }
        for i in self.position[0].keys():
            child_g = self.group_grid.findChild(QtWidgets.QGridLayout,i)
            for j in range(child_g.rowCount()):
                for k in range(child_g.columnCount()):
                    ind = self.position[0][i][j][k]
                    if "QPushButton" in str(child_g.itemAtPosition(j,k).widget()):
                        child_g.itemAtPosition(j,k).widget().setStyleSheet("QPushButton {background: "\
                            +f"{colors[ind]}"+";}")
                    elif "QLabel" in str(child_g.itemAtPosition(j,k).widget()):
                        child_g.itemAtPosition(j,k).widget().setStyleSheet("QLabel {background: "\
                            +f"{colors[ind]}"+"; border: 1px groove black;}")
                    else:
                        pass
        
    def to_up(self):
        self.rotate_all("up")
        self.coloring()

    def to_down(self):
        self.rotate_all("down")
        self.coloring()

    def to_left(self):
        self.rotate_all("left")
        self.coloring()
    
    def to_right(self):
        self.rotate_all("right")
        self.coloring()

    def to_around(self):
        self.rotate_all("around")
        self.coloring()

    def to_reverse(self):
        self.rotate_all("reverse")
        self.coloring()

    def is_enabled_but(self):
        ans = any(
            [
                self.button_lc1.isEnabled(),
                self.button_lc2.isEnabled(),
                self.button_lc3.isEnabled(),
                self.button_rc1.isEnabled(),
                self.button_rc2.isEnabled(),
                self.button_rc3.isEnabled(),
                self.button_tc1.isEnabled(),
                self.button_tc2.isEnabled(),
                self.button_tc3.isEnabled(),
                self.button_bc1.isEnabled(),
                self.button_bc2.isEnabled(),
                self.button_bc3.isEnabled(),
            ]
        )
        return ans

    def is_toggled_but(self):
        ans = any([
            self.button_f1.isChecked(),
            self.button_f2.isChecked(),
            self.button_f3.isChecked(),
            self.button_f4.isChecked(),
            self.button_f5.isChecked(),
            self.button_f6.isChecked(),
            self.button_f7.isChecked(),
            self.button_f8.isChecked(),
            self.button_f9.isChecked(),
        ])
        return ans

    def f1_activated(self):
        if self.button_f1.isChecked():
            self.button_lc1.setEnabled(True)
            self.button_rc1.setEnabled(True)
            self.button_tc1.setEnabled(True)
            self.button_bc1.setEnabled(True)
            self.drawing_new_buts()
        else:
            if not any([self.button_f2.isChecked(), self.button_f3.isChecked()]):
                self.button_lc1.setEnabled(False)
                self.button_rc1.setEnabled(False)
            if not any([self.button_f4.isChecked(), self.button_f7.isChecked()]):
                self.button_tc1.setEnabled(False)
                self.button_bc1.setEnabled(False)
            self.drawing_new_buts()

    def f2_activated(self):
        if self.button_f2.isChecked():
            self.button_lc1.setEnabled(True)
            self.button_rc1.setEnabled(True)
            self.button_tc2.setEnabled(True)
            self.button_bc2.setEnabled(True)
            self.drawing_new_buts()
        else:
            if not any([self.button_f1.isChecked(), self.button_f3.isChecked()]):
                self.button_lc1.setEnabled(False)
                self.button_rc1.setEnabled(False)
            if not any([self.button_f5.isChecked(), self.button_f8.isChecked()]):
                self.button_tc2.setEnabled(False)
                self.button_bc2.setEnabled(False)
            self.drawing_new_buts()

    def f3_activated(self):
        if self.button_f3.isChecked():
            self.button_lc1.setEnabled(True)
            self.button_rc1.setEnabled(True)
            self.button_tc3.setEnabled(True)
            self.button_bc3.setEnabled(True)
            self.drawing_new_buts()
        else:
            if not any([self.button_f1.isChecked(), self.button_f2.isChecked()]):
                self.button_lc1.setEnabled(False)
                self.button_rc1.setEnabled(False)
            if not any([self.button_f6.isChecked(), self.button_f9.isChecked()]):
                self.button_tc3.setEnabled(False)
                self.button_bc3.setEnabled(False)
            self.drawing_new_buts()

    def f4_activated(self):
        if self.button_f4.isChecked():
            self.button_lc2.setEnabled(True)
            self.button_rc2.setEnabled(True)
            self.button_tc1.setEnabled(True)
            self.button_bc1.setEnabled(True)
            self.drawing_new_buts()
        else:
            if not any([self.button_f5.isChecked(), self.button_f6.isChecked()]):
                self.button_lc2.setEnabled(False)
                self.button_rc2.setEnabled(False)
            if not any([self.button_f1.isChecked(), self.button_f7.isChecked()]):
                self.button_tc1.setEnabled(False)
                self.button_bc1.setEnabled(False)
            self.drawing_new_buts()

    def f5_activated(self):
        if self.button_f5.isChecked():
            self.button_lc2.setEnabled(True)
            self.button_rc2.setEnabled(True)
            self.button_tc2.setEnabled(True)
            self.button_bc2.setEnabled(True)
            self.drawing_new_buts()
        else:
            if not any([self.button_f4.isChecked(), self.button_f6.isChecked()]):
                self.button_lc2.setEnabled(False)
                self.button_rc2.setEnabled(False)
            if not any([self.button_f2.isChecked(), self.button_f8.isChecked()]):
                self.button_tc2.setEnabled(False)
                self.button_bc2.setEnabled(False)
            self.drawing_new_buts()

    def f6_activated(self):
        if self.button_f6.isChecked():
            self.button_lc2.setEnabled(True)
            self.button_rc2.setEnabled(True)
            self.button_tc3.setEnabled(True)
            self.button_bc3.setEnabled(True)
            self.drawing_new_buts()
        else:
            if not any([self.button_f4.isChecked(), self.button_f5.isChecked()]):
                self.button_lc2.setEnabled(False)
                self.button_rc2.setEnabled(False)
            if not any([self.button_f3.isChecked(), self.button_f9.isChecked()]):
                self.button_tc3.setEnabled(False)
                self.button_bc3.setEnabled(False)
            self.drawing_new_buts()

    def f7_activated(self):
        if self.button_f7.isChecked():
            self.button_lc3.setEnabled(True)
            self.button_rc3.setEnabled(True)
            self.button_tc1.setEnabled(True)
            self.button_bc1.setEnabled(True)
            self.drawing_new_buts()
        else:
            if not any([self.button_f8.isChecked(), self.button_f9.isChecked()]):
                self.button_lc3.setEnabled(False)
                self.button_rc3.setEnabled(False)
            if not any([self.button_f1.isChecked(), self.button_f4.isChecked()]):
                self.button_tc1.setEnabled(False)
                self.button_bc1.setEnabled(False)
            self.drawing_new_buts()

    def f8_activated(self):
        if self.button_f8.isChecked():
            self.button_lc3.setEnabled(True)
            self.button_rc3.setEnabled(True)
            self.button_tc2.setEnabled(True)
            self.button_bc2.setEnabled(True)
            self.drawing_new_buts()
        else:
            if not any([self.button_f7.isChecked(), self.button_f9.isChecked()]):
                self.button_lc3.setEnabled(False)
                self.button_rc3.setEnabled(False)
            if not any([self.button_f2.isChecked(), self.button_f5.isChecked()]):
                self.button_tc2.setEnabled(False)
                self.button_bc2.setEnabled(False)
            self.drawing_new_buts()

    def f9_activated(self):
        if self.button_f9.isChecked():
            self.button_lc3.setEnabled(True)
            self.button_rc3.setEnabled(True)
            self.button_tc3.setEnabled(True)
            self.button_bc3.setEnabled(True)
            self.drawing_new_buts()
        else:
            if not any([self.button_f7.isChecked(), self.button_f8.isChecked()]):
                self.button_lc3.setEnabled(False)
                self.button_rc3.setEnabled(False)
            if not any([self.button_f3.isChecked(), self.button_f6.isChecked()]):
                self.button_tc3.setEnabled(False)
                self.button_bc3.setEnabled(False)
            self.drawing_new_buts()

    def drawing_new_buts(self):
        group_cl = QtWidgets.QGridLayout()
        group_cl.addWidget(self.button_lc1,0,0)
        group_cl.addWidget(self.button_lc2,1,0)
        group_cl.addWidget(self.button_lc3,2,0)
        group_cl.setSpacing(0)
        group_cl.setObjectName("control left")
        group_cr = QtWidgets.QGridLayout()
        group_cr.addWidget(self.button_rc1,0,0)
        group_cr.addWidget(self.button_rc2,1,0)
        group_cr.addWidget(self.button_rc3,2,0)
        group_cr.setSpacing(0)
        group_cr.setObjectName("control right")
        group_ct = QtWidgets.QGridLayout()
        group_ct.addWidget(self.button_tc1,0,0)
        group_ct.addWidget(self.button_tc2,0,1)
        group_ct.addWidget(self.button_tc3,0,2)
        group_ct.setSpacing(0)
        group_ct.setObjectName("control top")
        group_cb = QtWidgets.QGridLayout()
        group_cb.addWidget(self.button_bc1,0,0)
        group_cb.addWidget(self.button_bc2,0,1)
        group_cb.addWidget(self.button_bc3,0,2)
        group_cb.setSpacing(0)
        group_cb.setObjectName("control bot")
        self.group_grid.addLayout(group_cl,1,0,alignment = QtCore.Qt.AlignRight)
        self.group_grid.addLayout(group_cr,1,2,alignment = QtCore.Qt.AlignLeft)
        self.group_grid.addLayout(group_ct,0,1,alignment = QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.group_grid.addLayout(group_cb,2,1,alignment = QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        if self.is_enabled_but() and self.is_toggled_but():
            self.group_grid.itemAtPosition(1,0).setAlignment(QtCore.Qt.AlignCenter)
            self.group_grid.itemAtPosition(1,2).setAlignment(QtCore.Qt.AlignCenter)
            self.group_grid.itemAtPosition(0,1).setAlignment(QtCore.Qt.AlignCenter)
            self.group_grid.itemAtPosition(2,1).setAlignment(QtCore.Qt.AlignCenter)
            for i in [group_cl,group_cr]:
                for j in range(i.rowCount()):
                    i.itemAtPosition(j,0).widget().show()
            for i in [group_cb,group_ct]:
                for j in range(i.columnCount()):
                    i.itemAtPosition(0,j).widget().show()
            #self.group_grid.update()
            #self.group_grid.setUpdatesEnabled(False)
        else:
            self.group_grid.itemAtPosition(1,0).setAlignment(QtCore.Qt.AlignRight)
            self.group_grid.itemAtPosition(1,2).setAlignment(QtCore.Qt.AlignLeft)
            self.group_grid.itemAtPosition(0,1).setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
            self.group_grid.itemAtPosition(2,1).setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
            for i in [group_cl,group_cr]:
                for j in range(i.rowCount()):
                    i.itemAtPosition(j,0).widget().hide()
            for i in [group_cb,group_ct]:
                for j in range(i.columnCount()):
                    i.itemAtPosition(0,j).widget().hide()


            #self.group_grid.setUpdatesEnabled(False)
            #self.group_grid.update()

    def top_to_left(self):
        self.rotate_edge('top','left')
        self.coloring()
    
    def mid_to_left(self):
        self.rotate_edge("mid","left")
        self.coloring()

    def bot_to_left(self):
        self.rotate_edge("bot","left")
        self.coloring()

    def top_to_right(self):
        self.rotate_edge("top","right")
        self.coloring()
    
    def mid_to_right(self):
        self.rotate_edge("mid","right")
        self.coloring()

    def bot_to_right(self):
        self.rotate_edge("bot","right")
        self.coloring()

    def left_to_up(self):
        self.rotate_edge("left","up")
        self.coloring()
    
    def center_to_up(self):
        self.rotate_edge("center","up")
        self.coloring()
    
    def right_to_up(self):
        self.rotate_edge("right","up")
        self.coloring()

    def left_to_down(self):
        self.rotate_edge("left","down")
        self.coloring()

    def center_to_down(self):
        self.rotate_edge("center","down")
        self.coloring()

    def right_to_down(self):
        self.rotate_edge("right","down")
        self.coloring()

    def mix_it_randomize(self):
        self.rand_pos()
        self.coloring()

    def undo(self):
        pos = self.pos
        if abs(self.count-1) <= len(pos):
            self.count -= 1
            self.position = pos[self.count]
            self.coloring()
            self.redo_but.setEnabled(True)
        else:
            self.undo_but.setEnabled(False)

    def redo(self):
        pos = self.pos
        if self.count+1 < 0:
            self.count += 1
            self.position = pos[self.count]
            self.coloring()
            self.undo_but.setEnabled(True)
        else:
            self.redo_but.setEnabled(False)
        
if __name__ == "__main__":
    import sys

    def showWindow():
        splash.close()
        win.show()
        
    app = QtWidgets.QApplication(sys.argv)
    pathToGIF = "media\\rubik.gif"
    splash = MovieSplashScreen(pathToGIF)
    splash.show()

    QtCore.QTimer.singleShot(12000,showWindow) #11500
    win = CubeWindow()
    win.setWindowTitle("rubik's cube")
    ico = QtGui.QIcon("media\\icon.png")
    win.setWindowIcon(ico)
    win.resize(512,512)
    app.setWindowIcon(ico)
    sys.exit(app.exec_())

