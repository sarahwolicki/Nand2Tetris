import sys
import os

def parser(filename: str) -> list:
    """
    reads a file of assembly code, stripping whitespace and comments
    :param filename: name of .asm file
    :return: list of commands read from file
    """
    f = open(filename, 'r')
    lines = []
    for line in f:
        line = line.split("//", 1)[0] #discard comments
        line = line.strip()
        if line: # discard pure whitespace lines
            line = line.replace(' ', '')
            lines.append(line)
    f.close()
    return lines


def make_symbol_table() -> dict:
    """
    initializes the standard symbol table
    :return: the symbol table
    """
    symbols = ["SP", "LCL", "ARG", "THIS", "THAT",
               "R0", "R1", "R2", "R3", "R4",
               "R5", "R6", "R7", "R8", "R9",
               "R10", "R11", "R12", "R13",
               "R14", "R15", "SCREEN", "KBD"]
    values = [0, 1, 2, 3, 4,
              0, 1, 2, 3, 4,
              5, 6, 7, 8, 9,
              10, 11, 12, 13,
              14, 15, 16384, 24576]
    table = {}
    for symbol, value in zip(symbols, values):
        table[symbol] = value
    return table


def make_comp_table() -> dict:
    comp_table = {
        '0': '1110101010',
        '1': '1110111111',
        '-1': '1110111010',
        'D': '1110001100',
        'A': '1110110000',
        '!D': '1110001101',
        '!A': '1110110001',
        '-D': '1110001111',
        '-A': '1110110011',
        'D+1': '1110011111',
        'A+1': '1110110111',
        'D-1': '1110001110',
        'A-1': '1110110010',
        'D+A': '1110000010',
        'D-A': '1110001110',
        'A-D': '1110000111',
        'D&A': '1110000000',
        'D|A': '1110010101',
        'M': '1111110000',
        '!M': '1111110001',
        '-M': '1111110011',
        'M+1': '1111110111',
        'M-1': '1111110010',
        'D+M': '1111000010',
        'D-M': '1111010011',
        'M-D': '1111000111',
        'D&M': '1111000000',
        'D|M': '1111010101',
        'D<<': '1010110000',
        'D>>': '1010010000',
        'A<<': '1010100000',
        'A>>': '1010000000',
        'M<<': '1011100000',
        'M>>': '1011000000'
    }
    return comp_table


def make_dest_table() -> dict:
    dest_table = {
        None: '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
    }
    return dest_table


def make_jmp_table() -> dict:
    jmp_table = {
        None: '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }
    return jmp_table


def first_pass(code: list, symbol_table: dict) -> None:
    """
    first pass over input, deals only with labels
    :param code:cinput assembly code
    :param symbol_table: table to which to add label symbols
    :return: None
    """
    line_count = 0
    for line in code:
        if line[0] == "(":
            label = line.strip("()")
            symbol_table[label] = line_count
        else:
            line_count += 1
    return


def a_instruction(instruction: str, symbol_table: dict, mem_counter: int) -> str:
    """
    converts an assembly language a-instruction to binary representation
    :param instruction:
    :param symbol_table:
    :param mem_counter: next free RAM slot
    :return: binary representation, boolean indicator for incrementing
    mem_counter
    """
    inc = False
    if instruction.isnumeric():
        num = int(instruction)
    else:
        if instruction not in symbol_table:
            symbol_table[instruction] = mem_counter
            inc = True
        num = symbol_table[instruction]
    command = format(num, '016b')
    return command, inc


def c_instruction(instruction: str) -> str:
    """
    converts an assembly language c-instruction to binary representation
    :param instruction:
    :return: binary representation
    """
    if "=" in instruction:
        dest, comp = instruction.split("=")
        jmp = None
    else:
        dest = None
        comp, jmp = instruction.split(";")
    comp_table = make_comp_table()
    dest_table = make_dest_table()
    jmp_table = make_jmp_table()
    command = comp_table[comp] + dest_table[dest] + jmp_table[jmp]
    return command


def second_pass(code: list, symbol_table: dict, outfilename: str):
    """
    second pass over input, every line converted to binary code and written
    to output file
    :param code:
    :param symbol_table:
    :param outfilename: None
    :return:
    """
    # open file to write to
    of = open(outfilename, 'a')
    mem_counter = 16
    for line in code:
        if line[0] == "(": #label, ignore the line
            continue
        elif line[0] == "@": # A instruction
            res = a_instruction(line[1:], symbol_table, mem_counter)
            out_line = res[0]
            if res[1]:
                mem_counter += 1
        else: # C instruction
            out_line = c_instruction(line)
        of.write(out_line) # write out_line to file
        of.write('\n')
    of.close()
    return


def assembler(filename):
    progname = filename[:-4]
    assembly_code = parser(filename)
    symbol_table = make_symbol_table()
    first_pass(assembly_code, symbol_table)
    outfilename = progname + '.hack'
    second_pass(assembly_code, symbol_table, outfilename)


def main():
    """
    main function
    :return:
    """
    input_path = sys.argv[1]
    if os.path.isfile(input_path): #given path is single file
        assembler(input_path)
    else: #path is directory
        files = os.listdir(input_path)
        for file in files:
            if file.endswith('.asm'):
                assembler(input_path + '\\' + file)


if __name__ == "__main__":
    main()


