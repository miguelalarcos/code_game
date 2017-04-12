class Asignacion:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return ' '*tab + '{a} = {b}'.format(a=self.left.to_code(0), b=self.right.to_code(0))

    def to_str(self, tab):
        return ' ' * tab + '{a} es igual a {b}'.format(a=self.left.to_str(0), b=self.right.to_str(0))


class Literal:
    def __init__(self, text):
        self.text = text

    def to_code(self, tab):
        return ' '*tab + self.text

    def to_str(self, tab):
        return ' ' * tab + self.text

class ListCode:
    def __init__(self, lista):
        self.code = lista

    def to_code(self, tab):
        return '\n'.join([c.to_code(tab) for c in self.code])

    def to_str(self, tab):
        return '\n'.join([c.to_str(tab) for c in self.code])

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

    def to_str(self, tab):
        lista = [' '*tab + 'si {expr}:'.format(expr=self.expresion.to_str(0)),
                 self.codeif.to_str(tab+4),
                 ' '*tab + 'en caso contrario:',
                 self.codeelse.to_str(tab+4)]
        return '\n'.join([c for c in lista])

class Procedimiento:
    def __init__(self, name, lista):
        self.name = name
        self.lista = lista

    def to_code(self, tab=0):
        return ' '*tab + 'def {a}():\n'.format(a=self.name) + self.lista.to_code(tab+4)

    def to_str(self, tab=0):
        return ' ' * tab + 'def {a}():\n'.format(a=self.name) + self.lista.to_str(tab + 4)


class MenorQue:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} < {right}'.format(left=self.left.to_code(0), right=self.right.to_code(0))

    def to_str(self, tab):
        return '{left} es menor que {right}'.format(left=self.left.to_str(0), right=self.right.to_str(0))


class MayorQue:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} > {right}'.format(left=self.left.to_code(0), right=self.right.to_code(0))

    def to_str(self, tab):
        return '{left} es mayor que {right}'.format(left=self.left.to_str(0), right=self.right.to_str(0))


class MenorIgualQue:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} <= {right}'.format(left=self.left.to_code(0), right=self.right.to_code(0))

    def to_str(self, tab):
        return '{left} es menor o igual que {right}'.format(left=self.left.to_str(0), right=self.right.to_str(0))


class MayorIgualQue:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} >= {right}'.format(left=self.left.to_code(0), right=self.right.to_code(0))

    def to_str(self, tab):
        return '{left} es mayor o igual que {right}'.format(left=self.left.to_str(0), right=self.right.to_str(0))

class Igual:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} == {right}'.format(left=self.left.to_code(0), right=self.right.to_code(0))

    def to_str(self, tab):
        return '{left} es igual a {right}'.format(left=self.left.to_str(0), right=self.right.to_str(0))


class Y:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} and {right}'.format(left=self.left.to_code(0), right=self.right.to_code(0))

    def to_str(self, tab):
        return '{left} y {right}'.format(left=self.left.to_str(0), right=self.right.to_str(0))


class O:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_code(self, tab):
        return '{left} or {right}'.format(left=self.left.to_code(0), right=self.right.to_code(0))

    def to_str(self, tab):
        return '{left} o {right}'.format(left=self.left.to_str(0), right=self.right.to_str(0))

class No:
    def __init__(self, code):
        self.code = code

    def to_code(self, tab):
        return 'not {code}'.format(code=self.code.to_code(0))

    def to_str(self, tab):
        return 'no es {code}'.format(code=self.code.to_str(0))


class Incrementar:
    def __init__(self, left, q):
        self.left = left
        self.q = q

    def to_code(self, tab):
        return ' '*tab + '{left} += {q}'.format(left=self.left.to_code(0), q=self.q.to_code(0))

    def to_str(self, tab):
        return ' ' * tab + 'sumar {q} a {left}'.format(left=self.left.to_str(0), q=self.q.to_str(0))


class Decrementar:
    def __init__(self, left, q):
        self.left = left
        self.q = q

    def to_code(self, tab):
        return ' ' * tab + '{left} -= {q}'.format(left=self.left.to_code(0), q=self.q.to_code(0))

    def to_str(self, tab):
        return ' ' * tab + 'restar {q} a {left}'.format(left=self.left.to_str(0), q=self.q.to_str(0))


class LlamarFuncion:
    def __init__(self, name, args):
        #self.left = left
        self.name = name
        self.args = args

    def to_code(self, tab):
        return ' '*tab + '{name}({args})'.format(name=self.name, args=', '.join([str(x) for x in self.args]))

    def to_str(self, tab):
        return ' ' * tab + '{name}({args})'.format(name=self.name, args=', '.join([str(x) for x in self.args]))


class Longitud:
    def __init__(self, lista_name):
        self.lista_name = lista_name

    def to_code(self, tab=0):
        return 'len({lista})'.format(lista=self.lista_name)

    def to_str(self, tab=0):
        return 'la longitud de {lista}'.format(lista=self.lista_name)


# ###################
enemigos = []
#expr = Asignacion(Literal('x'), LlamarFuncion('f', []))
expr = Asignacion(Literal('x'), Longitud('enemigos'))
incr = Incrementar(Literal('x'), Literal('5'))

and_expr = Y(MenorQue(Literal('x'), Literal('10')), MayorQue(Literal('x'), Literal('0')))

if1 = If(and_expr,
         ListCode([Literal('print("hola")')]),
         ListCode([Literal('print("mundo")')]))

lista_code = ListCode([Procedimiento('f', ListCode([Literal('return 5')])), expr,
                       incr, if1])
proc = Procedimiento('main', lista_code)
str_code = proc.to_code()

print(str_code)
exec(str_code)
main()

print(proc.to_str())