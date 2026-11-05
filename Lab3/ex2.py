
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.animation import FuncAnimation, PillowWriter


def generate_signal(t, f):
    return np.cos(2 * np.pi * f * t)


def wrap_signal(t, x, f):
    return x * np.exp(-2j * np.pi * f * t)


def plot_line(ax, x, y, colors):
    points = np.column_stack((x, y))
    segments = np.stack((points[:-1], points[1:]), axis=1)

    line = LineCollection(segments, cmap="viridis", linewidth=2)
    line.set_array((colors[:-1] + colors[1:]) / 2)
    line.set_clim(0, 1)
    ax.add_collection(line)

    return line, segments


def plot_complex(ax, z, x, title):
    line, segments = plot_line(ax, z.real, z.imag, np.abs(x))
    ax.set_title(title)
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect("equal")
    ax.grid(True)

    return line, segments


def make_figure(t, x, frequencies, filename, animate=False):
    if len(frequencies) == 1:
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))
        line, segments = plot_line(axs[0], t, x, np.abs(x))
        axs[0].set_title("Original signal - 6 Hz")
        axs[0].set_xlabel("Time (s)")
        axs[0].set_ylabel("Amplitude")
        axs[0].set_xlim(t[0], t[-1])
        axs[0].set_ylim(-1.2, 1.2)
        axs[0].grid(True)

        lines = [line]
        all_segments = [segments]
        data = [(t, x)]
        axes = [axs[1]]
    else:
        fig, axs = plt.subplots(2, 2, figsize=(10, 9))
        lines = []
        all_segments = []
        data = []
        axes = axs.flat

    for ax, f in zip(axes, frequencies):
        z = wrap_signal(t, x, f)
        line, segments = plot_complex(ax, z, x, f"Wrapping frequency = {f} Hz")

        lines.append(line)
        all_segments.append(segments)
        data.append((z.real, z.imag))

    fig.colorbar(lines[-1], ax=axs.ravel(), label="Distance from origin", shrink=0.8)

    if not animate:
        fig.savefig(filename + ".pdf", bbox_inches="tight")
        return None

    markers = []
    for ax in axs.flat:
        marker, = ax.plot([], [], "ro")
        markers.append(marker)

    for line in lines:
        line.set_segments([])

    def update(frame):
        i = min(frame * 5, len(t) - 1)

        for line, segments, marker, (a, b) in zip(lines, all_segments, markers, data):
            line.set_segments(segments[:i])
            marker.set_data([a[i]], [b[i]])

    anim = FuncAnimation(
        fig, update,
        frames=(len(t) - 1) // 5 + 2,
        interval=40,
        repeat=False
    )

    anim.save(filename + ".gif", writer=PillowWriter(fps=25))
    return anim


def ex_2():
    fs = 1000
    t = np.arange(fs) / fs
    x = generate_signal(t, 6)

    make_figure(t, x, [1], "ex_2_fig1")
    make_figure(t, x, [1, 3, 6, 9], "ex_2_fig2")

    anim1 = make_figure(t, x, [1], "ex_2_fig1", True)
    anim2 = make_figure(t, x, [1, 3, 6, 9], "ex_2_fig2", True)

    plt.show()


if __name__ == "__main__":
    ex_2()
