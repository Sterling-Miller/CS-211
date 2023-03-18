"""
Calculator
Sterling Miller, 2023-02-06, CIS 211
"""

# One global environment (scope) for
# the calculator

ENV: dict[str, "IntConst"] = dict()


class Expr(object):
    """ Abstract base class of all expressions """
    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        raise NotImplementedError(
            f"'eval' not implemented in {self.__class__.__name__}\n"
            "Each concrete Expr class must define 'eval'")

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        raise NotImplementedError(
            f"'__str__' not implemented in {self.__class__.__name__}\n"
            "Each concrete Expr class must define '__str__'")

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        raise NotImplementedError(
            f"'__repr__' not implemented in {self.__class__.__name__}\n"
            "Each concrete Expr class must define '__repr__'")


class BinOp(Expr):
    """ Abstract base class for binary operations """
    def __init__(self, left: Expr, right: Expr, symbol: str = "?Operation symbol undefined"):
        self.left = left
        self.right = right
        self.symbol = symbol

    def __str__(self) -> str:
        return f"({self.left} {self.symbol} {self.right})"

    def __repr__(self):
        return f'{self.__class__.__name__}({self.left.__repr__()}, {self.right.__repr__()})'

    def _apply(self, left_val: int, right_val: int) -> int:
        """Each concrete BinOp subclass provides the appropriate method"""
        raise NotImplementedError(
            f"'_apply' not implemented in {self.__class__.__name__}\n"
            "Each concrete BinOp class must define '_apply'")

    def eval(self) -> "IntConst":
        """Each concrete subclass must define _apply(int, int)->int"""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(self._apply(left_val.value, right_val.value))


class Unop(Expr):
    """Abstract base class for unary operations """
    def __init__(self, value: Expr, symbol: str = "?Operation symbol undefined"):
        self.value = value
        self.symbol = symbol

    def __str__(self) -> str:
        return f"({self.symbol} {self.value})"

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value.__repr__()})'

    def _apply(self, value: int) -> int:
        """Each concrete BinOp subclass provides the appropriate method"""
        raise NotImplementedError(
            f"'_apply' not implemented in {self.__class__.__name__}\n"
            "Each concrete BinOp class must define '_apply'")

    def eval(self) -> "IntConst":
        """Each concrete subclass must define _apply(int, int)->int"""
        value_val = self.value.eval()
        return IntConst(self._apply(value_val.value))


class IntConst(Expr):
    """ Represents an integer """
    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'IntConst({self.value})'

    def __eq__(self, other: Expr):
        return isinstance(other, IntConst) and self.value == other.value

    def eval(self):
        return self


class Plus(BinOp):
    """ left + right """
    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right, symbol="+")

    def _apply(self, left: int, right: int) -> int:
        return left + right


class Times(BinOp):
    """left * right"""
    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right, symbol="*")

    def _apply(self, left: int, right: int) -> int:
        return left * right


class Minus(BinOp):
    """ left - right """
    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right, symbol="-")

    def _apply(self, left: int, right: int) -> int:
        return left - right


class Div(BinOp):
    """ left / right """
    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right, symbol="/")

    def _apply(self, left: int, right: int) -> int:
        return left // right


class Neg(Unop):
    """ Changes an integers sign """
    def __init__(self, value: Expr):
        super().__init__(value, symbol="~")

    def _apply(self, value: int) -> int:
        return -value


class Abs(Unop):
    """ Returns the abs value of an int """
    def __init__(self, value: Expr):
        super().__init__(value, symbol="@")

    def _apply(self, value: int) -> int:
        if value < 0:
            return -value
        return value


class UndefinedVariable(Exception):
    """Raised when expression tries to use a variable that
    is not in ENV
    """
    pass


class Var(Expr):
    """ Creates a variable object that can then be assigned to an int """
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Var({self.name})"

    def eval(self):
        global ENV
        if self.name in ENV:
            return ENV[self.name]
        else:
            raise UndefinedVariable(f"{self.name} has not been assigned a value")

    def assign(self, value: IntConst):
        if self.name not in ENV:
            ENV[self.name] = value


class Assign(Expr):
    """Assignment:  x = E represented as Assign(x, E)"""
    def __init__(self, left: Var, right: Expr):
        assert isinstance(left, Var)  # Can only assign to variables!
        self.left = left
        self.right = right

    def __str__(self):
        return f'({self.left} = {self.right})'

    def __repr__(self):
        return f'Assign({self.left.__repr__()}, {self.right.__repr__()})'

    def eval(self) -> IntConst:
        r_val = self.right.eval()
        self.left.assign(r_val)
        return r_val


def env_clear():
    """Clear all variables in calculator memory"""
    global ENV
    ENV = dict()
