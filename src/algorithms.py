# src/algorithms.py

class StringMatcher:
    @staticmethod
    def naive_search(pattern, text):
        """O(m*n) standard nested loop search."""
        matches = []
        n, m = len(text), len(pattern)
        for i in range(n - m + 1):
            if text[i:i+m] == pattern:
                matches.append(i)
        return matches

    @staticmethod
    def compute_lps(pattern):
        """Computes the Longest Prefix Suffix array for KMP."""
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    @staticmethod
    def kmp_search(pattern, text):
        """O(n+m) KMP algorithm implementation."""
        if not pattern or not text: return []
        
        matches = []
        n, m = len(text), len(pattern)
        lps = StringMatcher.compute_lps(pattern)
        
        i = j = 0
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return matches

    @staticmethod
    def rabin_karp_search(pattern, text, prime=101):
        """O(n+m) average time rolling hash search."""
        if not pattern or not text: return []
        
        matches = []
        n, m = len(text), len(pattern)
        d = 256 # Number of characters in the input alphabet
        
        p_hash = 0
        t_hash = 0
        h = 1

        for i in range(m - 1):
            h = (h * d) % prime

        for i in range(m):
            p_hash = (d * p_hash + ord(pattern[i])) % prime
            t_hash = (d * t_hash + ord(text[i])) % prime

        for i in range(n - m + 1):
            if p_hash == t_hash:
                if text[i:i+m] == pattern:
                    matches.append(i)
            
            if i < n - m:
                t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
                if t_hash < 0:
                    t_hash += prime
                    
        return matches