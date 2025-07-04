# Kokoro TTS - Guia de Uso

Este repositório contém scripts de demonstração para o **Kokoro TTS**, um modelo de síntese de fala leve e eficiente com 82 milhões de parâmetros.

## 🚀 Instalação

```bash
uv sync
```

## 📁 Scripts Disponíveis

### 1. kokoro_basic.py

Script básico para gerar arquivos de áudio usando o Kokoro TTS.

**Funcionalidades:**
- Gera áudio a partir de texto
- Salva arquivo .wav único
- Demonstra diferentes idiomas e vozes

**Como usar:**
```bash
python kokoro_basic.py
```

**Saída:**
- `audio_completo.wav` - Arquivo de áudio com todo o texto

### 2. kokoro_stream.py

Script de streaming em tempo real usando pyaudio.

**Funcionalidades:**
- Reprodução de áudio em tempo real
- Geração e reprodução sequencial
- Demonstração simples de streaming

**Como usar:**
```bash
python kokoro_stream.py
```

## 🌍 Idiomas Suportados (lang_code)

```python
# 🇺🇸 'a' => American English
# 🇬🇧 'b' => British English  
# 🇪🇸 'e' => Spanish es
# 🇫🇷 'f' => French fr-fr
# 🇮🇳 'h' => Hindi hi
# 🇮🇹 'i' => Italian it
# 🇯🇵 'j' => Japanese (pip install misaki[ja])
# 🇧🇷 'p' => Brazilian Portuguese pt-br
# 🇨🇳 'z' => Mandarin Chinese (pip install misaki[zh])
```

## 🎤 Vozes Disponíveis

Você pode conferir todas as vozes disponíveis aqui:
**https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md**

### Exemplos de Vozes:
- `af_heart` - Voz feminina padrão
- `af_heart_2` - Segunda variação feminina
- `af_heart_3` - Terceira variação feminina
- `pm_santa` - Voz masculina
- `pf_dora` - Voz feminina brasileira

## 💻 Exemplos de Uso

### Geração básica de áudio
```python
from kokoro import KPipeline
import soundfile as sf
import numpy as np

pipeline = KPipeline(lang_code='p')
generator = pipeline("Olá mundo!", voice='pf_dora')

audio_chunks = []
for gs, ps, audio in generator:
    audio_chunks.append(audio)

if audio_chunks:
    audio_completo = np.concatenate(audio_chunks)
    sf.write('saida.wav', audio_completo, 24000)
```

### Streaming em tempo real
```python
from kokoro_stream import stream_kokoro_local

# O script já está configurado para streaming
# Basta executar: python kokoro_stream.py
```

## 🔧 Configuração dos Scripts

### kokoro_basic.py
```python
# Configurar idioma
lang_code = 'p'  # Português brasileiro

# Configurar voz
voice = 'pf_dora'  # Voz feminina brasileira

# Texto para converter
text = '''
Seu texto aqui...
'''
```

### kokoro_stream.py
```python
# Configurar idioma
pipeline = KPipeline(lang_code='p')

# Configurar voz
generator = pipeline(texto, voice='pm_santa')

# Texto para streaming
texto = "Seu texto para streaming..."
```

## 📊 Especificações Técnicas

- **Sample Rate:** 24000 Hz
- **Formato:** Float32
- **Canais:** Mono (1 canal)
- **Modelo:** Kokoro 82M (82 milhões de parâmetros)
- **Licença:** Apache

## 🛠️ Dependências

- `kokoro>=0.9.4` - Modelo TTS
- `soundfile>=0.13.1` - Manipulação de arquivos de áudio
- `pyaudio>=0.2.11` - Streaming de áudio
- `numpy>=1.24.0` - Processamento de arrays
- `torch` - Framework de deep learning

## 🔍 Troubleshooting

### Problemas com pyaudio no macOS
```bash
brew install portaudio
pip install pyaudio
```

### Problemas com pyaudio no Ubuntu
```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

### Problemas com idiomas específicos
Para japonês:
```bash
pip install misaki[ja]
```

Para chinês:
```bash
pip install misaki[zh]
```

## 📝 Estrutura do Projeto

```
Kokoro TTS/
├── kokoro_basic.py      # Geração básica de áudio
├── kokoro_stream.py     # Streaming em tempo real
├── pyproject.toml       # Dependências do projeto
└── README.md           # Este arquivo
```

## 🎯 Casos de Uso

- **Aplicações de TTS** - Conversão de texto para fala
- **Assistentes virtuais** - Interface de voz
- **Acessibilidade** - Leitura de texto para deficientes visuais
- **Educação** - Ferramentas de aprendizado
- **Streaming** - Reprodução em tempo real

## 📄 Licença

Este projeto segue a licença Apache do Kokoro TTS.

## 🔗 Links Úteis

- [Kokoro TTS no Hugging Face](https://huggingface.co/hexgrad/Kokoro-82M)
- [Lista completa de vozes](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md)
- [Documentação do Kokoro](https://github.com/hexgrad/Kokoro)
