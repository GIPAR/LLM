class LLMModel:
    def interpret(self, text):
        text = text.lower()

        if "frente" in text:
            return {"action": "forward"}

        if "gire" in text or "direita" in text:
            return {"action": "rotate"}

        if "pare" in text:
            return {"action": "stop"}

        return {"action": "stop"}

