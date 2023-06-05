from delta import Compiler, Phase


source = '#b10000000000000000000000000000000'

c = Compiler('program')
c.realize(source, Phase.EVALUATION)
print()
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)
