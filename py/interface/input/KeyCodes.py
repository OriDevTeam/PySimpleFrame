## XGPGBot ##
## Code Keys Script ##
## License:  - Description ##

## System imports ##
from enum import Enum, IntEnum, unique

## Library imports ##

## Application imports ##
from compatibility.Compatibility import OperativeSystem

## Import input according to detected OS
if OperativeSystem.IsWindows():
	from interface.input.windows.KeyCodes import KeyCodes
else:
	from interface.input.linux.KeyCodes import KeyCodes

