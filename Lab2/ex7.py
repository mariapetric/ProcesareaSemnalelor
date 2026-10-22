
import numpy as np
import matplotlib.pyplot as plt


def generate_signal(t, frequency):
    return np.sin(2 * np.pi * frequency * t)


def plot_signals(times, signals, titles):
    fig, axs = plt.subplots(len(signals), 1, figsize=(10, 8))

    for ax, t, signal, title in zip(axs, times, signals, titles):
        ax.stem(t, signal)
        ax.set_title(title)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.set_ylim(-1.2, 1.2)
        ax.grid(True)

    plt.tight_layout()
    plt.savefig("ex_7.pdf", bbox_inches="tight")
    plt.show()


def ex_7():
    fs = 1000
    frequency = 10
    duration = 0.3

    t = np.arange(int(fs * duration)) / fs
    x = generate_signal(t, frequency)

    x_decimated = x[::4]
    t_decimated = t[::4]

    x_shifted = x[1::4]
    t_shifted = t[1::4]

    times = [t, t_decimated, t_shifted]
    signals = [x, x_decimated, x_shifted]

    titles = [
        "Original signal (1000 Hz)",
        "Decimated signal (250 Hz)",
        "Decimated signal starting from second sample (250 Hz)"
    ]

    plot_signals(times, signals, titles)


ex_7()

'''
Prin decimarea semnalului la un sfert din frecventa initiala, numarul de esantioane se reduce de patru ori,
deci frecventa de esantionare scade de la 1000 Hz la 250 Hz. Frecventa semnalului e aceeasi, dar
reprezentarea discreta contine mai putine puncte.

Daca decimarea incepe de la al doilea element, se obtine un semnal cu aceeasi frecventa, dar cu un decalaj de faza,
pentru ca esantioanele sunt preluate la momente de timp diferite.
'''
