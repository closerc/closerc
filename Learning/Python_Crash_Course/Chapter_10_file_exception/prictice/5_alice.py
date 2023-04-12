# 处理文件找不到异常

filename = r'Chapter_10_test_file\alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename.split('\\')[-1] + " has about " + str(num_words) + " words.")
