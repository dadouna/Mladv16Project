import argparse

from text_classifier import buildGramMat as bgm
from simple_data import VERY_SIMPLE_DATA
from utils import load_data, write_data


def get_gram_matrices(x, y, n, l):
    print("starting x, x", len(x))
    X = bgm(x, x, l, n)
    print("starting x, y", len(x), len(y))
    Y = bgm(x, y, l, n)
    return X, Y


def _get_gram_file_name(i, n, l):
    return "grams/gram-{}-n{}-l{}.json".format(i, n, l)


def write_gram_to_file(i, n, l, X, Y):
    data = {"i": i, "n": n, "l": l, "X": X.tolist(), "Y": Y.tolist()}
    write_data(_get_gram_file_name(i, n, l), data)


def read_gram_from_file(i, n, l):
    data = load_data(_get_gram_file_name(i, n, l))
    return data


def save_grams_to_file(i, n, l):
    if i >= 0:
        ds = [VERY_SIMPLE_DATA[i]]
    else:
        ds = VERY_SIMPLE_DATA

    for i, d in zip(range(len(ds)), ds):
        X, Y = get_gram_matrices(d["train"]["x"], d["test"]["x"], n, l)
        write_gram_to_file(i, n, l, X, Y)
        print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Compute and save gram matrices for SIMPLE_DATA")
    parser.add_argument("n", type=int)
    parser.add_argument("l", type=float)
    parser.add_argument("-i", type=int, default=-1)

    res = parser.parse_args()
    save_grams_to_file(res.i, res.n, res.l)

