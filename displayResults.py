import matplotlib.pyplot as plt
import numpy as np

data = []

with open("log.txt", "r") as f:
	for line in f:
		data.append(line)

splitData = [c.replace(' ','').split("|") for c in data][1:]

xpoints = np.array([l[2] for l in splitData])
y1points = np.array([l[6] for l in splitData])
y2points = np.array([l[7] for l in splitData])

y1points = [float(n.replace("nan", "0")) for n in y1points]
y2points = [float(n.replace("nan", "0")) for n in y2points]

plt.figure(facecolor="#777777")
plt.gca().set_facecolor("#777777")
plt.gca().axes.get_xaxis().set_ticks([])
plt.plot(xpoints, y1points, label="Download", color='blue')
plt.plot(xpoints, y2points, label="Upload", color="red")
plt.xlabel("Time")
plt.ylabel("Speed")
plt.legend()
plt.show()
