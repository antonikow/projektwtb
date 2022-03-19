from PyQt5.QtWidgets import QApplication
from PackageWindow.WindowClass import MainWindow

import PackageNewton.functions
if __name__ == "__main__":
    app = QApplication([])
    nowe = MainWindow()
   
    #print(help(PackageNewton.functions))
    print(help(PackageNewton.NewtonClass))
    nowe.show()
    app.exec_()

   

    #C:\Users\antoni\Desktop\pythonprojekt\d1.txt