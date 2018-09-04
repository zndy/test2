from tarfile import calc_chksums

from mycode.util.MatrixUtil import *
from mycode.gui.BeanFactory import *


#      x: gesucht
#      y: gesucht
#      v: winkel
#    a_d: AbrichtScheibe Durchmesser
#    d_d: DiamondScheibe Durchmesser
#    a_f: AbrichtScheibe Flansch
#    d_f: DiamondScheibe Flansch
#     dx: (deltax) abstand zwischen maschine 0 und berechnung 0
#     dy: (deltay) abstand zwischen maschine 0 und berechnung 0
#     px: x value von AbrichtenPoint by Diamond Scheibe Koordinaten System
#     py: y value von AbrichtenPoint by Diamond Scheibe Koordinaten System


class AbrichtenPositionCalculator:
    x, y, v, a_d, a_f, d_d, d_f, dx, dy, px, py = symbols('x y v a_d a_f d_d d_f dx dy px py')

    @classmethod
    def __calcLeft(cls):
        abrichtenPoint = Matrix([0, 0, 1])
        left = MatrixUtil.translationMatrix2D(cls.x, cls.y) * MatrixUtil.rotationMatrix2D(
            cls.v) * MatrixUtil.translationMatrix2D(cls.a_d / 2, cls.a_f) * abrichtenPoint
        return left

    @classmethod
    def __calcRight(cls):
        diamondPoint = Matrix([cls.px, cls.py, 1])
        right = MatrixUtil.translationMatrix2D(cls.dx - cls.d_d / 2, cls.dy - cls.d_f) \
                * MatrixUtil.rotationMatrix2D(90) * diamondPoint
        return right

    @classmethod
    def calc(cls):
        left = cls.__calcLeft()
        print("left: " + str(left))
        right = cls.__calcRight()
        print("right: " + str(right))
        result = solve([left[0] - right[0], left[1] - right[1]], [cls.x, cls.y])
        print(result)
        return result


def main():
    test1()


def test1():
    calculator = AbrichtenPositionCalculator()
    result = calculator.calc()
    xResult = result.get(AbrichtenPositionCalculator.x)
    yResult = result.get(AbrichtenPositionCalculator.y)
    print(xResult.subs(
        {AbrichtenPositionCalculator.v: 30, AbrichtenPositionCalculator.a_d: 10, AbrichtenPositionCalculator.d_d: 20,
         AbrichtenPositionCalculator.dx: 50, AbrichtenPositionCalculator.dy: 40,
         AbrichtenPositionCalculator.a_f: 7, AbrichtenPositionCalculator.d_f: 8, AbrichtenPositionCalculator.px: 5,
         AbrichtenPositionCalculator.py: 0}).evalf())
    print(yResult.subs(
        {AbrichtenPositionCalculator.v: 30, AbrichtenPositionCalculator.a_d: 10, AbrichtenPositionCalculator.d_d: 20,
         AbrichtenPositionCalculator.dx: 50, AbrichtenPositionCalculator.dy: 40,
         AbrichtenPositionCalculator.a_f: 7, AbrichtenPositionCalculator.d_f: 8, AbrichtenPositionCalculator.px: 5,
         AbrichtenPositionCalculator.py: 0}).evalf())
    print(xResult.subs(
        {AbrichtenPositionCalculator.v: 30, AbrichtenPositionCalculator.a_d: 10, AbrichtenPositionCalculator.d_d: 20,
         AbrichtenPositionCalculator.dx: 50, AbrichtenPositionCalculator.dy: 40,
         AbrichtenPositionCalculator.d_f: 8, AbrichtenPositionCalculator.px: 5,
         AbrichtenPositionCalculator.py: 0}).evalf())
    print(yResult.subs(
        {AbrichtenPositionCalculator.v: 30, AbrichtenPositionCalculator.a_d: 10, AbrichtenPositionCalculator.d_d: 20,
         AbrichtenPositionCalculator.dx: 50, AbrichtenPositionCalculator.dy: 40,
         AbrichtenPositionCalculator.a_f: 7, AbrichtenPositionCalculator.px: 5,
         AbrichtenPositionCalculator.py: 0}).evalf())

    parameters = {}
    parameters[AbrichtenPositionCalculator.v] = 30
    parameters[AbrichtenPositionCalculator.a_d] = 10
    parameters[AbrichtenPositionCalculator.d_d] = 20
    parameters[AbrichtenPositionCalculator.dx] = 50
    parameters[AbrichtenPositionCalculator.dy] = 40
    parameters[AbrichtenPositionCalculator.a_f] = 7
    parameters[AbrichtenPositionCalculator.d_f] = 8
    parameters[AbrichtenPositionCalculator.px] = 5
    parameters[AbrichtenPositionCalculator.py] = 0
    print(type(xResult))
    print(xResult.subs(parameters).evalf())
    print(yResult.subs(parameters).evalf())


if __name__ == "__main__":
    main()
