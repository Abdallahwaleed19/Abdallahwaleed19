import statistics
import matplotlib.pyplot as plt 
import scipy.stats as stats
import numpy as np
X = list (map (int,input("Enter the values of x : ").split()))  # Values of X
Y = list (map (int,input("Enter the values of y : ").split())) # Values of Y 
# To Check before we start the mession 
if len(X) != len(Y):
       print("Error: The number of elements in X and Y must be the same.")
elif len(X) < 2:
       print("Error: X and Y must have at least two elements for correlation and regression.")
else :
# Mean
    mean_of_x = statistics.mean(X)
    mean_of_y = statistics.mean(Y)
    print(" Mean of X = " , mean_of_x) # Mean of X 
    print(" Mean of Y = " , mean_of_y) # Mean of Y
# Correlation Coefficient 
    correlation_of_x_y , p_value = stats.pearsonr(X, Y)
    print("Correlation Coefficient between X and Y =", correlation_of_x_y) # Correlation Result 
# linear Regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
    print("\nLinear Regression Results:")
    print("Slope (m):", slope)
    print("Intercept (b):", intercept)
    print("R-squared (r^2):", r_value ** 2)
    print("P-value:", p_value)
    print("Standard Error:", std_err)
# Generate the regression line
    regression_line = [slope * x + intercept for x in X]
# Scatter Plot with Regression Line
    plt.figure(figsize=(10, 6))
    plt.scatter(X, Y, color='blue', label='Data Points')
    plt.plot(X, regression_line, color='red', label='Regression Line')
    plt.title('Scatter Plot with Regression Line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()
# Histogram of X and Y
    plt.figure(figsize=(12, 6))
# Histogram for X
    plt.subplot(1, 2, 1)
    plt.hist(X, bins=10, color='green', alpha=0.7)
    plt.title('Histogram of X')
    plt.xlabel('X')
    plt.ylabel('Frequency')
# Histogram for Y
    plt.subplot(1, 2, 2)
    plt.hist(Y, bins=10, color='orange', alpha=0.7)
    plt.title('Histogram of Y')
    plt.xlabel('Y')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
 # Residual Plot
    residuals = [y - (slope * x + intercept) for x, y in zip(X, Y)]
    plt.figure(figsize=(10, 6))
    plt.scatter(X, residuals, color='purple')
    plt.axhline(y=0, color='black', linestyle='--')
    plt.title('Residual Plot')
    plt.xlabel('X')
    plt.ylabel('Residuals')
    plt.grid(True)
    plt.show()
# Box Plot for X and Y
    plt.figure(figsize=(10, 6))
    plt.boxplot([X, Y], labels=['X', 'Y'], patch_artist=True, boxprops=dict(facecolor='cyan'))
    plt.title('Box Plot of X and Y')
    plt.ylabel('Values')
    plt.grid(True)
    plt.show()    
# Polynomial Regression (Curve Fitting)
    degree = 2  # Degree of the polynomial (adjustable)
    polynomial_coefficients = np.polyfit(X, Y, degree)
    polynomial = np.poly1d(polynomial_coefficients)
    
    # Generate values for the curve using the polynomial
    curve = polynomial(np.linspace(min(X), max(X), 500))  # Smooth curve

    # Plotting the Polynomial Curve
    plt.figure(figsize=(10, 6))
    plt.scatter(X, Y, color='blue', label='Data Points')  # Optional: plot the data points
    plt.plot(np.linspace(min(X), max(X), 500), curve, color='green', label=f'Polynomial Curve (Degree {degree})')
    plt.title(f'Polynomial Curve (Degree {degree}) Fit')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()








