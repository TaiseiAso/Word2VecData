# Word2VecData
***
## 概要
単語の分散表現Word2Vecのモデルのためのコーパスを作成し学習するツール。

## 要件
- python3
- gensim
- pyyaml

## 使い方
1. "data/" フォルダを "corpus.py" などと同階層に作成する。

2. Word2Vecの学習データをすべて "data/" に保存する。

3. Word2Vecの学習に用いるコーパスが作成されて "corpus/" に保存される。
    ```
    $ python corpus.py
    ```
    保存されるファイル名は、 "config/config.yml" に保存した名前になる。

4. Word2Vecのモデルが学習されて "model/" に保存される。
    ```
    $ python word2vec.py
    ```
    学習方法やモデルの設定は、 "config/config.yml" を編集することで変更できる。
    保存されるモデル名は、 "config/config.yml" に保存した名前になる。

5. データをすべて削除する。
    ```
    $ python clear.py
    ```

## 設定
"config/config.yml" の各値の説明は以下の通り。

- filename: 保存されるファイルの名前 (文字列)
    - corpus_file: 学習に用いるコーパス
    - model_file: 学習モデル
- token: 特殊記号 (文字列)
    - sos: 開始トークン
- train: 学習モデルの設定 (整数)
    - sg: 学習アルゴリズム（1ならskip-gram, その他CBOW）
    - size: 単語ベクトルの次元数
    - min_count: この値よりも出現頻度の低い単語をカットする
    - window: window size（どれだけ広く前後の単語をとるか）
    - iter: 学習エポック回数
