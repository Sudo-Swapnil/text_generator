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


def main():
    input_file = input()
    corpus_file = open(input_file, "r", encoding="utf-8")
    corpus_data = corpus_file.read()
    white_space_tokenizer = WhitespaceTokenizer()
    data_list = white_space_tokenizer.tokenize(corpus_data)
    corpus_stats(data_list)
    print()
    while True:
        user_input = input()
        if user_input != 'exit':
            print(word_at_index(data_list, user_input))
        else:
            break
    corpus_file.close()


if __name__ == '__main__':
    main()
