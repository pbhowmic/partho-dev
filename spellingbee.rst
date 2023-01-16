Brute-forcing the NYTimes Spelling Bee
======================================

I am a fan of the NYTimes' `Spelling Bee puzzle <https://www.nytimes.com/puzzles/spelling-bee>`_, and there are days
that no matter how much I rack my brain, I simply cannot come of with the **pangram** (don't worry if you don't know
how to play the game or what the pangram is, we will review that shortly) and curiosity will get the best of me
- like it did today - so I came up with a small script to help with at least the pangram.

The rules
---------

In the Spelling Bee puzzle, the player is given 7 different letters of the English language and the player needs to make
different valid words using these 7 letters subject to the following rules:

#. Each word must a valid word that appears in the *dictionary* that the NY Times uses. In general, that would be any
   valid word in the English language but sometimes, obscene words such as c**t will not be allowed by the NYTimes
#. One letter of the seven is marked *cumpulsory* and each word that the player makes must make use of this letter at
   least once
#. Each word must be at least 4 letters long
#. A letter may be used more than once in a word
#. I have no clue how they score the game, I have never had any interest in that. All I care about is getting the
   pangram.

So, for example if you were to be given the letters `I F M U D H E` and the letter `I` were to be compulsory, invalid
words would be

* HID, HIM (3-letter words, too short)
* HEED, FEUD (do not have the cumpulsory letter I)

while valid words would be

* HUMID (5-letter word and contains the cumpulsory letter I)
* HUMIDIFIED (10-letter word and contains the cumpulsory letter I)

The last one (HUMIDIFIED) is a **pangram** which is to say it is a valid word made from using all 7 letters at least
once in the word. Sometimes, there is more than pangram in the puzzle: DEHUMIDIED is also a pangram for the example
puzzle.

The process
-----------

I started by identifying a "free" dictionary. I chose `this one <https://github.com/dwyl/english-words>`_ on Github.
Then I modified the script ``read_english_dictionary.py`` in that repo. The only thing that script did was to read the
words in a dictionary text file and create a Python ``set`` out of those words. I repurposed this script (did not even
bother to rename it)

The algo is pretty basic.

#. Pass the 7 letters from the puzzle as a single string, with the compulsory letter being the first letter of the string
#. Read the dictionary and store it in a list
#. Generate all combinations of this 7-letters as sets, each set being of size 4 to 7
#. Iterate over each generated set of letters
#. Reduce each word in the dictionary to its set of letters. If this set is the same as the set of letters in the
   previous step, then this word is a match and is added to the solution set.

Of course there are some optimizations can be made like immediately after reading the entire dictionary from file,
reject all words less than 4-letters long to reduce the search space. That aside, it's pretty much a brute-force
methodology.

The code
--------

.. literalinclude:: spellingbee.py
   :language: python

Run the code
------------
Here, I am using Python 3.8

.. code-block:: console

   $ python3 read_english_dictionary.py ifmduhe

