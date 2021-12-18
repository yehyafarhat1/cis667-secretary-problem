import number_helpers

if __name__ == "__main__":
    path1 = "../data/first_training_set.csv"
    path2 = "../data/second_training_set.csv"
    path3 = "../data/third_training_set.csv"
    path4 = "../data/fourth_training_set.csv"
    path5 = "../data/fifth_training_set.csv"
    sentences = []
    sen1 = number_helpers.augment_sentences(path1, 10)
    sen2 = number_helpers.augment_sentences(path2, 10)
    sen3 = number_helpers.augment_sentences(path3, 10)
    sen4 = number_helpers.augment_sentences(path4, 10)
    sen5 = number_helpers.augment_sentences(path5, 10)

    sentences.extend(sen1)
    sentences.extend(sen2)
    sentences.extend(sen3)
    sentences.extend(sen4)
    sentences.extend(sen5)

    print(sentences[:5])
    print(
        '------------------------------------------------------------------------------------------------------------------------')
    print('length:  ' + str(len(sentences)))

    # Make a dictionary mapping each word to a one-hot tensor
    words = set()
    for sentence in sentences:
        for word in sentence:
            # for word in sentence.split(" "):
            words.add(word)
    words = tuple(words)  # deterministic order

    print(words[:5])

    for sentence in sentences:
        #tokens = sentence.split(" ")
        tokens = sentence
    # PyTorch LSTM expects 3d tensors representing (sequence length, batch size, number of features)
    # I = tr.eye(len(words))
    # dictionary = {
    #     word: I[w].reshape(1, 1, len(words))
    #     for w, word in enumerate(words)}

    # print(len(dictionary))

    strategy = input("To start the test case, input a number to determine which strategy to use.\r\n"
                     "Input non-number other numbers which are not included into this hints "
                     "to exit without running any experiments;\r\n"
                     "input 0 to start all the pre-set experiments automatically;\r\n"
                     "input 1 to start interactive experiments.;\r\n"
                     "")  # Python 3
    # raw_input("......")  # Python 2