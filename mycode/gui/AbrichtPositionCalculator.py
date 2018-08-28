from mycode.util.MatrixUtil import *
from mycode.gui.BeanFactory import *


#      x: gesucht
#      y: gesucht
#      v: winkel
#    d_a: Durchmesser AbrichtScheibe
#    d_d: Durchmesser DiamondScheibe
#    f_a: Flansch AbrichtScheibe
#    f_d: Flansch DiamondScheibe
# deltaX: abstand zwischen maschine 0 und berechnung 0
# deltaY: abstand zwischen maschine 0 und berechnung 0


class AbrichtenPositionCalculator:

    def __init__(self):
        self.mainPageModel = beanFactory.mainPageModel
        self.diamondPointsPageModel = beanFactory.diamondPointsPageModel

    def __calcLeft(self):
        x, y, v, d_a, f_a = symbols('x y v d_a f_a')
        abrichtenPoint = Matrix([0, 0, 1])
        left = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            v) * MatrixUtil.translationMatrix2D(d_a / 2, f_a) * abrichtenPoint
        return left

    def __calcRight(self):
        deltax, deltay, d_d, f_d, px, py = symbols('deltax deltay d_d f_d px py')
        diamondPoint = Matrix([px, py, 1])
        right = MatrixUtil.translationMatrix2D(deltax - d_d / 2, deltay - f_d) * MatrixUtil.rotationMatrix2D(
            90) * diamondPoint
        return right

    def calc(self):
        x, y = symbols('x y')
        left = self.__calcLeft()
        print("left: " + str(left))
        right = self.__calcRight()
        print("right " + str(right))
        result = solve([left[0] - right[0], left[1] - right[1]], [x, y])
        print(result)
        return result


def main():
    test1()


def test1():
    result = AbrichtenPositionCalculator().calc()
    x, y, v, d_a, d_d, deltax, deltay, f_a, f_d, px, py = symbols('x y v d_a d_d deltax deltay f_a f_d px py')
    xResult = result.get(x)
    yResult = result.get(y)
    print(xResult.subs({v: 30, d_a: 10, d_d: 20, deltax: 50, deltay: 40, f_a: 7, f_d: 8, px: 5, py: 0}).evalf())
    print(yResult.subs({v: 30, d_a: 10, d_d: 20, deltax: 50, deltay: 40, f_a: 7, f_d: 8, px: 5, py: 0}).evalf())
    print(xResult.subs({v: 30, d_a: 10, d_d: 20, deltax: 50, deltay: 40, f_d: 8, px: 5, py: 0}).evalf())
    print(yResult.subs({v: 30, d_a: 10, d_d: 20, deltax: 50, deltay: 40, f_a: 7, px: 5, py: 0}).evalf())


if __name__ == "__main__":
    main()
