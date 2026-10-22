
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def generate_signals(t):
    x = np.sin(2 * np.pi * 5 * t)
    y = signal.sawtooth(2 * np.pi * 3 * t)

    return x, y, x + y


def plot_signals(t, signals, titles):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    for ax, current_signal, title in zip(axs, signals, titles):
        ax.plot(t, current_signal)
        ax.set_title(title)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)

    plt.tight_layout()
    plt.savefig("ex_4.pdf", bbox_inches="tight")
    plt.show()


def ex_4():
    fs = 1000
    t = np.arange(fs) / fs

    signals = generate_signals(t)
    titles = ["Sine wave (5 Hz)", "Sawtooth wave (3 Hz)", "Sum of signals"]

    plot_signals(t, signals, titles)


ex_4()
