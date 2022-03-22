def get_top_ngramms(n, ktop, mytext, mywords):
    result = {}

    def count_anagramms(word):
        word_len = len(word)

        for i in range(word_len):
            if i + n > word_len:
                break

            anagramm = word[i:i + n]
            result.update({anagramm: mytext.count(anagramm)})

    for word in mywords:
        count_anagramms(word)

    while(len(result) > ktop):
        result_keys = list(result.keys())
        min_key = result_keys[0]

        for key in result_keys[1:]:
            if(result[key] < result[min_key]):
                min_key = key

        result.pop(min_key)

    return result


def main():
    while True:
        choice = input(
            "Enter '0' to write text, or '1' to read from .txt file:")
        if choice == '0':
            text = input("Enter text:")
            break
        elif choice == '1':
            with open("./text.txt", "r") as f:
                text = f.read()
                print(text)
            break
        else:
            print("Wrong choice!")

    sentences = 0
    count_word_in_sentences = []
    words_in_sentence = 1
    i = 1
    text = text.replace(",", " ")
    text = text.replace("...", " ")
    text = text.replace(";", " ")
    text = text.replace(":", " ")
    text = text.strip()

    for c in text:
        if (c == '.' or c == '!' or c == '?') and i < int(len(text)) - 1 and text[i+1] != ' ':
            text = text[:i] + " " + text[i:]
            i += 1
        i += 1

    i = 0

    for c in text:
        if c == ' ' and text[i+1] != ' ' and text[i+1] != '.' and text[i+1] != '!' and text[i+1] != '?':
            words_in_sentence += 1
        elif c == '.' or c == '!' or c == '?':
            sentences += 1
            count_word_in_sentences.append(words_in_sentence)
            words_in_sentence = 0
        i += 1

    count_word_in_sentences.sort()
    print(count_word_in_sentences)

    if len(count_word_in_sentences) % 2 == 0:
        median = (count_word_in_sentences[int(len(count_word_in_sentences) / 2)] +
                  count_word_in_sentences[int(len(count_word_in_sentences) / 2 - 1)]) / 2
    else:
        median = count_word_in_sentences[len(count_word_in_sentences)//2]

    print(f"Median value:{median}")
    text = text.lower()
    text = text.replace(".", " ")
    text = text.replace("!", " ")
    text = text.replace("?", " ")
    words = text.split()
    avg_count = len(words) / sentences
    print(f"Average value:{round(avg_count, 2)}")
    print(f"Count of sentences:{sentences}")
    uniqe_dict = {}

    for i in range(len(words)):
        uniqe_dict.update({words[i]: words.count(words[i])})

    print(f"Every word count:{uniqe_dict}")
    print(f"Top ngrams:{ get_top_ngramms(4, 10, text, words) }")


if __name__ == '__main__':
    main()
