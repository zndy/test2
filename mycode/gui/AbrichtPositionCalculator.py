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

    def __init__(self):
        self.mainPageModel = BeanFactory.getInstance().mainPageModel
        self.diamondPointsPageModel = BeanFactory.getInstance().diamondPointsPageModel
        self.x, self.y, self.v, self.a_d, self.a_f, self.d_d, self.d_f, self.dx, self.dy, self.px, self.py = symbols(
            'x y v a_d a_f d_d d_f dx dy px py')

    def __calcLeft(self):
        abrichtenPoint = Matrix([0, 0, 1])
        left = MatrixUtil.translationMatrix2D(self.x, self.y) * MatrixUtil.rotationMatrix2D(
            self.v) * MatrixUtil.translationMatrix2D(self.a_d / 2, self.a_f) * abrichtenPoint
        return left

    def __calcRight(self):
        diamondPoint = Matrix([self.px, self.py, 1])
        right = MatrixUtil.translationMatrix2D(self.dx - self.d_d / 2, self.dy - self.d_f) \
                * MatrixUtil.rotationMatrix2D(90) * diamondPoint
        return right

    def calc(self):
        left = self.__calcLeft()
        print("left: " + str(left))
        right = self.__calcRight()
        print("right: " + str(right))
        result = solve([left[0] - right[0], left[1] - right[1]], [self.x, self.y])
        print(result)
        return result


def main():
    test1()


def test1():
    calculator = AbrichtenPositionCalculator()
    result = calculator.calc()
    xResult = result.get(calculator.x)
    yResult = result.get(calculator.y)
    print(xResult.subs({calculator.v: 30, calculator.a_d: 10, calculator.d_d: 20, calculator.dx: 50, calculator.dy: 40,
                        calculator.a_f: 7, calculator.d_f: 8, calculator.px: 5, calculator.py: 0}).evalf())
    print(yResult.subs({calculator.v: 30, calculator.a_d: 10, calculator.d_d: 20, calculator.dx: 50, calculator.dy: 40,
                        calculator.a_f: 7, calculator.d_f: 8, calculator.px: 5, calculator.py: 0}).evalf())
    print(xResult.subs({calculator.v: 30, calculator.a_d: 10, calculator.d_d: 20, calculator.dx: 50, calculator.dy: 40,
                        calculator.d_f: 8, calculator.px: 5, calculator.py: 0}).evalf())
    print(yResult.subs({calculator.v: 30, calculator.a_d: 10, calculator.d_d: 20, calculator.dx: 50, calculator.dy: 40,
                        calculator.a_f: 7, calculator.px: 5, calculator.py: 0}).evalf())

    parameters = {}
    parameters[calculator.v] = 30
    parameters[calculator.a_d] = 10
    parameters[calculator.d_d] = 20
    parameters[calculator.dx] = 50
    parameters[calculator.dy] = 40
    parameters[calculator.a_f] = 7
    parameters[calculator.d_f] = 8
    parameters[calculator.px] = 5
    parameters[calculator.py] = 0
    print(type(xResult))
    print(xResult.subs(parameters).evalf())
    print(yResult.subs(parameters).evalf())


if __name__ == "__main__":
    main()
