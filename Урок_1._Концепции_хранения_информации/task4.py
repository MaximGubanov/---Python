word_list = ['разработка', 'администрирование', 'protocol', 'standard']

for word in word_list:

    enc_word = word.encode()
    print(f'{word} - {type(word)} - {enc_word} - {type(enc_word)}')

    dec_word = enc_word.decode()
    print(f'{enc_word} - {dec_word} - {type(dec_word)}\n\n')