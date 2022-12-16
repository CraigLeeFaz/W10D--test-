from PyQt5 import QtWidgets, uic
import sys, os, subprocess

cwd = os.getcwd()

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('testWindow.ui', self)
        
        self.uninstallButton = self.findChild(QtWidgets.QPushButton, 'uninstallButton')
        self.uninstallButton.clicked.connect(self.removeApps)

        self.installButton = self.findChild(QtWidgets.QPushButton, 'installButton')
        self.installButton.clicked.connect(self.installApps)

        self.show()

    def removeApps(self):
        batfname = "runW10Duninstall.bat"
        batflocation = f"{cwd}\{batfname}"

        psfname = "W10Duninstall.ps1"
        psflocation = f"{cwd}\{psfname}"

        batCMD = """@ECHO OFF
        PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& {Start-Process PowerShell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File "%s"' -Verb RunAs}"
        """ % psflocation

        psCMD = """Get-AppxPackage -allusers *windowscamera* | Remove-AppxPackage
        pause
        """

        if os.path.isfile(batfname) == False:
            f = open(batfname, "a")
            f.write(batCMD)
            f.close()

        if os.path.isfile(psfname) == False:
            f = open(psfname, "a")
            f.write(psCMD)
            f.close()

        subprocess.call([batflocation])

    def installApps(self):
        batfname = "runW10Dinstall.bat"
        batflocation = f"{cwd}\{batfname}"

        psfname = "W10Dinstall.ps1"
        psflocation = f"{cwd}\{psfname}"

        batCMD = """@ECHO OFF
        PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& {Start-Process PowerShell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File "%s"' -Verb RunAs}"
        """ % psflocation

        psCMD = """Get-AppxPackage -allusers *Microsoft.WindowsCamera* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
        pause
        """

        if os.path.isfile(batfname) == False:
            f = open(batfname, "a")
            f.write(batCMD)
            f.close()

        if os.path.isfile(psfname) == False:
            f = open(psfname, "a")
            f.write(psCMD)
            f.close()

        subprocess.call([batflocation])

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()