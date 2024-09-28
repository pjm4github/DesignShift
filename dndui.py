"""
Experimental code for building a GUI (like QtDesigner) in pure Python.
"""
import sys

from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QFrame, QHBoxLayout, \
    QSizePolicy, QMenu, QAction, QRubberBand
from PyQt5.QtCore import Qt, QPoint, QMimeData, QByteArray, QRect, QSize


class DraggableWidget(QLabel):
    def __init__(self, text, deletable=True):
        super().__init__(text)
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setLineWidth(2)
        self.setText(text)
        self.deletable = deletable
        self.selected = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
        elif event.button() == Qt.RightButton:
            if self.deletable:
                self.showContextMenu(event.pos())

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(self.text())
        mime_data.setData('application/x-widget', QByteArray(str(id(self)).encode('utf-8')))

        drag.setMimeData(mime_data)
        drag.setHotSpot(event.pos() - self.rect().topLeft())

        drop_action = drag.exec_(Qt.MoveAction)

    def showContextMenu(self, pos):
        context_menu = QMenu(self)
        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(self.deleteWidget)
        context_menu.addAction(delete_action)
        context_menu.exec_(self.mapToGlobal(pos))

    def deleteWidget(self):
        self.setParent(None)
        self.deleteLater()

    def setSelected(self, selected):
        self.selected = selected
        if selected:
            self.setStyleSheet("background-color: lightblue; border: 2px solid black;")
        else:
            self.setStyleSheet("")  # "background-color: ''; border: ''")


class SpringWidget(DraggableWidget):
    def __init__(self, deletable=True):
        super().__init__('Spring', deletable)
        self.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    # def mouseMoveEvent(self, event):
    #     super().mouseMoveEvent(event)
    #     self.resize(event.pos().x() + 20, self.sizeHint().height())
    #     self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #
    # def resizeEvent(self, event):
    #     self.resize(event.size().width(), event.size().height())

class DropArea(QFrame):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setFrameStyle(QFrame.Box | QFrame.Raised)
        self.setLineWidth(2)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMouseTracking(True)
        self.rubberBand = None
        self.origin = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.origin = event.pos()
            if not self.rubberBand:
                self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
            self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            self.rubberBand.show()
        elif event.button() == Qt.RightButton:
            self.showContextMenu(event.globalPos())

    def mouseMoveEvent(self, event):
        if self.rubberBand:
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        if self.rubberBand:
            self.rubberBand.hide()
            rect = self.rubberBand.geometry()
            for i in range(self.layout.count()):
                item = self.layout.itemAt(i)
                widget = item.widget()
                if widget and isinstance(widget, DraggableWidget) and rect.intersects(widget.geometry()):
                    widget.setSelected(True)
                #else:
                elif widget and  isinstance(widget, DraggableWidget):
                    widget.setSelected(False)
            self.rubberBand = None

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        mime_data = event.mimeData()
        widget_id = int(mime_data.data('application/x-widget').data().decode('utf-8'))
        widget = self.find_widget_by_id(widget_id)
        if widget:
            event.setDropAction(Qt.MoveAction)
            event.accept()
            widget.setParent(None)  # Temporarily remove widget to insert it at the correct position
            insert_index = self.find_insert_index(event.pos())
            self.layout.insertWidget(insert_index, widget)
            widget.show()
        else:
            text = mime_data.text()
            if text == 'Spring':
                new_widget = SpringWidget()
            else:
                new_widget = DraggableWidget(f"{text}:{widget_id}")
            event.setDropAction(Qt.MoveAction)
            event.accept()

            insert_index = self.find_insert_index(event.pos())
            self.layout.insertWidget(insert_index, new_widget)
            new_widget.resize(self.width(), new_widget.sizeHint().height())
            new_widget.show()

    def find_widget_by_id(self, widget_id):
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i)
            widget = item.widget()
            if widget and id(widget) == widget_id:
                return widget
        return None

    def find_insert_index(self, position):
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i)
            widget = item.widget()
            if widget and widget.geometry().contains(position):
                return i
        return self.layout.count()

    def showContextMenu(self, pos):
        context_menu = QMenu(self)
        group_action = QAction("Group Selected", self)
        group_action.triggered.connect(self.groupSelectedWidgets)
        context_menu.addAction(group_action)
        context_menu.exec_(pos)

    def collect_selected_widgets(self, layout):
        selected_widgets = []
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget = item.widget()
            if widget and isinstance(widget, DraggableWidget) and widget.selected:
                selected_widgets.append(widget)
            elif widget and isinstance(widget, QWidget) and widget.layout():
                selected_widgets.extend(self.collect_selected_widgets(widget.layout()))
        return selected_widgets

    def groupSelectedWidgets(self):
        # selected_widgets = [self.layout.itemAt(i).widget() for i in range(self.layout.count())
        #                     if hasattr(self.layout.itemAt(i).widget(), 'selected') and
        #                     self.layout.itemAt(i).widget().selected]
        selected_widgets = self.collect_selected_widgets(self.layout)
        if not selected_widgets:
            return
        hbox = QHBoxLayout()
        hbox_container = QWidget()
        hbox_container.setLayout(hbox)
        self.layout.addWidget(hbox_container)

        for widget in selected_widgets:
            widget.setParent(None)
            hbox.addWidget(widget)
            widget.setSelected(False)

        hbox_container.setStyleSheet("border: 2px solid green;")  # Optional: to visually distinguish the grouped container


class MetaUIBuilder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Meta UI Builder')

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QHBoxLayout(main_widget)

        # Left panel for draggable widgets
        # left_panel = QVBoxLayout()
        left_panel_container = QWidget()
        left_panel_container.setFixedWidth(200)
        left_panel = QVBoxLayout(left_panel_container)

        # main_layout.addLayout(left_panel)
        main_layout.addWidget(left_panel_container)

        # Create draggable widgets
        self.label = DraggableWidget('Label', deletable=False)
        self.button = DraggableWidget('Button', deletable=False)
        self.spring = SpringWidget(deletable=False)
        left_panel.addWidget(self.label)
        left_panel.addWidget(self.button)
        left_panel.addWidget(self.spring)

        # Drop area
        self.drop_area = DropArea()
        main_layout.addWidget(self.drop_area)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MetaUIBuilder()
    sys.exit(app.exec_())