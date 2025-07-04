# Kokoro TTS - Guia de Uso

Este repositório contém uma guia criado pela Asimov Academy do **Kokoro TTS**, um modelo de síntese de fala leve e eficiente com 82 milhões de parâmetros.

## 🚀 Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/asimov-academy/Kokoro-TTS---Guia-de-uso
cd Kokoro-TTS---Guia-de-uso
```

### 2. Pré-requisitos

1. **Instalar uv** (gerenciador de pacotes Python):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Instalar espeak-ng** (necessário para síntese de fala):

**Linux:**
```bash
apt-get -qq -y install espeak-ng
```

**Windows:**
- Vá para [espeak-ng releases](https://github.com/espeak-ng/espeak-ng/releases)
- Clique em "Latest release"
- Baixe o arquivo *.msi apropriado (ex: espeak-ng-20191129-b702b03-x64.msi)
- Execute o instalador baixado

### 3. Instalar dependências do projeto
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


## 🛠️ Dependências
- `kokoro>=0.9.4` - Modelo TTS
- `soundfile>=0.13.1` - Manipulação de arquivos de áudio
- `pyaudio>=0.2.11` - Streaming de áudio
- `numpy>=1.24.0` - Processamento de arrays
- `torch` - Framework de deep learning


## 🎯 Casos de Uso

- **Aplicações de TTS** - Conversão de texto para fala
- **Assistentes virtuais** - Interface de voz
- **Acessibilidade** - Leitura de texto para deficientes visuais
- **Educação** - Ferramentas de aprendizado
- **Streaming** - Reprodução em tempo real



## 🔗 Links Úteis

- [Kokoro TTS no Hugging Face](https://huggingface.co/hexgrad/Kokoro-82M)
- [Lista completa de vozes](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md)
- [Documentação do Kokoro](https://github.com/hexgrad/Kokoro)
