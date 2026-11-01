import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

df = pd.read_csv("alignment_history.csv")

fig,(ax1,ax2,ax3)=plt.subplots(3,1,figsize=(7,8))

for ax in [ax1,ax2,ax3]:
    ax.grid(True)

ax1.set_title("Power")
ax2.set_title("Gap")
ax3.set_title("X Position")

ax1.set_xlim(0,len(df))
ax2.set_xlim(0,len(df))
ax3.set_xlim(0,len(df))

ax1.set_ylim(0,1.05)

ax2.set_ylim(
    df["gap"].min()*0.95,
    df["gap"].max()*1.05
)

ax3.set_ylim(
    df["x"].min()*0.95,
    df["x"].max()*1.05
)

line1,=ax1.plot([],[],'b')
line2,=ax2.plot([],[],'r')
line3,=ax3.plot([],[],'g')

dot1,=ax1.plot([],[],'ro')
dot2,=ax2.plot([],[],'ro')
dot3,=ax3.plot([],[],'ro')

def update(i):

    x=df["step"][:i+1]

    p=df["power"][:i+1]
    g=df["gap"][:i+1]
    xp=df["x"][:i+1]

    line1.set_data(x,p)
    line2.set_data(x,g)
    line3.set_data(x,xp)

    dot1.set_data([x.iloc[-1]],[p.iloc[-1]])
    dot2.set_data([x.iloc[-1]],[g.iloc[-1]])
    dot3.set_data([x.iloc[-1]],[xp.iloc[-1]])

    return line1,line2,line3,dot1,dot2,dot3

ani=FuncAnimation(
    fig,
    update,
    frames=len(df),
    interval=80
)

ani.save(
    "alignment_animation.mp4",
    writer="ffmpeg"
)
