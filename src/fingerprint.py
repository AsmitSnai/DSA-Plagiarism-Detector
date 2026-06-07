# src/fingerprint.py

class WinnowingEngine:
    @staticmethod
    def get_k_grams(text: str, k: int = 5):
        """Splits text into contiguous sequences of characters of length k."""
        return [text[i:i+k] for i in range(len(text) - k + 1)]

    @staticmethod
    def hash_string(s: str, prime: int = 101):
        """Generates a polynomial rolling hash value for a k-gram string."""
        h = 0
        for char in s:
            h = (h * 256 + ord(char)) % prime
        return h

    @staticmethod
    def winnow(text: str, k: int = 5, w: int = 4):
        """
        Applies the Winnowing algorithm to select a robust subset of hashes.
        Returns a set of tuples containing (hash_value, absolute_position).
        """
        # Normalize and clean text for structural fingerprinting
        clean_chars = [c.lower() for c in text if c.isalnum()]
        normalized_text = "".join(clean_chars)
        
        if len(normalized_text) < k:
            return set()

        k_grams = WinnowingEngine.get_k_grams(normalized_text, k)
        hashes = [WinnowingEngine.hash_string(gram) for gram in k_grams]
        
        fingerprints = set()
        # Sliding window over the generated hashes
        for i in range(len(hashes) - w + 1):
            window = hashes[i:i+w]
            min_val = min(window)
            
            # Find the rightmost occurrence of the minimum value in the current window
            min_index = i + max([idx for idx, val in enumerate(window) if val == min_val])
            fingerprints.add((min_val, min_index))
            
        return fingerprints