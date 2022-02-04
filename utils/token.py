import re
largest_count = 0
freq = {}

def tokenize(file_text, url):  # content should be string or file?
    global largest_count
    page_total_count = 0
    listt = []
    lineplus = re.sub(r'[^A-Za-z0-9]+', ' ', file_text)
    listt += lineplus.lower().split()

    stop_word_list = ['means', 'every', 'thence', 'truly', 'many', 'despite', 'now', 'self', 'such',
                      'followed', 'mug', 'somethan', 'mustn', 'hes', 'immediately', 'sufficiently', 'upon', 'uses',
                      'alone',
                      'anyhow', 'inc', 'said', 'most', 'serious', 'ca', 'appreciate', 'anyways', 'our', 'contain',
                      'shouldn',
                      'hasn', 'kg', 'these', 'want', 'then', 'who', 'let', 'rather', 'e', 'stop', 'two', 'willing',
                      'themselves',
                      'gets', 'unlikely', 'ah', 'showns', 'anything', 'from', 'whence', 'different', 'non', 'slightly',
                      'b',
                      'nos', 'www', 'considering', 'overall', 'shed', 'specifically', 'lets', 'whats', 'are', 'll',
                      'pages',
                      'which', 'instead', 'allows', 'weren', 'ever', 'seriously', 'five', 'theyd', 'only', 'anybody',
                      'couldnt',
                      'the', 'keep', 'v', 'took', 'via', 'formerly', 'before', 'hadn', 'welcome', 'found',
                      'significantly', 'fix',
                      'seven', 'plus', 'previously', 'promptly', 'may', 'consider', 'has', 'away', 'think', 'affects',
                      'quickly',
                      'fifth', 'three', 'too', 'old', 'few', 'ninety', 'twice', 'new', 'become', 'against', 'on',
                      'afterwards',
                      'throug', 'wed', 'appear', 'gone', 'hereafter', 'didn', 'some', 'being', 'whether', 'regarding',
                      'except',
                      'secondly', 'happens', 'i', 'ourselves', 'seemed', 'whereas', 'similarly', 'don', 'begins',
                      'provides',
                      'werent', 'kept', 'r', 'per', 'wouldn', 'without', 'meantime', 'insofar', 'own', 'along', 'eight',
                      'relatively',
                      'thereby', 'sorry', 'mr', 'made', 'use', 'value', 'yes', 'keeps', 'thus', 'obtain', 'anyone',
                      'came', 'oh',
                      'theyre', 'unfortunately', 'both', 'whither', 'briefly', 'especially', 'ok', 'outside', 'saw',
                      'won', 'gave',
                      'yourselves', 'nay', 'latter', 'its', 'nobody', 'after', 'get', 'tried', 'course', 'to',
                      'thereupon', 'mean',
                      'arise', 'predominantly', 'y', 'aside', 'regardless', 'nothing', 'yet', 'downwards', 'im',
                      'significant',
                      'sure', 'ran', 've', 'hardly', 'beyond', 'how', 'already', 'below', 'w', 'thereof', 'entirely',
                      'went', 'often',
                      'important', 'hereupon', 'know', 'as', 'readily', 'indicate', 'p', 'wheres', 'immediate',
                      'million', 'nor',
                      'having', 'substantially', 'co', 'ex', 'inner', 'several', 'besides', 'lest', 'wherein',
                      'sometime', 'date',
                      'youre', 'back', 'following', 'try', 'til', 'him', 'there', 'what', 'since', 'four', 'nearly',
                      'ones', 'heres',
                      'was', 'km', 'look', 'more', 'c', 'affecting', 'hers', 'believe', 'near', 'primarily', 'added',
                      'available',
                      'ord', 'th', 'seeming', 'her', 'containing', 'contains', 'exactly', 'n', 'possibly',
                      'approximately', 'line',
                      'once', 'unto', 'world', 'behind', 's', 'ed', 'a', 'herein', 'sub', 'well', 'ending', 'come',
                      'perhaps', 'vols',
                      'obtained', 'tip', 'z', 'actually', 'towards', 'of', 'looks', 'due', 'quite', 'id', 'my',
                      'effect', 'always',
                      'hundred', 'information', 'allow', 'obviously', 'na', 'those', 'indeed', 'similar', 'off',
                      'anymore', 'do',
                      'is', 'sensible', 'best', 'where', 'it', 'somewhere', 'need', 'therere', 'thousand', 'lately',
                      'better',
                      'reasonably', 'like', 'soon', 'us', 'thanks', 'indicated', 'adj', 'ml', 'importance', 'whod',
                      'usually',
                      'hi', 'past', 'resulting', 'associated', 'whos', 'in', 'vs', 'under', 'probably', 'ought',
                      'somehow', 'each',
                      'consequently', 'any', 'giving', 'suggest', 'wasnt', 'another', 'says', 'others', 're', 'refs',
                      'way', 'needs',
                      'something', 'j', 'among', 'likely', 'placed', 'wants', 'hid', 'make', 'though', 'taking',
                      'hereby', 'were',
                      'for', 'because', 'specifying', 'hopefully', 'widely', 'biol', 'rd', 'otherwise', 'act',
                      'ignored', 'okay',
                      'brief', 'nowhere', 'indicates', 'anyway', 'possible', 'whenever', 'far', 'yours', 'still',
                      'asking', 'their',
                      'arent', 'everybody', 'ask', 'next', 'that', 'f', 'moreover', 'usefulness', 'shows', 'normally',
                      'through',
                      'had', 'about', 'he', 'whim', 'goes', 'able', 'tries', 'me', 'presumably', 'h', 'thorough', 'am',
                      'hello',
                      'k', 'by', 'namely', 'your', 'least', 'youd', 'concerning', 'inward', 'invention', 'becomes',
                      'hed', 'shan',
                      'whomever', 'using', 'thank', 'say', 'we', 'becoming', 'zero', 'corresponding', 'etc', 'itself',
                      'q', 'done',
                      'given', 'poorly', 'ff', 'u', 'apart', 'greetings', 'awfully', 'que', 'again', 'shown', 'please',
                      'qv', 'than',
                      'showed', 'thou', 'clearly', 'can', 'around', 'seeing', 'thats', 'until', 'whole', 'described',
                      'g', 'liked',
                      'apparently', 'aren', 'eg', 'must', 'onto', 'wonder', 'howbeit', 'however', 'haven', 'someone',
                      'l', 'and',
                      'not', 'whereby', 'resulted', 'according', 'mon', 'necessary', 'why', 'sometimes', 'beside',
                      'mrs', 'words',
                      'somewhat', 'wish', 'beginning', 'noone', 'will', 'them', 'here', 'merely', 'mostly', 'saying',
                      'ie',
                      'recently', 'further', 'certainly', 'whereafter', 'isn', 'therein', 'affected', 'present',
                      'cause',
                      'but', 'certain', 'recent', 'does', 'at', 'wherever', 'omitted', 'largely', 'selves', 'whom',
                      'just', 'you',
                      'al', 'run', 'first', 'inasmuch', 'see', 'ours', 'taken', 'viz', 'cannot', 'right', 'myself',
                      'across', 'no',
                      'particularly', 'ain', 'meanwhile', 'tends', 'give', 'take', 'elsewhere', 'theres', 'related',
                      'couldn',
                      'third', 'herself', 'getting', 'throughout', 'thanx', 'ltd', 'currently', 'pp', 'everywhere', 'o',
                      'last',
                      'home', 'they', 'successfully', 'follows', 'toward', 'she', 'doing', 'wasn', 'nevertheless',
                      'definitely',
                      'end', 'amongst', 'enough', 'same', 'particular', 'beforehand', 'later', 'also', 'would',
                      'furthermore',
                      'little', 'latterly', 'abst', 'specify', 'when', 'became', 'did', 'very', 'whoever', 'wont',
                      'mainly',
                      'results', 'vol', 'part', 'comes', 'show', 'together', 'anywhere', 'nd', 'sup', 'ref', 'et',
                      'trying',
                      'eighty', 'this', 'thru', 'beginnings', 'sent', 'sec', 'into', 'x', 'changes', 'com', 'useful',
                      'over',
                      'miss', 'himself', 'nonetheless', 'used', 'might', 'neither', 'less', 'accordance', 'somebody',
                      'be',
                      'wouldnt', 'regards', 'index', 'hence', 'down', 'page', 'shall', 'go', 'unless', 'between',
                      'owing',
                      'respectively', 'proud', 'almost', 'announce', 'everything', 'his', 'therefore', 'unlike',
                      'whose', 't',
                      'thoroughly', 'with', 'else', 'really', 'put', 'seem', 'out', 'within', 'mg', 'gives', 'hither',
                      'un', 'so',
                      'specified', 'former', 'thoughh', 'research', 'example', 'none', 'tell', 'whatever', 'section',
                      'shes',
                      'everyone', 'usefully', 'strongly', 'itd', 'potentially', 'much', 'seems', 'have', 'seen',
                      'appropriate',
                      'knows', 'accordingly', 'gotten', 'auth', 'noted', 'help', 'one', 'begin', 'while', 'various',
                      'been', 'd',
                      'theirs', 'novel', 'looking', 'makes', 'all', 'if', 'above', 'thereto', 'necessarily', 'nine',
                      'name',
                      'known', 'ts', 'never', 'up', 'got', 'ups', 'or', 'doesn', 'even', 'yourself', 'thereafter',
                      'should',
                      'during', 'either', 'going', 'edu', 'could', 'six', 'although', 'an', 'causes', 'forth', 'second',
                      'thered', 'maybe', 'm', 'other', 'whereupon', 'cant']

    newlis = []
    for word in listt:
        page_total_count += 1
        if word not in stop_word_list:
            newlis.append(word)
    # print(page_total_count) #part_b # then need to only record the highest count with the URL or content

    if page_total_count >= largest_count:
        largest_count = page_total_count
        part_b_url = url

        with open('part_b.txt', 'w') as file:
            file.write(f"Longest page: {part_b_url}, word count:{page_total_count}")

    return newlis


def computeWordFrequencies(ls):
    global freq
    for word in ls:
        if word not in freq.keys():
            freq[word] = 1
        else:
            freq[word] += 1

    dicnew = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

    with open('part_c.txt', 'w') as file:
        count = 0
        for key in dicnew:
            if count < 50:
                file.write('{} -> {}\n'.format(key, dicnew[key]))
            count += 1
    return freq  # part_c
