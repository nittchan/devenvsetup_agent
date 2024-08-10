import subprocess
import sys
import os
import venv
import json
import platform
import requests

class DevEnvironmentSetupAgent:
    def __init__(self):
        self.python_version = "3.9"
        self.vscode_extensions = [
            "ms-python.python",
            "amazonwebservices.aws-toolkit-vscode"
        ]
        self.packages = [
            "boto3",
            "selenium",
            "webdriver_manager",
            "requests"
        ]

    def run_command(self, command):
        try:
            return subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {command}")
            print(f"Error details: {e.stderr}")
            return None

    def check_python_installation(self):
        try:
            version = subprocess.check_output(["python", "--version"]).decode().strip()
            if version.startswith(f"Python {self.python_version}"):
                print(f"Python {self.python_version} is installed.")
                return True
            else:
                print(f"Python {self.python_version} is not installed.")
                self.suggest_python_installation()
                return False
        except:
            print(f"Python {self.python_version} is not installed.")
            self.suggest_python_installation()
            return False

    def suggest_python_installation(self):
        print("Please install Python 3.9 from https://www.python.org/downloads/")
        if platform.system() == "Windows":
            print("Make sure to check 'Add Python 3.9 to PATH' during installation.")
        elif platform.system() == "Darwin":  # macOS
            print("You can also use Homebrew to install Python: brew install python@3.9")
        elif platform.system() == "Linux":
            print("You can use your distribution's package manager to install Python 3.9")

    def check_vscode_installation(self):
        if platform.system() == "Windows":
            vscode_path = os.path.join(os.environ["APPDATA"], "Code", "User", "settings.json")
        elif platform.system() == "Darwin":
            vscode_path = os.path.expanduser("~/Library/Application Support/Code/User/settings.json")
        else:  # Linux
            vscode_path = os.path.expanduser("~/.config/Code/User/settings.json")

        if os.path.exists(vscode_path):
            print("Visual Studio Code is installed.")
            return True
        else:
            print("Visual Studio Code is not installed.")
            print("Please install VS Code from https://code.visualstudio.com/")
            return False

    def setup_vscode(self):
        if not self.check_vscode_installation():
            return

        for extension in self.vscode_extensions:
            result = self.run_command(f"code --install-extension {extension}")
            if result and result.returncode == 0:
                print(f"Extension {extension} installed successfully.")
            else:
                print(f"Failed to install extension {extension}. Please install it manually from VS Code marketplace.")

    def setup_virtual_environment(self):
        venv_path = os.path.join(os.getcwd(), "venv")
        if not os.path.exists(venv_path):
            venv.create(venv_path, with_pip=True)
            print(f"Virtual environment created at: {venv_path}")
        else:
            print(f"Virtual environment already exists at: {venv_path}")

        # Activate the virtual environment
        activate_this = os.path.join(venv_path, "Scripts" if sys.platform == "win32" else "bin", "activate_this.py")
        exec(open(activate_this).read(), {'__file__': activate_this})

        # Install packages
        for package in self.packages:
            result = self.run_command(f"pip install {package}")
            if result and result.returncode == 0:
                print(f"Package {package} installed successfully.")
            else:
                print(f"Failed to install package {package}. Please install it manually using 'pip install {package}'")

    def check_aws_cli(self):
        result = self.run_command("aws --version")
        if result and result.returncode == 0:
            print("AWS CLI is installed.")
            return True
        else:
            print("AWS CLI is not installed.")
            return False

    def setup_aws_cli(self):
        if self.check_aws_cli():
            print("AWS CLI is already installed.")
        else:
            print("Installing AWS CLI...")
            if platform.system() == "Windows":
                print("Please download and install AWS CLI from https://awscli.amazonaws.com/AWSCLIV2.msi")
                print("After installation, restart your terminal and run this script again.")
                return
            elif platform.system() == "Darwin":
                self.run_command("curl 'https://awscli.amazonaws.com/AWSCLIV2.pkg' -o 'AWSCLIV2.pkg' && sudo installer -pkg AWSCLIV2.pkg -target /")
            else:
                self.run_command("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip' && unzip awscliv2.zip && sudo ./aws/install")

        # Configure AWS CLI
        print("Please enter your AWS credentials:")
        aws_access_key = input("AWS Access Key ID: ")
        aws_secret_key = input("AWS Secret Access Key: ")
        aws_region = input("Default region name: ")
        
        config = {
            "aws_access_key_id": aws_access_key,
            "aws_secret_access_key": aws_secret_key,
            "region": aws_region
        }
        
        os.makedirs(os.path.expanduser("~/.aws"), exist_ok=True)
        with open(os.path.expanduser("~/.aws/credentials"), "w") as f:
            json.dump(config, f)
        
        print("AWS CLI configured successfully.")

    def run(self):
        print("Starting development environment setup...")
        if not self.check_python_installation():
            return
        if not self.check_vscode_installation():
            return
        self.setup_vscode()
        self.setup_virtual_environment()
        self.setup_aws_cli()
        print("Development environment setup completed successfully!")

if __name__ == "__main__":
    setup_agent = DevEnvironmentSetupAgent()
    setup_agent.run()
