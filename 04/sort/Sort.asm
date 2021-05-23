//todo: set "end of array" variable. at the end of the forloop compare
//cur2 to it and end loop if equal


    @R14
    D=M
    @R15
    D=D+M
    @arrayend
    M=D //set array end to adress of bit after end of array
(WHILELOOP)
    @R14
    D=M
    @cur1
    M=D //set current index to starting address
    @cur2
    M=D+1
    @swapped
    M=0

(FORLOOP)
    @cur1
    A=M
    D=M
    @cur2
    A=M
    D=D-M //D=arr[cur1]-arr[cur2]
    @SWAP
    D;JLT //if arr[cur1]<arr[cur2] goto SWAP
(AFTERSWAP)
    @cur1
    M=M+1
    @cur2
    M=M+1
    
    @cur2
    D=M
    @arrayend
    D=D-M
    @FORLOOP
    D;JNE//jump only if cur2 != end of array
    
    @swapped
    D=M
    @WHILELOOP
    D;JNE //if swapped == 0 don't return to beginning
    @END
    0;JMP

(SWAP)
    @cur1
    A=M
    D=M
    @temp
    M=D
    @cur2
    A=M
    D=M
    @cur1
    A=M
    M=D

    @temp
    D=M
    @cur2
    A=M
    M=D

    @swapped
    M=1
    @AFTERSWAP
    0;JMP //resume for loop

(END)
    