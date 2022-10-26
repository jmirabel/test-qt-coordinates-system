import pytest
from PySide2.QtWidgets import QWidget, QHBoxLayout, QGraphicsView
from PySide2.QtCore import Qt, QPoint
import sys

import app

class MTestWidget(QWidget):
    def mousePressEvent(self, event):
        print("MTestWidget.mousePressEvent")
        if True:
            for c in self.children():
                if isinstance(c, QGraphicsView):
                    c.mousePressEvent(event)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        print("MTestWidget.mouseReleaseEvent")
        if False:
            for c in self.children():
                if isinstance(c, QGraphicsView):
                    c.mousePressEvent(event)
        super().mousePressEvent(event)

def no_test_widget(qtbot):
    w = MTestWidget()
    qtbot.addWidget(w)
    qtbot.mousePress(w, Qt.MouseButton.LeftButton)

def test_app(qtbot):
    w = MTestWidget()
    scene = app.Scene(w)
    l = QHBoxLayout(w)
    l.addWidget(scene.view)
    qtbot.addWidget(w)
    #scene.view.show()
    w.show()
    qtbot.wait(1000)
    rect = scene.a.boundingRect()
    scenePos = scene.a.mapToScene(rect.center().toPoint())
    viewPos = scene.view.mapFromScene(scenePos)
    qtbot.mouseClick(w, Qt.MouseButton.LeftButton, pos=viewPos, delay=1000)
    qtbot.wait(1000)

if __name__ == "__main__":
    pytest.main(sys.argv)
