import sys

def find_words(wordlist, letters, ctr_letter):

    answers = []

    for w in wordlist:
        word = w.lower().strip()

        if ctr_letter not in word:
            continue

        bad = False
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        bad_letters = ''.join([l for l in alphabet if l not in letters])

        for l in word:
            if l in bad_letters:
                bad = True
        if bad:
            continue
        else:
            answers.append(word)

    return answers


def find_pangrams(answers, letters):
    pangrams = []
    
    for word in answers:
        bad = False
        for l in letters:
            if l not in word:
                bad = True
        if bad:
                continue


def print_answers(answers):
    return


def main(wordlist_file):

    with open(wordlist_file, 'r') as wordlist:
        wl = wordlist.readlines()

        letters_input = input('Please enter the 7 letters with the central yellow letter capitalized: ')
        ctr_letter = [l for l in letters_input if l.isupper()][0]
        letters = letters_input.lower()

        answers = find_words(wl, letters, ctr_letter)
        print_answers(answers)

    return



if __name__ == "__main__":
    main(sys.argv[1])