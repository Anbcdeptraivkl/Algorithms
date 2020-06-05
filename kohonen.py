import matplotlib.pyplot as plt
import numpy as np
import random as ran
import pandas as pd
import math
import csv

# Vector 2D
class Vector2:
    x = 0
    y = 0
    def __init__(self, x_a, y_a):
        self.x = x_a
        self.y = y_a
    def values(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")
    @staticmethod
    def distance(vA, vB):
        dist = math.sqrt(pow((vA.x - vB.x), 2) + pow((vA.y - vB.y), 2))
        return dist

# Inputting from Files
# Neurons
neuronPoints = []
neuronsCSVPath = 'neurons.csv'
def neuronsCSVParse():
    data = pd.read_csv(neuronsCSVPath, names=['age', 'cp'])
    records = data.to_dict(orient='record')
    for row in records:
        neuronPoints.append(Vector2(row['age'], row['cp']))
    for point in neuronPoints:
        point.values()
# Vectors
vectors = []
vectorsCSVPath = 'vectors.csv'
def neuronsCSVParse():
    data = pd.read_csv(vectorsCSVPath, names=['w_age', 'w_cp'])
    records = data.to_dict(orient='record')
    for row in records:
        vectors.append(Vector2(row['w_age'], row['w_cp']))
    for vector in vectors:
        vector.values()

# Plot Points on the Map
def draw(points):
    for point in points:
        plt.scatter(point.x, point.y)
    plt.show()

# Changing Weight and Overriding the old Vectors
alpha = 0.4
def changedVector(neuron: Vector2, winner: Vector2):
    x = neuron.x + alpha * (winner.x - neuron.x)
    y = neuron.y + alpha * (winner.y - neuron.y)
    newNeuron = Vector2(x, y)
    newNeuron.values()
    return newNeuron

# Applying Algorithms
result = []
def calculate():
    result = neuronPoints
    # Loop for n times
    numLoops = int(input("How many Iterations? "))
    for i in range(0, numLoops):
        print("Iteration " + str(i + 1) + "... ")
        # Compare distance each neurons to each inputs
        for j in range(0, len(result)):
            # Smallest distance input => winner
            smallestDist = Vector2.distance(vectors[0], result[j])
            currentWinner = vectors[0]
            # One neuron for 3 inputs
            for i in range(1, len(vectors)):
                comparingDist = Vector2.distance(vectors[i], result[j])
                if comparingDist < smallestDist:
                    smallestDist = comparingDist
                    currentWinner = vectors[i]
            # Change weight
            result[j] = changedVector(result[j], currentWinner)
    draw(result)

# MAIN
def main():
    neuronsCSVParse()
    draw(neuronPoints)
    neuronsCSVParse()
    draw(vectors)
    calculate()

main()
