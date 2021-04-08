# RISCV-Simulator

=============================================
Functional Simulator for RISC Processor
=============================================

Table of contents:-
1. Directory Structure 
2. How to execute
3. Some assumptions
4. GUI Structure

======================
Directory Structure:-
======================

RISCV-Simulator
  |
  |- src
      |
      |- myRISCVSim
  |- doc
      |
      |- design-doc.docx
  |- README
      |
      |- myRISCVSim.h
  |- problem statement
      |- main.c
      |- Makefile
      |- myRISCVSim.h
  |- test
      |- simple_add.mc
      |- fib.mc
      |- array_add.mc
      |- fact.mc
      |- bubble.mc

==============
How to run
==============
	|
	$cd 
	|
	|_ _(With GUI)-
	|	|
	|	|
	| 1. python gui.py 
	| A window will appear
	| 2. Firstly click on Assemble
 	| If you want to run the code step by step:-
	| >>>>Click on run button on the gui 
	|	-In output log, will get the output after each step
	|	-Like the value stored in the register, opcode,immediate, Instruction Type etc.
	| If you want to run the whole code together:-
	|
	|
	| >>>>Click on run button
	|	-And the whole code will get executed
	|_ _(Without Gui-on terminal)-
	|	|
	|	|
	|  python main.py
	|   Output-Values stored in all the registers
	| 	  -Values stored in memory
	| 	  -Used dictionaries as a data structure for storing these values
		
	
	 
================
Assumptions
================
Delimiter-0xffffc


==================
More About GUI
==================
Output console 
--While proceeding with step button
--It will show opcode,func3,func7
--Instruction type
--Rs1,RS2,Immediate values

Open data.mc button
--This is the input file containing all the machine codes
------text instructions format:-
	PC<space>MachineInstruction
------Delimiter(0xffffc)
------Data instructions format:-
	MemoryLocation<space>ByteValue
	Our memory is Byte Addressable

Assemble button:-
--By clicking on it code will assemble
--Then all the data instructions will get executed

Step and Run button
--Function already explained above

Register view
--Shows value of all the registers

Memory view
--Shows value of memory byte by byte 
 


