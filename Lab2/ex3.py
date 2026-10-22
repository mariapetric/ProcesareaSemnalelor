
import numpy as np
import sounddevice as sd
from scipy.io import wavfile


def generate_signals(fs):
    t_a = np.arange(1600) / fs
    t_b = np.arange(3 * fs) / fs
    t_cd = np.arange(fs) / fs

    a = np.sin(2 * np.pi * 400 * t_a)
    b = np.sin(2 * np.pi * 800 * t_b)
    c = 2 * ((240 * t_cd) % 1) - 1
    d = np.where(np.sin(2 * np.pi * 300 * t_cd) >= 0, 1.0, -1.0)

    return [a, b, c, d]


def play_signals(signals, fs):
    for i, signal in enumerate(signals):
        print(f"Playing signal {chr(ord('a') + i)}")
        sd.play(signal, fs)
        sd.wait()


def ex_3():
    fs = 44100
    signals = generate_signals(fs)

    play_signals(signals, fs)

    signal = signals[1].astype(np.float32)
    wavfile.write("signal.wav", fs, signal)

    rate, loaded_signal = wavfile.read("signal.wav")

    print("Sampling frequency:", rate)
    print("Number of samples:", len(loaded_signal))
    print("Signals identical:", np.array_equal(signal, loaded_signal))


ex_3()
