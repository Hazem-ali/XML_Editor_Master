
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
    def OpenFile(self):
        # Load Data
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            MainWindow, "Open XML file", "", "XML Files (*.xml)", options=options)
        if fileName:
            print(fileName)
            self.Read_and_Fill(fileName, self.XML_TextBox)

    def Read_and_Fill(self, fileName, textbox):
        # This function reads a file and stores it in TextBox
        with open(fileName, 'r') as f:
            data = f.read()
            textbox.setPlainText(data)

    def SaveFile(self):
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

    def Fill_From_String(self, data, textbox):
        # This function stores a string into TextBox
        textbox.setPlainText(data)
        
        
        , clicked=lambda: self.OpenFile()
        , clicked=lambda: self.SaveFile()
        self.actionOpen.triggered.connect(lambda: self.OpenFile())
        
        self.actionSave_As.triggered.connect(lambda: self.SaveFile())
