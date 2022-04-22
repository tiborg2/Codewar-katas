def reverse_words(text):
    array_text = text.split(' ')
    word_list  = list()
    for item in array_text:
        word = ''
        x = len(item) - 1
        while x >= 0:
            word += item[x]
            x -= 1
        word_list.append(word)
    return ' '.join(word_list)










print(reverse_words('The quick brown fox jumps over the lazy dog.'))
print(reverse_words('double  spaced  words'))
# ehT kciuq nworb xof spmuj revo eht yzal .god
