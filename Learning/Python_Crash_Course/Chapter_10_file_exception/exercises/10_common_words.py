# 计算单词在文件中出现的次数

def count_words(filename, word):
    """计算单词在文件中出现的次数

    Args:
        filename (str): 文件名
        word (str): 单词
    """
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename.split('\\')[-1] + "does not exist."
        print(msg)
    else:
        count = contents.lower().count(word)
        print("The word " + word + " appears " + str(count) + " times in the file " + filename.split('\\')[-1])


word = 'the'
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
for filename in filenames:
    file_path = r'Chapter_10_test_file'
    file_path = file_path + '\\' + filename
    count_words(file_path, word)
