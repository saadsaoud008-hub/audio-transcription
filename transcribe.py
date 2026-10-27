import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Transcribe audio with timestamps")
    parser.add_argument("audio", type=Path, help="WAV or MP3 audio file")
    args = parser.parse_args()
    if not args.audio.is_file():
        parser.error("Audio file does not exist")
    try:
        from faster_whisper import WhisperModel
        model = WhisperModel("small", device="cpu", compute_type="int8")
        segments, info = model.transcribe(str(args.audio), beam_size=5)
        result = [{"start": round(s.start, 2), "end": round(s.end, 2),
                   "text": s.text.strip()} for s in segments]
        print(json.dumps({"language": info.language,
                          "transcript": " ".join(s["text"] for s in result),
                          "segments": result}, ensure_ascii=False, indent=2))
    except Exception as error:
        print(f"Transcription failed: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
