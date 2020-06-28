import requests
import json 



# To see kanji in stdout, for Testing
import sys
sys.stdout.reconfigure(encoding='utf-8')
    
import bs4 as bs 
from urllib.parse import unquote



def search_kanji(search_item) -> tuple:
    page = requests.get("https://jisho.org/search/" + search_item)
    soup = bs.BeautifulSoup(page.text, 'html.parser')
    kunyomi = None 
    onyomi = None
    
    for x in soup.find_all(class_='kun readings'):
        y = str(x).split('jisho.org/search/')[1]
        y = y.split('"')[0]
        kunyomi = unquote(y)[len(search_item) + 1:].strip()
        
    for x in soup.find_all(class_='on readings'):
        y = str(x).split('jisho.org/search/')[1]
        y = y.split('"')[0]
        onyomi = unquote(y)[len(search_item) + 1:].strip()
    
    wk_level = -1
    jlpt = None 
    
    for x in soup.find_all(class_="concept_light-status"):
        #print(x, '\n\n')
        x = str(x)
        if 'JLPT' in x and 'wanikani' in x:
            wk_level = x.split('Wanikani level ')[1]
            wk_level = int(wk_level.split('<')[0])
            
            jlpt = x.split('JLPT ')[1]
            jlpt = jlpt.split('<')[0]
            
            break # just take 1st occurence of jlpt and wk information in same hit 
            
    meanings = ''
    for x in soup.find_all(class_="meanings english sense"):
        for y in x.find_all("span"):            
            
            y = str(y)
            y = y.split('<span>')[1]
            #print(x)
            y = y.split(',')[0]
            #print(x)
            y = y.split('<')[0]
            meanings += y + '/'
            
    
    if len(meanings) > 0: meanings = meanings[:-1]
        
    return {'kunyomi': kunyomi, 'onyomi': onyomi, 'wk_level': wk_level, 'jlpt': jlpt, 'meanings': meanings}
    
def search_word(search_item):
    # Searches WORDS, not kanji 
    text = requests.get("https://jisho.org/api/v1/search/words?keyword=" + search_item).text

    res = json.loads(text)
    
    if res['meta']['status'] != 200:
        print('Error: Could not access search results by API.')
        return None

    if res['data']: 
        res = res['data'][0]

        
        
        out =  {'meanings':  str('/'.join(res['senses'][0]['english_definitions']).strip()),\
                'wk_level': -1,\
                'jlpt':     None,\
                'reading':  None}
                
        for tag in res['tags']:
            if 'wanikani' in tag:
                wk_level = int(tag.split('wanikani')[1])
                out['wk_level'] = wk_level
                
        if res['jlpt']:
            out['jlpt'] = res['jlpt'][0][-2:].upper()
            
        if res['japanese']:
            if 'reading' in res['japanese'][0]:
                out['reading'] = str(res['japanese'][0]['reading'])
                
            
            
        return out
        
    return {'meanings': 'Name', 'wk_level': -1, 'jlpt': None, 'reading': None}
        
           
def search_jisho(search_item, is_word: bool):
    
    if is_word: return search_word(search_item)
        
    return search_kanji(search_item)
    
        
if __name__ == "__main__":

    print(search_jisho('歩く', is_word=True))
    print(search_jisho('気を付けて', is_word=True))
    
    print(search_jisho('丁', is_word=False))
    print(search_jisho('車', is_word=False))

    
    
    
