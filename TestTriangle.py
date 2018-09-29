# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: ktq
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidTriangleA(self):
        self.assertEqual(classify_triangle(201,200,200), 'InvalidInput', '201,200,200 is invalid')

    def testInvalidTriangleB(self):
        self.assertEqual(classify_triangle(200,201,200), 'InvalidInput', '20,201,200 is invalid')

    def testInvalidTriangleC(self):
        self.assertEqual(classify_triangle(200,200,201), 'InvalidInput', '200,200,201 is invalid')   

    def testInvalidTriangleD(self):     
        self.assertEqual(classify_triangle('a',5,5), 'InvalidInput', 'a,5,5 is invalid')

    def testInvalidTriangleE(self):
        self.assertEqual(classify_triangle(5,'a',5), 'InvalidInput', '5,a,5 is invalid')

    def testInvalidTriangleF(self):
        self.assertEqual(classify_triangle(5,5,'a'), 'InvalidInput', '5,5,a is invalid')

    def testInvalidTriangleG(self):
        self.assertEqual(classify_triangle(-5,5,5), 'InvalidInput', '-5,5,5 is invalid')

    def testInvalidTriangleH(self):
        self.assertEqual(classify_triangle(5,-5,5), 'InvalidInput', '5,-5,5 is invalid')

    def testInvalidTriangleI(self):
        self.assertEqual(classify_triangle(5,5,-5), 'InvalidInput', '5,5,-5 is invalid')

    def testNotTriangleA(self):
        self.assertEqual(classify_triangle(20,5,5), 'NotATriangle','20,5,5 is not a triangle')

    def testNotTriangleB(self):
        self.assertEqual(classify_triangle(5,20,5), 'NotATriangle','5,20,5 is not a triangle')

    def testNotTriangleC(self):
        self.assertEqual(classify_triangle(5,5,20), 'NotATriangle','5,5,20 is not a triangle')

    def testEquilateralTriangle(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classify_triangle(3,5,4),'Right','3,5,4 is a Right triangle')

    def testRightTriangleD(self): 
        self.assertEqual(classify_triangle(5,4,3),'Right','5,4,3 is a Right triangle')

    def testRightTriangleE(self): 
        self.assertEqual(classify_triangle(4,3,5),'Right','4,3,5 is a Right triangle')

    def testRightTriangleF(self): 
        self.assertEqual(classify_triangle(4,5,3),'Right','4,5,3 is a Right triangle')

    def testScaleneTriangleA(self): 
        self.assertEqual(classify_triangle(2,3,4),'Scalene','2,3,4 is a Scalene triangle')

    def testScaleneTriangleB(self): 
        self.assertEqual(classify_triangle(3,4,2),'Scalene','3,4,2 is a Scalene triangle')

    def testScaleneTriangleC(self):
        self.assertEqual(classify_triangle(4,3,2),'Scalene','4,3,2 is a Scalene triangle')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,3),'Isosceles','3,4,3 is a Isoceles triangle')

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classify_triangle(3,3,4),'Isosceles','3,3,4 is a Isoceles triangle')

    def testIsoscelesTriangleC(self): 
        self.assertEqual(classify_triangle(4,3,3),'Isosceles','4,3,3 is a Isoceles triangle')
        


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()