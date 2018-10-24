"""
File:		gbd.py
Purpose:	Program entry point for Gameboy Disassembler
Date:		10/23/2018
Author:		Will B.

"""

import isa


def main():
	#Read in the entire file a single byte at a time
	with open('example.gb','rb') as inputFileHandle:
		with open('example.asm','w') as outputFileHandle:
			while(1):
				byte = inputFileHandle.read(1)
				# print type(byte)
				if byte == "":
					#Reached end of file, break out
					break
				outputFileHandle.write(isa.mnemonics[byte])
				outputFileHandle.write("\n")




if __name__ == '__main__':
	main()