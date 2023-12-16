class Solution {
    public boolean isAnagram(String s, String t) {
         if (s.length() != t.length()) {
        return false; // Anagrams must have the same length
    }

    int[] charCount = new int[26]; 

    // increase count for S
    for (char ch : s.toCharArray()) {
        charCount[ch - 'a']++;
    }

    // decrease count for t
    for (char ch : t.toCharArray()) {
        if (--charCount[ch - 'a'] < 0) {
            return false; // drops below 0 means diff
        }
    }

    return true; // all same
    }
}