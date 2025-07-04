from kokoro import KPipeline
import pyaudio
import numpy as np
import soundfile as sf
import io

pipeline = KPipeline(lang_code='p')
pyaudio_instance = pyaudio.PyAudio()

def stream_kokoro_local():
    stream = pyaudio_instance.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=24000,
        output=True
    )
    
    print("Iniciando streaming do Kokoro local...")
    
    texto = "Olá! Esta é uma demonstração de streaming com Kokoro TTS."
    generator = pipeline(texto, voice='pm_santa')
    
    audio_chunks = []
    for gs, ps, audio in generator:
        audio_chunks.append(audio)
    
    if audio_chunks:
        audio_completo = np.concatenate(audio_chunks)
        print(f"Reproduzindo áudio: {len(audio_completo)} samples")
        stream.write(audio_completo.tobytes())
    
    stream.stop_stream()
    stream.close()
    pyaudio_instance.terminate()
    print("Streaming concluído!")

if __name__ == "__main__":
    stream_kokoro_local() 