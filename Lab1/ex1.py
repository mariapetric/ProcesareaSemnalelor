import numpy as np
import matplotlib.pyplot as plt


def generate_signals(t):
    x = np.cos(520 * np.pi * t + np.pi / 3)
    y = np.cos(280 * np.pi * t - np.pi / 3)
    z = np.cos(120 * np.pi * t + np.pi / 3)

    return x, y, z


def plot_signals(t, signals, titles, filename, discrete=False):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    fig.suptitle("Discrete signals" if discrete else "Continuous signals")

    for ax, signal, title in zip(axs, signals, titles):
        if discrete:
            ax.stem(t, signal)
        else:
            ax.plot(t, signal)

        ax.set_title(title)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


def ex1_a():
    t = np.arange(0, 0.03 + 0.0005, 0.0005)
    print(t)
    return t


def ex1_b():
    t = ex1_a()
    x, y, z = generate_signals(t)

    plot_signals(
        t,
        (x, y, z),
        ("x(t) - 260 Hz", "y(t) - 140 Hz", "z(t) - 60 Hz"),
        "ex1_b.pdf"
    )


def ex1_c():
    fs = 200
    T = 1 / fs

    t = np.arange(0, 0.03 + T / 2, T)
    x, y, z = generate_signals(t)

    plot_signals(
        t,
        (x, y, z),
        ("x[n]", "y[n]", "z[n]"),
        "ex1_c.pdf",
        discrete=True
    )


def main():
    # ex1_a()
    ex1_b()
    ex1_c()


if __name__ == "__main__":
    main()