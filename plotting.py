# mauricio.calderon@iest.edu.mx

import matplotlib.pyplot as plt

# x and y values
x = [x for x in range(-100, 100)]
y = [x ** 5 for x in range(-100, 100)]
y1 = [x ** 3 for x in range(-100, 100)]
y2 = [x ** 2 for x in range(-100, 100)]

# Plotting the points
plt.plot(x, y)
plt.plot(x, y1)
plt.plot(x, y2)

# Adding labels and title
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Simple Line Plot')

# Displaying the plot
plt.show()