class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=s.strip().split()
        words=word[-1]
        return len(words)