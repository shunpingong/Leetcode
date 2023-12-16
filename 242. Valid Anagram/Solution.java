class Solution {
    public boolean isAnagram(String s, String t) {
         if (s.length() != t.length()) {
        return false; // Anagrams must have the same length
    }

    int[] charCount = new int[26]; // Assuming input contains only lowercase English letters

    // Increment character counts for string s
    for (char ch : s.toCharArray()) {
        charCount[ch - 'a']++;
    }

    // Decrement character counts for string t
    for (char ch : t.toCharArray()) {
        if (--charCount[ch - 'a'] < 0) {
            return false; // If charCount drops below zero, not an anagram
        }
    }

    return true; // All characters in s and t have been
    }
}