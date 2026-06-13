# Hinglish Subtitle Generator

Generate Hinglish (Roman Hindi) subtitles automatically from Hindi videos using Faster Whisper.

## 🎥 Demo

https://github.com/user-attachments/assets/c20b1a2a-946a-45ce-822f-af76f5041b4e

---

## Features

- Automatic Hindi speech transcription
- Converts Hindi subtitles into Hinglish (Roman Hindi)
- Generates `.srt` subtitle files
- Word-level timestamps
- Adjustable words per caption
- Works offline after the initial model download

> **Note**
>
> This project is configured to run on **CPU by default** for maximum compatibility.
> If you have an NVIDIA GPU with CUDA installed, you can modify the script to use GPU acceleration for significantly faster transcription.

---

## Example

### Input Speech

```text
नमस्ते दोस्तों आज हम एक नया प्रोजेक्ट बनाएंगे
```

### Generated Subtitle

```text
namaste dosto aaj
ham ek naya
project banaenge
```

---

## Installation

### 1. Install Python

Download Python 3.10 or later:

https://www.python.org/downloads/

During installation, make sure:

- Add Python to PATH

Verify installation:

```bash
python --version
```

### 2. Clone Repository

```bash
git clone https://github.com/CaptainAdarshh/Hinglish-Subtitle-Generator.git

cd hinglish-subtitle-generator
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Optional: GPU Acceleration (NVIDIA)

For NVIDIA GPU acceleration instructions, see utilize_gpu.txt.

This project runs on CPU by default.

If you have an NVIDIA GPU and CUDA installed, you can enable GPU acceleration by changing:

```python
model = WhisperModel(
    "large-v3",
    device="cpu",
    compute_type="int8"
)
```

to:

```python
model = WhisperModel(
    "large-v3",
    device="cuda",
    compute_type="float16"
)
```

GPU acceleration can significantly reduce transcription time compared to CPU execution.

### Requirements

- NVIDIA GPU
- CUDA installed and working
- Compatible PyTorch/CUDA environment

---

## Project Structure

```text
hinglish-subtitle-generator/

├── caption_video.py
├── requirements.txt
├── README.md
├── LICENSE
└── reel.mp4
```

---

## Usage

Place your video file inside the project folder.

Run:

```bash
python caption_video.py your_video.mp4
```

Examples:

```bash
python caption_video.py reel.mp4

python caption_video.py podcast.mp4
```

The generated subtitle file will automatically use the same filename as the input video.

---

## First Run

Whisper Large-v3 will be downloaded automatically.

Requirements:

- Download size: ~3 GB
- Recommended free disk space: ~5 GB
- Internet connection required only for the first run

After the model is downloaded, the script can run offline.

---

## Output

After processing completes:

```text
reel.srt
```

will be generated automatically.

---

## Customize Subtitle Speed

Open `caption_video.py` and modify:

```python
WORDS_PER_CAPTION = 3
```

Examples:

```python
WORDS_PER_CAPTION = 1
```

Fast reel-style subtitles.

```python
WORDS_PER_CAPTION = 5
```

Longer subtitle chunks.

---

## Improving Accuracy

The generated subtitles may contain transcription mistakes.

You can upload the generated `.srt` file to ChatGPT and use the following prompt:

```text
Fix this srt file and give me final srt file.

This is ML generated srt file from my video with hinglish language and it has many mistakes like words mistakes and spelling mistakes.

Get the idea from the subtitles file itself about the topic and fix that and give me final srt file with everything fixed.

Timestamps are correct.
```

---

## Technologies Used

- Faster Whisper
- Whisper Large-v3
- Indic Transliteration

---

## License

MIT License

---

## Contributing

Pull requests, issues, and feature suggestions are welcome.

If you find a bug or have an idea for improvement, feel free to open an issue.
