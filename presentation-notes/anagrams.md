Anagrams
========

An *anagram* of a word consists of the letters of the original word rearranged into a different order.

The word "cat" is an anagram of "act", and the words "genuine" and "ingenue" are anagrams of each other.
        
            
Problem: How to identify anagrams?
----------------------------------
                
Given two words `word1` and `word2` that are possibly anagrams of each other, how would you check them to identify whether they are or not?

It may help to consider a concrete example. Are these two "words" anagrams of each other? How could you determine that?

    word1 = "tyvcunaazhbeaqjolinucylllztjydjvdhfhsczdayrrmxkmhizpodhwkxlilkypllwqplothnysaoxgpmgatwtjqhdzzpzwkeed"
    word2 = "hljyzcqxmlmtlznnkjulacpszlarehpzemnkojdvowtpyawliaphyodtdldqhkpjvobigyukethraxhylhwfzdzadwyqgtcsizlx"

Anagram Detection Strategies
----------------------------

The following strategies are all valid for identifying anagrams.

* **Checking off letters one-by-one**  
    Go through `word1`, take each letter found, and look through `word2`, checking off the found letters in `word2` as you go.
    
* **Sort and Compare**  
    Sort the letters in `word1` and `word2` and compare the two words that result.
    
* **Brute Force**  
    Write all the possible combinations of the letters in `word1` and see if `word2` matches any of them.
    
* **Count and Compare**  
    Count the frequency of each letter in `word1`, and compare it to the frequencies of the letters in `word2`.
    
The *real* question, of course, is which strategy do you think might be most efficient?

That turns out to be a complex question, and one that requires more analysis and/or testing!
            
            