from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np


def plot_boxes(
    widths,
    strengths,
    y_start: 10,
    height: int = 1,
    center: int = 0,
    ax=None,
    equal_length=False,
    scale=None,
    scale_y=1,
    scale_x=1,
    uni_color="C1",
    colors: list = [],
    align_boxes: str = "center",
    ensure_square=True,
):
    if scale is not None:
        scale_x = scale
        scale_y = scale
    if ensure_square:
        scale_x = scale_y
    if not ax:
        fig, ax = plt.subplots(figsize=(5, 5))

    if equal_length:
        widths = [1 for i in range(len(strengths))]

    if align_boxes == "center":
        start = center - np.sum(widths) * 1 / 2
    if align_boxes == "left":
        start = 0

    for i, (width, strength) in enumerate(zip(widths, strengths)):
        c = uni_color if not colors else colors[i]
        ax.add_patch(
            Rectangle(
                (start, y_start - height),
                width * scale_x,
                height * scale_y,
                facecolor=c,
                alpha=strength,
            )
        )
        # opaque border
        ax.add_patch(
            Rectangle(
                (start, y_start - height),
                width * scale_x,
                height * scale_y,
                fill=False,
                edgecolor="black",
                linewidth=0.3,
            )
        )
        if ensure_square:
            start += width * scale_y
        else:
            start += width * scale_y
