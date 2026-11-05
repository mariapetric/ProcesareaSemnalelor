
import numpy as np
import matplotlib.pyplot as plt


def generate_fourier_matrix(N):
    k = np.arange(N)
    n = np.arange(N)

    F = np.exp(-2j * np.pi * np.outer(k, n) / N)

    return F


def plot_fourier_matrix(F):
    N = F.shape[0]
    n = np.arange(N)

    fig, axs = plt.subplots(N, 2, figsize=(12, 18))

    for k in range(N):
        axs[k, 0].stem(n, F[k].real)
        axs[k, 0].set_title(f"Row {k} - Real part")
        axs[k, 0].set_xlabel("n")
        axs[k, 0].set_ylabel("Real")
        axs[k, 0].set_ylim(-1.2, 1.2)
        axs[k, 0].grid(True)

        axs[k, 1].stem(n, F[k].imag)
        axs[k, 1].set_title(f"Row {k} - Imaginary part")
        axs[k, 1].set_xlabel("n")
        axs[k, 1].set_ylabel("Imaginary")
        axs[k, 1].set_ylim(-1.2, 1.2)
        axs[k, 1].grid(True)

    plt.tight_layout()
    plt.savefig("ex_1.pdf", bbox_inches="tight")
    plt.show()


def ex_1():
    N = 8

    F = generate_fourier_matrix(N)

    product = F.conj().T @ F
    expected = N * np.eye(N)


    print("Fourier matrix:")
    print(np.round(F, 4))

    print("\nF^H * F:")
    print(np.round(product, 4))

    print("\nOrthogonality:", np.allclose(product, expected))
    print("Error:", np.linalg.norm(product - expected))

    plot_fourier_matrix(F)


if __name__ == "__main__":
    ex_1()
