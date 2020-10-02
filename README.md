# Spirit-PacketPuller
**A GUI implementation of [MaplePacketPuller](https://github.com/Bratah123/MaplePacketPuller), for the Spirit Suite of server development tools.**
---
# Info

Features and known issues inherited from [MaplePacketPuller](https://github.com/Bratah123/MaplePacketPuller)
## Features:
 - Reads keywords from IDA-generated pseudocode, and formats them into a form that is friendly for server encodes
 - Options for varying the accuracy of packet structure pulls
 - Shows the structure of packets
 - Writes all packet structures to an identically named output file in `MaplePacketPuller/IDA Maple Script/FuncOutput/`
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
| Python | 3.8.5 | 3.8.5 |
| IDA Pro 32-bit | 7.0 | 7.0 |
| IDE/Text Editor | PyCharm Community Edition 2020.1.1 | Notepad++ v7.8.9 |
| CLI Interpretor | pwsh 7.0.3 | pwsh 6 |

Other variants for contributors to test:
  - [x] Python 2.7
    - **NOT COMPATIBLE:** use of os.scandir() makes it non-backwards compatible with versions older than 3.6
  - [x] Python 3.6
    - **NOT COMPATIBLE:** probably a result of how f-strings handle backslashes
  - [ ] IDA 6.8
  - [ ] IDA 7.5

---
# How to use
**Left blank until prototype completion**
