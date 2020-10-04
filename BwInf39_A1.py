fname = 'raetsel4.txt'

def read_file(fname):
    # reads a file and returns a text string and a word tuple
    with open('beispieldaten/'+fname, 'r') as fin:
        text = fin.readline().strip().split()
        text_list = text.copy()
        for i in range(len(text)):
            text_list[i] = text_list[i].strip(',!.?:;')
        words_list = fin.readline().split()
    return text, text_list, words_list


def replace_word(new_tuple, text_list):
    # tuple = word, word with _
    # text = text as list with , ! usw.
    word, word_ = new_tuple
    for i in range(len(text_list)):
        if text_list[i].strip(',!.?:;') == word_:
            new_word = word + text_list[i][len(word):]
            text_list[i] = new_word
    return text_list
    

def remove_word(new_tuple, text_strip_list, word_list):
    a, b = new_tuple
    word_list.remove(a)
    text_strip_list.remove(b)
    return text_strip_list, word_list


def word_is_word_(word, word_):
    for i in range(len(word_)):
        if word_[i] != '_' and word_[i] != word[i]:
            return False
    return True


def find_hits(word, text_strip_list):
    result = []
    for word_ in text_strip_list:
        if len(word) == len(word_) and '_' in word_:
            if word_is_word_(word, word_):
                result.append((word, word_))
    return result


def find_hits_rev(word_, word_list):
    result = []
    for word in word_list:
        if len(word) == len(word_) and '_' in word_:
            if word_is_word_(word, word_):
                result.append((word, word_))
    return result



# the main program
text_list, text_strip_list, word_list = read_file(fname)


while True:
    
    for word in word_list:
        hits_list = find_hits(word, text_strip_list)
        if len(hits_list) == word_list.count(hits_list[0][0]):
            for hit in hits_list:
                text_list = replace_word(hit, text_list)
                text_strip_list, word_list = remove_word(hit, text_strip_list, word_list)
    
    for word_ in text_strip_list:
        hits_list = find_hits_rev(word_, word_list)
        if len(hits_list) == word_list.count(hits_list[0][0]):
            for hit in hits_list:
                text_list = replace_word(hit, text_list)
                text_strip_list, word_list = remove_word(hit, text_strip_list, word_list)

    if not text_strip_list:
        break

print(' '.join(text_list))





