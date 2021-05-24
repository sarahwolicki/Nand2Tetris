from JackTokenizer import JackTokenizer
from SymbolTable import SymbolTable
from VMWriter import VMWriter


class CompilationEngine:

    mem_segs = {"field": "this",
                    "static": "static",
                    "var": "local",
                    "arg": "argument"}

    op_commands = {"+": "add",
               "-": "sub",
               "*": "call Math.multiply 2",
               "/": "call Math.divide 2",
               "&": "and",
               "|": "or",
               "<": "lt",
               ">": "gt",
               "=": "eq"}

    def __init__(self, tokenizer: JackTokenizer, vmwriter: VMWriter):
        self.tokenizer = tokenizer
        self.writer = vmwriter
        self.symbol_table = SymbolTable()
        self.while_count = 0
        self.if_count = 0


    def compile_class(self):
        self.tokenizer.advance() # class
        self.class_name = self.tokenizer.current_token
        self.tokenizer.advance() # class name
        self.tokenizer.advance() # {
        while self.tokenizer.current_token == 'field' or \
                self.tokenizer.current_token == 'static':
            self.compile_class_var_dec()
        while self.tokenizer.current_token == 'constructor' or \
                self.tokenizer.current_token == 'function' or \
                self.tokenizer.current_token == 'method':
            self.compile_subroutine()
        # }


    def compile_class_var_dec(self):
        var_kind = self.tokenizer.current_token # static/field
        self.tokenizer.advance()
        var_type = self.tokenizer.current_token # data type
        self.tokenizer.advance()
        var_name = self.tokenizer.current_token
        self.tokenizer.advance()
        self.symbol_table.define(var_name, var_type, var_kind)
        while self.tokenizer.current_token == ',': # if there are additional
            # variables being declared
            self.tokenizer.advance() # ,
            var_name = self.tokenizer.current_token
            self.symbol_table.define(var_name, var_type, var_kind)
            self.tokenizer.advance()
        self.tokenizer.advance() # ;


    def compile_subroutine(self):
        self.symbol_table.start_subroutine()
        sub_kind = self.tokenizer.current_token # constructor/method/function
        self.tokenizer.advance()
        self.tokenizer.advance()
        sub_name = self.tokenizer.current_token
        self.tokenizer.advance() # sub_name
        if sub_kind == 'method':
            self.symbol_table.define('this', self.class_name, 'arg')
        self.tokenizer.advance()  # (
        self.compile_parameter_list()
        self.tokenizer.advance() # )
        func_name = self.class_name + '.' + sub_name
        self.tokenizer.advance() # {
        while self.tokenizer.current_token == 'var':
            self.compile_var_dec()
        n_vars = self.symbol_table.indices['var']
        self.writer.write_function(func_name, n_vars)
        self.compile_subroutine_body(sub_kind)
        self.tokenizer.advance()  # }


    def compile_subroutine_body(self, sub_kind):
        if sub_kind == 'constructor':
            n_fields = self.symbol_table.indices['field']
            self.writer.write_push('constant', n_fields)
            self.writer.write_call('Memory.alloc', 1)
            self.writer.write_pop('pointer', 0)
        elif sub_kind == 'method':
            self.writer.write_push('argument', 0)
            self.writer.write_pop('pointer', 0)
        self.compile_statements()


    def compile_parameter_list(self):
        if self.tokenizer.current_token != ')': # if not empty parameter list
            type = self.tokenizer.current_token # type
            self.tokenizer.advance()
            name = self.tokenizer.current_token # parameter name
            self.tokenizer.advance()
            self.symbol_table.define(name, type, 'arg')
            while self.tokenizer.current_token == ',': #any additional parameters
                self.tokenizer.advance() # ,
                type = self.tokenizer.current_token  # type
                self.tokenizer.advance()
                name = self.tokenizer.current_token  # parameter name
                self.tokenizer.advance()
                self.symbol_table.define(name, type, 'arg')


    def compile_var_dec(self):
        self.tokenizer.advance() # var
        type = self.tokenizer.current_token
        self.tokenizer.advance()
        var_name = self.tokenizer.current_token
        self.tokenizer.advance()
        self.symbol_table.define(var_name, type, 'var')
        while self.tokenizer.current_token == ',':
            self.tokenizer.advance() # ,
            var_name = self.tokenizer.current_token
            self.tokenizer.advance()
            self.symbol_table.define(var_name, type, 'var') # additional var name
        self.tokenizer.advance() # ;


    def compile_statements(self):
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


    def compile_do(self):
        self.tokenizer.advance() # do
        self.compile_subroutine_call()
        self.writer.write_pop('temp', 0)
        self.tokenizer.advance()  # ;


    def compile_let(self):
        self.tokenizer.advance() # let
        var_name = self.tokenizer.current_token
        self.tokenizer.advance()
        var_kind = self.symbol_table.kind_of(var_name)
        var_index = self.symbol_table.index_of(var_name)

        if self.tokenizer.current_token == '[':
            self.tokenizer.advance() # [
            self.compile_expression()
            self.tokenizer.advance() # [
            mem_seg = self.mem_segs[var_kind]
            self.writer.write_push(mem_seg, var_index)
            self.writer.write_arithmetic('add')
            self.writer.write_pop('temp', 0)
            self.tokenizer.advance() # =
            self.compile_expression()
            self.writer.write_push('temp', 0)
            self.writer.write_pop('pointer', 1)
            self.writer.write_pop('that', 0)

        else:
            self.tokenizer.advance() # =
            self.compile_expression()
            mem_seg = self.mem_segs[var_kind]
            self.writer.write_pop(mem_seg, var_index)

        self.tokenizer.advance()  # ;


    def compile_while(self):
        while_count = str(self.while_count)
        exp_label = 'WHILE_EXP' + while_count
        end_label = 'WHILE_END' + while_count
        self.while_count += 1
        self.writer.write_label(exp_label)
        self.tokenizer.advance() # while
        self.tokenizer.advance() # (
        self.compile_expression()
        self.tokenizer.advance() # )
        self.writer.write_arithmetic('not')
        self.writer.write_if(end_label)
        self.tokenizer.advance() # {
        self.compile_statements()
        self.tokenizer.advance() # }
        self.writer.write_goto(exp_label)
        self.writer.write_label(end_label)



    def compile_return(self):
        self.tokenizer.advance() # return
        if self.tokenizer.current_token != ';':
            self.compile_expression()
        else:
            self.writer.write_push('constant', 0)
        self.writer.write_return()
        self.tokenizer.advance() # ;


    def compile_if(self):
        self.tokenizer.advance() # if
        self.tokenizer.advance() # (
        self.compile_expression()
        self.tokenizer.advance() # )
        self.tokenizer.advance()  # {
        if_count = str(self.if_count)
        if_label = 'IF' + if_count
        not_label = 'IF_NOT' + if_count
        end_label = 'IF_END' + if_count
        self.if_count += 1
        self.writer.write_if(if_label)
        self.writer.write_goto(not_label)
        self.writer.write_label(if_label)
        self.compile_statements()
        self.writer.write_goto(end_label)
        self.tokenizer.advance()  # }
        self.writer.write_label(not_label)
        if self.tokenizer.current_token == 'else':
            self.tokenizer.advance() # else
            self.tokenizer.advance() # {
            self.compile_statements()
            self.tokenizer.advance() # }
        self.writer.write_label(end_label)


    def compile_expression(self):
        self.compile_term()
        ops = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
        while self.tokenizer.current_token in ops:
            op = self.tokenizer.current_token
            self.tokenizer.advance() # operator
            self.compile_term()
            self.writer.write_arithmetic(self.op_commands[op])


    def compile_term(self):
        cur_type = self.tokenizer.token_type()
        cur = self.tokenizer.current_token
        next = self.tokenizer.next_token
        if cur_type == 'integerConstant':
            self.writer.write_push('constant', int(cur))
            self.tokenizer.advance()
        elif cur_type == 'stringConstant':
            self.writer.write_push('constant', len(cur))
            self.writer.write_call('String.new', 1)
            for char in cur:
                self.writer.write_push('constant', ord(char))
                self.writer.write_call('String.appendChar', 2)
            self.tokenizer.advance()
        elif cur in ['true', 'false', 'null', 'this']: # keyword constant
            if cur == 'true':
                self.writer.write_push('constant', 0)
                self.writer.write_arithmetic('not')
            elif cur == 'false' or cur == 'null':
                self.writer.write_push('constant', 0)
            else: # this
                self.writer.write_push('pointer', 0)
            self.tokenizer.advance()
        elif cur_type == 'identifier' and next not in ['[', '(', '.']: #varname
            var_name = cur
            var_kind = self.symbol_table.kind_of(var_name)
            mem_seg = self.mem_segs[var_kind]
            var_index = self.symbol_table.index_of(var_name)
            self.writer.write_push(mem_seg, var_index)
            self.tokenizer.advance()
        elif cur_type == 'identifier' and next == '[':
            var_name = cur
            self.tokenizer.advance() # var_name
            self.tokenizer.advance() # [
            self.compile_expression()
            self.tokenizer.advance()  # ]
            var_kind = self.symbol_table.kind_of(var_name)
            mem_seg = self.mem_segs[var_kind]
            var_index = self.symbol_table.index_of(var_name)
            self.writer.write_push(mem_seg, var_index)
            self.writer.write_arithmetic('add')
            self.writer.write_pop('pointer', 1)
            self.writer.write_push('that', 0)
        elif cur_type == 'identifier' and next in ['(', '.']:
            self.compile_subroutine_call()
        elif self.tokenizer.current_token == '(':
            self.tokenizer.advance()  # (
            self.compile_expression()
            self.tokenizer.advance()  # )
        elif self.tokenizer.current_token in ['-', '~']:
            self.tokenizer.advance()
            self.compile_term()
            if cur == '~':
                self.writer.write_arithmetic('not')
            else:
                self.writer.write_arithmetic('neg')


    def compile_subroutine_call(self):
        cur = self.tokenizer.current_token
        self.tokenizer.advance()
        n_args = 0
        if self.tokenizer.current_token == '.':
            self.tokenizer.advance() # .
            sub_rout = self.tokenizer.current_token
            self.tokenizer.advance()
            func_type = self.symbol_table.type_of(cur)

            func_kind = self.symbol_table.kind_of(cur)
            func_index = self.symbol_table.index_of(cur)
            if func_type:
                mem_seg = self.mem_segs[func_kind]
                self.writer.write_push(mem_seg, func_index)
                func_name = func_type + '.' + sub_rout
                n_args += 1
            else:
                class_name = cur
                func_name = class_name + '.' + sub_rout
        else: # (
            func_name = self.class_name + '.' + cur
            self.writer.write_push('pointer', 0)
            n_args += 1
        self.tokenizer.advance() # (
        n_args += self.compile_expression_list()
        self.tokenizer.advance() # )
        self.writer.write_call(func_name, n_args)



    def compile_expression_list(self):
        exp_count = 0
        if not self.tokenizer.current_token == ')':
            self.compile_expression()
            exp_count += 1
            while self.tokenizer.current_token == ',':
                self.tokenizer.advance() # ,
                self.compile_expression()
                exp_count += 1
        return exp_count
