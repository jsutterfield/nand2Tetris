// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.

// Create color var.
@color
@summedRow

// create numberOfRows variable
@8192
D=A
@numOfRows
M=D

(RUN)
@currentRow
M=0
@KBD
D=M // TODO see if you can remove this
@PAINTCOLOR
D;JGT
@PAINTCLEAR
0;JMP

(PAINTCOLOR)
// Do the loop check
@numOfRows
D=M
@currentRow
D=D-M
@RUN
D;JEQ

// Paint the whole screen
@SCREEN
D=A
@currentRow
A=D+M
D=-1
M=D

// Increase the row
@currentRow
M=M+1
@PAINTCOLOR
0;JMP

(PAINTCLEAR)
@numOfRows
D=M
@currentRow
D=D-M
@RUN
D;JEQ

// Paint the whole screen
@SCREEN
D=A
@currentRow
A=D+M
D=0
M=D

// Increase the row
@currentRow
M=M+1
@PAINTCLEAR
0;JMP
