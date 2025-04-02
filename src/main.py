from document_processing.processor import DocumentProcessor
from llm.translation_pipeline import ArabicToGermanTranslator

def main():

    translator = ArabicToGermanTranslator()

    arabic_text = "الله محبة، وهذه هي الوصية التي أعطانا إياها، أن يحب بعضنا بعضًا."
    translation = translator.translate(arabic_text)

    print("Original Arabic:\n", arabic_text)
    print("LLM German Translation:\n", translation)

    exit()
    doc_path = "docs/processed/sample.docx"
    german_start_page = 15  # adjust based on your document

    processor = DocumentProcessor(doc_path, german_start_page)
    arabic_paragraphs, german_paragraphs = processor.extract_text()

    for i, arabic in enumerate(arabic_paragraphs[:5]):  # limit for now
        print(f"\nOriginal Arabic:\n{arabic}")
        llm_translation = translator(arabic)
        print(f"LLM Translation:\n{llm_translation}")
        if i < len(german_paragraphs):
            print(f"Human Translation:\n{german_paragraphs[i]}")

if __name__ == "__main__":
    main()