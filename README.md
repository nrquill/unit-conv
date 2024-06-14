# Python CLI Program for Unit Conversion
## Used Modules:
  - argparse
  - re


### Usage:
    py unit-conv.py <length><unit><decimal_point>

    6.56ft -> 2m

The program will only runs if it's under the right syntax

### The Regex Key:
  `^\d+(.\d+)?(ft|m|cm|in)+[1-9]?`


---
### Example 1:
  Input:

    py unit-conv.py 2m
  Output:
  
    6.56ft

### Example 2:
  Input:

    py unit-conv.py 32.2cm
  Output:
  
    81.79ft



¯\_(ツ)_/¯
