# CAGI Translate

A free and powerful pipeline to translate Arabic Sunday School lessons of the Coptic Orthodox Church into German using RAG, pre-translated material, and open-source LLMs — all without paying for GPUs or fine-tuning.

## Project Structure

- `docs/`: Raw scanned PDFs and pre-translated Word files
- `data/`: Cleaned and aligned extracted text for training/evaluation
- `src/`: Modular codebase
  - `document_processing/`: Word/PDF extraction
  - `llm/`: Translation pipeline using free HuggingFace LLMs
  - `rag/`: Future context retrieval (vector store)
- `main.py`: Run the full pipeline
- `notebooks/`: Experiments & evaluation
- `tests/`: Unit tests

## Installation

```bash
git clone https://github.com/your-org/cagi_translate.git
cd cagi_translate
```

### On Windows

```bat
setup_env.bat
```

### On Linux / macOS

```bat
bash setup_env.sh
```

