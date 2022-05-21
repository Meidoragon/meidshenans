"""
#shebang will go here eventually
Purpose: Calculate a check digit for a string of
            numbers using the luhn algorithm
Author: Meidoragon
"""

import argparse
import os
import sys

def get_args(
    description="""Obtain and verify arguments""",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter):
        
    parser = argparse.ArgumentParser(description='Obtain and verify arguments')

    
    parser.add_argument('hex',
                        metavar='meid',
                        #nargs='*',
                        type=str,
                        default='35541909006007',
                        help='Hexidecimal meid input for determining Luhn digit')
    args = parser.parse_args()
    print(args.hex)
    args = parser.parse_args()
    """
    TODO: Properly sanitize these inputs
          Probably already done by argparse, but I mean that
          I should give it more thought than just cobbling
          it together out of paperclips and rubberbands
    TODO: Add the ability to do file input
          ideally make .txt, .csv, and .xlxs usable
          I have nothing against dropping .xlxs though.
    TODO: Verify input is 14 digit number stored as a str
    """
    return args

def main():
    """3, 2, 1, let's jam."""
    args = get_args()
    preLuhn = args.hex
    postLuhn = []
    rules = [preLuhn.isdigit(),
             len(preLuhn) == 14]
    
    if all(rules):
        double = True
        for i in reversed(preLuhn):
            if double:
                if len(str(int(i)*2)) == 2:
                    j = str(int(i) * 2)
                    postLuhn.append(str(int(j[0]) + int(j[1])))
                else:
                    postLuhn.append(str(int(i)*2))
                double = False
            else:
                postLuhn.append(i)
                double = True
        luhnVal = 0
        for each in postLuhn:
            luhnVal += int(each)
        print(preLuhn + str(10 - (luhnVal % 10)))
        """
        DONE: iterate through preLuhn string in reverse
              assigning the digits to the front of
              postLuhn, doubling every other one
        TODO: Clean up that nested if monstrosity 
        """
    else:
        print('Failed rules check')

#def luhn(preLuhn):
        
if __name__ == '__main__':
    main()
"""350039083322697"""





"""
TODO:
    Expand to become an entire 'Serial number check' emulator?
TODO:
    Use nargs='*', in argparse to allow multiple input MEIDs,
    then iterate through each of those.
"""
