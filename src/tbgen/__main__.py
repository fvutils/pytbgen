'''
Created on May 17, 2022

@author: mballance
'''
import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    pass

if __name__ == "__main__":
    main()