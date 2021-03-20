# coding:UTF-8
import os
import numpy as np
import math
import matplotlib.pyplot as plt

DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/../../data/Mathematical Functions/"

# Parameter
t1 = np.arange(-10.0, 10.1, 0.1)
t2 = np.arange(0.0, 10.1, 0.1)
r1 = np.linspace(-2 * np.pi, 2 * np.pi, 721)
r2 = np.linspace(-1 * np.pi, 1 * np.pi, 361)
r3 = np.linspace(0, 2 * np.pi, 361)
r4 = np.linspace(0, 4 * np.pi, 721)

# Elementary function
## linear function
x = t1
y = t1
np.savetxt("{0}Linear_Function.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="y=x", color="blue")

## quadratic function
x = t1
y = t1 ** 2
np.savetxt("{0}Quadratic_Function.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="y=x^2", color="orange")

## cubic function
x = t1
y = t1 ** 3
np.savetxt("{0}Cubic_Function.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="y=x^3", color="red")
# plt.axhline(0, linewidth=2, color="black")
# plt.axvline(0, linewidth=2, color="black")
# plt.legend()
# plt.show()

## square root function
x = t2
y = t2 ** (1/2)
np.savetxt("{0}Square_Root_Function.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="y=x^(1/2)", color="cyan")

## cubic root function
x = t2
y = t2 ** (1/3)
np.savetxt("{0}Cubic_Root_Function.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="y=x^(1/3)", color="green")
# plt.axhline(0, linewidth=2, color="black")
# plt.axvline(0, linewidth=2, color="black")
# plt.legend()
# plt.show()

## exponential function
### a = 2
x = t1
y = 2 ** t1
np.savetxt("{0}Two_to_the_xth_Power_Function.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="y=2^x", color="yellow")

### a = e
x = t1
y = np.exp(t1)
np.savetxt("{0}Napier's_Constant_to_the_xth_Power_Function.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(t1, y, label="y=e^x", color="magenta")
# plt.axhline(0, linewidth=2, color="black")
# plt.axvline(0, linewidth=2, color="black")
# plt.legend()
# plt.show()

## logarithm function
##### WIP #####

## trigonometric function
### sine
x = r1
y = np.sin(r1)
np.savetxt("{0}Sine.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="y=sin(x)", color="blue")

### cosine
x = r1
y = np.cos(r1)
np.savetxt("{0}Cosine.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="y=cos(x)", color="orange")
# plt.xticks(np.linspace(-2 * np.pi, 2 * np.pi, 9), ["-2π", "-3π/2", "-π", "-π/2", "0", "π/2", "π", "2π/2", "2π"])
# plt.axhline(0, linewidth=2, color="black")
# plt.axvline(0, linewidth=2, color="black")
# plt.legend()
# plt.show()

### tangent
x = r2
y = np.tan(r2)
np.savetxt("{0}Tangent.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="y=tan(x)", color="green", marker=".", ls="None")
# plt.xticks(np.linspace(-1 * np.pi, np.pi, 5), ["-π", "-π/2", "0", "π/2", "π"])
# plt.axhline(0, linewidth=2, color="black")
# plt.axvline(0, linewidth=2, color="black")
# plt.legend()
# plt.show()

### cosecant csc
##### WIP #####

### secant sec
##### WIP #####

### cotangent cot
##### WIP #####


## hyperbolic function
### sinh
##### WIP #####

### cosh
##### WIP #####

### tanh
##### WIP #####

### sech
##### WIP #####

### csch
##### WIP #####

### coth
##### WIP #####

## inverse hyperbolic functions
### arsinh
##### WIP #####

### arcosh
##### WIP #####

### artanh
##### WIP #####

### arsech
##### WIP #####

### arcsch
##### WIP #####

### arcot
##### WIP #####

# Parametric Representation
## cycloid
x = r3 - np.sin(r3)
y = 1 - np.cos(r3)
np.savetxt("{0}Cycloid.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.title("cycloid")
# plt.plot(x, y, label="a=1", color="blue", marker=".")
# plt.axhline(0, linewidth=2, color="black")
# plt.axvline(0, linewidth=2, color="black")
# plt.legend()
# plt.show()

## astroid
x = np.cos(r3) ** 3
y = np.sin(r3) ** 3
np.savetxt("{0}Astroid.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.title("astroid")
# plt.plot(x, y, label="a=1", color="blue", marker=".")
# plt.axhline(0, linewidth=2, color="black")
# plt.axvline(0, linewidth=2, color="black")
# plt.legend()
# plt.show()

## cardioid
x = (1 + np.cos(r3)) * np.cos(r3)
y = (1 + np.cos(r3)) * np.sin(r3)
np.savetxt("{0}Cardioid.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.title("cardioid")
# plt.plot(x, y, label="a-1", color="blue", marker=".")
# plt.axhline(0, linewidth=2, color="black")
# plt.axvline(0, linewidth=2, color="black")
# plt.legend()
# plt.show()

## logarithmic spiral
## circle
x = np.cos(r3)
y = np.sin(r3)
np.savetxt("{0}Circle.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="a=1, b=0", color="blue", marker=".")

## general
x = np.exp(r4 / 4) * np.cos(r4)
y = np.exp(r4 / 4) * np.sin(r4)
np.savetxt("{0}Logarithmic_Spiral.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.title("logarithmic spiral")
# plt.plot(x, y, label="a=1, b=1/4", color="orange", marker=".")
# plt.axhline(0, linewidth=2, color="black")
# plt.axvline(0, linewidth=2, color="black")
# plt.legend()
# plt.show()

## Lissajous curve
### a=1, b=2, ∂=0
x = np.sin(1 * r4)
y = np.sin(2 * r4)
np.savetxt("{0}Lissajous_Curve_1.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="a=1, b=2, ∂=0", color="blue", marker=".")

### a=3, b=4, ∂=0
x = np.sin(3 * r4)
y = np.sin(4 * r4)
np.savetxt("{0}Lissajous_Curve_2.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="a=3, b=4, ∂=0", color="orange", marker=".")

### a=5, b=6, ∂=0
x = np.sin(5 * r4)
y = np.sin(6 * r4)
np.savetxt("{0}Lissajous_Curve_3.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="a=5, b=6, ∂=0", color="red", marker=".")
# plt.title("Lissajous curve")
# plt.axhline(0, linewidth=2, color="black")
# plt.axvline(0, linewidth=2, color="black")
# plt.legend()
# plt.show()

## involute curve
x = np.cos(r4) + r4 * np.sin(r4)
y = np.sin(r4) - r4 * np.cos(r4)
np.savetxt("{0}Involute_Curve.csv".format(DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
# plt.plot(x, y, label="a=1", color="blue", marker=".")
# plt.title("involute curve")
# plt.axhline(0, linewidth=2, color="black")
# plt.axvline(0, linewidth=2, color="black")
# plt.legend()
# plt.show()
