def format_output(i):
    return '%d' % i

def cut_end(list):
    new_end = len(list)
    last = list[new_end - 1]
    for i in range(len(list) - 2, 1, -1):
        if last != list[i]:
            new_end = i + 1
            break
    return list[:new_end]

def build_relevant_list(input):
    data = input.split("\n")
    n, m = data[0].split(' ')
    n = int(n)
    m = int(m)

    list = []
    for i in range(n):
        list.append(int(data[1 + i]))

    result = [0]
    return ' '.join(map(format_output, result))

if __name__ == '__main__':
    print(build_relevant_list(sys.stdin.read()))