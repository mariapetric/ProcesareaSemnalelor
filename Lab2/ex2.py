import numpy as np
import matplotlib.pyplot as plt

def generate_signal(t, frequency, phase):
    return np.sin(2 * np.pi * frequency * t + phase)

def add_noise(signal, noise, snr):
    gamma = np.linalg.norm(signal) / (np.sqrt(snr) * np.linalg.norm(noise))
    return signal + gamma * noise

def plot_signals(t, signals, titles):
    fig, axs = plt.subplots(len(signals), 1, figsize=(10, 9))

    for ax, signal, title in zip(axs, signals, titles):
        ax.plot(t, signal)
        ax.set_title(title)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)

    plt.tight_layout()
    plt.savefig("ex_2_b.pdf", bbox_inches="tight")
    plt.show()

def ex_2():
    frequency = 5
    fs = 1000
    t = np.arange(fs) / fs

    phases = [0, np.pi / 2, np.pi, 3 * np.pi / 2]
    signals = [generate_signal(t, frequency, phase) for phase in phases]

    plt.figure(figsize=(10, 5))

    for signal, phase in zip(signals, phases):
        plt.plot(t, signal, label=f"Phase = {phase / np.pi:.2f} pi")

    plt.title("Sinusoidal signals with different phases")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("ex_2_a.pdf", bbox_inches="tight")
    plt.show()

    signal = signals[0]
    rng = np.random.default_rng(42)
    noise = rng.normal(0, 1, len(signal))

    snr_values = [0.1, 1, 10, 100]
    noisy_signals = [add_noise(signal, noise, snr) for snr in snr_values]
    titles = [f"SNR = {snr}" for snr in snr_values]

    plot_signals(t, noisy_signals, titles)

ex_2()