

class VMWriter:

    def __init__(self, outfile):
        of = open(outfile, 'w')
        self.out = of

    def write_push(self, segment, index):
        self.out.write('push ' + segment + ' ' + str(index) + '\n')

    def write_pop(self, segment, index):
        self.out.write('pop ' + segment + ' ' + str(index) + '\n')

    def write_arithmetic(self, command):
        self.out.write(command + '\n')

    def write_label(self, label):
        self.out.write('label ' + label + '\n')

    def write_goto(self, label):
        self.out.write('goto ' + label + '\n')

    def write_if(self, label):
        self.out.write('if-goto ' + label + '\n')

    def write_call(self, name, n_args):
        self.out.write('call ' + name + ' ' + str(n_args) + '\n')

    def write_function(self, name, n_locals):
        self.out.write('function ' + name + ' ' + str(n_locals) + '\n')

    def write_return(self):
        self.out.write('return\n')

    def close(self):
        self.out.close()

