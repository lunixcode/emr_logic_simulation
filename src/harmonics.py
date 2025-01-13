# Utility functions for wave generation and analysisimport numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

# Time and frequency settings
time = np.linspace(0, 1, 1000)  # 1 second, sampled at 1 kHz
frequency_optical = 100  # Optical wave frequency (Hz)
frequency_microwave = 10  # Microwave modulation frequency (Hz)
amplitude = 1  # Base amplitude
chi_2 = 0.5  # Second-order susceptibility
chi_3 = 0.2  # Third-order susceptibility

# Generate optical wave
optical_wave = amplitude * np.sin(2 * np.pi * frequency_optical * time)

# Microwave modulation
microwave = np.sin(2 * np.pi * frequency_microwave * time)
modulated_wave = optical_wave * (1 + 0.1 * microwave)

# Nonlinear effects
second_harmonic = chi_2 * modulated_wave**2
third_harmonic = chi_3 * modulated_wave**3

# Combine waves
output_wave = modulated_wave + second_harmonic + third_harmonic

# Perform FFT to analyze frequency spectrum
fft_output = np.abs(fft(output_wave))
frequencies = fftfreq(len(time), time[1] - time[0])

# Plot results
plt.figure(figsize=(12, 8))

# Time-domain signals
plt.subplot(3, 1, 1)
plt.plot(time, modulated_wave, label='Modulated Wave')
plt.legend()
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(time, second_harmonic, label='Second Harmonic (2f)', color='orange')
plt.plot(time, third_harmonic, label='Third Harmonic (3f)', color='green')
plt.legend()
plt.grid()

# Frequency-domain analysis
plt.subplot(3, 1, 3)
plt.plot(frequencies[:len(frequencies)//2], fft_output[:len(frequencies)//2], label='Frequency Spectrum')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
