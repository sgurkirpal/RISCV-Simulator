# RISCV-Simulator Phase 3

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
	| On the right side of GUI
	| Enter the input in Cache Memory block for
	| 1. Cache Size:- Input should be only integer and it should be in bytes
	| 2. Block Size :- It should be integer and should be in bytes
	| 3. Ways for SA :- Enter the value for k way set associative(k=this input)
	|
	|---------------------------------------------------------
	| After this click on Assemble button
	|---------------------------------------------------------
	| Now you have two options to proceed further
	| 1. Going step by step
	| 2. running the whole code together
 	|
	|
	|--If you want to run the code step by step:-
	| >>>>Click on Step button on the gui 
	|	-In output log, Output after each step will get printed
	|	- Detailed view of output log is shown at the bottom of the README
	|	-If the instruction is load or store:- Data cache will get updated accordingly
	|
	|
	|
	| If you want to run the whole code together:-
	|
	|
	| >>>>Click on run button
	|	-And the whole code will get executed
	|	-All the necessary things will get printed in the output log
	| 	-You can see the Data cache as well as instruction cache on the GUI by switching tabs 
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
No. of Accesses:- like in Sw and lw instruction, our code is byte addressable so we are checking byte by byte
for eg in lw instruction:- word is 4byte 
so firstly we will check for 1st byte of the word
then for 2nd byte 
and in all these steps we are accessing data cache 
so I am calculating no. of accesses to be 4 in this case

No. of hits and misses:- same is the situation for hits and misses in case of lw and sw. as the word is 4 bytes so I am accessing data cache 4 times so I am counting hits and misses accordingly in each and every access.

No. of accesses of data cache and instruction cache:- we printed the total accesses of data cache and instruction cache separately.
No. of hits and No. of misses:- printed no. of hits and no. of misses separately in case of data cache and instruction cache.

Input:-1. Total sets should not be equal to 0
	   2. Block size should be less than cache size
	   3. (cachesize//block size)//(k way associativity) this value should be greater than 0

==================
More About GUI
==================
Output  
--While proceeding with step button
--It will show opcode,func3,func7
--Instruction type
--Rs1,RS2,Immediate values
--Messages like which function executed.
-------------------------------------
In case of lw, sw instructions
--Printing the data cache structure
--It will show the tag, blockoffset and index for a particular instruction
--Will also tell whether the cache accessing is missed or hit.
--In case of miss, it will show the value of the block which we have to replace and we found it using lru method
--This is actually the victim block which we will replace from the data cache
--Similarly we will do for instruction cache.

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
