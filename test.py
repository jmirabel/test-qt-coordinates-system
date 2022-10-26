import pytest
from PySide2.QtWidgets import QWidget, QHBoxLayout, QGraphicsView
from PySide2.QtCore import Qt, QPoint, QSize
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
    scene.view.fitInView(100, 100, 300, 300)
    transform = scene.view.transform()
    transform.scale(1/10, 1/10)
    scene.view.setTransform(transform)
    rect = scene.a.boundingRect()
    scenePos = scene.a.mapToScene(rect.center())
    print("Initial scene pos", scenePos)
    viewPos = scene.view.mapFromScene(scenePos)
    qtbot.mouseClick(w, Qt.MouseButton.LeftButton, pos=viewPos, delay=1000)
    qtbot.wait(1000)

if __name__ == "__main__":
    pytest.main(sys.argv)
