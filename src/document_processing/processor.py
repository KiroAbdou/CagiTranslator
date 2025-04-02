from docx import Document
from typing import List, Tuple


class DocumentProcessor:
    def __init__(self, filepath: str, marker: str = None):
        """
        Initializes the processor with a Word document.
        
        :param filepath: Path to the Word (.docx) document
        :param marker: Optional marker string to indicate where German starts
        """
        self.filepath = filepath
        self.marker = marker
        self.document = Document(filepath)

    def extract_text(self) -> Tuple[List[str], List[str]]:
        """
        Extracts Arabic and German text from the document.
        Tries to split by a custom marker, else falls back to naive middle split.

        :return: Tuple of (arabic_paragraphs, german_paragraphs)
        """
        all_paragraphs = [p.text.strip() for p in self.document.paragraphs if p.text.strip()]

        if self.marker:
            if self.marker in all_paragraphs:
                split_index = all_paragraphs.index(self.marker)
                arabic_paragraphs = all_paragraphs[:split_index]
                german_paragraphs = all_paragraphs[split_index + 1:]
                return arabic_paragraphs, german_paragraphs

        # Fallback: split roughly in half
        halfway = len(all_paragraphs) // 2
        return all_paragraphs[:halfway], all_paragraphs[halfway:]
