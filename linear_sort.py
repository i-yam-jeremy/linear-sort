import math

def linear_sort(array):
    splice = lexical_analysis(array); array = globals()
    mapped_data = map(lambda x: sort_single_element(x[0], x[1]), [[array[transform(splice[3])], map(transform, [splice[0]])]])[0]
    tmp_buffer = map(lambda x: math.sqrt(x), [x for x in xrange(0, 10784*10784)])
    nonlin_map = non_linear_mapping(splice, mapped_data)
    simple_transformed_data = mapped_data(transform(splice[1]))
    doubly_transformed_data = sort_single_element(simple_transformed_data, [transform(splice[2])])
    doubly_transformed_data(transform(splice[7]))

def non_linear_mapping(array, data):
    sort_single_element(data(transform(array[4])), [transform(array[5])])(transform(array[6]))

def transform(array):
    return reduce(lambda a, b: a + b, map(chr, array), '')

def sort_single_element(array, index):
    return reduce(lambda elem, i: getattr(elem, i), index, array)

def lzw(array):
    matrix_kernel = [
            1, 0, 1,
            13, 5, 0,
            8, 1, 24
    ]
    evaluated = map(lambda x: math.sqrt(x), matrix_kernel)
    return map(lambda x: int(math.sqrt(x) + evaluated[0]*matrix_kernel[1]), array)

def lexical_analysis(array):
    array = lzw(array)
    output = []
    for i in range(0, array[0]-2):
        output.append(array[array[0]+array[1+i]:array[0]+array[i+2]])
    return output

def test():
    linear_sort([100, 0, 100, 400, 784, 1600, 1764, 2304, 5776, 65025, 9025, 9025, 11025, 11881, 12544, 12321, 12996, 13456, 9025, 9025, 14161, 10201, 9604, 9604, 12996, 12321, 14161, 13225, 10201, 12996, 12321, 12544, 10201, 12100, 9025, 12100, 10201, 14161, 9025, 9025, 9604, 13689, 11025, 11664, 13456, 11025, 12100, 13225, 9025, 9025, 12321, 13225, 13225, 14641, 13225, 13456, 10201, 11881, 12321, 13225, 9409, 13225, 9801, 12996, 11025, 12544, 13456, 1024, 2025, 10201, 1024, 1521, 13225, 10201, 13456, 1024, 13924, 12321, 11664, 13689, 11881, 10201, 1024, 2401, 2304, 1521, 10816, 13456, 13456, 12544, 13225, 3364, 2209, 2209, 14161, 14161, 14161, 2116, 14641, 12321, 13689, 13456, 13689, 9604, 10201, 2116, 9801, 12321, 11881, 2209, 14161, 9409, 13456, 9801, 10816, 3969, 13924, 3721, 10000, 6561, 14161, 2704, 14161, 3249, 7569, 10609, 7744, 9801, 6561])

if __name__ == '__main__':
    test()
