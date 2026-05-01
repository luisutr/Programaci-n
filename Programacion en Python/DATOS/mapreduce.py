def map(in_text):
     in_text = in_text.strip() # Removemos espacios en extremos
     words = in_text.split() # Separamos por palabra
     for w in words:
        print("{}\t{}".format(w, 1)) # Palabra w aparece una vez
map("Maria esta contenta, porque Maria ve que hace sol. Los dias de sol Maria esta contenta.")


def reduce(in_stream):
    current_word = None
    count = 0
    for w, c in in_stream:
        if w != current_word:
            if current_word is not None:
                print("{}\t{}".format(current_word, count))
            current_word = w
            count = 0
        count += int(c)