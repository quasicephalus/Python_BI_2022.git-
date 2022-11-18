import seaborn as sns
import re
from urllib import request
from matplotlib import pyplot as plt

# 1
ref_url = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references'
with request.urlopen(ref_url) as r, open('ftps', 'w') as ftps:
    # Its line by line
    # For some reason if decode line with .decode('UTF-8') it works like 100 times slower, so I decided to let it be
    ref = str(r.readline())
    while ref != "b''":
        match = re.findall(r'ftp\.[^\t;\\]*', ref)
        for m in match:
            ftps.write(m + '\n')
        ref = str(r.readline())

ad_url = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD'
with request.urlopen(ad_url) as url:
    ad = url.read().decode('UTF-8')
# 2
    # just digits or digits separated with dot
    nums = re.findall(r'\d+\.\d+|\d+', ad)
    # print(nums)
# 3
    # Word (\b smth \b) with [Aa] and with any number of any symbols before or after [Aa]
    aaa = re.findall(r'\b\w*[aA]\w*\b', ad)
    # print(len(aaa))
    # print(aaa)
# 4
    # Find all exclamatory sentences
    excl = re.findall(r'[A-Z]\w*[^\.\n\t\?]*?!', ad)
    # print(excl)
# 5
    # Using set to get unique words (not including any digits)
    words = set(word.lower() for word in re.findall(r'\b[A-Za-z\']+\b', ad))
    # print(*sorted(list(words)), sep='\n')
    # print(len(words)) #932
    ln = [len(word) for word in words]  # For the histogram
    # Histogram in seaborn
    sns.histplot(x=ln, bins=15)
    plt.xlabel('word length')
    plt.ylabel('count in text')
    plt.title('Distribution of length of unique words')
    plt.show()


# 6
def brick_top(string):
    # Thanks to Nikita for the hint about fr strings!
    vows = 'АаЕеЁёИиОоУуЫыЭэЮюЯя'
    bricked = re.sub(fr'([{vows}])', r'\1к\1', string)
    return bricked


# Ходят слухи, что Кирпич любит избавляться от людей с помощью электрошокера,
# пластикового мешка, липкой ленты и своры голодных свиней.
#
# простите.....

# 7
# It's poorly tested and works really bad with apostrophes:
# the word with an apostrophe is divided by "\b" into two groups and in some cases will be present with both n and n+1
def find_n_words_sentences(string, n):
    # It really hard to put the end of the string in brackets,
    # so it seems like simplest way to get last sentence without "."
    if n == 0:
        return []
    string += '.'
    pattern = r'(?<![\w\"\:\-\,\;] )' + r'(\b[\w\d\']+\b)[ \"\:\-\,\;]*' * n + r'[\.\!\?]+'
    return re.findall(pattern, string)
