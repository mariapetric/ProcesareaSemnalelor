
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


def generate_signals(t):
    x = np.sin(2 * np.pi * 400 * t)
    y = np.sin(2 * np.pi * 800 * t)

    return x, y


def plot_signals(t, x, y, combined):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    axs[0].plot(t, x)
    axs[0].set_title("Signal 1 - 400 Hz")

    axs[1].plot(t, y)
    axs[1].set_title("Signal 2 - 800 Hz")

    t_combined = np.arange(len(combined)) / 44100
    axs[2].plot(t_combined, combined)
    axs[2].set_title("Concatenated signal")

    for ax in axs:
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)

    plt.tight_layout()
    plt.show()


def ex_5():
    fs = 44100
    t = np.arange(fs) / fs

    x, y = generate_signals(t)

    combined = np.concatenate((x, y))

    sd.play(combined, fs)
    sd.wait()

    plot_signals(t, x, y, combined)


ex_5()
