import argparse
import re

def main():

    FOOT_IN_METER = 3.281
    INCH_IN_CM = 2.54
    ROUND_AMOUNT = 2


    # Add args
    parser = argparse.ArgumentParser(prog='Meters & Feet Converter', description='Calculates the length of human proportions based on a 7.5 Head Ratio') 
    parser.add_argument("entry", action='store', type=str, metavar="(<length><ft|m><rounding_number>)", help="Usage: <length><ft|m><rounding_number> ~ the rounding number is optional, but is 2 on default")
    arg = parser.parse_args().entry

    # Validates the arg into a variable
    userArg = re.search(r"^\d+(.\d+)?(ft|m|cm|in)+[1-9]?", arg) or sys.exit(1)
    userArg = re.split(r"(ft|m|cm|in)", userArg.string)

    # Sets a rounder if entered
    if userArg[2] != '':
        ROUND_AMOUNT = int(userArg[2])

    # Creates vars
    INPUT = userArg[0]
    UNIT = userArg[1]
    # Converts for a result

    # m to ft
    if UNIT == 'm':
        result = round((float(INPUT) * FOOT_IN_METER), ROUND_AMOUNT)
    elif UNIT == 'cm':
        result = round((float(INPUT) * INCH_IN_CM), ROUND_AMOUNT)
    elif UNIT == 'ft':
        result = round((float(INPUT) / FOOT_IN_METER), ROUND_AMOUNT)
    elif UNIT == 'in':
        result = round((float(INPUT) / INCH_IN_CM), ROUND_AMOUNT)
    
    print(f"{result}ft")

if __name__ == "__main__":
    main()