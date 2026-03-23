"""
Rectangle Visualization Module
Provides a function to visualize a Rectangle object with grid lines,
axes, and axis tick labels using SVG.
"""

from IPython.display import display, HTML


def _nice_tick(data_range, target_ticks=8):
    """Return a nice tick spacing for the given data range."""
    rough = data_range / target_ticks
    nice_steps = [1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000]
    for step in nice_steps:
        if step >= rough:
            return step
    return rough


def visualize(rectangle):
    """
    (Rectangle) -> None
    Draw the rectangle on a coordinate plane with grid lines, axes,
    and tick labels so the size and position can be measured.
    """
    # Rectangle properties
    rx = rectangle.bottom_left_corner.x
    ry = rectangle.bottom_left_corner.y
    rw = rectangle.width
    rh = rectangle.height

    # Canvas size
    canvas_w = 1000
    canvas_h = 500

    # Margins for axis labels
    margin_left = 60
    margin_right = 30
    margin_top = 20
    margin_bottom = 40

    # Plot area
    plot_w = canvas_w - margin_left - margin_right
    plot_h = canvas_h - margin_top - margin_bottom

    # Axis ranges (auto-scale with padding)
    data_max_x = max(rx + rw, 10) * 1.15
    data_max_y = max(ry + rh, 10) * 1.15

    # Fixed grid spacing of 100
    tick_x = 100
    tick_y = 100
    axis_max_x = tick_x * ((int(data_max_x) // tick_x) + 1)
    axis_max_y = tick_y * ((int(data_max_y) // tick_y) + 1)

    # Scale: data coordinates -> canvas pixel coordinates
    def sx(data_x):
        return margin_left + (data_x / axis_max_x) * plot_w

    def sy(data_y):
        return canvas_h - margin_bottom - (data_y / axis_max_y) * plot_h

    # Start building SVG
    parts = []
    parts.append(f'<svg width="{canvas_w}" height="{canvas_h}" '
                 f'style="font-family: sans-serif; font-size: 12px;">')
    parts.append(f'<rect width="100%" height="100%" fill="#F3F3F7" />')

    # White plot background
    parts.append(f'<rect x="{margin_left}" y="{margin_top}" '
                 f'width="{plot_w}" height="{plot_h}" fill="white" />')

    # Grid lines and tick labels - X axis
    val = 0
    while val <= axis_max_x:
        px = sx(val)
        # Grid line
        parts.append(f'<line x1="{px:.1f}" y1="{margin_top}" '
                     f'x2="{px:.1f}" y2="{canvas_h - margin_bottom}" '
                     f'stroke="#DDDDDD" stroke-width="1" />')
        # Tick label
        parts.append(f'<text x="{px:.1f}" y="{canvas_h - margin_bottom + 20}" '
                     f'text-anchor="middle" fill="#555">{int(val)}</text>')
        val += tick_x

    # Grid lines and tick labels - Y axis
    val = 0
    while val <= axis_max_y:
        py = sy(val)
        # Grid line
        parts.append(f'<line x1="{margin_left}" y1="{py:.1f}" '
                     f'x2="{canvas_w - margin_right}" y2="{py:.1f}" '
                     f'stroke="#DDDDDD" stroke-width="1" />')
        # Tick label
        parts.append(f'<text x="{margin_left - 10}" y="{py + 4:.1f}" '
                     f'text-anchor="end" fill="#555">{int(val)}</text>')
        val += tick_y

    # Axes (x and y)
    # X axis (y=0)
    y0 = sy(0)
    parts.append(f'<line x1="{margin_left}" y1="{y0:.1f}" '
                 f'x2="{canvas_w - margin_right}" y2="{y0:.1f}" '
                 f'stroke="#333" stroke-width="2" />')
    # Y axis (x=0)
    x0 = sx(0)
    parts.append(f'<line x1="{x0:.1f}" y1="{margin_top}" '
                 f'x2="{x0:.1f}" y2="{canvas_h - margin_bottom}" '
                 f'stroke="#333" stroke-width="2" />')

    # Draw the rectangle
    rect_x1 = sx(rx)
    rect_y1 = sy(ry + rh)  # top-left in canvas coords
    rect_w = sx(rx + rw) - sx(rx)
    rect_h = sy(ry) - sy(ry + rh)

    # Fill
    parts.append(f'<rect x="{rect_x1:.1f}" y="{rect_y1:.1f}" '
                 f'width="{rect_w:.1f}" height="{rect_h:.1f}" '
                 f'fill="rgba(99, 132, 255, 0.25)" '
                 f'stroke="#4466CC" stroke-width="2.5" />')

    # Corner dots
    bl_cx, bl_cy = sx(rx), sy(ry)
    tr_cx, tr_cy = sx(rx + rw), sy(ry + rh)
    parts.append(f'<circle cx="{bl_cx:.1f}" cy="{bl_cy:.1f}" r="5" fill="#4466CC" />')
    parts.append(f'<circle cx="{tr_cx:.1f}" cy="{tr_cy:.1f}" r="5" fill="#4466CC" />')

    # Bottom-left corner label
    bl_label = f'({int(rx)}, {int(ry)})'
    parts.append(f'<text x="{bl_cx - 5:.1f}" y="{bl_cy + 18:.1f}" '
                 f'text-anchor="start" fill="#4466CC" font-size="13" '
                 f'font-weight="bold">{bl_label}</text>')

    # Top-right corner label
    tr_label = f'({int(rx + rw)}, {int(ry + rh)})'
    parts.append(f'<text x="{tr_cx + 8:.1f}" y="{tr_cy - 8:.1f}" '
                 f'text-anchor="start" fill="#4466CC" font-size="13" '
                 f'font-weight="bold">{tr_label}</text>')

    # Dimension labels
    # Width label (centered along top edge)
    mid_top_x = (rect_x1 + rect_x1 + rect_w) / 2
    parts.append(f'<text x="{mid_top_x:.1f}" y="{rect_y1 - 6:.1f}" '
                 f'text-anchor="middle" fill="#4466CC" font-size="13" '
                 f'font-weight="bold">w = {int(rw)}</text>')

    # Height label (centered along right edge)
    mid_right_y = (rect_y1 + rect_y1 + rect_h) / 2
    parts.append(f'<text x="{rect_x1 + rect_w + 8:.1f}" y="{mid_right_y + 4:.1f}" '
                 f'text-anchor="start" fill="#4466CC" font-size="13" '
                 f'font-weight="bold">h = {int(rh)}</text>')

    parts.append('</svg>')
    display(HTML('\n'.join(parts)))
