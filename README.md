# Docswell Downloader

[![pre-commit](https://github.com/11nu/docswell_downloader/actions/workflows/pre-commit.yaml/badge.svg?event=push)](https://github.com/11nu/docswell_downloader/actions/workflows/pre-commit.yaml)

スライドシェアサービス「[ドクセル（Docswell）](https://www.docswell.com/)」のスライドをダウンロードするためのツールです。

ダウンロードが許可されているスライドを CLI 経由でダウンロードするときにお使いください。

実装上、ダウンロードが許可されていないスライドもダウンロードできますが、ドクセルの[利用規約](https://www.docswell.com/note/terms)の禁止事項に抵触する可能性が高いので、**自己責任**のもとで利用してください。

現時点では、非公開のスライドのダウンロードには対応していません。

## 使い方

### 1. 依存関係をインストールする（初回のみ）

```shell
pip install -r requirements.txt
```

### 2. `docswell_downloader.py` を開き、変数 `slide_url` の値をダウンロードしたいスライドの URL に変更する

例：

```python
slide_url = "https://www.docswell.com/s/ku-suke/LK7J5V-hello-docswell"
```

### 3. `docswell_downloader.py` を実行する

```shell
python docswell_downloader.py
```

結果として、 `output` ディレクトリ内にスライドの PDF ファイルが生成されます。

## ドクセル関係者の方へ

本リポジトリの公開に問題がある場合は、 Issue でその旨をお伝えください。

関係者の GitHub アカウントであることの確認が取れ次第、早急に非公開等の然るべき対応を取らせていただきます。

## License

Copyright (c) 2022 [@11nu](https://github.com/11nu). All rights reserved.

Licensed under the [Apache License, Version 2.0](LICENSE.txt).
