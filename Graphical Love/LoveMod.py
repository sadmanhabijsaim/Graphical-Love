import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

t = np.linspace(0, 2 * np.pi, 300)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

heart = ax.fill(x, y, color='red', alpha=0.6)[0]

crack_x = [0, -1, 1, -1.5, 1.5, -2, 2, -2.5, 2.5, 0]
crack_y = np.linspace(10, -12, len(crack_x))
crack_line, = ax.plot([], [], color='white', linewidth=2)

text = ax.text(0, 0, "LOVE ❤️", color='white',
               fontsize=24, fontweight='bold',
               ha='center', va='center', alpha=1)

n_particles = 100
particles = ax.scatter([], [], s=[], c='orange', alpha=0.8)

rng = np.random.default_rng(42)
angles = rng.uniform(0, 2*np.pi, n_particles)
speeds = rng.uniform(1, 3, n_particles)
dx = np.cos(angles) * speeds
dy = np.sin(angles) * speeds

ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')
ax.axis('off')

def init():
    crack_line.set_data([], [])
    heart.set_visible(True)
    particles.set_offsets(np.empty((0, 2)))
    particles.set_sizes([])
    text.set_alpha(1)
    return heart, crack_line, particles, text

def animate(i):
    if i < 30:
        crack_line.set_data(crack_x[:i], crack_y[:i])
    elif i == 30:
        heart.set_visible(False)
        crack_line.set_visible(False)
        text.set_alpha(0)
    elif i > 30:
        step = i - 30
        px = dx * step
        py = dy * step
        offsets = np.column_stack([px, py])
        sizes = rng.uniform(20, 80, n_particles)
        particles.set_offsets(offsets)
        particles.set_sizes(sizes)

    return heart, crack_line, particles, text

ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=70, interval=40, blit=False, repeat=False
)


plt.show()
