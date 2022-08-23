# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:37:06 2022

@author: arman hossain
"""

import sys
from radon.raw import analyze
from metrics import h_visit_src
from radon.visitors import ComplexityVisitor
from staticfg import CFGBuilder

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from main_window_ui import Ui_MainWindow
from PyQt5.QtGui import QPixmap
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.actionopen.triggered.connect(self.dojob)
    
    
    def file(self,filepath):
        with open(filepath, 'r') as src_file:
            self.src = src_file.read()
        cfg = CFGBuilder().build_from_file(filepath, "./"+filepath) # cfg is an ast.nodeVisitor
        cfg.build_visual('exampleCFG', 'png',True,False)
    
    def calculate(self):
        metcs = analyze(self.src)
        self.locc = metcs.loc - metcs.single_comments - metcs.blank
        hal = h_visit_src(self.src)
        self.h11,self.h22,self.N1,self.N2,self.hh,self.N,self.volume,self.difficulty,self.effort = hal[0]
        compl = ComplexityVisitor.from_code(self.src)
        self.complx = compl.functions[0].complexity

    def dojob(self):
        self.file("example2.py")
        self.pixmap = QPixmap('exampleCFG.png')
        self.image_label.setPixmap(self.pixmap)
        self.image_label.resize(self.pixmap.width(),self.pixmap.height())
        self.calculate()
        # print(self.h1)
        self.h1.setText(str(self.h11))
        self.h2.setText(str(self.h22))
        self.h.setText(str(self.hh))
        self.n1.setText(str(self.N1))
        self.n2.setText(str(self.N2))
        self.n.setText(str(self.N))
        self.vol.setText(str(self.volume))
        self.diff.setText(str(self.difficulty))
        self.eff.setText(str(self.effort))
        self.loc.setText(str(self.locc))
        self.comp.setText(str(self.complx))
        
    # def about(self):
    #     QMessageBox.about(
    #         self,
    #         "About Sample Editor",
    #         "<p>A sample text editor app built with:</p>"
    #         "<p>- PyQt</p>"
    #         "<p>- Qt Designer</p>"
    #         "<p>- Python</p>",
    #     )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())