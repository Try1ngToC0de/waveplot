# by Try1ngToC0de
# made in Russia with love

import math as m
import struct

def _apply_pan(samples, num_channels, position):
    if num_channels == 1:
        return samples
    elif num_channels == 2:
        stereo = []
        if position == "both":
            for s in samples:
                stereo.extend([s, s])
        elif position == "left":
            for s in samples:
                stereo.extend([s, 0.0])
        elif position == "right":
            for s in samples:
                stereo.extend([0.0, s])
        else:
            raise ValueError(f"Invalid position: {position}. Use 'left', 'right', or 'both'.")
        return stereo
    else:
        raise ValueError(f"Invalid num_channels: {num_channels}. Use 1 or 2.")

def plot_square(freq, samplerate, amp, duration, num_channels=1, position="both"):
    samplecount = int(round(duration * samplerate))
    samples = []
    for i in range(samplecount):
        sine_val = m.sin(2 * m.pi * freq * (i / samplerate))
        samples.append(amp if sine_val >= 0 else -amp)
    return _apply_pan(samples, num_channels, position)

def plot_sine(freq, samplerate, amp, duration, num_channels=1, position="both"):
    samplecount = int(round(duration * samplerate))
    samples = []
    for i in range(samplecount):
        samples.append(amp * m.sin(2 * m.pi * freq * (i / samplerate)))
    return _apply_pan(samples, num_channels, position)

def plot_triangle(freq, samplerate, amp, duration, num_channels=1, position="both"):
    samplecount = int(round(duration * samplerate))
    samples = []
    for i in range(samplecount):
        samples.append(amp * (2 / m.pi) * m.asin(m.sin(2 * m.pi * freq * (i / samplerate))))
    return _apply_pan(samples, num_channels, position)

def plot_sawtooth(freq, samplerate, amp, duration, num_channels=1, position="both"):
    samplecount = int(round(duration * samplerate))
    samples = []
    for i in range(samplecount):
        phase = (freq * (i / samplerate)) % 1.0
        samples.append(amp * (2.0 * phase - 1.0))
    return _apply_pan(samples, num_channels, position)

def byte_master(samples, bit_depth):
    data = bytearray()
    for sample in samples:
        sample = max(-1.0, min(1.0, sample))
        if bit_depth == 8:
            data.append(round((sample + 1) * 127.5))
        elif bit_depth == 16:
            data.extend(struct.pack('<h', round(sample * 32767)))
        elif bit_depth == 24:
            value = int(sample * 8388607)
            data.extend([value & 0xFF, (value >> 8) & 0xFF, (value >> 16) & 0xFF])
        elif bit_depth == 32:
            data.extend(struct.pack('<f', sample))
        else:
            raise ValueError("Available bit depth: 8/16/24/32")
    return data

def wav_header(payload_size, samplerate, bit_depth, num_channels):
    audio_format = 3 if bit_depth == 32 else 1
    block_align = num_channels * bit_depth // 8
    byte_rate = samplerate * block_align
    file_size = 36 + payload_size
    header = struct.pack(
        '<4sI4s4sIHHIIHH4sI',
        b'RIFF', file_size, b'WAVE',
        b'fmt ', 16, audio_format,
        num_channels, samplerate, byte_rate,
        block_align, bit_depth,
        b'data', payload_size
    )
    return header
