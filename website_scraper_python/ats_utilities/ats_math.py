import math
# math.e
# >>> 2.718281828459045
# math.inf
# >>> inf
# math.nan
# >>> nan
# math.pi
# >>> 3.141592653589793
# math.tau
# >>> 6.283185307179586

ROOT_TWO = 1.4142135623730951
# SQUARE_ROOT_OF_TWO = 1.4142135623730951
# 2ND_ROOT = 1.4142135623730951
SECOND_ROOT = 1.4142135623730951
# sqrt(2) ~= 99/70
SQUARE_ROOT_OF_TWO = 1.41421356237309504880168872420969807856967187537694807317667973799  # 65 decimal places
# Golden Ratio
# represented by the Greek lower-case letter phi
# small phi	φ	&#966; or &phi;
SMALL_PHI = 1.61803398874989484820458683436563811772030917980576  # 50 decimal places
# e (mathematical constant) AKA Euler's number AKA Napier's constant
# approximately equal to 2.71828
# ....is the limit of (1 + 1/n)n as n approaches infinity
# sequence A001113 in the OEIS)
# https://oeis.org/A001113
e = 2.71828182845904523536028747135266249775724709369995  # 50 decimal places
EULERS_NUMBER = 2.71828182845904523536028747135266249775724709369995  # 50 decimal places


def calculate_side_of_inscribed_square_from_radius_of_circle(radius_of_the_circle):
    # https://socratic.org/questions/what-is-the-length-of-the-side-of-a-square-whose-diagonal-is-10
    # a^2 + b^2 = c^2
    # Since it is a square, b = a and a^2 + a^2 = c^2 and 2a^2 = c^2
    # 2 * radius of the circle = diameter of the circle
    # the hypotenuse of the inscribed square = the diameter of the circle
    # the side of a square =
    # ...
    # hypotenuse = diagonal = radius of the circle * 2 = side of the square * sqrt(2)
    # ...
    # if a square is inscribed in a circle,
    #  then the diameter of the circle is also the diagonal of the square
    # the diagonal of a square is a bisector, which produces two equilateral, right triangles
    # the diagonal of the square is therefore the hypotenuse of the triangle
    # the hypotenuse of an equilateral,
    #  right triangle is equal to the length of the side times the square-root of two
    # ...
    # diagonal = side * sqrt(2)
    # side = (diagonal / 2) * sqrt(2)
    diameter_of_the_circle = radius_of_the_circle * 2
    diagonal_of_the_inscribed_square = diameter_of_the_circle
    hypotenuse_of_the_equilateral_right_triangle = diagonal_of_the_inscribed_square
    sides_of_the_equilateral_right_triangle = (hypotenuse_of_the_equilateral_right_triangle / 2) * math.sqrt(2)
    sides_of_the_inscribed_square = sides_of_the_equilateral_right_triangle
    return sides_of_the_inscribed_square


def calculate_sides_of_the_equilateral_right_triangle(hypotenuse_of_the_equilateral_right_triangle):
    sides_of_the_equilateral_right_triangle = (hypotenuse_of_the_equilateral_right_triangle / 2) * math.sqrt(2)
    return sides_of_the_equilateral_right_triangle

