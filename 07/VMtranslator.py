import sys
import os
import mem
import arithmetic


def parser(filename: str):
    """
    parses a given file into a list containing the file line by line
    :param filename:
    :return: lines[]
    """
    f = open(filename, 'r')
    lines = []
    for line in f:
        line = line.split("//", 1)[0]  # discard comments
        line = line.strip()
        if line:  # discard pure whitespace lines
            lines.append(line)
    f.close()
    return lines


def trans_line(line: str, progname):
    """
    translates a given line of VM code to assembly code using the mem and
    arithmetic translators
    :param line: a line of VM code given as one string
    :param progname: the name of the program being translated, for use in
    generating static variable names
    :return: the translated line of assembly code as a string
    """
    splitline = line.split()
    command = splitline[0]
    if command == 'push':
        segment = splitline[1]
        index = splitline[2]
        out = mem.push(segment, index, progname)
    elif command == 'pop':
        segment = splitline[1]
        index = splitline[2]
        out = mem.pop(segment, index, progname)
    else:
        out = arithmetic.generate(command)
    return out


def translator(filename: str, outfile):
    """
    manages the translation of a single file of VM to assembly
    :param filename: name of VM file to be translated
    :param outfile: name of asm file to write to
    :return: None
    """
    progname = filename[:-3]
    vm_code = parser(filename)
    for line in vm_code:
        out_line = trans_line(line, progname)
        outfile.write(out_line)  # write out_line to file


def main():
    input_path = sys.argv[1]
    if os.path.isfile(input_path):  # given path is single file
        progname = input_path[:-3]
        outfilename = progname + '.asm'
        of = open(outfilename, 'w')
        translator(progname + '.vm', of)
        of.close()
    else:  # path is directory
        files = os.listdir(input_path)
        outfile = input_path + '/' + os.path.basename(input_path) + '.asm'
        of = open(outfile, 'w')
        for file in files:
            if file.endswith('.vm'):
                progname = input_path + '/' + file
                translator(progname, of)
        of.close()


if __name__ == "__main__":
    main()