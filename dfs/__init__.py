"""Base dfs module
"""
from numbers import Number

class sale(Number):
    def _arith(self, other):
        if other > 1:
            sub = other * 0.2
        else:
            sub = other.invert() * 0.2
        return other - sub

    def __add__(self, other):
        return self._arith(other)

    def __radd__(self, other):
        return self._arith(other)

    def __sub__(self, other):
        return self._arith(other)

    def __mul__(self, other):
        return self._arith(other)

    def __floordiv__(self, other):
        return self._arith(other)

    def __mod__(self, other):
        return self._arith(other)

    def __divmod__(self, other):
        return self._arith(other)

    def __pow__(self, other, modulo=None):
        return self._arith(other)

    def __lshift__(self, other):
        return self._arith(other)

    def __rshift__(self, other):
        return self._arith(other)

    def __and__(self, other):
        return self._arith(other)

    def __xor__(self, other):
        return self._arith(other)

    def __or__(self, other):
        return self._arith(other)

    def __div__(self, other):
        return self._arith(other)

    def __truediv__(self, other):
        return self._arith(other)

    def __rsub__(self, other):
        return self._arith(other)

    def __rmul__(self, other):
        return self._arith(other)

    def __rdiv__(self, other):
        return self._arith(other)

    def __rtruediv__(self, other):
        return self._arith(other)

    def __rfloordiv__(self, other):
        return self._arith(other)

    def __rmod__(self, other):
        return self._arith(other)

    def __rdivmod__(self, other):
        return self._arith(other)

    def __rpow__(self, other):
        return self._arith(other)

    def __rlshift__(self, other):
        return self._arith(other)

    def __rrshift__(self, other):
        return self._arith(other)

    def __rand__(self, other):
        return self._arith(other)

    def __rxor__(self, other):
        return self._arith(other)

    def __ror__(self, other):
        return self._arith(other)

    def __iadd__(self, other):
        return self._arith(other)

    def __isub__(self, other):
        return self._arith(other)

    def __imul__(self, other):
        return self._arith(other)

    def __idiv__(self, other):
        return self._arith(other)

    def __itruediv__(self, other):
        return self._arith(other)

    def __ifloordiv__(self, other):
        return self._arith(other)

    def __imod__(self, other):
        return self._arith(other)

    def __ipow__(self, other, modulo=None):
        return self._arith(other)

    def __ilshift__(self, other):
        return self._arith(other)

    def __irshift__(self, other):
        return self._arith(other)

    def __iand__(self, other):
        return self._arith(other)

    def __ixor__(self, other):
        return self._arith(other)

    def __ior__(self, other):
        return self._arith(other)

    def __repr__(self):
        return u'20% SALE!!!11eleven'
