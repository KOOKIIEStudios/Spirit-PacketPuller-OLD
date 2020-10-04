# Spirit-PacketPuller
A GUI implementation of [MaplePacketPuller](https://github.com/Bratah123/MaplePacketPuller), for the ***Spirit Suite*** of server development tools.
---
# Info

Features and known issues have been inherited from [MaplePacketPuller](https://github.com/Bratah123/MaplePacketPuller).
  *(To be updated as development continues)*

Note on style: This project uses PyQt, which utilises camel case. Hence, part of `main.py` (and the bulk of `view.py`) will be in camel case (with the exception of constants), with other non-Qt Python modules being in the typical snake case. 

Developmental Progress: ![25%](https://progress-bar.dev/25)

[Milestones](https://github.com/KOOKIIEStudios/Spirit-PacketPuller/milestones?with_issues=no)

## Features:
 - Reads keywords from IDA-generated pseudocode, and formats them into a form that is friendly for server encodes
 - Options for varying the accuracy of packet structure pulls
 - Shows the structure of packets
 - Writes all packet structures to an identically named output file in <del>`MaplePacketPuller/IDA Maple Script/FuncOutput/`</del>
   - *IO folders to be specified later*
 - Ability to search for InHeader opcodes
 
  
## Known Issues:
  - Edge-case functions may cause errors; see comments in the source code for possible fixes, i.e. line 159
  - `while()` loops aren't properly handled, i.e. whether a decode is in the scope of one well
    - Possible circumvention: may be rectified if `GET_ALL_DECODES = true`
  - The constant `GET_ALL_DECODES` when set to `True` for increased accuracy, has major aesthetic drawbacks
  - This script assumes that you have named the disassembled function in IDA according to the function you want to pull packet structures from
  - This script does not display switch cases - can be added by user
  
## Technical Stack
|  | Target | Tested |
| --- | --- | --- |
| Python | 3.6.12 | 3.6.12 |
| PyQt5 | 5.9.2 | 5.9.2 |
| qdarkstyle | 2.8.1 | 2.8.1 |
| fbs | 0.9.0 | 0.9.0 |
| [NSIS](http://nsis.sourceforge.net/Main_Page) | 3.0.5 | 3.0.5 |
| IDA Pro 32-bit | 7.0 | 7.0 |
| IDE/Text Editor | [PyCharm Community Edition 2020.1.1](https://www.jetbrains.com/pycharm/download) | [Notepad++ v7.8.9](https://notepad-plus-plus.org/downloads/) |
| CLI Interpretor | [pwsh 7.0.3](https://github.com/PowerShell/PowerShell/releases/tag/v7.0.3) | Windows PowerShell 5.1 |

Other variants for contributors to test:
  - [x] Python 2.7
    - **NOT COMPATIBLE:** use of os.scandir() makes it non-backwards compatible with versions older than 3.6
  - [x] Python 3.6
    - <del>**NOT COMPATIBLE:** probably a result of how f-strings handle backslashes</del>
    - *[MaplePacketPuller](https://github.com/Bratah123/MaplePacketPuller) project  back-ported to 3.6 for fbs-compatibility*
  - [ ] PyQt5 5.15.1 or other late versions
    - PyQt5 and PyQtTools 5.15.1 used for design; 5.9.2 used for freeze in release 
  - [ ] IDA 6.8
  - [ ] IDA 7.5

### Technical Notes:
- `Python 3.6.12` does not have official installers available, and requires building from source code. I tried building an installer from source but it refused to work.
  - See [this repository](https://github.com/KOOKIIEStudios/ToolArchive) for the unofficial installer I obtained from elsewhere for my own personal use.
  - <del>`PyQt5 5.9.2` and `fbs 0.9.0` should already be part of the venv</del> *venv added to `.gitignore`*
- NSIS is only required if you wish to create installers for Windows (i.e. only for me to build for releases)
- qdarkstyle is a stylesheet for a dark theme. If you do not wish to use it, just comment out its imports and instantiation in main.py
E.g.:
![comment out qdarkstyle](https://i.imgur.com/xf7faJk.png)

Current Folder Structure:

![](https://i.imgur.com/i8nhEaY.png)


Sample GUI:

![](https://i.imgur.com/58zHVgR.png)
![](https://i.imgur.com/7sggcT9.png)
![Action](https://i.imgur.com/L6qre4m.gifv)
---
# How To Use

## Install
***Intentionally left mostly blank until prototype completion***

## Application

**INPUT:**  `.txt` file containing C-pseudocode from IDA disassembly

**OUTPUT:**  `.txt` file containing packet structure


## How To Build

1. In the root of the repository, create a virtual environment using `Python -m venv venv`
2. Activate the virtual environment using `call venv\scripts\activate.bat` in Command Prompt
    - Alternatively, you can activate the virtual environment (venv) using `& venv\scripts\activate.ps1` in Power Shell - which is what I use
    - Note: You can deactivate the venv by using the command `deactivate`
3. Use `pip install fbs` and `pip install PyQt5==5.9.2` while the venv is activated to install to the virtual environment
    - Use `pip install wheel`, if the above commands throw errors
4. You can run the application from source code (while venv is activated) to test using `fbs run`
    - Alternatively, configure your IDE with the venv interpreter, to avoid the hassle of needing to activate the venv manually (see below)
    
Sample IDE Configuration (PyCharm):

![](https://i.imgur.com/TZSz7wz.png)
![](https://i.imgur.com/2QHKQPL.png)


## How To Release

### Freezing The App
- Use the command `fbs freeze` to convert the source code into an executable.

Refer to the [fbs GitHub page](https://github.com/mherrmann/fbs-tutorial) for more information. 

### Creating An Installer
- Make sure that `NSIS` is installed and added to `PATH`.
- Use the command `fbs installer` to create an installer.

Refer to the [fbs GitHub page](https://github.com/mherrmann/fbs-tutorial) for more information.