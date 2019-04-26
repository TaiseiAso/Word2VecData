# coding: utf-8

"""Word2Vecを学習する"""
__author__ = "Aso Taisei"
__version__ = "1.0.0"
__date__ = "25 Apr 2019"


# 必要なモジュールのインポート
import os
from gensim.models import word2vec
import yaml


def train(config):
    """
    word2vecを学習
    @param config 設定ファイル情報
    """
    fn = config['filename']
    corpus_file_path = "corpus/" + fn['corpus_file'] + ".txt"
    model_file_path = "model/" + fn['model_file'] + ".model"

    if not os.path.isdir("corpus"):
        print("no corpus folder")
        return

    if not os.path.isfile(corpus_file_path):
        print("no " + corpus_file_path + " file")
        return

    # modelフォルダがなければ作成する
    if not os.path.isdir("model"):
        os.mkdir("model")

    # modelフォルダ内のファイルをすべて削除
    for root, _, files in os.walk("model", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))

    # 学習データを1文ずつ読み込む
    sentences = word2vec.LineSentence(corpus_file_path)

    # モデルを学習
    tr = config['train']
    model = word2vec.Word2Vec(
        sentences,                  # 学習する文
        sg=tr['sg'],                # 学習アルゴリズム（1ならskip-gram, その他CBOW）
        size=tr['size'],            # 単語ベクトルの次元数
        min_count=tr['min_count'],  # この値よりも出現頻度の低い単語をカットする
        window=tr['window'],        # window size（どれだけ広く前後の単語をとるか）
        iter=tr['iter']             # 学習エポック回数
    )

    # モデルを保存
    model.save(model_file_path)


if __name__ == '__main__':
    # 設定ファイルを読み込む
    config = yaml.load(stream=open("config/config.yml", 'rt'), Loader=yaml.SafeLoader)

    # word2vecを学習
    train(config)
