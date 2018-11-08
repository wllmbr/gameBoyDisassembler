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
			outputFileHandle.write("Address | Inst | Bytes | Mnenomic              |  Arguments\n")
			memoryAddress = -1;
			while(1):
				byte = inputFileHandle.read(1)
				# print type(byte)
				if byte == "":
					#Reached end of file, break out
					break
				memoryAddress += 1

				#Print the memory address
				outputFileHandle.write("0x%04x  |" % memoryAddress)
				

				# Write the byte
				outputFileHandle.write(" 0x%02x |" % ord(byte))
				
				outputFileHandle.write(" %05d |" % isa.mnemonicsSize[byte])



				# Write the Mnemonic
				outputFileHandle.write(isa.mnemonics[byte])

				# If any extra bytes are needed, read those and write them as arguments
				outputFileHandle.write("| ")
				argString = []
				for i in range(0,isa.mnemonicsSize[byte] -1):
					#Gameboy memory is little-endian
					argString.append("%02x" % ord(inputFileHandle.read(1)))
					memoryAddress += 1

				# Weird range to go in reverse order on the argument string
				for i in range(isa.mnemonicsSize[byte] -2, -1, -1):
					outputFileHandle.write(argString[i])

				outputFileHandle.write("\n")

				# If the byte was Prefix CB, jump to the next table
				if byte == '\xcb':
					newByte = inputFileHandle.read(1)
					memoryAddress += 1

					#Print the memory address
					outputFileHandle.write("0x%04x  |" % memoryAddress)
					memoryAddress += 1

					outputFileHandle.write(" 0x%02x |" % ord(newByte))

					outputFileHandle.write(" %05d |" % isa.prefixCBSize[byte])

					# Write the Mnemonic
					outputFileHandle.write(isa.prefixCB[newByte])

					# If any extra bytes are needed, read those and write them as arguments
					outputFileHandle.write("| ")
					argString = []
					for i in range(0,isa.prefixCBSize[newByte] -1):
						#Gameboy memory is little-endian
						argString.append("%02x" % ord(inputFileHandle.read(1)))
						memoryAddress += 1

					# Weird range to go in reverse order on the argument string
					for i in range(isa.prefixCBSize[newByte] -2, -1, -1):
						outputFileHandle.write(argString[i])
					outputFileHandle.write("\n")



if __name__ == '__main__':
	main()