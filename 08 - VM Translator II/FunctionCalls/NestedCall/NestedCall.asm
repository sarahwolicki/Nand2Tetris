//function Sys.init 0
(Sys.init)
//push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
@SP
AM=M-1
D=M
@R5
M=D
@3
D=A
@0
D=D+A
@R6
M=D
@R5
D=M
@R6
A=M
M=D
//push constant 5000
@5000
D=A
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
//call Sys.main 0
@RETURN1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M+D
@Sys.main
0;JMP
(RETURN1)
//pop temp 1
@SP
AM=M-1
D=M
@R5
M=D
@5
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
//label LOOP
(Sys$LOOP)
//goto LOOP
@Sys$LOOP
0;JMP
//function Sys.main 5
(Sys.main)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
@SP
AM=M-1
D=M
@R5
M=D
@3
D=A
@0
D=D+A
@R6
M=D
@R5
D=M
@R6
A=M
M=D
//push constant 5001
@5001
D=A
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
//push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 1
@1
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
//push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 2
@1
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
//push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 3
@1
D=M
@3
D=D+A
@R5
M=D
@SP
AM=M-1
D=M
@R5
A=M
M=D
//push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
//call Sys.add12 1
@RETURN2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@6
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M+D
@Sys.add12
0;JMP
(RETURN2)
//pop temp 0
@SP
AM=M-1
D=M
@R5
M=D
@5
D=A
@0
D=D+A
@R6
M=D
@R5
D=M
@R6
A=M
M=D
//push local 0
@1
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
//push local 1
@1
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
//push local 2
@1
D=M
@2
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 3
@1
D=M
@3
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 4
@1
D=M
@4
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
A=A-1
D=M+D
M=D
//add
@SP
AM=M-1
D=M
A=A-1
D=M+D
M=D
//add
@SP
AM=M-1
D=M
A=A-1
D=M+D
M=D
//add
@SP
AM=M-1
D=M
A=A-1
D=M+D
M=D
//return
@LCL
D=M
@R14
M=D
@5
D=D-A
A=D
D=M
@R15
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@R14
D=M
@1
A=D-A
D=M
@THAT
M=D
@R14
D=M
@2
A=D-A
D=M
@THIS
M=D
@R14
D=M
@3
A=D-A
D=M
@ARG
M=D
@R14
D=M
@4
A=D-A
D=M
@LCL
M=D
@R15
A=M
0;JMP
//function Sys.add12 0
(Sys.add12)
//push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
@SP
AM=M-1
D=M
@R5
M=D
@3
D=A
@0
D=D+A
@R6
M=D
@R5
D=M
@R6
A=M
M=D
//push constant 5002
@5002
D=A
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
//push constant 12
@12
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
A=A-1
D=M+D
M=D
//return
@LCL
D=M
@R14
M=D
@5
D=D-A
A=D
D=M
@R15
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@R14
D=M
@1
A=D-A
D=M
@THAT
M=D
@R14
D=M
@2
A=D-A
D=M
@THIS
M=D
@R14
D=M
@3
A=D-A
D=M
@ARG
M=D
@R14
D=M
@4
A=D-A
D=M
@LCL
M=D
@R15
A=M
0;JMP
