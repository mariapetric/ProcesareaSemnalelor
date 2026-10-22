
import numpy as np
import matplotlib.pyplot as plt


def generate_continuous_signals(t_cont, fs):
    x_cont = np.sin(2 * np.pi * (fs / 2) * t_cont)
    y_cont = np.sin(2 * np.pi * (fs / 4) * t_cont)
    z_cont = np.sin(2 * np.pi * 0 * t_cont)
    return x_cont, y_cont, z_cont


def generate_sampled_signals(t_disc, fs):
    x_disc = np.sin(2 * np.pi * (fs / 2) * t_disc)
    y_disc = np.sin(2 * np.pi * (fs / 4) * t_disc)
    z_disc = np.sin(2 * np.pi * 0 * t_disc)
    return x_disc, y_disc, z_disc


def plot_signals(t_cont, continuous_signals, t_disc, sampled_signals, titles):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    for ax, cont, disc, title in zip(axs, continuous_signals, sampled_signals, titles):
        ax.plot(t_cont, cont)
        ax.stem(t_disc, disc, linefmt='C1-', markerfmt='C1o', basefmt=' ')
        ax.set_title(title)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.set_ylim(-1.2, 1.2)
        ax.grid(True)

    plt.tight_layout()
    plt.savefig("ex_6.pdf", bbox_inches="tight")
    plt.show()


def ex_6():
    fs = 100
    t_disc = np.arange(20) / fs
    t_cont = np.linspace(0, t_disc[-1], 5000)

    continuous_signals = generate_continuous_signals(t_cont, fs)
    sampled_signals = generate_sampled_signals(t_disc, fs)

    titles = ["f = fs / 2", "f = fs / 4", "f = 0 Hz"]

    plot_signals(t_cont, continuous_signals, t_disc, sampled_signals, titles)


ex_6()

'''
Pentru f = fs/2, toate esantioanele sunt zero, desi semnalul continuu oscileaza.
Pentru f = fs/4, esantioanele surprind variatiile semnalului, iar pentru f=0 semnalul e constant nul.

Deci, doua semnale continue diferite pot produce aceleasi esantioane, ceea ce arata ca o frecventa
de esantionare care nu e suficienta poate duce la pierderea informatiei si poate face imposibila reconstruirea
semnalului original.
'''
