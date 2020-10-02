# Spirit-PacketPuller
A GUI implementation of [MaplePacketPuller](https://github.com/Bratah123/MaplePacketPuller), for the ***Spirit Suite*** of server development tools.
---
# Info

Features and known issues have been inherited from [MaplePacketPuller](https://github.com/Bratah123/MaplePacketPuller).
  *(To be updated as development continues)*

Developmental Progress: ![5%](https://progress-bar.dev/5)

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
    - *[MaplePacketPuller](https://github.com/Bratah123/MaplePacketPuller) project to be back-ported to 3.6 for fbs-compatibility*
  - [ ] PyQt5 5.15.1 or other late versions
  - [ ] IDA 6.8
  - [ ] IDA 7.5

### Technical Notes:
- `Python 3.6.12` does not have official installers available, and requires building from source code. I tried building an installer from source but it refused to work.
  - See [this repository](https://github.com/KOOKIIEStudios/ToolArchive) for the unofficial installer I obtained from elsewhere for my own personal use.
  - <del>`PyQt5 5.9.2` and `fbs 0.9.0` should already be part of the venv</del> *venv added to `.gitignore`*
  - You can create a virtual environment using `Python -m venv venv`
  - You can activate the virtual environment using `call venv\scripts\activate.bat` in Command Prompt
  - Alternatively, you can activate the virtual environment using `& venv\scripts\activate.ps1` in Power Shell - which is what I use
  - Use `pip install fbs` and `pip install PyQt5==5.9.2` while the venv is activated to install to the virtual environment
  - Use `pip install wheel`, if the above commands throw errors
  - You can run the application from source code using `fbs run`
- NSIS is only required if you wish to create installers for Windows (i.e. only for me to build for releases)

Current Folder Structure:

![](https://i.imgur.com/q3KX7xY.png)

---
# How to use

## Install
***Intentionally left mostly blank until prototype completion***

## Application

**INPUT:**  `.txt` file containing C-pseudocode from IDA disassembly

**OUTPUT:**  `.txt` file containing packet structure

