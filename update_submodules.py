import subprocess

def update_submodules():
    try:
        # Command to initialize and update all submodules
        subprocess.run(["git", "submodule", "update", "--init", "--recursive"], check=True)
        
        # Command to update each submodule to its most updated master branch
        subprocess.run(["git", "submodule", "foreach", "git", "checkout", "master"], check=True)
        subprocess.run(["git", "submodule", "foreach", "git", "pull", "origin", "master"], check=True)
        
        print("Submodules updated successfully!")
    except subprocess.CalledProcessError as e:
        print("Error updating submodules:", e)

if __name__ == "__main__":
    update_submodules()