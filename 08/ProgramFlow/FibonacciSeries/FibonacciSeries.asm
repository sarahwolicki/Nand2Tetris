//push argument 1
@2
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1
@SP
AM=M-1
D=M
@R5
M=D
@3
D=A
@1
D=D+A
@R6
M=D
@R5
D=M
@R6
A=M
M=D
//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 0
@4
D=M
@0
D=D+A
@R5
M=D
@SP
AM=M-1
D=M
@R5
A=M
M=D
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 1
@4
D=M
@1
D=D+A
@R5
M=D
@SP
AM=M-1
D=M
@R5
A=M
M=D
//push argument 0
@2
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
//pop argument 0
@2
D=M
@0
D=D+A
@R5
M=D
@SP
AM=M-1
D=M
@R5
A=M
M=D
//label MAIN_LOOP_START
(FibonacciSeries$MAIN_LOOP_START)
//push argument 0
@2
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//if-goto COMPUTE_ELEMENT
@SP
AM=M-1
D=M
@FibonacciSeries$COMPUTE_ELEMENT
D;JNE
//goto END_PROGRAM
@FibonacciSeries$END_PROGRAM
0;JMP
//label COMPUTE_ELEMENT
(FibonacciSeries$COMPUTE_ELEMENT)
//push that 0
@4
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push that 1
@4
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
M=M+1
//pop that 2
@4
D=M
@2
D=D+A
@R5
M=D
@SP
AM=M-1
D=M
@R5
A=M
M=D
//push pointer 1
@3
D=A
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
M=M+1
//pop pointer 1
@SP
AM=M-1
D=M
@R5
M=D
@3
D=A
@1
D=D+A
@R6
M=D
@R5
D=M
@R6
A=M
M=D
//push argument 0
@2
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
//pop argument 0
@2
D=M
@0
D=D+A
@R5
M=D
@SP
AM=M-1
D=M
@R5
A=M
M=D
//goto MAIN_LOOP_START
@FibonacciSeries$MAIN_LOOP_START
0;JMP
//label END_PROGRAM
(FibonacciSeries$END_PROGRAM)
