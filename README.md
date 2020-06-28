# Persona-4-SRS

Want to learn and practice Japanese with Persona 4? This repo contains Persona 4 Spaced Repetition System (SRS) items and a simple, unofficial Jisho.org Python API used to generate them. The SRS items are generated based on an extracted [dialogue script](https://github.com/jcr179/Persona-4-SRS/blob/master/) for Persona 4 **(not Golden, and Japanese in the interface doesn't seem to be included)** that I found [here](https://www.reddit.com/r/LearnJapanese/comments/h9l6r0/persona_4_golden_is_available_on_steam_and_there/) and the corresponding [kanji](https://github.com/jcr179/Persona-4-SRS/blob/master/) and [word](https://github.com/jcr179/Persona-4-SRS/blob/master/) frequency lists.

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

Step 1/x: Download this repository as a zip, and unzip it in a location of your choice. 

Step 2/x: [Download and install Houhou](http://houhou-srs.com/)

...

## How were the SRS items generated?
Given the game script and frequency lists, I used a combination of [Jisho.org's API for word searches](https://jisho.org/api/v1/search/words?keyword=house) and web scraping Jisho.org with BeautifulSoup for the kanji searches. The meat of this code is in search.py. I couldn't find a more robust Jisho.org API, written in Python or otherwise, so feel free to use and/or improve what little I've laid out. Pandas was used for tabulating the data and sorting it. I did some random sample testing and saw that most of the SRS items are correct, but some have inaccurate readings or meanings, or are just partially or completely wrong. Most names and other words that Jisho.org couldn't give a reading for are ignored when importing into Houhou but can be seen in the master lists kanji.csv and words.csv.

## Future considerations
- Improve SRS item accuracy
- Associate kanji with their radicals
