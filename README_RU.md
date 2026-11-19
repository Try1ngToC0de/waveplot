# waveplot

**waveplot** — это легковесная библиотека на Python без внешних зависимостей для генерации звуковых волн и упаковки их в WAV-файлы. она была создана с нуля в образовательных целях для низкоуровневого синтеза звука.

## возможности
*   **генерация волн:** создание базовых волноформ (синусоида, прямоугольная, треугольная, пила).
*   **поддержка стерео/моно:** генерация моно-звука или панорамирование (влево, вправо, в оба канала) для стерео.
*   **низкоуровневая упаковка:** ручная упаковка битовой глубины (8, 16, 24 и 32-bit float) с помощью модуля `struct`.
*   **сборщик WAV-заголовков:** генерация валидных заголовков WAV для легкого сохранения звука в файл.

## установка
так как библиотеки пока нет на PyPI, вы можете склонировать репозиторий и установить её локально:

```bash
git clone https://github.com/Try1ngToC0de/waveplot.git
cd waveplot
pip install -e .
```

## быстрый старт

вот пример того, как сгенерировать 2-секундную синусоиду частотой 440Гц (A4) и сохранить её в WAV-файл:

```python
import struct
from waveplot import plot_sine, byte_master, wav_header

# 1. генерируем аудио-сэмплы (моно, 44100Гц, амплитуда 0.5, 2 секунды)
samples = plot_sine(freq=440.0, samplerate=44100, amp=0.5, duration=2.0)

# 2. упаковываем сэмплы в байты (16-битная глубина)
audio_data = byte_master(samples, bit_depth=16)

# 3. создаем WAV-заголовок
header = wav_header(payload_size=len(audio_data), samplerate=44100, bit_depth=16, num_channels=1)

# 4. сохраняем в файл
with open("test_sine.wav", "wb") as f:
    f.write(header)
    f.write(audio_data)

print("Файл test_sine.wav создан!")
```

## описание API

### `plot_square(freq, samplerate, amp, duration, num_channels=1, position="both")`
### `plot_sine(...)`
### `plot_triangle(...)`
### `plot_sawtooth(...)`
генерирует волноформу и возвращает список float-сэмплов.

### `byte_master(samples, bit_depth)`
конвертирует список float-сэмплов (от -1.0 до 1.0) в `bytearray`. поддерживает 8, 16, 24 и 32-бит float.

### `wav_header(payload_size, samplerate, bit_depth, num_channels)`
возвращает упакованный объект `bytes` с заголовком RIFF/WAVE.

## лицензия
MIT
