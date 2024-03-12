import subprocess

def init():
    # Example of what might be in a 'make init' command
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    subprocess.run(["python", "setup.py", "develop"], check=True)

if __name__ == "__main__":
    init()
