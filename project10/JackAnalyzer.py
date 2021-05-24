import sys
import os
from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine


def main():
    input_path = sys.argv[1]
    if os.path.isfile(input_path):
        tokenizer = JackTokenizer(input_path)
        tokenizer.advance()
        name = input_path[:-5]
        outfile_name = name + '.xml'
        of = open(outfile_name, 'w')
        compiler = CompilationEngine(tokenizer, of)
        compiler.compile_class()
    else: #input is directory
        files = os.listdir(input_path)
        for file in files:
            if file.endswith('.jack'):
                tokenizer = JackTokenizer(input_path + '/' + file)
                tokenizer.advance()
                outfile_name = input_path + '/' + file[:-5] + '.xml'
                of = open(outfile_name, 'w')
                compiler = CompilationEngine(tokenizer, of)
                compiler.compile_class()



if __name__ == '__main__':
    main()
