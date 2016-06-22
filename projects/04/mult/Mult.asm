// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// initialize R2 to 0
@R2
M=0

// initialize i to 0
@i 
M=0 

// Set R0
@R0
D=M
// Go to end if R0 == 0
@END
D;JEQ
@R0
M=D

// Set R1 to 5
@R1
D=M
// Go to end if R1 == 0
@END
D;JEQ
@R1
M=D

(LOOP)
// Add R0 to R2 (which stores the product)
@R0
D=M
@R2
M=M+D


// Do the loop check
@i
M=M+1
@R1
D=M
@i
D=D-M
@LOOP
D;JGT

// Infinite loop at end
(END)
@END
0;JMP
