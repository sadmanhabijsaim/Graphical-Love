import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patheffects as pe

plt.style.use('dark_background')

t = np.linspace(0, 2 * np.pi, 200)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

poly = ax.fill(x, y, color=(1.0, 0.08, 0.3, 0.18))[0]

line, = ax.plot([], [], color=(1.0, 0.2, 0.4), linewidth=3, solid_capstyle='round')
line.set_path_effects([
    pe.Stroke(linewidth=8, foreground='magenta', alpha=0.15),
    pe.Stroke(linewidth=4, foreground='red', alpha=0.5),
    pe.Normal()
])

spark = ax.scatter([], [], s=[], c=[], cmap='autumn', edgecolors='none')

custom_text = "I❤️U DIU"
text_color = '#30808C'
text_obj = ax.text(0, 0, custom_text, color=text_color,
                   fontsize=20, fontweight='bold',
                   ha='center', va='center')

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')
ax.axis('off')

rng = np.random.default_rng(42)

def init():
    line.set_data([], [])
    poly.set_alpha(0.18)
    spark.set_offsets(np.empty((0, 2)))
    spark.set_sizes([])
    spark.set_array(np.array([]))
    return line, poly, spark, text_obj

def animate(i):
    if i < 1:
        return line, poly, spark, text_obj

    line.set_data(x[:i], y[:i])

    alpha = 0.12 + 0.12 * (0.5 + 0.5 * np.sin(2 * np.pi * i / len(t)))
    poly.set_alpha(alpha)

    n = min(12, max(1, i // 5))
    base_x, base_y = x[i % len(x)], y[i % len(y)]
    offsets = np.column_stack([
        base_x + 0.6 * rng.normal(0, 1, size=n),
        base_y + 0.6 * rng.normal(0, 1, size=n)
    ])
    sizes = (rng.random(n) * 80 + 20) * (0.6 + 0.4 * np.sin(i / 6.0))
    colors = (np.linspace(0, 1, n) + rng.random(n) * 0.2)

    spark.set_offsets(offsets)
    spark.set_sizes(sizes)
    spark.set_array(colors)

    return line, poly, spark, text_obj

ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=len(t), interval=40, blit=False, repeat=True
)


plt.show()
