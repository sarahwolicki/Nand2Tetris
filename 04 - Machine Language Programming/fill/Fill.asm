// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(RESET)    
    @SCREEN
    D=A 
    @pixel
    M=D //set current pixel to 1st of screen

(LOOP)
    @KBD
    D=M
    @PRESSED
    D;JNE //goto PRESSED if kbd != 0
    @NOTPRESSED
    0;JMP //goto NOTPRESSED


(PRESSED)
    @pixel
    A=M
    M=-1 //set current pixel to black
    @pixel
    M=M+1 //increase current pixel
    @KBD
    D=A
    @pixel
    D=D-M
    @LOOP
    D;JGT
    @RESET
    0;JMP

(NOTPRESSED)
    @pixel
    A=M
    M=0 //set current pixel to white
    @pixel
    M=M+1 //increase current pixel
    @KBD
    D=A
    @pixel
    D=D-M
    @LOOP
    D;JGT
    @RESET
    0;JMP //if end of screen reached reset to first pixel
    




