import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Set up the time axis (1 second, sampled at 1 kHz)
time = np.linspace(0, 1, 1000)

# Default wave parameters
frequency_1 = 10  # Hz
frequency_2 = 15  # Hz
amplitude_1 = 1   # Units
amplitude_2 = 0.8 # Units
phase_1 = 0       # Radians
phase_2 = 0       # Radians

# Generate initial waves
wave_1 = amplitude_1 * np.sin(2 * np.pi * frequency_1 * time + phase_1)
wave_2 = amplitude_2 * np.sin(2 * np.pi * frequency_2 * time + phase_2)
interference = wave_1 + wave_2

# Set up the figure and axes
fig, ax = plt.subplots(3, 1, figsize=(10, 8))
plt.subplots_adjust(left=0.1, bottom=0.35)

# Plot initial waves and interference
line1, = ax[0].plot(time, wave_1, label='Wave 1', color='blue')
line2, = ax[1].plot(time, wave_2, label='Wave 2', color='green')
line3, = ax[2].plot(time, interference, label='Interference', color='red')

# Set labels and grids
for i in range(3):
    ax[i].legend()
    ax[i].grid()

# Add sliders for dynamic control
ax_freq1 = plt.axes([0.1, 0.2, 0.65, 0.03])
ax_amp1 = plt.axes([0.1, 0.15, 0.65, 0.03])
ax_phase1 = plt.axes([0.1, 0.1, 0.65, 0.03])

ax_freq2 = plt.axes([0.1, 0.05, 0.65, 0.03])
ax_amp2 = plt.axes([0.1, 0.0, 0.65, 0.03])

slider_freq1 = Slider(ax_freq1, 'Freq 1', 1, 50, valinit=frequency_1)
slider_amp1 = Slider(ax_amp1, 'Amp 1', 0.1, 2.0, valinit=amplitude_1)
slider_phase1 = Slider(ax_phase1, 'Phase 1', -np.pi, np.pi, valinit=phase_1)

slider_freq2 = Slider(ax_freq2, 'Freq 2', 1, 50, valinit=frequency_2)
slider_amp2 = Slider(ax_amp2, 'Amp 2', 0.1, 2.0, valinit=amplitude_2)

# Update function for sliders
def update(val):
    global frequency_1, amplitude_1, phase_1, frequency_2, amplitude_2
    frequency_1 = slider_freq1.val
    amplitude_1 = slider_amp1.val
    phase_1 = slider_phase1.val
    frequency_2 = slider_freq2.val
    amplitude_2 = slider_amp2.val

    wave_1 = amplitude_1 * np.sin(2 * np.pi * frequency_1 * time + phase_1)
    wave_2 = amplitude_2 * np.sin(2 * np.pi * frequency_2 * time + phase_2)
    interference = wave_1 + wave_2

    line1.set_ydata(wave_1)
    line2.set_ydata(wave_2)
    line3.set_ydata(interference)

    fig.canvas.draw_idle()

# Connect sliders to update function
slider_freq1.on_changed(update)
slider_amp1.on_changed(update)
slider_phase1.on_changed(update)
slider_freq2.on_changed(update)
slider_amp2.on_changed(update)

plt.show()
