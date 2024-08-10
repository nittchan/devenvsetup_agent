# devenvsetup_agent
# Development Environment Setup Agent

This project provides an intelligent script to set up a development environment for Python-based AWS projects. It checks for existing installations, sets up required components, and provides guidance for manual installation when necessary.

## Features

- Checks for and verifies Python 3.9 installation
- Detects Visual Studio Code installation
- Sets up Visual Studio Code with essential extensions
- Creates and configures a virtual environment
- Installs required Python packages
- Checks for, installs (where possible), and configures AWS CLI
- Provides platform-specific instructions for manual installations

## Prerequisites

- Internet connection
- Administrative privileges on your system

## Installation

1. Clone this repository or download the `dev_environment_setup.py` script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `dev_environment_setup.py`.

## Usage

Run the script using Python:

_python dev_environment_setup.py_

The script will guide you through the process, checking for existing installations and providing instructions when manual intervention is needed.

## What the Script Does

1. Checks for Python 3.9 installation and suggests installation if not found
2. Verifies VS Code installation and provides download link if not found
3. Installs specified VS Code extensions (Python and AWS Toolkit)
4. Sets up a virtual environment (if not already present)
5. Installs required Python packages in the virtual environment
6. Checks for AWS CLI, installs it if possible, and guides through configuration

## Troubleshooting

- If the script fails to install any component, it will provide instructions for manual installation.
- Ensure you have the necessary permissions to install software and create directories on your system.
- For VS Code extension issues, try installing them manually through the VS Code marketplace.
- If AWS CLI installation fails, follow the provided links to download and install it manually.

## Contributing

Contributions to improve the script or documentation are welcome. Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This script is provided as-is. Always review scripts before running them on your system, especially those that install software or modify system settings. While this script checks for existing installations and aims to be non-destructive, always ensure you have backups of important data.
