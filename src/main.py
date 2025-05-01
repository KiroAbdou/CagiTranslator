from document_processing.processor import DocumentProcessor
from llm.translation_pipeline import ArabicToGermanTranslator

def test_LLM():
    translator = ArabicToGermanTranslator()

    arabic_text = "الله محبة، وهذه هي الوصية التي أعطانا إياها، أن يحب بعضنا بعضًا."
    translation = translator.translate(arabic_text)

    print("Original Arabic:\n", arabic_text)
    print("LLM German Translation:\n", translation)

def main():

    pass

if __name__ == "__main__":
    main()