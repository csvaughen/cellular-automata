# this file thanks to ChatGPT :)

import matplotlib.pyplot as plt
import numpy as np


def get_rule_binary(rule_number):
    """Convert rule number to 8-bit binary representation."""
    return np.array([int(x) for x in np.binary_repr(rule_number, width=8)], dtype=int)


def apply_rule(left, center, right, rule_binary):
    """Determine new cell state based on neighbors and rule."""
    idx = 7 - (4 * left + 2 * center + right)  # Convert neighborhood to index
    return rule_binary[idx]


def generate_ca(rule_number, size=101, generations=50):
    """Generate and return cellular automaton grid."""
    rule_binary = get_rule_binary(rule_number)
    grid = np.zeros((generations, size), dtype=int)

    # Start with single black cell in the center
    grid[0, size // 2] = 1

    # Apply rule for each generation
    for gen in range(1, generations):
        for i in range(size):
            left = grid[gen - 1, (i - 1) % size]  # Wrap around edges
            center = grid[gen - 1, i]
            right = grid[gen - 1, (i + 1) % size]
            grid[gen, i] = apply_rule(left, center, right, rule_binary)

    return grid


def plot_ca(grid, rule_number):
    """Visualize the cellular automaton."""
    plt.figure(figsize=(10, 6))
    plt.imshow(grid, cmap='binary', interpolation='nearest')
    plt.title(f'Elementary Cellular Automaton - Rule {rule_number}')
    plt.xlabel('Cell Index')
    plt.ylabel('Generation')
    plt.show()


# Example: Run Rule 30
rule_number = 110  # Change this to test other rules (0-255)
grid = generate_ca(rule_number, size=201, generations=100)
plot_ca(grid, rule_number)
