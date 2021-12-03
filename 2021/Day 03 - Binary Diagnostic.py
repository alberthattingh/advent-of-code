def readLines():
    numbers = []

    with open('2021/input/Day03.txt') as f:
        for line in f.readlines():
            numbers.append(line.strip())

    return numbers


def getBitCount(diagnostics):
    bitCounters = [0 for i in range(12)]
    for binary in diagnostics:
        for index in range(len(binary)):
            if binary[index] == '1':
                bitCounters[index] += 1

    return bitCounters


def s1():
    diagnostics = readLines()
    bitCounters = getBitCount(diagnostics)    

    gammaRate = ''.join(['1' if bits > len(diagnostics) - bits else '0' for bits in bitCounters])
    epsilonRate = ''.join(['1' if bits <= len(diagnostics) - bits else '0' for bits in bitCounters])

    print(f'Solution 1: {int(gammaRate, 2) * int(epsilonRate, 2)}')


def s2():
    diagnostics = readLines()
    o2GeneratorRating = None
    co2ScrubberRating = None

    filtered = diagnostics
    for index in range(12):
        bits = getBitCount(filtered)[index]
        bit = '1' if bits >= len(filtered) - bits else '0'
        if len(filtered) > 1:
            filtered = list(filter(lambda binary: binary[index] == bit, filtered))
        else:
            o2GeneratorRating = filtered[0]
            break

    filtered = diagnostics
    for index in range(12):
        bits = getBitCount(filtered)[index]
        bit = '1' if bits < len(filtered) - bits else '0'
        if len(filtered) > 1:
            filtered = list(filter(lambda binary: binary[index] == bit, filtered))
        else:
            co2ScrubberRating = filtered[0]
            break

    print(f'Solution 2: {int(o2GeneratorRating, 2) * int(co2ScrubberRating, 2)}')
        



if __name__ == '__main__':
    s1()
    s2()