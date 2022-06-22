# Drive letter: Z
# Shared drive path: \\clalit\dfs$\Docs\Institute\
import subprocess
import os


yesChoice = ['y', 'Y', 'ye', 'Ye', 'Yes', 'yes', 'YES', 'YE']
noChoice = ['n', 'N', 'no', 'No', 'Nah', 'nah', 'NAH', 'NO']
ClalitDrive = "\\clalit\dsf$\docs\institute"
path = ('"'+os.getcwd()+'"')

print('Made by Philip Boubenchikov Clalit Innvoation IT')

while True:
        MapDrive = input("Would you like to map institute drive?: ")

        if MapDrive in noChoice:
            print("Skipping..")
            break
        
        if MapDrive in yesChoice:
            print("Mapping..")
        subprocess.call(r'net use Z: /del', shell=True)
        print("anything connected to Z is removed")
        subprocess.call(r'net use z: \\clalit\dfs$\Docs\Institute', shell=True)
        print("Drive mapped..")
        break

while True:

    Teams = input("Install MS Teams?: ")
    
    if Teams in noChoice:
        print("Skipping..")
        break

    if Teams in yesChoice:
        cmd = ClalitDrive + "\Apps\Teams_windows_x64.exe"
        print("Downloading MS Teams from server..")
        os.system(r"robocopy \\clalit\dfs$\Docs\Institute\Apps Installs Teams_windows_x64.exe")
        print("Installing...")
        os.system(path + '\Installs\Teams_windows_x64.exe')
        break

while True:

    Chrome = input("Install Google Chrome?: ")

    if Chrome in noChoice:
        print("Skipping..")
        break

    if Chrome in yesChoice:
        print("Downloading Google Chrome from server..")
        os.system(r"robocopy \\clalit\dfs$\Docs\Institute\Apps\GoogleChrome\x64 Installs googlechromestandaloneenterprise64.msi")
        print("Installing...")
        os.system(path + '\Installs\googlechromestandaloneenterprise64.msi')
        break

while True:

    Citrix = input("Install Citrix?: ")

    if Citrix in noChoice:
        print("Skipping..")
        break

    if Citrix in yesChoice:
        print("Downloading Citrix from server..")
        os.system(r"robocopy \\clalit\dfs$\Docs\Institute\Apps\CitrixClient\CitrixWorkspace Installs CitrixWorkspaceApp2109.1.exe")
        print("Installing...")
        os.system(path + '\Installs\CitrixWorkspaceApp2109.1.exe')
        break

while True:

    SSMS = input("Install SSMS?: ")

    if SSMS in noChoice:
        print("Skipping..")
        break

    if SSMS in yesChoice:
        print("Downloading SSMS from server..")
        os.system(r"robocopy \\clalit\dfs$\Docs\Institute\Apps\SQL2019Studio Installs SSMS-Setup-ENU_18.9.1.exe")
        print("Installing...")
        os.system(path + '\Installs\SSMS-Setup-ENU_18.9.1.exe')
        break

while True:

    Office = input("Install Office?: ")

    if Office in noChoice:
        print("Skipping..")
        break

    if Office in yesChoice:
        print("Downloading Office from server..")
        os.system(r"robocopy \\clalit\dfs$\Docs\Institute\Apps\Office\2016\x64\English Installs setup.exe")
        print("Installing...")
        os.system(path + '\Installs\setup.exe')
        break

while True:

    DeleteFolder = input("Delete installs folder?: ")

    if DeleteFolder in noChoice:
        print("Skipping..")
        break

    if DeleteFolder in yesChoice:
        os.system('rmdir ' + path + '\Installs')
        exit(0)
