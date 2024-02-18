import os

# Define a list of directories to loop through
directories = [
    ".\\WebView\\tests\\cefsimple",
    ".\\Wiki",
    ".\\WebServer",
    ".\\AccountsServer",
    ".\\InferenceServer"
]

# Loop through each directory
for directory in directories:
    # Change directory
    os.chdir(directory)
    
    # Run git commands
    os.system("git fetch")
    os.system("git checkout master")
    os.system("git pull origin master")

    if directory == ".\\AccountsServer":
        # Construct the path to postgres-data directory relative to AccountsServer directory
        postgres_data_dir = os.path.join(os.getcwd(), "postgres-data")
        if not os.path.exists(postgres_data_dir):
            # Create postgres-data directory
            os.mkdir(postgres_data_dir)
    if directory == ".\\WebView\\tests\\cefsimple":
        os.chdir("..\\..\\..\\")
    else:
        # Change back to parent directory
        os.chdir("..")

# Commit and push changes in the main repository
os.system("git add .")
os.system("git commit -m \"updated submodules to latest commit, and left them at master\"")
os.system("git push origin master")