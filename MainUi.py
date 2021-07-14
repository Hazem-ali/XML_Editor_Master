# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile, QTextStream


# must execute "pip install qdarkstyle" to enable new themes
import qdarkstyle as theme
import random
import xml_private_functions as xml_fn
import xml_convert


class Ui_MainWindow(object):
    def __init__(self):
        self.filename = ''
        self.retrieved_xml = ''
        self.correct_xml = ''
        self.converted_json = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 560)
        MainWindow.setMinimumSize(QtCore.QSize(800, 580))
        MainWindow.setMaximumSize(QtCore.QSize(800, 580))
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.XML_TextBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.XML_TextBox.setGeometry(QtCore.QRect(20, 160, 371, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.XML_TextBox.setFont(font)
        self.XML_TextBox.setReadOnly(True)
        self.XML_TextBox.setObjectName("XML_TextBox")
        self.XML_TextBox.setTabStopDistance(10)
        self.Open_Button = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.OpenFile())
        self.Open_Button.setGeometry(QtCore.QRect(20, 120, 80, 30))
        self.Open_Button.setObjectName("Open_Button")
        self.Json_TextBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Json_TextBox.setGeometry(QtCore.QRect(410, 160, 371, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Json_TextBox.setFont(font)
        self.Json_TextBox.setReadOnly(True)
        self.Json_TextBox.setObjectName("Json_TextBox")
        self.Json_TextBox.setTabStopDistance(10)
        self.Check_Button = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.Check_XML())
        self.Check_Button.setGeometry(QtCore.QRect(110, 120, 91, 30))
        self.Check_Button.setObjectName("Check_Button")
        self.Solve_Button = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.Solve_XML())
        self.Solve_Button.setGeometry(QtCore.QRect(210, 120, 91, 30))
        self.Solve_Button.setObjectName("Solve_Button")
        self.Minify_Button = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.Minify_XML())
        self.Minify_Button.setGeometry(QtCore.QRect(310, 120, 80, 30))
        self.Minify_Button.setObjectName("Minify_Button")
        self.Convert_Button = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.toJSON())
        self.Convert_Button.setGeometry(QtCore.QRect(490, 120, 111, 30))
        self.Convert_Button.setObjectName("Convert_Button")
        self.Compress_Button = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.Compress_XML())
        self.Compress_Button.setGeometry(QtCore.QRect(610, 120, 80, 30))
        self.Compress_Button.setObjectName("Compress_Button")
        self.SaveAs_Button = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.SaveFile())
        self.SaveAs_Button.setGeometry(QtCore.QRect(700, 120, 80, 30))
        self.SaveAs_Button.setObjectName("SaveAs_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(230, 20, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAutoFillBackground(False)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Prettify_Button = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.Prettify_XML())
        self.Prettify_Button.setGeometry(QtCore.QRect(410, 120, 70, 30))
        self.Prettify_Button.setObjectName("Prettify_Button")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        self.menuTheme = QtWidgets.QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        self.statusBar.showMessage("Welcome to XML Editor")

        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(lambda: self.OpenFile())
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.triggered.connect(lambda: self.SaveFile())
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.triggered.connect(lambda: sys.exit())
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setCheckable(False)
        self.actionLight.setChecked(False)
        self.actionLight.setObjectName("actionLight")
        self.actionLight.triggered.connect(lambda: Change_Theme("light"))
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setCheckable(False)
        self.actionDark.setChecked(False)
        self.actionDark.setObjectName("actionDark")
        self.actionDark.triggered.connect(lambda: Change_Theme("dark"))
        self.menuOpen.addAction(self.actionOpen)
        self.menuOpen.addSeparator()
        self.menuOpen.addAction(self.actionSave_As)
        self.menuOpen.addSeparator()
        self.menuOpen.addAction(self.actionClose)
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionDark)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuTheme.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Check_XML(self):
        # Check XML Correctness
        
        cur_format = QtGui.QTextCharFormat()
        color=QtGui.QColor("#147DBD")
        cur_format.setBackground(color)
        
        indices = [(200,400),(700,1200),(2000,2500)]
        for start, end in indices:
            
            cursor = self.XML_TextBox.textCursor()
            cursor.setPosition(start)
            cursor.setPosition(end, QtGui.QTextCursor.KeepAnchor)
            cursor.setCharFormat(cur_format)
            self.XML_TextBox.setTextCursor(cursor)
            
        self.statusBar.showMessage(str(len(indices)) + " Errors Found")
        
        return

    def Solve_XML(self):
        # Solving XML Errors
        return

    def Minify_XML(self):
        # Remove XML spaces and lines
        
        # Check That we've xml file
        if not self.retrieved_xml:
            self.statusBar.showMessage("Please add an XML file first")
            return
        
        
        self.retrieved_xml = xml_fn.minify(self.retrieved_xml)
        self.XML_TextBox.setPlainText(self.retrieved_xml)
        self.statusBar.showMessage("XML Minified Successfully")
        
        return

    def Prettify_XML(self):
        # Prettify XML by adding spaces and lines
        
        
        # Check That we've xml file
        if not self.retrieved_xml:
            self.statusBar.showMessage("Please add an XML file first")
            return
        
        xml_data = xml_convert.Xml()
        xml_data.insert(self.retrieved_xml)
        self.retrieved_xml = xml_data.toXml()
        self.XML_TextBox.setPlainText(self.retrieved_xml)
        self.statusBar.showMessage("XML Prettified Successfully")
        
        
        return

    def toJSON(self):
        # Convert correct XML into JSON
        
        # Check That we've xml file
        if not self.retrieved_xml:
            self.statusBar.showMessage("Please add an XML file first")
            return
        
        xml_data = xml_convert.Xml()
        xml_data.insert(self.retrieved_xml)
        self.converted_json = xml_data.toJson()
        self.Json_TextBox.setPlainText(self.converted_json)
        self.statusBar.showMessage("Converted to JSON Successfully")
        return
   
    def Compress_XML(self):
        # Compress XML Data
        
        # Check if XML was given before compression
        if not self.retrieved_xml:
            self.statusBar.showMessage("Please add an XML file first")
            return
        
        # Perform Compression
        import compress
        # Ask for compressed location
        name, _ = QtWidgets.QFileDialog.getSaveFileName(
            MainWindow, 'Save Compressed File', filter="Compressed File (*.lzw)")
        # If a name is written
        if name:
            compress.LZW_Compress(self.retrieved_xml, name)
            self.statusBar.showMessage("Compression Done Successfully")
        return

    def OpenFile(self):
        # Load Data
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            MainWindow, "Open XML file", "", "XML Files (*.xml)", options=options)
        if fileName:
            print("Opened File:",fileName)
            self.filename = fileName
            self.Read_and_Fill(fileName, self.XML_TextBox)
            self.statusBar.showMessage("File Opened")
        return

    def Read_and_Fill(self, fileName, textbox):
        # This function reads a file and stores it in TextBox
        with open(fileName, 'r') as f:
            data = f.read()
            self.retrieved_xml = data
            textbox.setPlainText(data)
        return

    def SaveFile(self):
        # Check if XML was given before saving
        if not self.retrieved_xml:
            self.statusBar.showMessage("Please add an XML file first")
            return
        # elif not self.correct_xml:
        #     self.statusBar.showMessage("No changes to save....!")
        #     return
            
        
        # Save Data
        name, extension = QtWidgets.QFileDialog.getSaveFileName(
            MainWindow, 'Save File', filter="JSON (*.json);;XML (*.xml)")
        print(name)
        # If a name is written
        if name:
            with open(name, 'w') as f:
                if extension.startswith("XML"):
                    f.write(self.current_xml)
                elif extension.startswith("JSON"):
                    f.write(self.current_json)
            self.statusBar.showMessage("Saved Successfully")
        return

    def Fill_From_String(self, data, textbox):
        # This function stores a string into TextBox
        textbox.setPlainText(data)
        return

    def Highlight_Error_Text(self, error_text):
        # Coloring Text that has errors
        result = "<span style=\" color:#ff0000;\">"+str(error_text)+"</span>"
        return result

    def Add_Formalized_Text(self, data, ind):
        # Prints text with highlighted errors

        # TestCase until actual data comes
        if not ind:
            ind = [(2, 20), (50, 90), (250, 400)]
        if not data:
            data = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

        # Highlighting all errors
        i = 0
        text = ''
        for start, end in ind:
            text += data[i:start]
            text += self.Highlight_Error_Text(data[start:end])
            i = end

        text += data[i:]  # Adding rest of data
        # Put it in HTML format in order to color it
        final_result = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n""</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n""""<xmp><textarea style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"""+str(text)+"""</textarea></xmp></body></html>"""
        return final_result

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XML Editor"))

        # self.XML_TextBox.setHtml(_translate(
        #     "MainWindow", self.Add_Formalized_Text('', [])))

        self.XML_TextBox.setPlaceholderText(
            _translate("MainWindow", "XML Data..."))
        self.Open_Button.setText(_translate("MainWindow", "Open"))

#         self.Json_TextBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LOL <span style=\" color:#ff0000;\">MMM</span> AAAA</p></body></html>"))

        self.Json_TextBox.setPlaceholderText(
            _translate("MainWindow", "JSON Data..."))
        self.Check_Button.setText(_translate("MainWindow", "Check Errors"))
        self.Solve_Button.setText(_translate("MainWindow", "Solve Errors"))
        self.Minify_Button.setText(_translate("MainWindow", "Minify"))
        self.Convert_Button.setText(
            _translate("MainWindow", "To JSON"))
        self.Compress_Button.setText(_translate("MainWindow", "Compress"))
        self.SaveAs_Button.setText(_translate("MainWindow", "Save As"))
        self.Title.setText(_translate("MainWindow", "XML Editor"))
        self.Prettify_Button.setText(_translate("MainWindow", "Prettify"))
        self.menuOpen.setTitle(_translate("MainWindow", "File"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))


def Change_Theme(color):

    # Change GUI Theme
    # get the QApplication instance,  or crash if not set
    app = QtWidgets.QApplication.instance()
    if app is None:
        raise RuntimeError("No Qt Application found.")

    if color == "dark":
        app.setStyleSheet(theme.load_stylesheet(palette=theme.DarkPalette))
    elif color == "light":
        app.setStyleSheet(theme.load_stylesheet(palette=theme.LightPalette))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    try:
        app.setStyleSheet(theme.load_stylesheet(palette=theme.LightPalette))
    except:
        pass
    MainWindow.show()
    sys.exit(app.exec_())
