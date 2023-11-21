# This project was completed by Uriel Martinez and Kieran Murray.

# Factorial function
def factorial(n):
  if n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result


# Sine function using Taylor series
def calculate_sin(x_deg):
  pi = 3.14159
  x = x_deg * (pi / 180)  # Convert degrees to radians
  x = x % (2 * pi)  # Convert x to an equivalent angle in [0, 2pi]
  result = 0
  n = 0
  term = x
  while True:
    result += term
    n += 1
    term *= (-x * x) / ((2 * n + 1) * (2 * n))
    error = abs(term)
    if error < 0.00001:
      break
  return result, n


# Cosine function using Taylor series
def calculate_cos(x_deg):
  pi = 3.14159
  x = x_deg * (pi / 180)  # Convert degrees to radians
  x = x % (2 * pi)  # Convert x to an equivalent angle in [0, 2pi]
  result = 0
  n = 0
  term = 1
  while True:
    result += term
    n += 1
    term *= (-x * x) / ((2 * n) * (2 * n - 1))
    error = abs(term)
    if error < 0.00001:
      break
  return result, n


# Tangent function using sine and cosine calculations
def calculate_tan(x_deg):
  sin_result, sin_n = calculate_sin(x_deg)
  cos_result, cos_n = calculate_cos(x_deg)

  tan_result = sin_result / cos_result
  return tan_result


def exp(x, target_error=0.00001):
  sum_result, term, n = 1, 1, 1
  while True:
    term *= x / n
    sum_result += term
    n += 1
    error = abs(term)
    if error < target_error:
      break
  return sum_result, n


def ln(x, target_error=0.00001):
  if x <= 0:
    return float('nan')

  y = x - 1
  result = 0
  n = 1
  sign = 1

  while True:
    term =y / n * sign
    result += term
    n += 1
    sign *= -1
    error = abs(term)
    y*= x-1

    if error < target_error:
      break

  return result, n


def calculate_arctan(x_rad, target_error=0.000001):
  pi = 3.14159
  result = 0
  n = 0
  term = x_rad
  while True:
    result += term
    n += 1
    term *= (2*n-1) * -x_rad * x_rad / (2 * n + 1)
    error = abs(term)
    if error < target_error:
      break
  return result*6, n


# Sin usage:
print(f"Sine of 124.56 degrees: {calculate_sin(124.56)}")
print(f"Sine of 277 degrees: {calculate_sin(277)}")
print(f"Sine of π/3 radians: {calculate_sin(60)}")

# Cos usage:
print(f"Cosine of 53 degrees: {calculate_cos(53)}")
print(f"Cosine of 200 degrees: {calculate_cos(200)}")
print(f"Cosine of π/4 radians: {calculate_cos(45)}")

# Tan usage:
print(f"Tangent of 315 degrees: {calculate_tan(315)}")
print(f"Tangent of 68 degrees: {calculate_tan(68)}")
print(f"Tangent of π/6 radians: {calculate_tan(30)}")

# Exponential usage:
print(f"Exponential of 1.5: {exp(1.5)}")
print(f"Exponential of e: {exp(2.718281828)}")

sin_45_deg, sin_n = calculate_sin(45)
exp_sin_45 = exp(sin_45_deg)
print(f"Exponential of sin(45 degrees): {exp_sin_45}")

# Logarithm usage:
print(f"Natural logarithm of 1.5: {ln(1.5)}")

# Arctan usage:
print(f"6 times arctan(0.57735026): {calculate_arctan(0.57735026)}")
