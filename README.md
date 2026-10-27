# Audio transcription

A Python CLI that transcribes a WAV or MP3 file using faster-whisper and outputs JSON with text and timestamps in seconds. It runs on CPU. The model is downloaded on first use, which requires internet access.

## Setup and run

```bash
python -m pip install -r requirements.txt
python transcribe.py recording.mp3
python transcribe.py recording.wav > transcript.json
```

## Scope

This is a single-file CLI. Queues, concurrent uploads, persistent storage, retries, and an HTTP API are proposed production extensions, not implemented here. Audio is processed locally after the model is downloaded.
