import sys
import os

from faster_whisper import WhisperModel
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate


WORDS_PER_CAPTION = 3


if len(sys.argv) < 2:
    print("Usage:")
    print("python caption_video.py <video_file>")
    sys.exit(1)

VIDEO = sys.argv[1]

if not os.path.exists(VIDEO):
    print(f"File not found: {VIDEO}")
    sys.exit(1)

OUTPUT_SRT = os.path.splitext(VIDEO)[0] + ".srt"


def format_time(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)

    return f"{hrs:02}:{mins:02}:{secs:02},{ms:03}"


print("Loading Whisper model...")

model = WhisperModel(
    "large-v3",
    device="cpu",
    compute_type="int8"
)

print(f"Processing: {VIDEO}")

segments, info = model.transcribe(
    VIDEO,
    language="hi",
    beam_size=5,
    word_timestamps=True
)

subtitle_index = 1

with open(OUTPUT_SRT, "w", encoding="utf-8") as f:

    for seg in segments:

        if not seg.words:
            continue

        words_data = []

        for w in seg.words:

            try:
                roman_word = transliterate(
                    w.word.strip(),
                    sanscript.DEVANAGARI,
                    sanscript.HK
                )
            except:
                roman_word = w.word.strip()

            words_data.append(
                {
                    "word": roman_word,
                    "start": w.start,
                    "end": w.end
                }
            )

        for i in range(
            0,
            len(words_data),
            WORDS_PER_CAPTION
        ):

            chunk = words_data[i:i + WORDS_PER_CAPTION]

            text = " ".join(
                item["word"]
                for item in chunk
            )

            start = chunk[0]["start"]
            end = chunk[-1]["end"]

            f.write(f"{subtitle_index}\n")
            f.write(
                f"{format_time(start)} --> "
                f"{format_time(end)}\n"
            )
            f.write(text + "\n\n")

            subtitle_index += 1

print(f"Done! Subtitle saved as: {OUTPUT_SRT}")
