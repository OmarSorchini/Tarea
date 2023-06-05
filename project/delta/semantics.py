from arpeggio import PTNodeVisitor


class SemanticMistake(Exception):

    def __init__(self, message):
        super().__init__(f'Semantic error: {message}')


class SemanticVisitor(PTNodeVisitor):

    RESERVED_WORDS = ['true', 'false', 'var', 'if', 'else', 'while', 'do']

    def __init__(self, parser, **kwargs):
        super().__init__(**kwargs)
        self.__parser = parser
        self.__symbol_table = []

    def position(self, node):
        return self.__parser.pos_to_linecol(node.position)

    @property
    def symbol_table(self):
        return self.__symbol_table

    def visit_decl_variable(self, node, children):
        name = node.value
        if name in SemanticVisitor.RESERVED_WORDS:
            raise SemanticMistake(
                'Reserved word not allowed as variable name at position '
                f'{self.position(node)} => {name}'
            )
        if name in self.__symbol_table:
            raise SemanticMistake(
                'Duplicate variable declaration at position'
                f'{self.position(node)} => {name}'
            )
        self.__symbol_table.append(name)

    def visit_lhs_variable(self, node, children):
        name = node.value
        if name not in self.__symbol_table:
            raise SemanticMistake(
                'Assignment to undeclared variable at position '
                f'{self.position(node)} => {name}'
            )

    def visit_binary(self, node, children):
        value = node.value[2:]
        value = value[::-1]
        decVal = 0
        for i in range(len(value)):
            if int(value[i]) == 1:
                decVal += 2**i
        if decVal >= 2 ** 31:
            raise SemanticMistake(
                'Out of range decimal integer literal at position '
                f'{self.position(node)} => {value[::-1]}'
            )

    def visit_octal(self, node, children):
        value = node.value[2:]
        value = value[::-1]
        decVal = 0
        for i in range(len(value)):
            decVal += (8 ** i) * int(value[i])
        if decVal >= 2 ** 31:
            raise SemanticMistake(
                'Out of range decimal integer literal at position '
                f'{self.position(node)} => {value[::-1]}'
            )

    def visit_hexa(self, node, children):
        value = node.value[2:]
        value = value[::-1]
        decVal = 0
        for i in range(len(value)):
            if value[i].isdigit():
                decVal += (16 ** i) * int(value[i])
            elif (value[i].lower() in "abcdef"):
                letter = value[i].lower()
                if letter == "a":
                    decVal += (16 ** i) * 10
                elif letter == "b":
                    decVal += (16 ** i) * 11
                elif letter == "c":
                    decVal += (16 ** i) * 12
                elif letter == "d":
                    decVal += (16 ** i) * 13
                elif letter == "e":
                    decVal += (16 ** i) * 14
                elif letter == "f":
                    decVal += (16 ** i) * 15

        if decVal >= 2 ** 31:
            raise SemanticMistake(
                'Out of range decimal integer literal at position '
                f'{self.position(node)} => {value[::-1]}'
            )
        
    def visit_decimal(self, node, children):
        value = int(node.value)
        if value >= 2 ** 31:
            raise SemanticMistake(
                'Out of range decimal integer literal at position '
                f'{self.position(node)} => {value}'
            )

    def visit_rhs_variable(self, node, children):
        name = node.value
        if name not in self.__symbol_table:
            raise SemanticMistake(
                'Undeclared variable reference at position '
                f'{self.position(node)} => {name}'
            )
