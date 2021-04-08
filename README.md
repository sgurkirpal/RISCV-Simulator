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
      |- main.py(containing whole code to run on terminal)
      |- fetch.py(containing the code for fetch step)
      |- decode.py(containing the code for decode step)
      |- execute.py(containing the code for execute step)
      |- memory.py(containing the code for memory step) 
      |- writeback.py(containing the code for writeback step)
      |- gui.py
      |- gui_main.py(containing whole code to run on gui window)
      |- data.mc
      |- makefile 
  |- doc
      |
      |- design-doc.docx
  |- README.md
      |
  |- test
      |- fibonacci.mc
      |- factorial.mc
      |- bubble_sort.mc

==============
Requirements
==============
Python library - "PyQt5" is required to run the GUI.
It Can be installed using:
"pip install PyQt5".

==============
How to run
==============
	|
	$cd src
	$cd make 
	|
	|_ _(With GUI)-
	|	|
	|	| 
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
Output  
--While proceeding with step button
--It will show opcode,func3,func7
--Instruction type
--Rs1,RS2,Immediate values
--Messages like which function executed.

Output log:-
--By clicking on this button, complete output file will be displayed

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
 


