def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if length > 0 else None
    return length, first


sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)

if __name__ == "__main__":
    print("Length: {:d} - First character: {}".format(length, first))