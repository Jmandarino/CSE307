import string
import sys
import tpg

"""
Need help with multiple symbol inputs.

need help processing list


need help with "in" and not

"""

class SemanticError(Exception):
    """
    This is the class of the exception that is raised when a semantic error
    occurs.
    """

# These are the nodes of our abstract syntax tree.
class Node(object):
    """
    A base class for nodes. Might come in handy in the future.
    """

    def evaluate(self):
        """
        Called on children of Node to evaluate that child.
        """
        raise Exception("Not implemented.")

class IntLiteral(Node):
    """
    A node representing integer literals.
    """

    def __init__(self, value):
        self.value = int(value)

    def evaluate(self):
        return self.value


class RealLiteral(Node):
    """
    A node representing real literals.
    """

    def __init__(self, value):
        self.value = float(value)

    def evaluate(self):
        return self.value

class StringLiteral(Node):
    """
    A node representing string
    """
    def __init__(self, value):
        self.value = str(value).strip('"')


    def evaluate(self):
        return self.value


class ListLiteral(Node):
    """
    A node representing list literals.
    """

    def __init__(self, value):
        if value == None:
            self.value = []
        else:
            print("this is a value"+ str(value))
            self.value = list(value.strip(']').strip('[').split(','))

    def evaluate(self):
        return self.value

    def index(self, value):


        if isinstance(self.value, list) and isinstance(value.evaluate(), int):
            l = self.value
            if isinstance(l[0], int):
                return IntLiteral(l[value.evaluate()])
            elif isinstance(l[0], float):
                return RealLiteral(l[value.evaluate()])
            elif isinstance(l[0], str):
                return StringLiteral(l[value.evaluate()])
        else:
            raise SemanticError()

    def append(self, value):
        #print("does apparend work????")
        #print(self)

        #print(value.evaluate())
        if isinstance(self.value, list):
            if isinstance(value.evaluate(), int):
                self.value.append(int(value.evaluate()))
            elif isinstance(value.evaluate(), float):
                self.value.append(float(value.evaluate()))
            elif isinstance(value.evaluate(), str):
                self.value.append(str(value.evaluate()))
            else:
                self.value.append(value.evaluate())



class Multiply(Node):
    """
    A node representing multiplication.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int) or isinstance(left, float):
            raise SemanticError()
        if not isinstance(right, int) or isinstance(right, float):
            raise SemanticError()
        return left * right

class Divide(Node):
    """
    A node representing division.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int) or isinstance(left, float):
            raise SemanticError()
        if not isinstance(right, int)or isinstance(right, float):
            raise SemanticError()
        if right == 0:
            raise SemanticError()
        return left / right

class Pow(Node):
    """
    A node representing Exponents.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int) or isinstance(left, float):
            raise SemanticError()
        if not isinstance(right, int) or isinstance(right, float):
            raise SemanticError()
        return left ** right

class FloorDiv(Node):
    """
    A node representing Exponents.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int) or isinstance(left, float):
            raise SemanticError()
        if not isinstance(right, int) or isinstance(right, float):
            raise SemanticError()
        return left // right

class Add(Node):
    """
    A node representing addition.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not( isinstance(left, int) or isinstance(left, float) or isinstance(left, str)):
            raise SemanticError()
        if not (isinstance(right, int) or isinstance(right, float) or isinstance(right, str)):
            raise SemanticError()
        if (isinstance(right, int) or isinstance(right, float)) and (isinstance(left, str)):
            raise SemanticError()
        if (isinstance(left, int) or isinstance(left, float)) and (isinstance(right, str)):
            raise SemanticError()
        return left + right


class Index(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def evaluate(self):


        left = self.left.evaluate()
        right = self.right.evaluate()

        if not isinstance(left, list):
            raise SemanticError()
        return left[right]



class Subtract(Node):
    """
    A node representing subtraction.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int) and not isinstance(left, float):
            raise SemanticError()
        if not isinstance(right, int) and not isinstance(right, float):
            raise SemanticError()
        return left - right


class Le(Node):
    """
    A node representing less than.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if ((isinstance(right, int) and not isinstance(left, int))
            or (isinstance(right, float) and not isinstance(left, float))
            or (isinstance(right, str) and not isinstance(left, str))):
            raise SemanticError()
        if(left < right):
            return 1
        else:
            return 0


class LeEqual(Node):
    """
    A node representing less than.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        print("leequal")
        left = self.left.evaluate()
        right = self.right.evaluate()
        if ((isinstance(right, int) and not isinstance(left, int))
            or (isinstance(right, float) and not isinstance(left, float))):
            raise SemanticError()
        if(left <= right):
            return 1
        else:
            return 0

class Ge(Node):
    """
    A node representing greater than.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if ((isinstance(right, int) and not isinstance(left, int))
            or (isinstance(right, float) and not isinstance(left, float))
            or (isinstance(right, str) and not isinstance(left, str))):
            raise SemanticError()
        if(left > right):
            return 1
        else:
            return 0

class GeEqual(Node):
    """
    A node representing greater than.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if ((isinstance(right, int) and not isinstance(left, int))
            or (isinstance(right, float) and not isinstance(left, float))):
            raise SemanticError()
        if(left >= right):
            return 1
        else:
            return 0

class Equal(Node):
    """
    A node representing Equal than.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        print("in eval")
        left = self.left.evaluate()
        right = self.right.evaluate()
        if ((isinstance(right, int) and not isinstance(left, int))
            or (isinstance(right, float) and not isinstance(left, float))
            or (isinstance(right, str) and not isinstance(left, str))):
            raise SemanticError()
        if(left == right):
            return 1
        else:
            return 0

class NotEqual(Node):
    """
    A node representing Equal than.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        print("in not eval")
        left = self.left.evaluate()
        right = self.right.evaluate()
        if ((isinstance(right, int) and not isinstance(left, int))
            or (isinstance(right, float) and not isinstance(left, float))
            or (isinstance(right, str) and not isinstance(left, str))):
            raise SemanticError()
        if(left != right):
            return 1
        else:
            return 0


class Mod(Node):
    """
    A node representing modulous.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return left % right





class And(Node):
    """
    A node representing boolean AND.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        if (left and right > 0):
            return 1
        else:
            return 0




class Not(Node):
    """
    A node representing boolean NOT.
    """

    def __init__(self, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = right


    def evaluate(self):
        #right = self.right.evaluate()
        left = self.left.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        r = not left
        return  r



class Or(Node):
    """
    A node representing boolean OR.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()

        if (left or right > 0):
            return 1
        else:
            return 0

class InOperator(Node):
    """
    A node representing boolean OR.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(right, list) and not isinstance(right, str):
            raise SemanticError()

        if (left in right):
            return 1
        else:
            return 0

def operation(a, op, b):


    if op =="+":
        return Add(a,b)
    if op == "-":
        return Subtract(a,b)
    if op =="*":
        return Multiply(a,b)
    if op =="/":
        return Divide(a,b)
    if op ==">=":
        return GeEqual(a,b)
    if op =="<=":
        return LeEqual(a,b)
    if op =="==":
        return Equal(a, b)
    if op =="<>":
        return NotEqual(a,b)
    if op == ">":
        return Ge(a,b)
    if op =="<":
        return Le(a,b)
    if op =="in":
        return InOperator(a,b)
    if op == "or":
        #print("we made it")
        return Or(a,b)
    if op == "and":
        return And(a,b)
    if op =="not":
        return Not(b)
    elif op =="[":
        print("attempt to index")
        return a.index(b)# index a list
    elif op =="]":
        return ListLiteral(None) #init list only
    elif op =="//":
        return FloorDiv(a,b)
    elif op =="**":
        print("about to calc")
        return Pow(a,b)
    elif op =="%":
        return Mod(a,b);
    else:
         return 17


# This is the TPG Parser that is responsible for turning our language into
# an abstract syntax tree.
class Parser(tpg.Parser):
    """
    separator space "\s+";

    token string '"(.*?)"' StringLiteral;
    token real "(\d+\.\d*|\d*\.\d+)([eE][-+]?\d+)?|\d+[eE][-+]?\d+"  RealLiteral;
    token int "\d+" IntLiteral;




	START/a -> expression/a ;

	expression/a -> boolOR/a ;

	boolOR/a -> boolAND/a ( "or"/op boolAND/b $ a = operation(a, op, b) $ )* ;

	boolAND/a -> boolNOT/a ( "and"/op boolNOT/b	$ a= operation(a, op, b) $ )* ;

	boolNOT/a -> comparison/a | "not"/op expression/b $ a = operation(b, op, b) $  ;

	comparison/a -> xor/a ( ("in"/op | "<>"/op | "=="/op | "<="/op | ">="/op | "<"/op | ">"/op) xor/b     $ a = operation(a, op, b) $ )* ;

	xor/a -> addsub/a ( "xor"/op addsub/b   $ a = operation(a, op, b) $ )* ;

	addsub/a -> muldiv/a ( ("\+"/op | "-"/op) muldiv/b  $ a = operation(a, op, b) $ )* ;

	muldiv/a -> index/a  ( ( "\*\*"/op | "\*"/op  | "//"/op | "/"/op | "%"/op) index/b $ a = operation(a, op, b) $ )* ;

	index/a -> parens/a ( "\[" expression/b "\]" $ a = operation(a, '[', b) $ )* ;

	parens/a -> "\(" expression/a "\)" | literal/a;

    literal/a->  string/a | real/a | int/a | array/a;


    array/a -> "\["        $ a = ListLiteral(None) $
        expression/b $ a.append(b) $

        ("," expression/b    $ a.append(b) $ )*

        "\]"
        | "\[" "\]" $ a = ListLiteral(None) $;



    """

# Make an instance of the parser. This acts like a function.
parse = Parser()

# This is the driver code, that reads in lines, deals with errors, and
# prints the output if no error occurs.

# Open the file containing the input.
try:
    f = open(sys.argv[1], "r")
except(IndexError, IOError):
    f = open("input1.txt", "r")

# For each line in f
for l in f:
    try:
        # Try to parse the expression.

        node = parse(l)



        # Try to get a result.
        result = node.evaluate()

        # Print the representation of the result.
        print(repr(result))


    # If an exception is thrown, print the appropriate error.
    except tpg.Error:
        print("SYNTAX ERROR")
        # Uncomment the next line to re-raise the syntax error,
        # displaying where it occurs. Comment it for submission.
        # raise

    except SemanticError:
        print("SEMANTIC ERROR")
        # Uncomment the next line to re-raise the semantic error,
        # displaying where it occurs. Comment it for submission.
        # raise

f.close()
