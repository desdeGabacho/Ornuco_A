"""
Test A:
    Write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap.
    As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
"""
def test_assert(first_seg, second_seg):
    try:
        assert len(first_seg)==2
        assert len(second_seg)==2
        # many more statements like this
    except AssertionError:
        print ('\n','Houston, we have a problem.')
        print ('One of the segments does not follow the rules --> Invalid number of values')
        exit(1)
    try:
        assert first_seg[0] < first_seg[1]
        assert second_seg[0] < second_seg[1]
        # many more statements like this
    except AssertionError:
        print ('\n','Houston, we have a problem.')
        print ('One of the segments does not follow the rules. Mismatch boundaries')
        exit(1)


def overlap(first_seg, second_seg):
    A, B = first_seg
    C, D = second_seg

    return B>C and A<D


if __name__ == '__main__':
    first_seg_string = input("Enter the first segment (x, y): ")
    second_seg_string = input("Enter the second segment (x, y): ")

    first_segment = tuple(map(int, first_seg_string.split(',')))
    second_segment = tuple(map(int, second_seg_string.split(',')))

    test_assert(first_segment, second_segment)
    print(overlap(first_segment, second_segment))

