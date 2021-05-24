STACK_ACCESS = '@SP\nAM=M-1\n'
STACK_INC = '@SP\nM=M+1\n'


seg_base = {'local': '1', 'argument': '2', 'this': '3', 'that': '4', 'temp':
    '5', 'pointer': '3'}

static_counter = 0


def push(segment, index, progname=None):
    out = ''
    if segment == 'constant':
        out += '@' + index + '\nD=A\n' #get value i
        out += '@SP\nA=M\nM=D\n' #set stack value to i
        out += STACK_INC
    elif segment == 'temp' or segment == 'pointer':
        out += '@' + seg_base[segment] + '\nD=A\n'  # get segment base
        out += '@' + index + '\nD=D+A\nA=D\nD=M\n'  # access segment[base+i]
        out += '@SP\nA=M\nM=D\n'  # set stack value to segment[base+i]
        out += STACK_INC
    elif segment == 'static':
        out += '@' + progname + index + '\nD=M\n'
        out += '@SP\nA=M\nM=D\n'
        out += STACK_INC
    else: #lcl, arg, this, that
        out += '@' + seg_base[segment] + '\nD=M\n' #get segment base
        out += '@' + index + '\nD=D+A\nA=D\nD=M\n' #access segment[base+i]
        out += '@SP\nA=M\nM=D\n' #set stack value to segment[base+i]
        out += STACK_INC
    return out


def pop(segment, index, progname):
    out = ''
    if segment == 'temp' or segment == 'pointer':
        out += STACK_ACCESS + 'D=M\n@R13\nM=D\n'  # set temp1 to value from
        # stack
        out += '@' + seg_base[segment] + '\nD=A\n'  # get segment base
        out += '@' + index + '\nD=D+A\n'  # get segment base+index
        out += '@R14\nM=D\n'  # set temp2 to base+index
        out += '@R13\nD=M\n'  # access value from stack
        out += '@R14\nA=M\n'  # access RAM[base+index]
        out += 'M=D\n'  # set RAM[base+index] to value from stack
    elif segment == 'static':
        out += STACK_ACCESS + 'D=M\n'
        out += '@' + progname + index + '\nM=D\n'
    else: #lcl, arg, this, that
        out += '@' + seg_base[segment] + '\nD=M\n'  # get segment base
        out += '@' + index + '\nD=D+A\n'  # get segment base+index
        out += '@R13\nM=D\n'  # set temp to base+index
        out += STACK_ACCESS + 'D=M\n' #get value from stack
        out += '@R13\nA=M\nM=D\n'
    return out