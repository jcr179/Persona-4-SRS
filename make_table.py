import pandas as pd
from search import *
from read import *

# progress bar, optional
from tqdm import tqdm 

# For testing to have kanji in stdout
import sys
sys.stdout.reconfigure(encoding='utf-8')


def make_table():

    # Kanji list
    kanji_info = read_kanji_list("persona4_kanji.txt")
    print('Kanji frequency list successfully read.')
    num_kanji = len(kanji_info)
    df = pd.DataFrame(columns=('Ja', 'En', 'Kunyomi', 'Onyomi', 'Frequency Rank', 'Cumulative Freq. Pct.',\
                            'Frequency Pct.', 'JLPT Level', 'WK Level', 'Item Type', 'Tags'))

    kanji_dict = {} # map kanji to index in kanji_info for adding kunyomi to word list later 

    for i in tqdm(range(num_kanji)):
        kanji = kanji_info[i]['kanji']
        jisho_info = search_jisho(kanji, is_word=False)
        #print(kanji, jisho_info, kanji_info[i])
        df.loc[i] = [kanji, ','.join(jisho_info['meanings'].split('/')), jisho_info['kunyomi'], jisho_info['onyomi'],\
                    kanji_info[i]['f_rank'], kanji_info[i]['f_cum'], kanji_info[i]['f_per'],\
                    jisho_info['jlpt'], jisho_info['wk_level'], 'K', 'p4']
        kanji_dict[kanji] = jisho_info['kunyomi']
                    
    print('Dataframe build successful.')

    path_to_output_csv = 'kanji.csv'

    # Making sep argument =',' or default lets Excel open it up nicely.
    df.to_csv(path_to_output_csv, encoding='utf-8-sig', sep=';')

    print('Dataframe successfully saved as csv: ', path_to_output_csv)


    # Word list 
    word_info = read_word_list("word_freq_report.txt")
    print('Word frequency list successfully read.')
    num_words = len(word_info)
    df = pd.DataFrame(columns=('Ja', 'En', 'Reading', 'Frequency Rank', 'Cumulative Freq. Pct.',\
                            'Frequency Pct.', 'JLPT Level', 'WK Level', 'Item Type', 'Tags'))
                            
    word_dict = {}

    for i in tqdm(range(num_words)):
        word = word_info[i]['word']
        
        jisho_info = search_jisho(word, is_word=True)
        #print(word, jisho_info, word_info[i])
        

        df.loc[i] = [word, ','.join(jisho_info['meanings'].split('/')), jisho_info['reading'],\
                    word_info[i]['f_rank'], word_info[i]['f_cum'], word_info[i]['f_per'],\
                    jisho_info['jlpt'], jisho_info['wk_level'], 'V', 'p4']
        word_dict[word] = jisho_info['reading']
        
        
                    
    print('Dataframe build successful.')

    path_to_output_csv = 'words.csv'

    # Making sep argument =',' or default lets Excel open it up nicely.
    df.to_csv(path_to_output_csv, encoding='utf-8-sig', sep=';')

    print('Dataframe successfully saved as csv: ', path_to_output_csv)
    
if __name__ == "__main__":
    make_table()
