import function

def generate(command, label_name, progname):
    if command == 'label':
        return '(' + progname + '$' + label_name + ')\n'
    elif command == 'goto':
        return '@' + progname + '$' + label_name +'\n0;JMP\n'
    else: #if-goto
        return '@SP\nAM=M-1\nD=M\n@' + progname + '$' + label_name +'\nD;JNE\n'


def bootstrap():
    out = '@256\nD=A\n@SP\nM=D\n'
    out += function.generate('call', 'Sys.init', 0)
    return out