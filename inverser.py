#!/usr/bin/python3

import sys
import numpy as np 

class Matrix:
	def __init__(self):
		'''
			Initialize matrix to zero matrix of the 
			given shape and its inverse to identity matrix
		'''
		self.degree = int(input("Enter the degree of the square matrix:\n"))
		self.original_matrix = np.zeros((self.degree,self.degree))
		self.inverse_matrix = np.eye(self.degree)

	def set_matrix(self):
		'''
			Set the matrix got from user
		'''
		print("\nEnter the square matrix below:")
		print("\'\'\'")
		print("\tFormat:")
		print("\tFor 2 by 2 matrix, the input is given as::")
		print("\t1 2")
		print("\t4 5")
		print("\'\'\'")

		for i in range(self.degree):
			self.original_matrix[i] = [int(j) for j in input().split()]

	def transform_to_row_echelon_form(self):
		'''
			Reduces the matrix into row echelon form and put
			the transformation matrix into inverse matrix
		'''
		for i in range(self.degree):
			pivot = self.original_matrix[i][i]
			if pivot == 0:
				print("The inverse does not exist.")
				sys.exit()
			else:
				transformation_matrix_t = np.eye(self.degree)
				transformation_matrix_t[i][i] = self.inverse_matrix[i][i]/pivot
				self.original_matrix = np.matmul(transformation_matrix_t, self.original_matrix)
				self.inverse_matrix = np.matmul(transformation_matrix_t, self.inverse_matrix)

			for j in range(i+1, self.degree):
				transformation_matrix_t = np.eye(self.degree)
				transformation_matrix_t[j][i] = - self.original_matrix[j][i]
				self.inverse_matrix = np.matmul(transformation_matrix_t, self.inverse_matrix)
				self.original_matrix = np.matmul(transformation_matrix_t, self.original_matrix)

	def transform_to_reduced_row_echelon_form(self):
		'''
			Reduce the row echelon form matrix indo
			reduced row echelon form
		'''
		for i in range(1, self.degree):
			for j in range(self.degree - i):
				transformation_matrix_t = np.eye(self.degree)
				transformation_matrix_t[j][-i] = - self.original_matrix[j][-i]
				self.inverse_matrix = np.matmul(transformation_matrix_t, self.inverse_matrix)
				self.original_matrix = np.matmul(transformation_matrix_t, self.original_matrix)

	def inverse(self):
		self.transform_to_row_echelon_form()
		self.transform_to_reduced_row_echelon_form()

def main():
	matrix = Matrix()
	matrix.set_matrix()
	matrix.transform_to_row_echelon_form()
	matrix.transform_to_reduced_row_echelon_form()

	print("\nThe inverse matrix is:\n{}".format(matrix.inverse_matrix))

if __name__ == "__main__":
	main()