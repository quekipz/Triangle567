# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@author: ktq
"""

def classify_triangle(s_a, s_b, s_c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(s_a, int) and isinstance(s_b, int) and isinstance(s_c, int)):
        return 'InvalidInput'

    # require that the input values be > 0 and <= 200
    if s_a > 200 or s_b > 200 or s_c > 200:
        return 'InvalidInput'

    if s_a <= 0 or s_b <= 0 or s_c <= 0:
        return 'InvalidInput'



    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (s_a >= (s_b+s_c)) or (s_b >= (s_a+s_c)) or (s_c >= (s_a+s_b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if s_a == s_b and s_b == s_c:
        result = 'Equilateral'
    elif (s_a**2+s_b**2) == s_c**2 or (s_a**2+s_c**2) == s_b**2 or (s_b**2+s_c**2) == s_a**2:
        result = 'Right'
    elif (s_a != s_b) and  (s_b != s_c) and (s_a != s_c):
        result = 'Scalene'
    else:
        result = 'Isosceles'
    return result
