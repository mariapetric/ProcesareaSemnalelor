
import numpy as np
import matplotlib.pyplot as plt


def generate_functions(alpha):
    exact = np.sin(alpha)
    taylor = alpha
    pade = (alpha - 7 * alpha**3 / 60) / (1 + alpha**2 / 20)

    return exact, taylor, pade


def plot_functions(alpha, exact, taylor, pade):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    axs[0, 0].plot(alpha, exact, label="sin(alpha)")
    axs[0, 0].plot(alpha, taylor, label="Taylor")
    axs[0, 0].plot(alpha, pade, label="Pade")
    axs[0, 0].set_title("Function comparison")

    error_taylor = np.abs(exact - taylor)
    error_pade = np.abs(exact - pade)

    axs[0, 1].plot(alpha, error_taylor, label="Taylor error")
    axs[0, 1].plot(alpha, error_pade, label="Pade error")
    axs[0, 1].set_title("Absolute errors")

    axs[1, 0].plot(alpha, error_taylor, label="Taylor error")
    axs[1, 0].plot(alpha, error_pade, label="Pade error")
    axs[1, 0].set_yscale("log")
    axs[1, 0].set_title("Errors - logarithmic scale")

    axs[1, 1].plot(alpha, exact, label="sin(alpha)")
    axs[1, 1].plot(alpha, taylor, label="Taylor")
    axs[1, 1].plot(alpha, pade, label="Pade")
    axs[1, 1].set_xlim(-0.5, 0.5)
    axs[1, 1].set_title("Zoom near zero")

    for ax in axs.flat:
        ax.set_xlabel("Alpha (radians)")
        ax.grid(True)
        ax.legend()

    plt.tight_layout()
    plt.savefig("ex_8.pdf", bbox_inches="tight")
    plt.show()


def ex_8():
    alpha = np.linspace(-np.pi / 2, np.pi / 2, 1000)

    exact, taylor, pade = generate_functions(alpha)

    plot_functions(alpha, exact, taylor, pade)


ex_8()
