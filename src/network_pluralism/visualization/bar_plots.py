import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def show_perspectives_as_bars(
    perspectives: list[list],
    width=0.1,
    colors=["#A83131", "#233488", "green"],
    perspective_labels=[],
    x_labels=["a", "b", "c", "d", "e"],
    ax=None,
    fig_size=(5, 10),
    legend_in_extra_plot=True,
    rotation=0,
    layout="horizontal",
    legend=True,
    save_dir: Path = None,
    file_name: str = None,
):
    x = np.arange(len(perspectives[0]))

    num_of_perspectives = len(perspectives)

    if ax is None:
        fig, ax = plt.subplots(figsize=fig_size)

    gap = width / 1.5

    total_width = num_of_perspectives * width + (num_of_perspectives - 1) * gap

    start = -total_width / 2 + width / 2

    for i, p in enumerate(perspectives):
        offset = start + i * (width + gap)
        color = colors[i % len(colors)]
        if layout == "horizontal":
            ax.bar(
                x + offset,
                p,
                width,
                color=color,
                alpha=0.9,
                label=perspective_labels[i] if perspective_labels else "",
            )
        else:
            ax.barh(
                x + offset,
                p,
                width,
                color=color,
                alpha=0.9,
                label=perspective_labels[i] if perspective_labels else "",
            )

    plt.axhline(0, color="black", linewidth=1.5, linestyle="--")
    ax.tick_params("y", labelsize=30)

    if layout == "horizontal":
        ax.set_xticks(x, x_labels, rotation=rotation)

    else:
        ax.set_yticks(x, x_labels, rotation=rotation)
        ax.xaxis.tick_top()
        ax.spines["top"].set_visible(True)
        ax.spines["top"].set_position(("outward", 0))
        ax.spines["bottom"].set_visible(False)
        ax.xaxis.set_label_position("top")
    if legend:
        if legend_in_extra_plot:
            fig_legend, ax_legend = plt.subplots(figsize=(3, 1))
            fig_legend.legend(*ax.get_legend_handles_labels(), loc="center")
            ax_legend.axis("off")
            plt.tight_layout()
            plt.show()
        else:
            ax.legend()

    if (save_dir) and (file_name):
        file_name = file_name.replace(".pdf", "")
        fig.tight_layout()
        fig_legend.tight_layout()
        fig.savefig(save_dir / f"{file_name}.pdf", dpi=600)
        fig_legend.savefig(
            save_dir / f"{file_name}_legend.pdf", dpi=600, transparent=True
        )


def show_perspective_difference(
    perspectives: list[list],
    width=0.1,
    colors=["red", "blue", "green"],
    perspective_labels=["P1", "P2"],
    p_labels_align="left",
    x_labels=["a", "b", "c", "d", "e"],
    fig_size=(10, 5),
    legend_in_extra_plot=False,
    rotation=0,
    perspective_labels_offset=0,
):
    # make symmetric
    absolute_values = [abs(y) for y_list in perspectives for y in y_list]
    maximum_y_value = max(absolute_values)
    y_lim = maximum_y_value + maximum_y_value / 10

    x = np.arange(len(perspectives[0]))

    fig, ax = plt.subplots(figsize=fig_size)

    show_perspectives_as_bars(
        perspectives=perspectives,
        width=width,
        colors=colors,
        x_labels=x_labels,
        ax=ax,
        legend_in_extra_plot=legend_in_extra_plot,
        rotation=rotation,
    )
    ax.set_xticks(x, x_labels)
    ax.set_ylim(-y_lim, y_lim)
    ax.axhline(0, color="black", linewidth=1.5, linestyle="--")

    # Add labels to the top-right and bottom-right of the y-axis
    ax.text(
        (-0.15 if p_labels_align else 1.02) + perspective_labels_offset,
        1.05,
        perspective_labels[0],
        transform=ax.transAxes,
        va="bottom",
        ha="left",
    )
    ax.text(
        (-0.15 if p_labels_align else 1.02) + perspective_labels_offset,
        -0.1,
        perspective_labels[1],
        transform=ax.transAxes,
        va="top",
        ha="left",
    )
