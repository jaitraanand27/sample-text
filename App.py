words = "aabbccdd"
def count_letters(word):
    output = {}
    for i in word:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1
    return output
print(count_letters("aabbccdd"))