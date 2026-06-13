Hinglish Subtitle Generator
Generate Hinglish (Roman Hindi) subtitles from Hindi videos automatically using Faster Whisper.
Features
• Automatic Hindi speech transcription
• Converts Devanagari words to Hinglish/Roman Hindi
• Generates .srt subtitle files
• Word-level timestamps
• Adjustable words per caption
• Works offline after model download

---

Example
Input Speech
नमस्ते दोस्तों आज हम एक नया प्रोजेक्ट बनाएंगे
Generated Subtitle
namaste dosto aaj
ham ek naya
project banaenge

---

Demo
https://github.com/user-attachments/assets/c20b1a2a-946a-45ce-822f-af76f5041b4e

---

Installation

1. Install Python
   Download Python 3.10 or later:
   https://www.python.org/downloads/
   During installation make sure:
   • Add Python to PATH ✓
   Verify installation:
   python --version

---

2. Clone Repository
   git clone https://github.com/YOUR_USERNAME/hinglish-subtitle-generator.git

cd hinglish-subtitle-generator

---

3. Install Dependencies
   pip install -r requirements.txt

---

Usage
Place your video file inside the project folder:
hinglish-subtitle-generator/
│
├── reel.mp4
└── caption_video.py
Run:
python caption_video.py

---

First Run
Whisper Large-v3 will be downloaded automatically.
Approximate download size:
• Model: ~3 GB
• Recommended free space: ~5 GB
Internet connection required only for the initial download.

---

Output
After processing:
reel.srt

---

Customize Subtitle Speed
Open:
WORDS_PER_CAPTION = 3
Examples:
WORDS_PER_CAPTION = 1
Fast reel-style captions
WORDS_PER_CAPTION = 5
Longer captions

---

Improving Accuracy
The generated subtitles may contain transcription mistakes.
You can upload the generated .srt file to ChatGPT and use:
Fix this srt file and give me final srt file.
This is ML generated srt file from my video with Hinglish language and it has many mistakes like word mistakes and spelling mistakes.
Get the idea from the subtitles file itself about the topic and fix that.
Timestamps are correct.

---

Technologies Used
• Faster Whisper
• Whisper Large-v3
• Indic Transliteration

---

License
MIT License

---

Contributing
Pull requests are welcome.
If you find a bug or have an idea for improvement, feel free to open an issue.
