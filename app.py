from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QMainWindow, QApplication, QGraphicsItem, QGraphicsRectItem

import sys

class GraphicsView(QGraphicsView):
    def mousePressEvent(self, event):
        print("mousePressEvent")
        print("event.localPos", event.localPos())
        print("mapToScene", self.mapToScene(event.localPos().toPoint()))

        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        print("mouseReleaseEvent")
        super().mouseReleaseEvent(event)

class GraphicsRectItem(QGraphicsRectItem):
    def mousePressEvent(self, event):
        print("GraphicsRectItem.mousePressEvent")
        super().mousePressEvent(event)

class Scene:
    def __init__(self, parent):
        self.scene = QGraphicsScene(parent)
        self.view = GraphicsView(self.scene, parent)

        self.a = GraphicsRectItem(0, 0, 100, 100)
        self.scene.addItem(self.a)
        self.a.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.b = self.scene.addRect(200, 0, 50, 50)

def open_app():
    app = QApplication(sys.argv)

    main = QMainWindow()
    scene = Scene(main)
    main.setCentralWidget(scene.view)

    main.show()
    scene.view.fitInView(0, 0, 300, 300)

    app.exec_()

if __name__ == "__main__":
    open_app()
