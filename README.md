# RISCV-Simulator Phase 2 

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
	  |- gui_stalling
	  |- gui_forwarding
	  |- output.txt
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
	| 
	|
	|
	| 
	CONTROL KNOBS
	| PIPELINE EXECUTION
	| --when you select this button
	------code will execute with pipeline
	| -------two buttons will appear
	----Data Forwarding(when you select this option data hazards will be solved using data forwarding)
	----Stalling(when you select this option, data hazards will be solved using stalling)
	| --when you don't select this button
	-----your code will execute without pipeline
	|
	|
	|
	|
	PRINT PIPELINE REGISTER
	|- after adding any pc value into it, buffer values for that instruction will be printed
	|-if we check the checkbox "PRINT ALL PRINT REGISTER" , and press the button "PRINT PIPELINE REGISTER",
  	|	all of the buffers will get printed at the end of output.
	|
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
 
Print pipeline Register
--All the pipeline registers will be printed by selecting this option

1-Bit Branch Predictor:-
--Hit(when prediction matches with the actual result) 
--Miss(when prediction doesn't match with the actual result)


Block diagram of Instructions
So basically it's a rectangle 
---
	--1st row means first instruction which will get executed
	--2nd row means 2nd instruction which will get executed in the code
---
	--1st column shows which part of which instruction get executed in the first cycle
	--similarly 2nd column shows which part of which instruction will get executed in the 2nd cycle

for eg:- in the first cycle fetch of 1st instruction will occur
in the second cycle decode of first instruction and fetch of second instruction will occur

then block diagram will be:- 

	1	2
1	F	D
2		F

--all the outputs which we have to print will get printed in the end in output file
--if we check the checkbox "PRINT ALL PRINT REGISTER" , and press the button "PRINT PIPELINE REGISTER",
  all of the buffers will get printed at the end of output.
