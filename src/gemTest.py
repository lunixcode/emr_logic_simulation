import numpy as np
import matplotlib.pyplot as plt

def and_gate(wave1, wave2):
    """Simulates an AND gate using wave multiplication."""
    output_wave = wave1 * wave2
    return output_wave

def or_gate(wave1, wave2):
    """Simulates an OR gate using wave addition and clipping."""
    output_wave = np.clip(wave1 + wave2, -1, 1)  # Clip to [-1, 1]
    return output_wave

def not_gate(wave):
    """Simulates a NOT gate by inverting the phase."""
    output_wave = -wave
    return output_wave

if __name__ == "__main__":
    time = np.linspace(0, 1, 1000)
    freq = 5  # Reduced frequency for clearer visualization
    amplitude = 1

    # Input waves
    wave_high = amplitude * np.sin(2 * np.pi * freq * time)  # Logic 1
    wave_low = np.zeros_like(time)  # Logic 0

    # Test cases
    test_cases = [
        {"inputs": (wave_high, wave_high), "gate": and_gate, "label": "AND (1,1)"},
        {"inputs": (wave_high, wave_low), "gate": and_gate, "label": "AND (1,0)"},
        {"inputs": (wave_low, wave_high), "gate": and_gate, "label": "AND (0,1)"},
        {"inputs": (wave_low, wave_low), "gate": and_gate, "label": "AND (0,0)"},
        {"inputs": (wave_high, wave_high), "gate": or_gate, "label": "OR (1,1)"},
        {"inputs": (wave_high, wave_low), "gate": or_gate, "label": "OR (1,0)"},
        {"inputs": (wave_low, wave_high), "gate": or_gate, "label": "OR (0,1)"},
        {"inputs": (wave_low, wave_low), "gate": or_gate, "label": "OR (0,0)"},
        {"inputs": (wave_high,), "gate": not_gate, "label": "NOT (1)"},
        {"inputs": (wave_low,), "gate": not_gate, "label": "NOT (0)"},
    ]

    plt.figure(figsize=(15, 12))  # Increased figure size

    for i, test in enumerate(test_cases):
        inputs = test["inputs"]
        gate = test["gate"]
        label = test["label"]
        
        if len(inputs) == 2:
            output_wave = gate(inputs[0], inputs[1])
        else:
            output_wave = gate(inputs[0])
        
        plt.subplot(4, 3, i + 1)  # Adjusted subplot grid
        for j, input_wave in enumerate(inputs):
            plt.plot(time, input_wave, label=f"Input {j+1}")
        plt.plot(time, output_wave, label=f"{label} Output", linewidth=2) # increased linewidth
        plt.title(label)
        plt.legend()
        plt.grid(True)
        plt.ylim(-1.2, 1.2) # set consistent y axis

    plt.tight_layout()
    plt.show()