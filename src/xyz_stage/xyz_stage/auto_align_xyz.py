import math

tx_x = 0.0
tx_y = 0.0
tx_z = 0.0

rx_x = 0.4
rx_y = 0.2
rx_z = 0.3

step = 0.02


def power(tx_x, tx_y, tx_z,
          rx_x, rx_y, rx_z):

    dx = tx_x - rx_x
    dy = tx_y - rx_y
    dz = tx_z - rx_z

    return math.exp(
        -(dx*dx + dy*dy + dz*dz) * 10
    )


for i in range(100):

    current = power(
        tx_x, tx_y, tx_z,
        rx_x, rx_y, rx_z
    )

    candidates = [

        (rx_x+step, rx_y, rx_z),
        (rx_x-step, rx_y, rx_z),

        (rx_x, rx_y+step, rx_z),
        (rx_x, rx_y-step, rx_z),

        (rx_x, rx_y, rx_z+step),
        (rx_x, rx_y, rx_z-step),
    ]

    best = current
    best_pos = (rx_x, rx_y, rx_z)

    for x, y, z in candidates:

        p = power(
            tx_x, tx_y, tx_z,
            x, y, z
        )

        if p > best:
            best = p
            best_pos = (x, y, z)

    rx_x, rx_y, rx_z = best_pos

    print(
        f"{i:03d}",
        f"x={rx_x:.3f}",
        f"y={rx_y:.3f}",
        f"z={rx_z:.3f}",
        f"power={best:.4f}"
    )
