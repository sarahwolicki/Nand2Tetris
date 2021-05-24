
STACK_ACCESS = '@SP\nAM=M-1\n'
STACK_INC = '@SP\nM=M+1\n'
SET_FALSE = '@SP\nA=M-1\nM=0\n'
SET_TRUE = '@SP\nA=M-1\nM=-1\n'


operations = {'add': 'M=M+D\n',
              'sub': 'M=M-D\n',
              'neg': 'M=-M\n',
              'comp': 'D=M-D\n',
              'and': 'M=M&D\n',
              'or': 'M=M|D\n',
              'not': 'M=!M\n'
              }


jumps = {'eq': 'D;JEQ\n',
         'gt': 'D;JGT\n',
         'lt': 'D;JLT\n',
         'end': '0;JMP\n'}


eq_counter = 0
lt_counter = 0
gt_counter = 0



def gen_add():
    return STACK_ACCESS + 'D=M\nA=A-1\nD=M+D\nM=D\n'


def gen_sub():
    return STACK_ACCESS + 'D=M\nA=A-1\nD=M-D\nM=D\n'


def gen_neg():
    return STACK_ACCESS + operations['neg']


def gen_eq():
    global eq_counter
    eq_counter += 1
    eq = STACK_ACCESS + 'D=M\nA=A-1\n' + operations['comp']
    eq += '@EQ_TRUE' + str(eq_counter) + '\n' + jumps['eq']
    eq += SET_FALSE
    eq += '@END_EQ' + str(eq_counter) + '\n' + jumps['end']
    eq += '(EQ_TRUE' + str(eq_counter) + ')\n'
    eq += SET_TRUE
    eq += '(END_EQ' + str(eq_counter) + ')\n'
    return eq


def gen_gt():
    global gt_counter
    gt_counter += 1
    gt = STACK_ACCESS + 'D=M\nA=A-1' + operations['comp']
    gt += '@GT_TRUE' + str(gt_counter) + '\n' + jumps['gt']
    gt += SET_FALSE
    gt += '@END_GT' + str(gt_counter) + '\n' + jumps['end']
    gt += '(GT_TRUE' + str(gt_counter) + ')\n'
    gt += SET_TRUE
    gt += '(END_GT' + str(gt_counter) + ')\n'
    return gt


def gen_lt():
    global lt_counter
    lt_counter += 1
    lt = STACK_ACCESS + 'D=M\nA=A-1\n' + operations['comp']
    lt += '@LT_TRUE' + str(lt_counter) + '\n' + jumps['lt']
    lt += SET_FALSE
    lt += '@END_LT' + str(lt_counter) + '\n' + jumps['end']
    lt += '(LT_TRUE' + str(lt_counter) + ')\n'
    lt += SET_TRUE
    lt += '(END_LT' + str(lt_counter) + ')\n'
    return lt


def gen_and():
    return STACK_ACCESS + 'D=M\nA=A-1\n' + operations['and']


def gen_or():
    return STACK_ACCESS + 'D=M\nA=A-1\n' + operations['or']


def gen_not():
    return '@SP\nA=M-1\n' + operations['not']



def generate(command):
    out = ''
    if command == 'add':
        out += gen_add()
    elif command == 'sub':
        out += gen_sub()
    elif command == 'neg':
        out += gen_neg()
    elif command == 'eq':
        out += gen_eq()
    elif command == 'gt':
        out += gen_gt()
    elif command == 'lt':
        out += gen_lt()
    elif command == 'and':
        out += gen_and()
    elif command == 'or':
        out += gen_or()
    elif command == 'not':
        out += gen_not()
    return out
