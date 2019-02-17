Counting Words
==============

Counting words is one of those things that is so easy for <i>us</i> to do that it's hard to identify how you would instruct someone else to do it. In trying to explain how to count words, you might end up saying, in frustration, "Well, you just COUNT THE WORDS!"

But how do you explain that to a computer? What's the algorithm?

Let's try two different algorithms. One algorithm might consist of simply recognizing that a word is (usually) surrounded by space, so... if we count the number of spaces in the text, that will help us figure out the number of words.

If the text is "i love you", there are how many spaces? Two. And there are three words there, so... maybe it's just the number of spaces plus 1? Try that out with a few sentences and see if that's true.

The Python code for this algorithm looks like this:

    # counting words using spaces
    space_count = 0
    text = "i love you"
    for letter in text:
        if letter == " ":
            space_count = space_count + 1
    word_count = space_count + 1
    print(word_count)
    
That strategy turns out to work a lot of the time, but not all the time. What happens in this text where there are spaces at the beginning, end, and multiple spaces in the middle?


    "i love you.  i really do.  "
      _    _    __ _      _   __
      1    2    34 5      6   78
      
There are 8 spaces in that text&mdash;two after each period in addition to the ones between the words, but there are not 9 words (as our "spaces + 1" algorithm would predict... just 6. So... we'd like to find a better algorithm for identifying words.

What we'd like to be able to do is ignore all the spaces, and just focus on the words. One strategy for doing is is to:

1. Go through each letter in the text
2. If it <i>isn't</i> a space, and we weren't "in a word", recognize that we're "in a word," and add one to our word counter.
3. If it <i>is</i> a space, realize that we're not "in a word" anymore.

To implement this strategy, we have to have some way of remember if we're "in a word" or not, and an easy way to do that is by using a "Boolean flag": we'll have an indicator called "in_word" that is set to False when we're not in a word, and True when we ARE in a word, and working our way through the letters in there.

The Python code for implementing this algorithm looks like this:

    text = "i love you.  i really do.  "
    word_count = 0
    in_word = False
    for letter in text:
        if letter != " ":
            if not in_word:
                in_word = True
                word_count += 1
        else:
            in_word = False
    print(word_count)
    
This particular algorithm turns out to be quite a bit more robust.
