


class SymbolTable:

    def __init__(self):
        self.table = {}

        self.table['static'] = {}
        self.table['field'] = {}
        self.table['var'] = {}
        self.table['arg'] = {}
        self.indices = {'static': 0, 'field': 0, 'var': 0, 'arg': 0}

    def start_subroutine(self):
        self.table['var'] = {}
        self.table['arg'] = {}
        self.indices['arg'] = 0
        self.indices['var'] = 0

    def define(self, name: str, type: str, kind):
        self.table[kind][name] = (type, self.indices[kind])
        self.indices[kind] += 1


    def kind_of(self, name: str):
        if name in self.table['static']:
            return 'static'
        elif name in self.table['field']:
            return 'field'
        elif name in self.table['var']:
            return 'var'
        elif name in self.table['arg']:
            return 'arg'


    def type_of(self, name: str):
        if name in self.table['static']:
            return self.table['static'][name][0]
        elif name in self.table['field']:
            return self.table['field'][name][0]
        elif name in self.table['var']:
            return self.table['var'][name][0]
        elif name in self.table['arg']:
            return self.table['arg'][name][0]


    def index_of(self, name: str):
        if name in self.table['static']:
            return self.table['static'][name][1]
        elif name in self.table['field']:
            return self.table['field'][name][1]
        elif name in self.table['var']:
            return self.table['var'][name][1]
        elif name in self.table['arg']:
            return self.table['arg'][name][1]