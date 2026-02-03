import numpy as np
import matplotlib.pyplot as plt
from dateutil import parser
from datetime import timedelta

start_time = parser.parse("2025-01-01T00:00:00")
time_steps = [start_time + timedelta(minutes=10 * i) for i in range(100)]
time_values = [t.strftime("%Y-%m-%d %H:%M:%S") for t in time_steps]

x_values = np.linspace(0, 10 * np.pi, 100)
y_values = np.sin(x_values)

plt.figure(figsize=(10, 6))
plt.plot(time_values, y_values, label="Sine Wave")
tick_step = 10
plt.xticks(range(0, len(time_values), tick_step), time_values[::tick_step], rotation=45)

plt.xlabel("Time")
plt.ylabel("Sine Value")
plt.title("Sine Wave Over Time")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
