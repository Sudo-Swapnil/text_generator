from nltk.tokenize import WhitespaceTokenizer


def corpus_stats(tokens_list):
    print("Corpus statistics:")
    print(f"All tokens: {len(tokens_list)}")
    print(f"Unique tokens: {len(set(tokens_list))}")


def word_at_index(tokens_list, index):
    error_text = ""
    word = ""
    try:
        word = tokens_list[int(index)]
    except IndexError:
        error_text = "Index Error. Please input an integer that is in the range of the corpus"
    except (TypeError, ValueError):
        error_text = "Type Error. Please input an integer"
    finally:
        if len(error_text) == 0:
            return word
        return error_text


def bigram_at(bigrams_list, index):
    error_text = ""
    word = ""
    try:
        bigram = bigrams_list[int(index)]
        print(f"Head: {bigram[0]} \tTail: {bigram[1]}")
    except IndexError:
        error_text = "Index Error. Please input a value that is not greater than the number of all bigrams."
    except (TypeError, ValueError):
        error_text = "Typerror. Please input an integer"
    finally:
        if len(error_text) == 0:
            return word
        return error_text


def generate_bigrams(tokens_list):
    bigrams = [[tokens_list[i], tokens_list[i + 1]] for i in range(len(tokens_list) - 1)]
    print("Number of bigrams: " + str(len(bigrams)))
    return bigrams


def main():
    input_file = input()
    corpus_file = open(input_file, "r", encoding="utf-8")
    corpus_data = corpus_file.read()
    white_space_tokenizer = WhitespaceTokenizer()
    data_list = white_space_tokenizer.tokenize(corpus_data)
    bigrams = generate_bigrams(data_list)
    print()
    while True:
        user_input = input()
        if user_input != 'exit':
            print(bigram_at(bigrams, user_input))
        else:
            break
    corpus_file.close()


if __name__ == '__main__':
    main()