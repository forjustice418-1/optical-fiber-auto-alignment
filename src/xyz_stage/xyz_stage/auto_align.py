import math

tx_x = 0.0
rx_x = 0.8

step = 0.02

def power(tx, rx):
    dx = tx - rx
    return math.exp(-(dx**2) * 5)

for i in range(50):

    current = power(tx_x, rx_x)

    left = power(tx_x, rx_x - step)
    right = power(tx_x, rx_x + step)

    if left > current:
        rx_x -= step
    elif right > current:
        rx_x += step

    print(
        f"{i:02d}",
        f"rx={rx_x:.3f}",
        f"power={power(tx_x, rx_x):.4f}"
    )
