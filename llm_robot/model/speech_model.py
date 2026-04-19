import whisper

class SpeechModel:
    def __init__(self, model_size="base"):
        self.model = whisper.load_model(model_size)

    def listen(self):
        print("🎙️ Ouvindo...")
        result = self.model.transcribe(
            audio=None,
            fp16=False,
            language="pt"
        )
        return result["text"]
