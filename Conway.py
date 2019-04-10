#!/usr/bin/env python3
#from gui import *
import random

######################
#FUNCIONES
######################

#Generates a grid full of 0's
def deadGrid(width,height):
	grid = [[0 for i in range(width)] for j in range(height)]
	return grid

#Generates a grid with random 1's and 0's
def rndGrid(width,height):
	grid = [[random.randint(0,1) for i in range(width)] for j in range(height)]
	return grid

# 'o' == Alive cell(1), '#'== Dead cell(0)
def render(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j]==1:
				print ('o'+' ',end="")
			else:
				print ('#'+' ',end="")
		print ('\r')

#Implemenattion of the rules of the game to create the next state
def nextboardstate(oldstate,w,h):
	vivas=0;
	newstate = deadGrid(w,h)
	for i in range(len(oldstate)):
		for j in range(len(oldstate[i])):
			vivas = checkNeighbours(oldstate,i,j)
			if oldstate[i][j]==1:
				if vivas == 2 or vivas == 3:
					newstate[i][j]=1
				
			elif oldstate[i][j]==0:
				if vivas ==3:
					newstate[i][j]=1
			vivas=0

	return newstate

#Checks every neighbour cell and returns the number of alive neighbour cells
def checkNeighbours(state,i,j):
	vivas = 0
	for x in range(i-1,i+1):
		for y in range(j-1,j+1):
			if state[x][y]==1:
				vivas+=1
	if state[i][j]==1:
		vivas-=1

	return vivas
######################

w = 10
h = 10
state =rndGrid(w,h)
render(state)
print ("Next:")
render(nextboardstate(state,w,h))