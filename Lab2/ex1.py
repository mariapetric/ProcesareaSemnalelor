import numpy as np
import matplotlib.pyplot as plt

def generate_signals(t, amplitude, frequency, phase):
    x = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    y = amplitude * np.cos(2 * np.pi * frequency * t + phase - np.pi / 2)

    return x, y

def plot_signals(t, x, y):
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))

    axs[0].plot(t, x)
    axs[0].set_title("Sine signal")
    axs[0].set_xlabel("Time (s)")
    axs[0].set_ylabel("Amplitude")
    axs[0].grid(True)

    axs[1].plot(t, y)
    axs[1].set_title("Cosine signal")
    axs[1].set_xlabel("Time (s)")
    axs[1].set_ylabel("Amplitude")
    axs[1].grid(True)

    plt.tight_layout()
    plt.savefig("ex_1.pdf", bbox_inches="tight")
    plt.show()

def ex_1():
    amplitude = 2
    frequency = 5
    phase = np.pi / 4

    t = np.linspace(0, 1, 1000)

    x, y = generate_signals(t, amplitude, frequency, phase)

    plot_signals(t, x, y)

    print("Signals identical:", np.allclose(x, y))

ex_1()