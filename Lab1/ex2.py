
import numpy as np
import matplotlib.pyplot as plt


def generate_time(fs, duration):
    return np.arange(0, duration, 1 / fs)


def generate_sine(t, frequency):
    return np.sin(2 * np.pi * frequency * t)


def plot_signal(t, signal, title, filename):
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal)

    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


def plot_2d_signal(signal, title, filename):
    plt.figure(figsize=(6, 6))
    plt.imshow(signal, cmap="gray", vmin=0, vmax=1)

    plt.title(title)
    plt.colorbar(label="Amplitude")

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()



def ex2_a():
    fs = 8000
    frequency = 400
    num_samples = 1600

    t = np.arange(num_samples) / fs
    signal = generate_sine(t, frequency)

    plot_signal(t, signal, "2(a) - Sine 400 Hz",
                "ex2_a.pdf")


def ex2_b():
    fs = 8000
    frequency = 800
    duration = 3

    t = generate_time(fs, duration)
    signal = generate_sine(t, frequency)

    plot_signal(t, signal, "2(b) - Sine 800 Hz",
                "ex2_b.pdf")


def ex2_c():
    fs = 8000
    frequency = 240
    duration = 0.025

    t = generate_time(fs, duration)

    signal = 2 * np.mod(frequency * t, 1) - 1

    plot_signal(t, signal, "2(c) - Sawtooth 240 Hz",
                "ex2_c.pdf")


def ex2_d():
    fs = 8000
    frequency = 300
    duration = 0.025

    t = generate_time(fs, duration)

    signal = np.where(
        np.sin(2 * np.pi * frequency * t) >= 0,
        1, -1
    )

    plot_signal(t, signal, "2(d) - Square 300 Hz",
                "ex2_d.pdf")


def ex2_e():
    signal = np.random.rand(128, 128)

    plot_2d_signal(signal, "2(e) - Random 2D signal",
                   "ex2_e.pdf")


def ex2_f():
    signal = np.zeros((128, 128))

    signal[0:30, 0:30] = 1

    plot_2d_signal(signal, "2(f) - Custom 2D signal",
                   "ex2_f.pdf")


def main():
    # ex2_a()
    # ex2_b()
    # ex2_c()
    # ex2_d()
    ex2_e()
    ex2_f()


if __name__ == "__main__":
    main()
