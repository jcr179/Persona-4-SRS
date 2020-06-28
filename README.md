# Persona-4-SRS

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/opener.png"></p>

Want to learn and practice Japanese with Persona 4? This repo contains Persona 4 Spaced Repetition System (SRS) items and a simple, unofficial Jisho.org Python API used to generate them. The SRS items are generated based on an extracted [dialogue script](https://github.com/jcr179/Persona-4-SRS/blob/master/persona4%20script.txt) for Persona 4 **(not Golden, and Japanese in the interface doesn't seem to be included)** that I found [here](https://www.reddit.com/r/LearnJapanese/comments/h9l6r0/persona_4_golden_is_available_on_steam_and_there/) and the corresponding [kanji](https://github.com/jcr179/Persona-4-SRS/blob/master/persona4_kanji.txt) and [word](https://github.com/jcr179/Persona-4-SRS/blob/master/word_freq_report.txt) frequency lists (authors unknown; please let me know if you know the authors).

***Disclaimer***: This is a super early version of a personal project, and as such, I can't guarantee the accuracy of every SRS item generated. Please consider asking for a more fleshed-out Jisho.org API, making your own suggestions for improving the pipeline, or correcting whatever SRS items you can and push the updates to me. There are particularly egregious errors with some particles and character names, so please use these as a learning tool responsibly. I don't own anything related to Persona.

# How to use the SRS items to learn and practice
You can download the SRS items in this repository and import them to [Houhou](http://houhou-srs.com/). I've included a tutorial of how to do so below. Using SRS, you can target learning Japanese in Persona 4 in a manner similar to Wanikani or Bunpro, which each also use SRS. There is a lot of content out there about how to use SRS and its efficacy so I won't bloat things here.

The SRS items are split into batches accessible in their respective folder. The batches are organized by:
- Cumulative frequency percentage, by percentage 
  - e.g. If 車, 上, and 方 represent 40%, 35%, and 25% of all kanji occurences in the script, respectively, then 車 and 上 appear in the < 80% batch, but 方 does not. 方 is the only kanji to appear in the 80% <= percent < 100% batch. If you're able to understand all items in the < N% batch, you can expect to understand ~N% of all instances of kanji in the game's dialogue (but not necessarily ~N% of all unique kinds of kanji in the game!).
- Cumulative frequency percentage, by number of items 
  - Batch 1 contains the 25 most frequently appearing kanji, batch 2 contains the 25 next most frequently appearing kanji, ..., the last batch contains the least frequently appearing kanji. Wanikani introduces about 25 new kanji at each new level. You can change the batch size in make_batches.py
- Wanikani level 
  - Each batch corresponds to 5 Wanikani levels. There is another 'undefined' batch for items that didn't have a corresponding Wanikani level attached.
- JLPT level
  - Each batch corresponds to a JLPT level from N5 to N1 inclusive. There is another 'undefined' batch for items that didn't have a corresponding JLPT level. 

# How to import the SRS items into Houhou

**Note**: This tutorial was made using Houhou version 1.3.0

Step 1: Download this repository as a zip, and unzip it in a location of your choice. 

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut1.png"></p>


Step 2: [Download and install Houhou](http://houhou-srs.com/)


Step 3: Open Houhou and click on the green SRS tab at the top of the window.

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut2.png"></p>


Step 4: Click "Import SRS items" at the bottom of the window.

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut3.png"></p>


Step 5: Under the option to Import SRS items from a CSV file, click "Select this option".

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut4.png"></p>


Step 6: Check the checkbox "First line is a header". Click "Browse" and select the .csv file you want to import. How do you choose which file to import? 
- If you want to import kanji onyomi readings (pink cards in Wanikani), choose a file from the kanji_onyomi folder and go to step 7a next. 
- If you want to import kanji kunyomi readings (purple cards in Wanikani), choose a file from the kanji_kunyomi folder and go to step 7c next. 
- If you want to import words/vocab (purple cards in Wanikani), choose a file from the word folder and go to step 7b next.  
**Note**: kanji.csv and words.csv are the master kanji/word lists, and you can select smaller subsets of either master list according to the corresponding folders *kanji_onyomi, kanji_kunyomi*, and *word*.

For example, in the image below I'm importing some kanji onyomi readings. You can tell from the path to the .csv file including 'kanji_onyomi'.
<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut5.png"></p>


Step 7a: **You should be here if you want to import kanji onyomi readings.** Please set the following field parameters:
- Kanji reading: Ja 
- Accepted meanings: En 
- Accepted readings: Onyomi 
- Item type: Item Type
- Tags: Tags

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut6a.png"></p>

Click "Next", then "Start import" on the next screen. When the import is complete, click "Finish". The SRS items should now be imported.

If you want to import other types of items, repeat steps 3 to 6 go to their corresponding step (7b or 7c). Otherwise, go to step 8.


Step 7b: **You should be here if you want to import word/vocabulary readings.** Please set the following field parameters:
- Kanji reading: Ja 
- Accepted meanings: En 
- Accepted readings: Reading 
- Item type: Item Type
- Tags: Tags

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut6b.png"></p>

Click "Next", then "Start import" on the next screen. When the import is complete, click "Finish". The SRS items should now be imported.

If you want to import other types of items, repeat steps 3 to 6 go to their corresponding step (7a or 7c). Otherwise, go to step 8.


Step 7c: **You should be here if you want to import kanji kunyomi readings.** Please set the following field parameters:
- Kanji reading: Ja 
- Accepted meanings: En 
- Accepted readings: Kunyomi 
- Tags: Tags
- **When "Item type" is not specified...: Set as Vocab**

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut6c1.png"></p>

Now, we want to remove any duplicate instances of single-character kanji that may have already appeared from a 'word' .csv file import. Click the radio button "Remove the existing item" under "About the existing item...":

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut6c2.png"></p>
  
This extra step is not essential but should prevent duplicate instances of the same kanji but with different readings - this is a bit of a quirk with the way I extract readings for now and I'll try streamlining this in the future. Sorry for the inconvenience.

Click "Next", then "Start import" on the next screen. When the import is complete, click "Finish". The SRS items should now be imported.

If you want to import other types of items, repeat steps 3 to 6 go to their corresponding step (7a or 7b). Otherwise, go to step 8.


Step 8: Let's confirm that your SRS items were correctly imported. Click "Browse SRS items" in the bottom-right corner.

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut7.png"></p>
  

Step 9: Enter "p4" in the "Containing the tag:" search bar and click "Refresh"!

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut8.png"></p>
  
You should now see your imported SRS items, ready for you to practice with!

<p align="center"><img src="https://github.com/jcr179/Persona-4-SRS/blob/master/images/tut9.png"></p>

## How were the SRS items generated?
Given the game script and frequency lists, I used a combination of [Jisho.org's API for word searches](https://jisho.org/api/v1/search/words?keyword=house) and web scraping Jisho.org with BeautifulSoup for the kanji searches. The meat of this code is in search.py. I couldn't find a more robust Jisho.org API, written in Python or otherwise, so feel free to use and/or improve what little I've laid out. Pandas was used for tabulating the data and sorting it. I did some random sample testing and saw that most of the SRS items are correct, but some have inaccurate readings or meanings, or are just partially or completely wrong. Most names and other words that Jisho.org couldn't give a reading for are ignored when importing into Houhou but can be seen in the master lists kanji.csv and words.csv.

## Future considerations
- Improve SRS item accuracy
  - There are vocab items that are just the kanji, but the recorded correct reading is the corresponding verb or adjective (e.g. kanji is 難し but correct reading is むずかしい)
- Associate kanji with their radicals

## Contact and extra
For help or feedback, <jcrebanal17@gmail.com>

Please consider [donating to Houhou](http://houhou-srs.com/) for such a useful language learning tool.

I've got a lot of help learning Japanese from friends and strangers, so I'm happy to try and give back a bit. Hope this helps some of you out. Thanks.
