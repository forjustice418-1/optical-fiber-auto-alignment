import subprocess
import time

x = 0.4
y = 0.2

for i in range(10):

    x -= 0.02
    y -= 0.01

    cmd = (
        f"gz model "
        f"-m rx_fiber "
        f"-x {x} "
        f"-y {y} "
        f"-z 0"
    )

    subprocess.run(cmd, shell=True)

    print(
        f"{i:02d}",
        f"x={x:.3f}",
        f"y={y:.3f}"
    )

    time.sleep(1)
