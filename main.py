class Asignacion:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return ' '*tab + '{a} = {b}'.format(a=self.left, b=self.right)


class Arbitrary:
    def __init__(self, text):
        self.text = text

    def to_code(self, tab):
        return ' '*tab + self.text


class ListCode:
    def __init__(self, lista):
        self.code = lista

    def to_code(self, tab):
        return '\n'.join([c.to_code(tab) for c in self.code])


class If:
    def __init__(self, expresion, codeif, codeelse):
        self.expresion = expresion
        self.codeif = codeif
        self.codeelse = codeelse

    def to_code(self, tab):
        lista = [' '*tab + 'if {expr}:'.format(expr=self.expresion.to_code(0)),
                 self.codeif.to_code(tab+4),
                 ' '*tab + 'else:',
                 self.codeelse.to_code(tab+4)]
        return '\n'.join([c for c in lista])


class Procedimiento:
    def __init__(self, name, lista):
        self.name = name
        self.lista = lista

    def to_code(self, tab=0):
        return ' '*tab+  'def {a}():\n'.format(a=self.name) + self.lista.to_code(tab+4)


class MenorQue:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} < {right}'.format(left=self.left, right=self.right)


class MayorQue:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} > {right}'.format(left=self.left, right=self.right)


class MenorIgualQue:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} <= {right}'.format(left=self.left, right=self.right)


class MayorIgualQue:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} >= {right}'.format(left=self.left, right=self.right)


class Igual:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} == {right}'.format(left=self.left, right=self.right)

class Y:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} and {right}'.format(left=self.left.to_code(0), right=self.right.to_code(0))


class O:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} or {right}'.format(left=self.left.to_code(0), right=self.right.to_code(0))


class No:
    def __init__(self, code):
        self.code = code

    def to_code(self, tab):
        return 'not {code}'.format(code=self.code.to_code(0))


class Incrementar:
    def __init__(self, left, q):
        self.left = left
        self.q = q

    def to_code(self, tab):
        return ' '*tab + '{left} += {q}'.format(left=self.left, q=self.q)


class Decrementar:
    def __init__(self, left, q):
        self.left = left
        self.q = q

    def to_code(self, tab):
        return ' ' * tab + '{left} -= {q}'.format(left=self.left, q=self.q)


class LlamarProc:
    def __init__(self, left, name, args):
        self.left = left
        self.name = name
        self.args = args

    def to_code(self, tab):
        return ' '*tab + '{left} = {name}({args})'.format(left=self.left, name=self.name, args=', '.join([str(x) for x in self.args]))


# ###################

#expr = Asignacion('x', 5)
expr = LlamarProc('x', 'f', [])
incr = Incrementar('x', 10)

and_expr = Y(MenorQue('x', 10), MayorQue('x', 0))

if1 = If(and_expr,
         ListCode([Arbitrary('print("hola")')]),
         ListCode([Arbitrary('print("mundo")')]))

lista_code = ListCode([Procedimiento('f', ListCode([Arbitrary('return 5')])), expr,
                       incr, if1])
proc = Procedimiento('main', lista_code)
str_code = proc.to_code()

print(str_code)
exec(str_code)
main()

