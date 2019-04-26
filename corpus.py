# coding: utf-8

"""Word2Vecの学習用コーパスを作成する"""
__author__ = "Aso Taisei"
__version__ = "1.0.0"
__date__ = "25 Apr 2019"


# 必要なモジュールのインポート
import glob
import os
import yaml


def corpus(config):
    """
    1つ以上のデータからword2vec学習用のコーパスを作成
    @param config 設定ファイル情報
    """
    corpus_file_path = "corpus/" + config['filename']['corpus_file'] + ".txt"
    sos_token = config['token']['sos']

    if not os.path.isdir("data"):
        print("no data folder")
        return

    # corpusフォルダがなければ作成する
    if not os.path.isdir("corpus"):
        os.mkdir("corpus")

    # corpusフォルダ内のファイルをすべて削除
    for root, _, files in os.walk("corpus", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))

    # dataフォルダ内のファイルに開始トークンを追加してcorpusフォルダに保存
    files = glob.glob("data/*")

    if files == []:
        print("no data file")
        return

    for file in files:

        with open(file, 'r', encoding='utf-8') as f_in,\
        open(corpus_file_path, 'a', encoding='utf-8') as f_out:

            line = f_in.readline()

            while line:
                if line != "\n":
                    f_out.write(sos_token + " " + line)

                line = f_in.readline()


if __name__ == '__main__':
    # 設定ファイルを読み込む
    config = yaml.load(stream=open("config/config.yml", 'rt'), Loader=yaml.SafeLoader)

    # 1つ以上のデータからword2vec学習用のコーパスを作成
    corpus(config)
