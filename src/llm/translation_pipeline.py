from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class ArabicToGermanTranslator:
    """
    Loads a pretrained model to translate Arabic text into German.
    Uses GPU if available.
    """

    def __init__(self):
        # Choose a high-quality multilingual model from Hugging Face
        self.model_name = "Helsinki-NLP/opus-mt-ar-de"

        # Load tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

        # Use GPU if available
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        # Set up translation pipeline
        self.translator = pipeline(
            task="translation_ar_to_de",
            model=self.model,
            tokenizer=self.tokenizer,
            device=0 if torch.cuda.is_available() else -1
        )

    def translate(self, arabic_text: str) -> str:
        """
        Translates the given Arabic text to German.

        :param arabic_text: Arabic input string
        :return: Translated German string
        """
        if not arabic_text.strip():
            return ""

        result = self.translator(arabic_text, max_length=512)
        return result[0]['translation_text']
