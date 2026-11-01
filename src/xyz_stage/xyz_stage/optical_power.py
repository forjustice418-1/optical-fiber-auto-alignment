import math

tx_x = 0.0
rx_x = 0.0

dx = tx_x - rx_x

power = math.exp(-(dx**2) * 5)

print(f"dx={dx:.3f}")
print(f"power={power:.4f}")
