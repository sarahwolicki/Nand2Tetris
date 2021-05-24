
STACK_ACCESS = '@SP\nAM=M-1\n'
STACK_INC = '@SP\nM=M+1\n'
SET_FALSE = '@SP\nA=M\nM=0\n'
SET_TRUE = '@SP\nA=M\nM=-1\n'


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
    return 'D=M\n' + STACK_ACCESS + operations['add']


def gen_sub():
    return 'D=M\n' + STACK_ACCESS + operations['sub']


def gen_neg():
    return operations['neg']


def gen_eq():
    global eq_counter
    eq_counter += 1
    eq = 'D=M\n' + STACK_ACCESS + operations['comp']
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
    gt = 'D=M\n' + STACK_ACCESS + operations['comp']
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
    lt = 'D=M\n' + STACK_ACCESS + operations['comp']
    lt += '@LT_TRUE' + str(lt_counter) + '\n' + jumps['lt']
    lt += SET_FALSE
    lt += '@END_LT' + str(lt_counter) + '\n' + jumps['end']
    lt += '(LT_TRUE' + str(lt_counter) + ')\n'
    lt += SET_TRUE
    lt += '(END_LT' + str(lt_counter) + ')\n'
    return lt


def gen_and():
    return 'D=M\n' + STACK_ACCESS + operations['and']


def gen_or():
    return 'D=M\n' + STACK_ACCESS + operations['or']


def gen_not():
    return operations['not']



def generate(command):
    out = STACK_ACCESS
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
    out += STACK_INC
    return out
