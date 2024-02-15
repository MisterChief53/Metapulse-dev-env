import os

os.system("cd .\\WebView\\tests\\cefsimple")
os.system("git fetch")
os.system("git checkout master")
os.system("git pull origin master")
os.system("cd ..\\..\\..\\")

os.system("cd .\\Wiki\\")
os.system("git fetch")
os.system("git checkout master")
os.system("git pull origin master")
os.system("cd ..\\")

os.system("cd .\\WebServer\\")
os.system("git fetch")
os.system("git checkout master")
os.system("git pull origin master")
os.system("cd ..\\")

os.system("cd .\\AccountsServer\\")
os.system("git fetch")
os.system("git checkout master")
os.system("git pull origin master")
os.system("cd ..\\")

os.system("git add .")
os.system("git commit -m \"updated submodules to latest commit, and left them at master\"")
os.system("git push origin master")