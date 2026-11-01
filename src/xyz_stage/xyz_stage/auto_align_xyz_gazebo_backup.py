import math
import random
import subprocess
import time

# 導波路入口座標
wafer_center_x = 0.0
wafer_width = 0.4

wafer_left = -0.2

waveguide_x = wafer_left
waveguide_y = 0.0
waveguide_z = 0.08

# ファイバー初期位置
rx_x = -1.0
rx_y = 0.3
rx_z = 0.12

step = 0.02

safe_gap = 0.03

# ウェハ左側面
wafer_left = -1.0

position_error = 0.005

history = []


def actual_position(x, y, z):

    return (
        x + random.uniform(-position_error,
                           position_error),

        y + random.uniform(-position_error,
                           position_error),

        z + random.uniform(-position_error,
                           position_error)
    )


def power(wx, wy, wz,
          rx, ry, rz):

    dx = wx - rx
    dy = wy - ry
    dz = wz - rz

    base = (
        math.exp(-(dx * dx) * 25)
        * math.exp(-(dy * dy) * 25)
        * math.exp(-(dz * dz) * 200)
    )

    ripple = (
        1.0
        + 0.15 * math.sin(dx * 30)
        + 0.10 * math.sin(dy * 30)
    )

    noise = random.uniform(-0.02, 0.02)

    return max(
        0.0,
        base * ripple + noise
    )


for i in range(150):

    ax, ay, az = actual_position(
        rx_x,
        rx_y,
        rx_z
    )

    current = power(
        waveguide_x,
        waveguide_y,
        waveguide_z,
        ax,
        ay,
        az
    )

    candidates = [

        (rx_x + step, rx_y, rx_z),
        (rx_x - step, rx_y, rx_z),

        (rx_x, rx_y + step, rx_z),
        (rx_x, rx_y - step, rx_z),

        (rx_x, rx_y, rx_z + step),
        (rx_x, rx_y, rx_z - step)

    ]

    best_power = current
    best_pos = (rx_x, rx_y, rx_z)

    for x, y, z in candidates:

        ax, ay, az = actual_position(
            x, y, z
        )

        p = power(
            waveguide_x,
            waveguide_y,
            waveguide_z,
            ax,
            ay,
            az
        )

        if p > best_power:

            best_power = p
            best_pos = (x, y, z)

    rx_x, rx_y, rx_z = best_pos

    if rx_x < waveguide_x + safe_gap:
        rx_x = waveguide_x + safe_gap
    if rx_x > wafer_left:
    rx_x = wafer_left

    subprocess.run(
        [
            "gz",
            "model",
            "-m",
            "rx_fiber",
            "-x",
            str(rx_x),
            "-y",
            str(rx_y),
            "-z",
            str(rx_z)
        ]
    )

    history.append(
        [
            i,
            rx_x,
            rx_y,
            rx_z,
            best_power
        ]
    )

    print(
        f"{i:03d}",
        f"x={rx_x:.3f}",
        f"y={rx_y:.3f}",
        f"z={rx_z:.3f}",
        f"power={best_power:.5f}"
    )

    time.sleep(0.2)

with open(
    "alignment_history.csv",
    "w"
) as f:

    f.write(
        "step,x,y,z,power\n"
    )

    for row in history:

        f.write(
            f"{row[0]},"
            f"{row[1]},"
            f"{row[2]},"
            f"{row[3]},"
            f"{row[4]}\n"
        )

print("alignment_history.csv saved")
