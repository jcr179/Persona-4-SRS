import pandas as pd 
import os 

# To see kanji in stdout, for Testing
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Sorting full list from master kanji.csv and words.csv for different users 

def make_batches(mode):
    
    if mode == 'kanji_onyomi' or mode == 'kanji_kunyomi':
        path_to_kanji = 'kanji.csv'
        df = pd.read_csv(path_to_kanji, encoding='utf-8', header=0, sep=';')
        
    elif mode == 'word':
        path_to_words = 'words.csv'
        df = pd.read_csv(path_to_words, encoding='utf-8', header=0, sep=';')
        
    else:
        print("No batches made. Usage: make_batches(['kanji_onyomi' | 'kanji_kunyomi' | 'word'])")
        return None
        
    if not os.path.isdir('./' + mode):
        os.mkdir(mode)
    
    prefix = mode
    df_len = len(df)

    # Sort by Cumulative frequency percent (percent)
    thresholds = [0.0, 30.0, 40.0, 50.0, 60.0, 70.0, 75.0, 80.0,\
                  82.5, 85.0, 87.5, 90.0, 91.0, 92.0, 93.0, 94.0,\
                  95.0, 96.0, 97.0, 98.0, 99.0, 99.25, 99.5, 99.75, 100.0] # Arbitrarily chosen 

    thr = len(thresholds)

    if not os.path.isdir(os.path.join(prefix, 'cum_freq_pct')):
        os.mkdir(os.path.join(prefix, 'cum_freq_pct'))

    for i in range(1, thr):
        df_slice = df.loc[(df['Cumulative Freq. Pct.'] > thresholds[i-1]) & (df['Cumulative Freq. Pct.'] <= thresholds[i])]
        output_path = os.path.join(prefix, 'cum_freq_pct', str(thresholds[i]).replace('.', 'p') + '.csv')
        df_slice.to_csv(output_path, encoding='utf-8-sig', sep=';')

    # Sort by Cumulative frequency percent (number of items) 
    batch_size = 25 # How many new items per file 

    full_batches = df_len // batch_size 
    
    if not os.path.isdir(os.path.join(prefix, 'cum_freq_pct_num')):
        os.mkdir(os.path.join(prefix, 'cum_freq_pct_num'))

    for i in range(full_batches):
        df_slice = df[i*batch_size:(i+1)*batch_size]
        output_path = os.path.join(prefix, 'cum_freq_pct_num', str(i) + '.csv')
        df_slice.to_csv(output_path, encoding='utf-8-sig', sep=';')

    df_slice = df[i*batch_size:]
    output_path = os.path.join(prefix, 'cum_freq_pct_num', str(i) + '.csv')
    df_slice.to_csv(output_path, encoding='utf-8-sig', sep=';')

    # Sort by Wanikani level 
    df = df.sort_values(by=['WK Level'])
    thresholds = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, float("inf")]
    thr = len(thresholds)
    
    if not os.path.isdir(os.path.join(prefix, 'wk_level')):
        os.mkdir(os.path.join(prefix, 'wk_level'))

    for i in range(1, thr):
        df_slice = df.loc[(df['WK Level'] > thresholds[i-1]) & (df['WK Level'] <= thresholds[i])]
        output_path = os.path.join(prefix, 'wk_level', str(thresholds[i-1]+1) + '_to_' + str(thresholds[i]) + '.csv')
        df_slice.to_csv(output_path, encoding='utf-8-sig', sep=';')
        
    # handle wk level = -1 (not in wk)
    df_slice = df.loc[df['WK Level'] == -1]
    df_slice.to_csv(os.path.join(prefix, 'wk_level', 'undefined' + '.csv'), encoding='utf-8-sig', sep=';')

    # Sort by JLPT level
    df = df.sort_values(by=['JLPT Level'], ascending=False)

    levels = ['N1', 'N2', 'N3', 'N4', 'N5']
    
    if not os.path.isdir(os.path.join(prefix, 'jlpt_level')):
        os.mkdir(os.path.join(prefix, 'jlpt_level'))

    for i in range(len(levels)):
        df_slice = df.loc[df['JLPT Level'] == levels[i]]
        output_path = os.path.join(prefix, 'jlpt_level', str(levels[i]) + '.csv')
        df_slice.to_csv(output_path, encoding='utf-8-sig', sep=';')
        
    df_slice = df.loc[df['JLPT Level'].isnull()]
    df_slice.to_csv(os.path.join(prefix, 'jlpt_level', 'undefined' + '.csv'), encoding='utf-8-sig', sep=';')
    
    print('Batches made successfully for ', mode)


if __name__ == "__main__":
    make_batches('kanji_onyomi')
    make_batches('kanji_kunyomi')
    make_batches('word')

