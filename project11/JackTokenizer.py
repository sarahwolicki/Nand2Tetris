import re

class JackTokenizer:

    def __init__(self, filename):
        """
        opens input file and gets ready to tokenize it
        :param filename:
        """
        input_file = open(filename, 'r')
        input_lines = input_file.readlines()

        lines = []
        #removecomments and empty lines
        for line in input_lines:
            line = re.sub('[/][*].*[*][/]', '', line)
            line = (line.partition("//")[0]).lstrip()
            if not line in (None, '', '\n'):
                if line[0] != '*' and line[0:3] != '/**':
                    lines.append(line)


        #join all lines into one string
        text = " ".join(lines)
        strings = re.findall('["].*["]', text)
        for i, s in enumerate(strings):
            strings[i] = s.strip('"')
        text = re.sub('["].*["]', '#string_literal', text)

        #add spaces surrounding symbols
        symbols = re.compile('[{}()\[\].,;+\-*/&|<>=~]')
        text = symbols.sub(' \g<0> ', text)

        self.tokens = text.split()

        string_counter = 0
        for i, token in enumerate(self.tokens):
            if token == '#string_literal':
                self.tokens[i] = strings[string_counter]
                string_counter += 1

        self.more_tokens = True
        self.token_index = 0
        self.current_token = None
        self.next_token = None
        self.string_constants = strings
        self.num_tokens = len(self.tokens)

    def has_more_tokens(self):
        """
        checks if there are more tokens in the input
        :return: boolean
        """
        return self.more_tokens


    def advance(self):
        """
        gets next token and makes it current token
        :return: None
        """
        if self.current_token == None:
            self.current_token = self.tokens[0]
        else:
            self.token_index += 1
            self.current_token = self.next_token
        if self.token_index < self.num_tokens - 1:
            self.next_token = self.tokens[self.token_index + 1]
        else:
            self.more_tokens = False


    def token_type(self):
        """
        returns type of current token
        :return: str
        """
        keywords = ['class', 'constructor', 'function', 'method', 'field',
                    'static', 'var', 'int', 'char', 'boolean', 'void', 'true',
                    'false', 'null', 'this', 'let', 'do', 'if', 'else',
                    'while', 'return']
        symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+',
                        '-', '*', '/', '&', '|', '<', '>', '=', '~']
        if self.current_token in keywords:
            return 'keyword'
        elif self.current_token in symbols:
            return 'symbol'
        elif self.current_token in self.string_constants:
            return 'stringConstant'
        elif self.current_token.isdigit():
            return 'integerConstant'
        else:
            return 'identifier'


    def get_current_token(self):
        return self.current_token

