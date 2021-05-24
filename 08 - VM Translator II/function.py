import mem

pointers = ['LCL', 'ARG', 'THIS', 'THAT']
func_counter = 0

def generate(command, function_name, n):
    out = ''
    if command == 'call':
        global func_counter
        func_counter += 1
        #push return address
        out += '@RETURN' + str(func_counter) + '\nD=A\n'
        out += '@SP\nA=M\nM=D\n'
        out += mem.STACK_INC
        #push LCL, ARG, THIS, THAT
        global pointers
        for pointer in pointers:
            out += '@' + pointer + '\nD=M\n'
            out += '@SP\nA=M\nM=D\n'
            out += mem.STACK_INC
        #ARG = SP - 5 - n
        out += '@' + str(int(n) + 5) + '\nD=A\n'
        out += '@SP\nD=M-D\n'
        out += '@ARG\nM=D\n'
        #LCL = SP
        out += '@SP\nD=M\n@LCL\nM=D\n'
        #goto function_name
        out += '@' + function_name + '\n0;JMP\n'
        #(return_address)
        out += '(RETURN' + str(func_counter) + ')\n'
    else: #function
        out += '(' + function_name + ')\n'
        for i in range(int(n)):
            out += mem.push('constant', '0')
    return out



def gen_return():
    out = ''
    #endFrame = LCL
    out += '@LCL\nD=M\n'
    out += '@R14\nM=D\n' #R14 holds endFrame
    #retAddr = *(EndFrame - 5)
    out += '@5\nD=D-A\nA=D\nD=M\n'
    out += '@R15\nM=D\n' #R15 holds return address
    #*ARG = pop()
    out += mem.STACK_ACCESS + 'D=M\n'
    out += '@ARG\nA=M\nM=D\n'
    #SP = ARG + 1
    out += '@ARG\nD=M\n@SP\nM=D+1\n'
    #THAT = *(endFrame - 1), THIS = *(endFrame - 2), ARG = *(endFrame - 3), LCL = *(endFrame - 4)
    global pointers
    for i , pointer in enumerate(reversed(pointers)):
        out += '@R14\nD=M\n'
        out += '@' + str(i + 1) + '\n'
        out += 'A=D-A\nD=M\n'
        out += '@' + pointer + '\nM=D\n'
    #goto retAdrr
    out += '@R15\nA=M\n'
    out += '0;JMP\n'
    return out













