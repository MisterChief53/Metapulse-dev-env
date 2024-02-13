import os

os.system("cd .\\WebView\\tests\\cefsimple")
os.system("git fetch")
os.system("git pull origin master")
os.system("cd ..\\..\\..\\")

os.system("cd .\\Wiki\\")
os.system("git fetch")
os.system("git pull origin master")
os.system("cd ..\\")

os.system("git add .")
os.system("git commit -m \"updated submodules to latest commit\"")
os.system("git push origin master")