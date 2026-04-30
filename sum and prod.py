import numpy
n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

sum_axis_0 = numpy.sum(arr, axis=0)
print(numpy.prod(sum_axis_0))
