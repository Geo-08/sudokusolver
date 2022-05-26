import pandas as pd
import numpy as np


def find_df_place(block,co):
	if block == 0:
		return co
	if block == 1:
		return [co[0],co[1]+3]
	if block == 2:
		return [co[0],co[1]+6]
	if block == 3:
		return [co[0]+3,co[1]]
	if block == 4:
		return [co[0]+3,co[1]+3]
	if block == 5:
		return [co[0]+3,co[1]+6]
	if block == 6:
		return [co[0]+6,co[1]]
	if block == 7:
		return [co[0]+6,co[1]+3]
	if block == 8:
		return [co[0]+6,co[1]+6]



def exists_in_block(df,block,number):
	for i in range(3):
		for j in range(3):
			co = find_df_place(block,[i,j])
			if df.iloc[co[0]][co[1]] == number:
				return True
	return False

def belongs_to_block(co):
	if co[0]<3:
		if co[1]<3:
			return 0
		if co[1]<6:
			return 1
		if co[1]<9:
			return 2
	if co[0]<6:
		if co[1]<3:
			return 3
		if co[1]<6:
			return 4
		if co[1]<9:
			return 5
	if co[0]<9:
		if co[1]<3:
			return 6
		if co[1]<6:
			return 7
		if co[1]<9:
			return 8


def exists_in_row(df,row,number):
	for i in range(9):
		if df.iloc[row,i] == number:
			return True
	return False

def exists_in_column(df,column,number):
	for i in range(9):
		if df.iloc[i,column] == number:
			return True
	return False



def valid_move(df,co,number):
	block = belongs_to_block(co)
	if exists_in_block(df,block,number) == False and exists_in_row(df,co[0],number) == False and exists_in_column(df,co[1],number) == False:
		return True
	return False


def b_solver(df,row,column):
	if row == 8 and column == 9:
		return True
	if column == 9:
		row += 1
		column = 0
	if df.iloc[row,column] >0:
		return b_solver(df,row,column+1)
	for g in range(1,10):
		if valid_move(df,[row,column],g) == True:
			df.iloc[row,column] = g
			if b_solver(df,row,column+1):
				return True
			df.iloc[row,column] = 0
	return False


print("Type the name of the sudoku puzzle you want solved. The solution will be printed on terminal as well as exported as an .ods file with the name format of 'puzzlename'_s.ods")
puzzle = input()
df = pd.read_excel(puzzle+".ods",engine='odf',header=None,dtype=np.int32)
print(df)
if b_solver(df,0,0) == True:
	print(df)
	filename = puzzle+"_s.ods"
	df.to_excel(filename)
print("Puzzle is unsolvable")