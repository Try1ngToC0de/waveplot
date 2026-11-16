# waveplot

**waveplot** is a lightweight, dependency-free Python library for generating audio waveforms and packing them into WAV files. It was created from scratch for educational purposes and low-level audio synthesis.

## features
*   **waveform generation:** Create basic waveforms (Sine, Square, Triangle, Sawtooth).
*   **stereo/mono support:** Generate mono audio or apply panning (left, right, both) for stereo.
*   **low-level packing:** Manual bit-depth packing (8, 16, 24, and 32-bit float) using Python's `struct` module.
*   **WAV header builder:** Generate valid WAV headers to easily save your audio to a file.

## installation
since the library is not on PyPI yet, you can clone the repository and install it locally:

```bash
git clone https://github.com/Try1ngToC0de/waveplot.git
cd waveplot
pip install -e .
```

## quick start

here is an example of how to generate a 2-second 440Hz (A4) sine wave and save it as a WAV file:

```python
import struct
from kid_synth import plot_sine, byte_master, wav_header

# 1. generate audio samples (mono, 44100Hz, 0.5 amplitude, 2 seconds)
samples = plot_sine(freq=440.0, samplerate=44100, amp=0.5, duration=2.0)

# 2. pack samples into bytes (16-bit depth)
audio_data = byte_master(samples, bit_depth=16)

# 3. create WAV header
header = wav_header(payload_size=len(audio_data), samplerate=44100, bit_depth=16, num_channels=1)

# 4. save to file
with open("test_sine.wav", "wb") as f:
    f.write(header)
    f.write(audio_data)

print("File test_sine.wav created!")
```

## API reference

### `plot_square(freq, samplerate, amp, duration, num_channels=1, position="both")`
### `plot_sine(...)`
### `plot_triangle(...)`
### `plot_sawtooth(...)`
generates a waveform and returns a list of float samples.

### `byte_master(samples, bit_depth)`
converts a list of float samples (-1.0 to 1.0) into a `bytearray`. Supports 8, 16, 24, and 32-bit float.

### `wav_header(payload_size, samplerate, bit_depth, num_channels)`
returns a packed `bytes` object with the RIFF/WAVE header.

## license
MIT
