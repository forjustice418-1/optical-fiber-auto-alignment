import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

df = pd.read_csv("alignment_history.csv")

fig, ax = plt.subplots()

line, = ax.plot([], [], lw=2)

ax.set_xlim(0, len(df))
ax.set_ylim(df["power"].min()*0.99,
            df["power"].max()*1.01)

ax.set_xlabel("Iteration")
ax.set_ylabel("Power")

def update(frame):

    x = df["step"][:frame]
    y = df["power"][:frame]

    line.set_data(x, y)

    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=len(df),
    interval=50
)

ani.save("power_animation.mp4")