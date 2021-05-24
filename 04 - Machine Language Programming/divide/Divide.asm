// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Divides R13 and R14 and stores the result in R15.

    @R15
    M=0
    @rem
    M=0
    @R13
    D=M // D = R13
    @div
    M=D
(LOOP)
    @div
    D=M // D = dividend
    @R14
    D=D-M // D = dividend - divisor
    @END
    D;JLT // If (dividend - divisor) <= 0 goto END
    @R15
    M=M+1 // increase result by 1
    @R14
    D=M // D = divisor
    @div
    M=M-D //dividend -= divisor
    //if div<divisor end program
    @R14
    D=M
    @div
    D=D-M
    @END
    D;JGE
    @LOOP
    0;JMP
(END)
    

    