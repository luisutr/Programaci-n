# -*- coding: utf-8 -*-

import sys
sys.path.append("C:/Program Files/FreeCAD 0.18/bin/")
import FreeCAD
import FreeCADGui
import Part
import sys
from PySide2.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    FreeCADGui.showMainWindow()

    doc = FreeCAD.newDocument()
    box = Part.makeBox(100, 100, 100)
    Part.show(box)
    sys.exit(app.exec_())