import matplotlib.pyplot as plt


def plot_legend(
    mapping, item_spacing=0.5, marker_size=100, labels_dict={}, font_size=12
):
    num_items = len(mapping)
    fig_height = item_spacing * num_items

    fig, ax = plt.subplots(figsize=(2.5, fig_height))  # Width fixed, height dynamic
    ax.axis("off")

    for i, (label, color) in enumerate(mapping.items()):
        y = fig_height - (i + 0.5) * item_spacing
        ax.scatter(0, y, color=color, s=marker_size)
        ax.text(
            0.2,
            y,
            labels_dict.get(label, label),
            fontsize=font_size,
            va="center",
            ha="left",
        )

    ax.set_xlim(-0.2, 2)
    ax.set_ylim(0, fig_height)
    ax.set_aspect("auto")
    plt.tight_layout()
