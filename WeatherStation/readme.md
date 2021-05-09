# Weather Underground Publishing observations

## Setup Instructions

On the Raspberry PI, please follow these steps to ensure we have the components required for the weather station.

```bash
# Determine the version of python are installed. E.g. v2.7.16 or 3.9.4
python --version
python3 --version

# Confirm the python 3.7 directory exists on your raspberry (newer versions may be available via the operating system updates)
cd /usr/bin/
ls python*
# copy down the highest version of python3 available 

# Change the raspberry pi default python version to v3.7 (or higher)
ls --all
cd ~/
ls --all

# Using Visual Code via SSH 
# Press Ctrl Key
# Click on the .bashrc file in the terminal ouput to open the file in the editor.
# Add the following line to the end of the file and save that file
alias python='/usr/bin/python3.7'

# Confirm the version of the Python package manager is installed 
# pip --version
pip3 --version
# Upgrade Python package manager to the latest version available.
pip3 install --upgrade pip

# Install the Web Service code needed to publish to the weather underground.
# pip3 install requests
python3 -m pip install --upgrade requests

```

## Keyboard shortcuts

Exit python prompt

> Ctrl + Z -> Enter

## References

[Python Editions Running](https://raspberry-valley.azurewebsites.net/Python-Default-Version/)
[Changing to Python 3 on Raspberry Pi](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux)
[How to install Python requests code](https://stackoverflow.com/questions/23283045/importerror-no-module-named-requests-python-3-4-0/23283081)
[Pip warning - 9859](https://github.com/pypa/pip/issues/9859)