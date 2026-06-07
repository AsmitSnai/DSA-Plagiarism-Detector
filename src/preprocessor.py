# src/preprocessor.py
import re

def clean_text(text):
    """Normalizes text by removing extra whitespace but keeping sentence structure."""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def get_sentences(text):
    """Splits text into sentences for granular matching."""
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [s.strip() for s in sentences if len(s.strip()) > 10]