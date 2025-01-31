
# File Multiscanning using MetaDefender
[![Python](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/downloads/)

> Analyze files with 30+ anti-malware engines.

> Uses OPSWAT MetaDefender Cloud Public APIs.


## Features

- File Analysis
- Deep CDR (aka Content Disarm and Reconstruction) with support for 100+ file types
- Sandbox dynamic analysis to detect more unknown and targeted attacks
- Binary vulnerability data assessment
- Threat Intelligence Feeds


## Requirements

Running `file_scan` requires:

* Python 3 (recommended Python 3.10)
* pip 3 (recommended pip 22.1.2)
* git

#### To install requirements on Ubuntu:
```bash
sudo apt-get update
```
```bash
sudo apt install python3.10
```
```bash
sudo apt-get -y install python3-pip
```
```bash
sudo apt install git
```

###### verify if all packages are properly installed by runnning these commands
```bash
python3 --version
pip3 --version
git --version
```

#### To install requirements on Windows:

##### [Python 3 Release - Python 3.10.6](https://www.python.org/downloads/release/python-3106/)
##### [Git for Windows](https://git-scm.com/download/win)
> #### Make sure to add Python to PATH during installation
## Installation

This package runs on Windows as well as Ubuntu but additional steps will be required to run on Windows.


### Ubuntu Installation
#### Open a terminal in a desired location and run the following commands:
```bash
git clone https://github.com/prakrutpatel/OPSWAT.git && cd OPSWAT
```
```bash
chmod +x build.sh
```
#### To build the application replace YOUR_API_KEY with your MetaDefender Cloud API Key. You can find it on [MetaDefender Cloud](https://metadefender.opswat.com/account)
```bash
./build.sh YOUR_API_KEY
```
```bash
source ~/.bashrc
```
#### **After this your application should have finished building and an alias called `scan` should have been created in the system which allows you to call it from any directory.**
___
### Windows Installation
#### Open a terminal in a desired location and run the following commands:
```bash
git clone https://github.com/prakrutpatel/OPSWAT.git && cd OPSWAT
```
#### To build the application replace YOUR_API_KEY with your MetaDefender Cloud API Key. You can find it on [MetaDefender Cloud](https://metadefender.opswat.com/account)
```bash
build.bat YOUR_API_KEY
```
#### This will create a file called scan.bat in your project directory which will be embedded with your API Key.
&nbsp;  
**We need to go through a few more steps to be able to call this file from any directory in Windows.**
##### 1. Open the Start Search, type in “env”, and choose “Edit the system environment variables”:
![](https://www.architectryan.com/static/start_menu-91c0473bae32fa3862658e4d6e62d75c-2facb.png)
&nbsp;
##### 2. Click the “Environment Variables…” button.
![](https://www.architectryan.com/static/system_properties-f3a4f86cdd178c48ed9d8398743f85df-39c95.png)
&nbsp;
##### 3. Under the “System Variables” section (the lower half), find the row with “Path” in the first column, and click edit.
![](https://www.architectryan.com/static/select_row_and_edit-48423a2a0724e226bd3f69468d9eaabd-70c4b.png)
&nbsp;
##### 4. The “Edit environment variable” UI will appear. Here, you can click “New” and type in the path of the project folder (or click on "Browse Directory" to select the project folder).
![](https://www.architectryan.com/static/edit_path_variable-42eb044d39582f04f1f213e17e4fcb30-c532b.png)
&nbsp;
##### 5. Dismiss all of the dialogs by choosing “OK”. Your changes are saved!
##### 6. You will probably need to restart apps for them to pick up the change. Restarting the machine would ensure all apps are run with the PATH change.
&nbsp;
#### **After this an alias called `scan.bat` should be created in the system which allows you to call it from any directory.**
## Usage
#### Ubuntu
```bash
scan FILE_TO_SCAN
```
#### Windows
```bash
scan.bat FILE_TO_SCAN
```

## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

