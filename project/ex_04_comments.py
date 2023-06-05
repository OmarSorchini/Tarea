from delta import Compiler, Phase


source = '''
/* A block comment. */
// A line comment.

0

/*
   A block
   comment.
*/
'''

c = Compiler('program')
c.realize(source, Phase.EVALUATION)
print()
# print(c.parse_tree_str)
# print()
print(c.wat_code)
print()
print(c.result)
