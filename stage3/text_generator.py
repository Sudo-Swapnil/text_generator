from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
import random


def generate_trigrams(tokens_list):
    trigrams = [[tokens_list[i], tokens_list[i + 1], tokens_list[i + 2]] for i in range(len(tokens_list) - 2)]
    return trigrams


def generate_head_tail_freq_dict(trigrams):
    head_tails_dict = {}
    head_tails_freq_dict = {}
    for head1, head2, tail in trigrams:
        head = head1 + " " + head2
        head_tails_dict.setdefault(head, []).append(tail)
    for head, tails_list in head_tails_dict.items():
        head_tails_freq_dict[head] = dict(Counter(tails_list).most_common())
    return head_tails_freq_dict


def print_tails_of(head_tails_freq_dict, key):
    print(f"Head: {key}")
    if key in head_tails_freq_dict.keys():
        tails_dict = head_tails_freq_dict[key]
        for tail, count in tails_dict.items():
            print(f"Tails: {tail}\tCount: {count}")
    else:
        print("Key Error. The requested word is not in the model. Please input another word.")


def print_sent(head_tails_freq_dict, data_list):
    tokens = []
    terminals = ['!', '.', '?']
    word = random.choice(list(head_tails_freq_dict.keys())).split()
    while True:
        if word[0][0].istitle() and word[0][-1] not in terminals and word[1][0].islower() and word[1][-1] not in terminals:
            break
        else:
            word = random.choice(list(head_tails_freq_dict.keys())).split()
    word = ' '.join(word)
    tokens.append(word)
    while True:
        words_list = [key for key in head_tails_freq_dict[word].keys()]
        weight = [value for value in head_tails_freq_dict[word].values()]
        new_word = random.choices(words_list, weight, cum_weights=None, k=1)[0]
        if new_word.istitle() and word[1][-1] in terminals:
            continue
        tokens.append(new_word)
        word = word.split()
        word[0] = word[1]
        word[1] = new_word
        word = ' '.join(word)
        if word[-1][-1] in terminals and len(tokens) > 3:
            break
    for _word in tokens:
        print(_word, end=' ')
    print()


def main():
    input_file = input()
    corpus_file = open(input_file, "r", encoding="utf-8")
    corpus_data = corpus_file.read()
    white_space_tokenizer = WhitespaceTokenizer()
    data_list = white_space_tokenizer.tokenize(corpus_data)
    trigrams = generate_trigrams(data_list)
    head_tails_freq_dict = generate_head_tail_freq_dict(trigrams)
    sent_count = 10
    while sent_count != 0:
        print_sent(head_tails_freq_dict, data_list)
        sent_count -= 1
    corpus_file.close()


if __name__ == '__main__':
    main()
