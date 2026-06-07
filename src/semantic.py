# src/semantic.py
import math
import re

class SemanticEngine:
    @staticmethod
    def tokenize(text: str):
        """Extracts normalized words from text."""
        return re.findall(r'\w+', text.lower())

    @staticmethod
    def build_vector(tokens):
        """Creates a frequency map vector for tokens."""
        vector = {}
        for token in tokens:
            vector[token] = vector.get(token, 0) + 1
        return vector

    @staticmethod
    def calculate_cosine_similarity(text_a: str, text_b: str):
        """Computes the cosine similarity between two text blocks vector representations."""
        vec_a = SemanticEngine.build_vector(SemanticEngine.tokenize(text_a))
        vec_b = SemanticEngine.build_vector(SemanticEngine.tokenize(text_b))
        
        intersection = set(vec_a.keys()) & set(vec_b.keys())
        
        # Calculate dot product
        dot_product = sum([vec_a[x] * vec_b[x] for x in intersection])
        
        # Calculate magnitudes
        sum_a = sum([vec_a[x]**2 for x in vec_a.keys()])
        sum_b = sum([vec_b[x]**2 for x in vec_b.keys()])
        
        magnitude_a = math.sqrt(sum_a)
        magnitude_b = math.sqrt(sum_b)
        
        if not magnitude_a or not magnitude_b:
            return 0.0
        
        return float(dot_product) / (magnitude_a * magnitude_b)