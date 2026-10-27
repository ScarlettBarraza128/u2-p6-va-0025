import matplotlib.pyplot as plt
import numpy as np

# Emily Barraza NC = 0025
cant_productos=[100,150,200,300,500]
precio=[3000, 8000, 5000, 15000, 17000]

plt.plot(cant_productos, precio)
plt.show()

# personalizar grafica
plt.plot(
    cant_productos,
      precio,
      color="blue",
      marker="*",
      linestyle="dashed",
      linewidth=2,
      markersize=12
)
plt.title("ventas de walmart 0025")
plt.xlabel("precios")
plt.ylabel("cant prod")
plt.show()



