import math
#求解一元2次方程
def quadratic(a, b, c):
	Δ = (b * b) - (4 * a * c)
	if Δ < 0:
		print("方程式无解")
	elif Δ == 0:
		return -(b / 2*a)
	else:
		x1 = (-b + math.sqrt(Δ)) / (2*a)
		x2 = (-b - math.sqrt(Δ)) / (2*a)
		return x1,x2


# 测试:
print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)
