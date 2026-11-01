import subprocess
import time

x = 0.8

for i in range(20):

    x -= 0.03

    cmd = (
        f"gz model "
        f"-m xyz_stage "
        f"-x {x} "
        f"-y 0 "
        f"-z 0.1"
    )

    subprocess.run(cmd, shell=True)

    print(f"x={x:.3f}")

    time.sleep(0.5)
