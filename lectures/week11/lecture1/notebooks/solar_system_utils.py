"""
Solar System Visualization Module
Provides functions to visualize and animate a solar system using turtle graphics.
"""

import math
import time
import random
from utils import Turtle, Drawing, Path, Point as TPoint


def _draw_dot(t, x, y, size, color):
    """Draw a filled circle at (x, y) with given diameter and color."""
    t.pen_color = color
    t.pen_width = size
    t.jump_to(x, y)
    t.move_to(x + 0.5, y)


def _draw_circle(t, cx, cy, radius, color, width=1, steps=60):
    """Draw a circle outline centered at (cx, cy)."""
    t.pen_color = color
    t.pen_width = width
    for i in range(steps + 1):
        a = 2 * math.pi * i / steps
        px = cx + radius * math.cos(a)
        py = cy + radius * math.sin(a)
        if i == 0:
            t.jump_to(px, py)
        else:
            t.move_to(px, py)


def _draw_ellipse(t, cx, cy, rx, ry, color, width=2, steps=40):
    """Draw an ellipse outline centered at (cx, cy)."""
    t.pen_color = color
    t.pen_width = width
    for i in range(steps + 1):
        a = 2 * math.pi * i / steps
        px = cx + rx * math.cos(a)
        py = cy + ry * math.sin(a)
        if i == 0:
            t.jump_to(px, py)
        else:
            t.move_to(px, py)


def _generate_stars(count=80, seed=42, canvas_size=550):
    """Generate random star positions and properties."""
    rng = random.Random(seed)
    stars = []
    for _ in range(count):
        x = rng.randint(10, canvas_size - 10)
        y = rng.randint(10, canvas_size - 10)
        size = rng.choice([1, 1, 1, 2, 2, 3])
        b = rng.randint(150, 255)
        color = '#{0:02x}{0:02x}{0:02x}'.format(b)
        stars.append((x, y, size, color))
    return stars


def _draw_scene(t, solar_system, stars, cx, cy, frame=0, animated=False):
    """Draw the complete solar system scene for one frame."""

    # Stars
    for x, y, size, color in stars:
        _draw_dot(t, x, y, size, color)

    # Sun with glow effect (layered circles)
    if animated:
        pulse = 30 + 3 * math.sin(frame * 0.15)
    else:
        pulse = 30
    _draw_dot(t, cx, cy, pulse + 20, '#1A1000')
    _draw_dot(t, cx, cy, pulse + 10, '#332200')
    _draw_dot(t, cx, cy, pulse, '#FFD700')

    # Draw each planet
    for planet in solar_system.planets:

        # Orbit path (thin ring)
        _draw_circle(t, cx, cy, planet.distance, '#1A1A3A', width=1, steps=50)

        # Compute planet position on orbit
        if animated:
            # Closer planets orbit faster (simplified Kepler's laws)
            speed = 100 / (planet.distance ** 0.8)
            angle = planet.angle + frame * speed
        else:
            angle = planet.angle

        angle_rad = math.radians(angle)
        px = cx + planet.distance * math.cos(angle_rad)
        py = cy + planet.distance * math.sin(angle_rad)

        # Draw the planet
        _draw_dot(t, px, py, planet.radius * 2, planet.color)

        # Saturn gets rings (ellipse around the planet)
        if planet.name.lower() == 'saturn':
            _draw_ellipse(t, px, py,
                          planet.radius * 2.5, planet.radius * 0.8,
                          '#C8A84E', width=2, steps=40)


def visualize(solar_system):
    """
    (SolarSystem) -> None
    Draw a static visualization of the solar system.
    """
    size = 550
    drawing = Drawing(width=size, height=size, bgcolor='#0B0B2B')
    t = Turtle(animate=False, drawing=drawing)
    t.paths = []
    cx, cy = size // 2, size // 2
    stars = _generate_stars(count=80, seed=42)

    _draw_scene(t, solar_system, stars, cx, cy)

    t.hide()
    t.draw()


def animate(solar_system, frames=150, dt=0.05):
    """
    (SolarSystem, int, float) -> None
    Animate the solar system with planets orbiting the sun.
    Closer planets orbit faster (simplified Kepler's laws).
    frames: number of animation frames.
    dt: seconds between frames.
    """
    size = 550
    drawing = Drawing(width=size, height=size, bgcolor='#0B0B2B')
    t = Turtle(animate=False, drawing=drawing)
    t.paths = []
    cx, cy = size // 2, size // 2
    stars = _generate_stars()

    for frame in range(frames):
        # Clear previous frame
        t.paths = []

        # Draw everything at current frame
        _draw_scene(t, solar_system, stars, cx, cy, frame=frame, animated=True)

        t.hide()
        t.draw()
        time.sleep(dt)
