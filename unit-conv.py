import argparse
import re

def main():

    FOOT_IN_METER = 3.281
    INCH_IN_CM = 2.54
    DECIMAL_POINT = 2


    # Add args
    parser = argparse.ArgumentParser(prog='Meters & Feet Converter', description='Calculates the length of human proportions based on a 7.5 Head Ratio') 
    parser.add_argument("entry", action='store', type=str, metavar="(<length><ft|m><decimal_point>)", help="Usage: <length><ft|m><decimal_point> ~ the decimal point is optional, but is 2 on default")
    arg = parser.parse_args().entry

    # Validates the arg into a variable
    userArg = re.search(r"^\d+(.\d+)?(ft|m|cm|in)+[1-9]?", arg) or sys.exit(1)
    userArg = re.split(r"(ft|m|cm|in)", userArg.string)

    # Sets a rounder if entered
    if userArg[2] != '':
        DECIMAL_POINT = int(userArg[2])

    # Creates vars
    INPUT = userArg[0]
    UNIT = userArg[1]
    NEW_UNIT = None
    # Converts for a result

    # m to ft
    if UNIT == 'm':
        NEW_UNIT = 'ft'
        result = round((float(INPUT) * FOOT_IN_METER), DECIMAL_POINT)
    elif UNIT == 'cm':
        NEW_UNIT = 'in'
        result = round((float(INPUT) * INCH_IN_CM), DECIMAL_POINT)
    elif UNIT == 'ft':
        NEW_UNIT = 'm'
        result = round((float(INPUT) / FOOT_IN_METER), DECIMAL_POINT)
    elif UNIT == 'in':
        NEW_UNIT = 'cm'
        result = round((float(INPUT) / INCH_IN_CM), DECIMAL_POINT)
    
    print(f"{result}{NEW_UNIT}")

if __name__ == "__main__":
    main()
