from __future__ import annotations
import os.path, os, time, numpy as np, scipy.io.wavfile as wavfile
from multiprocessing import Pool

def gen_fake_data(filenames):
    print('generating fake data')
    try: os.mkdir('sounds')
    except FileExistsError: pass
    for filename in filenames:
        if not os.path.exists(filename):
            print(f'creating {filename}')
            gen_wave_file(filename, frequency=440, duration=240)
def gen_wave_file(filename: str, frequency: int, duration: int):
    samplerate = 44100
    t = np.linspace(0, duration, duration * samplerate)
    data = np.sin(2 * np.pi * frequency * t)
    scipy.io.wavfile.write(filename, samplerate, data.astype(np.float32))
def etl(filename: str) -> tuple[str, float]:
    start_t = time.perf_counter()
    samplerate, data = scipy.io.wavfile.read(filename)
    
