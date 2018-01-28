import itertools


WATERBLUE = 'waterblue'
FLOWERED = 'flowered'
GRAY = 'gray'
STARRED = 'starred'

FLEECY = 'fleecy'
BLUE = 'blue'
BLACK = 'black'


def generate_perms(first, second):
    return itertools.permutations(itertools.permutations(range(second)), first)


def generate_seqs(first, second):
    perms = generate_perms(first, second)
    for perm in perms:
        seq = list()
        for item in perm:
            seq += list(item)
        yield seq


def generate_filtered_seqs(first, second):
    seqs = generate_seqs(first, second)
    for seq in seqs:
        ind = second
        while ind < len(seq):
            if seq[ind] == seq[ind - 1]:
                break
            ind += second
        else:
            yield translate_seq(seq, first, second)


def find_best_seq(first, second):
    first, second = sorted([first, second])

    highest_mark = -float('inf')
    best_seqs = list()

    # i = 1
    for seq in generate_filtered_seqs(first, second):
        # print(i)
        # i += 1
        # print(seq)
        mark = evaluate_seq(seq)
        if mark > highest_mark:
            highest_mark = mark
            best_seqs = [seq]
        elif mark == highest_mark:
            best_seqs.append(seq)

    return highest_mark, best_seqs


def evaluate_seq(seq):
    evaluator = {((BLACK, GRAY), (FLEECY, WATERBLUE), (BLUE, FLOWERED), (FLEECY, STARRED)): 1,
                 ((BLACK, STARRED), (BLACK, FLOWERED), (FLEECY, FLOWERED), (BLUE, GRAY), (BLUE, WATERBLUE)): -1}

    mark = 0
    for item in seq:
        for key in evaluator:
            if item in key:
                mark += evaluator[key]
    return mark


def translate_seq(raw_seq, first, second):
    values = {0: WATERBLUE, 1: FLOWERED, 2: GRAY, 3: STARRED}
    indices = {ind: ((FLEECY, BLUE, BLACK) * 4)[ind] for ind in range(first * second)}
    seq = list()
    for ind in range(len(raw_seq)):
        seq.append((indices[ind], values[raw_seq[ind]]))
    return seq


if __name__ == '__main__':
    m, sqs = find_best_seq(4, 3)
    # print(m)
    # print()
    # for sq in sqs:
    #     print(sq)
    #     print()
    m1, sqs1 = find_best_seq(3, 4)
    # print(m)
    # print()
    # for sq in sqs:
    #     print(sq)
    #     print()
    print(len(sqs), len(sqs1), m, m1)
    # sqs1 = [[(i[1], i[0]) for i in sq] for sq in sqs1]
    for s in sorted(sqs):
        if s in sqs1:
            sqs1.remove(s)
        else:
            print(s)
    print()
    print()
    for sq in sorted(sqs1):
        print(sq)
