from sympy import *


class MatrixUtil:

    @staticmethod
    def rotationMatrix2D(degree):
        theta = rad(degree)
        rotationMatrix = Matrix([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])
        return rotationMatrix

    @staticmethod
    def translationMatrix2D(dx, dy):
        translationMatrix = Matrix([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
        return translationMatrix

    @staticmethod
    def scalingMatrix2D(s_x, s_y):
        scalingMatrix = Matrix([[s_x, 0, 0], [0, s_y, 0], [0, 0, 1]])
        return scalingMatrix

    # ---------------------------------test-------------------------------------
    @staticmethod
    def rotationTest():
        print("-----------------------rotationTest------------------------")
        point = Matrix([10, 0, 1])
        print("original coord " + str(point))
        pointAfterRotation90 = MatrixUtil.rotationMatrix2D(90) * point
        print("90 degree rotation " + str(pointAfterRotation90))
        pointAfterRotation180 = MatrixUtil.rotationMatrix2D(
            90) * MatrixUtil.rotationMatrix2D(90) * point
        print("180 degree rotation " + str(pointAfterRotation180))
        pointAfterRotation270 = MatrixUtil.rotationMatrix2D(270) * point
        print("270 degree rotation " + str(pointAfterRotation270))

    @staticmethod
    def rotationWithSymbolTest():
        print("-----------------------rotationWithSymbolTest------------------------")
        point = Matrix([10, 0, 1])
        degree = symbols('degree')
        print("original coord " + str(point))
        pointAfterRotation = MatrixUtil.rotationMatrix2D(degree) * point
        print("rotation with symbol " + str(pointAfterRotation))
        pointAfterRotation = pointAfterRotation.subs(degree, 90)
        print("90 degree rotation " + str(pointAfterRotation))

    @staticmethod
    def translationTest():
        print("----------------translationTest------------------------")
        point = Matrix([0, 0, 1])
        print("original coord " + str(point))
        pointAfterTranslation = MatrixUtil.translationMatrix2D(4, 6) * point
        print("point after translation " + str(pointAfterTranslation))

    @staticmethod
    def rotTranTest():
        print("-----------------------rotationTranslationTest------------------------")
        point = Matrix([10, 0, 1])
        print("original coord " + str(point))
        pointAfterRotation90 = MatrixUtil.rotationMatrix2D(90) * point
        print("90 degree rotation " + str(pointAfterRotation90))
        pointAfterTranslation = MatrixUtil.translationMatrix2D(
            1, 2) * pointAfterRotation90
        print("point after translation " + str(pointAfterTranslation))

    @staticmethod
    def inverseMatrixTest1():
        print("-----------------------inverseMatrixTest1------------------------")
        matrix = Matrix([[2, 0, 0], [0, 3, 0], [0, 0, 4]])
        print("original matrix " + str(matrix))
        inverseMatrix = matrix.inv()
        print("inverse Matrix " + str(inverseMatrix))

    @staticmethod
    def inverseMatrixTest2():
        print("-----------------------inverseMatrixTest2------------------------")
        point = Matrix([10, 0, 1])
        print("original coord " + str(point))
        point = MatrixUtil.rotationMatrix2D(90) * point
        print("90 degree rotation " + str(point))
        point = MatrixUtil.translationMatrix2D(1, 2) * point
        print("point after translation " + str(point))

        point = MatrixUtil.translationMatrix2D(1, 2).inv() * point
        print("point after inv translation" + str(point))
        point = MatrixUtil.rotationMatrix2D(90).inv() * point
        print("point after inv rotation" + str(point))

    @staticmethod
    def symbolTest():
        print("----------------symbolTest------------------")
        x, y, degree = symbols('x y degree')
        point = Matrix([x, y, 1])
        print("original coord " + str(point))
        point = MatrixUtil.rotationMatrix2D(degree) * point
        print("rotation " + str(point))
        point = point.subs({x: 10, y: 0, degree: 90})
        print("90 degree rotation " + str(point))

    @staticmethod
    def scalingTest():
        print("-----------scalingTest---------------")
        point = Matrix([2, 2, 1])
        print("original coord " + str(point))
        pointAfterScaling = MatrixUtil.scalingMatrix2D(4, 6) * point
        print("point after scaling " + str(pointAfterScaling))


def main():
    # MatrixUtil.rotationTest()
    # MatrixUtil.rotationWithSymbolTest()
    # MatrixUtil.translationTest()
    # MatrixUtil.rotTranTest()
    # MatrixUtil.inverseMatrixTest1()
    # MatrixUtil.inverseMatrixTest2()
    # MatrixUtil.symbolTest()
    MatrixUtil.scalingTest()

if __name__ == "__main__":
    main()
