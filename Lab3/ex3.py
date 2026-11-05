
import numpy as np
import matplotlib.pyplot as plt


def generate_signal(t):
    x1 = np.cos(2 * np.pi * 10 * t)
    x2 = 2 * np.cos(2 * np.pi * 25 * t)
    x3 = 0.5 * np.cos(2 * np.pi * 60 * t)

    return x1 + x2 + x3


def calculate_fourier(signal, N, frequencies):
    X = np.zeros(len(frequencies), dtype=complex)

    for i, k in enumerate(frequencies):
        for n in range(N):
            X[i] += signal[n] * np.exp(-2j * np.pi * k * n / N)

    return X


def plot_signals(t, signal, frequencies, X):
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    axs[0].plot(t, signal)
    axs[0].set_title("Original signal")
    axs[0].set_xlabel("Time (s)")
    axs[0].set_ylabel("Amplitude")
    axs[0].grid(True)

    axs[1].plot(frequencies, np.abs(X))
    axs[1].set_title("Fourier transform magnitude")
    axs[1].set_xlabel("Frequency (Hz)")
    axs[1].set_ylabel("|X(f)|")
    axs[1].grid(True)

    plt.tight_layout()
    plt.savefig("ex_3.pdf", bbox_inches="tight")
    plt.show()


def ex_3():
    fs = 1000
    duration = 1
    N = fs * duration

    t = np.arange(N) / fs
    signal = generate_signal(t)

    frequencies = np.arange(1, 101)
    X = calculate_fourier(signal, N, frequencies)

    plot_signals(t, signal, frequencies, X)

    for frequency in [10, 25, 60]:
        index = np.where(frequencies == frequency)[0][0]
        print(f"{frequency} Hz: {np.abs(X[index]):.2f}")


if __name__ == "__main__":
    ex_3()
