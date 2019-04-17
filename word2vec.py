##################################################
# Word2Vecを学習する
# 実装開始日: 2019/4/15
# 実装完了日: 2019/4/15
# 実行方法: $ python word2vec.py
##################################################

# 必要なモジュールのインポート
import os
from gensim.models import word2vec

# 学習データを1文ずつ読み込む
sentences = word2vec.LineSentence("corpus/corpus.txt")

# モデルを学習
model = word2vec.Word2Vec(
    sentences,      # 学習する文
    sg=1,           # 学習アルゴリズム（1ならskip-gram, その他CBOW）
    size=256,       # 単語ベクトルの次元数
    min_count=5,    # この値よりも出現頻度の低い単語をカットする
    window=5,       # window size（どれだけ広く前後の単語をとるか）
    iter=10         # 学習エポック回数
)

# modelフォルダがなければ作成する
if not os.path.isdir("model"):
    os.mkdir("model")

# modelフォルダ内のファイルをすべて削除
for root, _, files in os.walk("model", topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))

# モデルを保存
model.save("model/word2vec.model")
