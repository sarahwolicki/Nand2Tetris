from JackTokenizer import JackTokenizer

class CompilationEngine:

    def __init__(self, tokenizer, outfile):
        self.tokenizer = tokenizer
        self.out = outfile
        self.indent = 0


    def write_tok_to_xml(self):
        line = self.indent*2*' '
        line += '<' + self.tokenizer.token_type() + '> '
        if self.tokenizer.current_token == '<':
            line += '&lt;'
        elif self.tokenizer.current_token == '<':
            line += '&gt;'
        elif self.tokenizer.current_token == '&':
            line += '&amp;'
        else:
            line += self.tokenizer.current_token
        line += ' </' + self.tokenizer.token_type() + '>\n'
        self.out.write(line)
        if self.tokenizer.more_tokens == True:
            self.tokenizer.advance()


    def compile_class(self):
        #print('compiling class\n')
        self.out.write('<class>\n')
        self.indent += 1
        for i in range(3): # class, class name, {
            self.write_tok_to_xml()
        while self.tokenizer.current_token == 'field' or \
                self.tokenizer.current_token == 'static':
            self.compile_class_var_dec()
        while self.tokenizer.current_token == 'constructor' or \
                self.tokenizer.current_token == 'function' or \
                self.tokenizer.current_token == 'method':
            self.compile_subroutine()
        self.indent -= 1
        self.write_tok_to_xml() # }
        self.out.write('</class>\n')


    def compile_class_var_dec(self):
        #print('compiling class var dec\n')
        self.out.write('<classVarDec>\n')
        self.indent += 1
        for i in range(3): #static/field, type, var name
            self.write_tok_to_xml()
        while self.tokenizer.current_token == ',': #if there are additional
            # variables being declared
            self.write_tok_to_xml()
            self.write_tok_to_xml()
        self.write_tok_to_xml() #;
        self.indent -= 1
        self.out.write('</classVarDec>\n')


    def compile_subroutine(self):
        #print('compiling subroutine\n')
        self.out.write('<subroutineDec>\n')
        self.indent += 1
        for i in range(4): # constructor/method/function, type, name, (
            self.write_tok_to_xml()
        self.compile_parameter_list()
        self.write_tok_to_xml() # )
        #self.write_tok_to_xml() # :
        self.compile_subroutine_body()
        self.indent -= 1
        self.out.write('</subroutineDec>\n')


    def compile_subroutine_body(self):
        #print('compiling subroutine body\n')
        self.out.write('<subroutineBody>\n')
        self.indent += 1
        self.write_tok_to_xml() # {
        while self.tokenizer.current_token == 'var':
            self.compile_var_dec()
        self.compile_statements()
        self.write_tok_to_xml()  # }
        self.indent -= 1
        self.out.write('</subroutineBody>\n')


    def compile_parameter_list(self):
        #print('compiling parameter list\n')
        self.out.write(self.indent*' ' + '<parameterList>\n')
        if self.tokenizer.current_token != ')': # if not empty parameter list
            self.indent += 1
            self.write_tok_to_xml() # type
            self.write_tok_to_xml() # parameter name
            while self.tokenizer.current_token == ',': #any additional parameters
                self.write_tok_to_xml()  # type
                self.write_tok_to_xml()  # parameter name
            self.indent += 1
        self.out.write(self.indent*' ' + '</parameterList>\n')


    def compile_var_dec(self):
        #print('compiling var dec\n')
        self.out.write('<varDec>\n')
        self.indent += 1
        for i in range(3): # var, type, varname
            self.write_tok_to_xml()
        while self.tokenizer.current_token == ',':
            self.write_tok_to_xml() # ,
            self.write_tok_to_xml() # additional var name
        self.write_tok_to_xml() # ;
        self.indent -= 1
        self.out.write('</varDec>\n')


    def compile_statements(self):
        #print('compiling statements\n')
        self.out.write('<statements>\n')
        self.indent += 1
        while self.tokenizer.current_token != '}':
            if self.tokenizer.current_token == 'do':
                self.compile_do()
            if self.tokenizer.current_token == 'let':
                self.compile_let()
            if self.tokenizer.current_token == 'while':
                self.compile_while()
            if self.tokenizer.current_token == 'return':
                self.compile_return()
            if self.tokenizer.current_token == 'if':
                self.compile_if()
        self.indent -= 1
        self.out.write('</statements>\n')


    def compile_do(self):
        #print('compiling do\n')
        self.out.write('<doStatement>\n')
        self.indent += 1
        self.write_tok_to_xml() # do
        self.write_tok_to_xml() # identifier
        if self.tokenizer.current_token == '.':
            self.write_tok_to_xml() # .
            self.write_tok_to_xml() # identifier
        self.write_tok_to_xml() # (
        self.compile_expression_list()
        self.write_tok_to_xml() # )
        self.write_tok_to_xml() # ;
        self.indent -= 1
        self.out.write('</doStatement>\n')


    def compile_let(self):
        #print('compiling let\n')
        self.out.write('<letStatement>\n')
        self.indent += 1
        self.write_tok_to_xml()  # let
        self.write_tok_to_xml()  # identifier
        if self.tokenizer.current_token == '[':
            self.write_tok_to_xml() # [
            self.compile_expression()
            self.write_tok_to_xml() # ]
        self.write_tok_to_xml() # =
        self.compile_expression()
        self.write_tok_to_xml() # ;
        self.indent -= 1
        self.out.write('</letStatement>\n')


    def compile_while(self):
        #print('compiling while\n')
        self.out.write('<whileStatement>\n')
        self.indent += 1
        self.write_tok_to_xml() # while
        self.write_tok_to_xml() # (
        self.compile_expression()
        self.write_tok_to_xml() # )
        self.write_tok_to_xml() # {
        self.compile_statements()
        self.write_tok_to_xml() # }
        self.indent -= 1
        self.out.write('</whileStatement>\n')


    def compile_return(self):
        #print('compiling return\n')
        self.out.write('<returnStatement>\n')
        self.write_tok_to_xml() # return
        if self.tokenizer.current_token != ';':
            self.compile_expression()
        self.write_tok_to_xml() # ;
        self.out.write('</returnStatement>\n')


    def compile_if(self):
        #print('compiling if\n')
        self.out.write('<ifStatement>\n')
        self.indent += 1
        self.write_tok_to_xml() # if
        self.write_tok_to_xml() # (
        self.compile_expression()
        self.write_tok_to_xml() # )
        self.write_tok_to_xml() # {
        self.compile_statements()
        self.write_tok_to_xml()  # }
        if self.tokenizer.current_token == 'else':
            self.write_tok_to_xml()  # else
            self.write_tok_to_xml()  # {
            self.compile_statements()
            self.write_tok_to_xml()  # }
        self.indent -= 1
        self.out.write('</ifStatement>\n')


    def compile_expression(self):
        #print('compiling expression\n')
        self.out.write('<expression>\n')
        self.indent += 1
        self.compile_term()
        ops = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
        while self.tokenizer.current_token in ops:
            self.write_tok_to_xml() # operator
            self.compile_term()
        self.indent -= 1
        self.out.write('</expression>\n')


    def compile_term(self):
        #print('compiling term\n')
        self.out.write('<term>\n')
        self.indent += 1
        cur_type = self.tokenizer.token_type()
        next = self.tokenizer.next_token
        if cur_type == 'integerConstant' or cur_type == 'stringConstant' or \
                self.tokenizer.current_token in ['true', 'false', 'null', 'this']:
            self.write_tok_to_xml()
        elif cur_type == 'identifier' and next not in ['[', '(', '.']: #varname
            self.write_tok_to_xml()
        elif cur_type == 'identifier' and next == '[':
            self.write_tok_to_xml() # varname
            self.write_tok_to_xml() # [
            self.compile_expression()
            self.write_tok_to_xml()  # ]
        elif cur_type == 'identifier' and next in ['(', '.']:
            self.compile_subroutine_call()
        elif self.tokenizer.current_token == '(':
            self.write_tok_to_xml()  # (
            self.compile_expression()
            self.write_tok_to_xml()  # )
        elif self.tokenizer.current_token in ['-', '~']:
            self.write_tok_to_xml()  # unary operator
            self.compile_term()
        self.indent -= 1
        self.out.write('</term>\n')


    def compile_subroutine_call(self):
        #print('compiling subroutine call\n')
        self.write_tok_to_xml()
        if self.tokenizer.current_token == '.':
            self.write_tok_to_xml()
            self.write_tok_to_xml()
        self.write_tok_to_xml() # (
        if self.tokenizer.current_token != ')':
            self.compile_expression_list()
        self.write_tok_to_xml()  # )



    def compile_expression_list(self):
        #print('compiling expression list\n')
        self.out.write('<expressionList>\n')
        if not self.tokenizer.current_token == ')':
            self.indent += 1
            self.compile_expression()
            while self.tokenizer.current_token == ',':
                self.compile_expression()
            self.indent -= 1
        self.out.write('</expressionList>\n')