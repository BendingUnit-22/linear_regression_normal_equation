import re
import sys
import matplotlib.pyplot as plt

# A
def inverse(A):
    if len(A) != 2:
        print "inverse: input must be 2x2"
        sys.exit(0)
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    det = 1.0 / float(a * d - b * c)

    A[0][0] = d * det
    A[0][1] = -b * det
    A[1][0] = -c * det
    A[1][1] = a * det
    return A

def normal(d):
    B = []
    A = []
    ypos = len(d[0]) - 1
    for a in d:
        row_i = [1.0 ,a[0]]
        A.append(row_i)
        row_b = [a[ypos]]
        B.append(row_b)
    A_transpose = transpose(A)
    A_transpose_A = mult(A_transpose, A)
    A_transpose_B = mult(A_transpose, B)
    inverse_A_transpose_A = inverse(A_transpose_A)
    params = mult(inverse_A_transpose_A, A_transpose_B)
    return params


def transpose(a):
    row = len(a)
    if (row <= 0):
        return []
    col = len (a[0])
    m = []
    # from i in 0..2
    for i in range(0,col):
        r = []
        # for every vector in matrix
        for j in range(0,row):
            r.append(a[j][i])
        # add row i
        m.append(r)
    return m



# dot product of two arrays
def dot(line1, line2):
    if len(line1) != len(line2):
        print("Error zip args are difference size")
        return []
    return sum([line1[i] * line2[i] for i in range(len(line1))])

# mutiply A * B
def mult(A, B):
    rowA = len(A)
    rowB = len(B)
    if (rowA <= 0) or (len(B) <= 0): # ensures no empty
        return []
    colA = len(A[0])
    if colA != rowB:    # check matrix size for compatibility
        print "A and B cannot be multiplied because of their incompatible size"
        return []
    m = []
    B = transpose(B)# transposing B will back loop below easier to perform
    rowB = len(B)
    for i in range(rowA):
        l = []
        row = A[i] # for each row in A
        for j in range(rowB):
            col = B[j]
            # dot every col in B
            product = dot(row, col)
            l.append(product)
        m.append(l)
    return m


def dataFromFile(filename):
    file = open(filename, 'r')
    data = file.readlines()
    points  = []
    for d in data:
        # split at space
        l = d.split(' ')
        p = []
        for s in l:
            p.append(float(s))
        points.append(p)
    return points

# draw line linear line given b and x
# b y-intercept
# x slope
def drawLine(plot, y, x, x_width):
    # Create a list of values in the best fit line
    abline_values = [slope * i + intercept for i in x]



def plot(points, result):
    # plotting points
    pointsT = transpose(points)
    Xs = pointsT[0]
    Ys = pointsT[1]
    plt.plot(Xs, Ys, '*')
    margin = 1
    plt.xlim(xmin=0, xmax=max(Xs)+margin) # define x range of the plot
    plt.ylim(ymin=0, ymax=max(Ys)+margin) # define y range of the plot
    # plotting line
    b = result[0][0]
    slope = result[1][0]
    print "Y-intercept : " , b
    print "Slope       : " , slope
    linespace = [float(i) for i in range(0, int(max(Xs)) + margin)]
    abline_values = [slope * x + b for x in linespace]
    plt.plot(linespace, abline_values, '--')
    plt.show()

def main():
    if len(sys.argv) < 2:
        print("no argument given, please supply a data file")
        print(" - usage: python linear_regression.py [filename]")
        sys.exit(0)
    # read from file and convert to nx2 matrix
    points = dataFromFile(sys.argv[1])
    result = normal(points)
    # result is 2 x 1 matrix
    plot(points, result)

if __name__ == "__main__":
    main()


