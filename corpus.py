##################################################
# Word2Vecの学習用コーパスを作成する
# 実装開始日: 2019/4/15
# 実装完了日: 2019/4/15
# 実行方法: $ python corpus.py
##################################################

# 必要なモジュールのインポート
import glob, os

if not os.path.isdir("corpus"):
    os.mkdir("corpus")

# corpusフォルダ内のファイルをすべて削除
for root, _, files in os.walk("corpus", topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))

# dataフォルダ内のファイルに<SOS>トークンを追加してcorpusフォルダに保存
files = glob.glob("data/*")
for file in files:
    with open(file, 'r', encoding='utf-8') as f_in,\
    open("corpus/corpus.txt", 'a', encoding='utf-8') as f_out:
        line = f_in.readline()
        while line:
            if line != "\n":
                f_out.write("<SOS> " + line)
            line = f_in.readline()
