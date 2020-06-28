import codecs

# To see kanji in stdout, for Testing
import sys
sys.stdout.reconfigure(encoding='utf-8')

def str_to_float(string: str) -> float:
    a, b = string.split(',')
    b = '0.' + b
    return float(a) + float(b)

def read_kanji_list(input_file: str) -> list:
    """
    f_num:      Number of times kanji appears in script
    kanji:      The kanji 
    f_rank:     Lower ranks mean more frequently appeared in script 
    f_per:      Percentage of all kanji that this kanji appeared 
    f_cum:      Cumulative percentage of kanji for this kanji's frequency rank and lower
    """
    
    counter = 0
    
    try:
        with codecs.open(input_file, 'r', encoding='utf8') as f:
            lines = f.readlines()
            content = []
            for line in lines:
                components = [x.strip() for x in line.split('\t')]
                
                if counter == 0: # Corner case of first kanji having character in front
                    components[0] = components[0][1:]
                    
                counter += 1
                
                content.append({'f_num':    int(components[0]),\
                                'kanji':    components[1],\
                                'f_rank':   int(components[3]),\
                                'f_per':    str_to_float(components[4]),\
                                'f_cum':    str_to_float(components[5])})
                
        print(f"Kanji list read successfully. {counter} kanji read.")
        return content
        
    
    except FileNotFoundError:
        print('Error: Given path to input file does not exist. Kanji list not read.')
        return None 
        
def read_word_list(input_file: str) -> list:
    """
    f_num:      Number of times word appears in script
    word:       The word 
    f_rank:     Lower ranks mean more frequently appeared in script 
    f_per:      Percentage of all word that this kanji appeared 
    f_cum:      Cumulative percentage of word for this word's frequency rank and lower
    """
    
    counter = 0
    
    try:
        with codecs.open(input_file, 'r', encoding='utf8') as f:
            lines = f.readlines()
            content = []
            for line in lines:
                components = [x.strip() for x in line.split('\t')]
                
                if counter == 0: # Corner case of first kanji having character in front
                    components[0] = components[0][1:]
                    
                counter += 1
                
                content.append({'f_num':    int(components[0]),\
                                'word':    components[1],\
                                'f_rank':   int(components[3]),\
                                'f_per':    str_to_float(components[4]),\
                                'f_cum':    str_to_float(components[5])})
                
        print(f"Word list read successfully. {counter} words read.")
        return content
        
    
    except FileNotFoundError:
        print('Error: Given path to input file does not exist. Kanji list not read.')
        return None 

if __name__ == "__main__":
    # Test
    x = read_kanji_list("persona4_kanji.txt")
    #print(x)
    y = read_word_list("word_freq_report.txt")
    print(y)