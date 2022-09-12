# Docswell Downloader

スライドシェアサービス「[ドクセル（Docswell）](https://www.docswell.com/)」のスライドをダウンロードするためのツール。

ダウンロードが許可されているスライドを CLI 経由でダウンロードするときにお使いください。

ダウンロードが許可されていないスライドをダウンロードする場合、ドクセルの[利用規約](https://www.docswell.com/note/terms)の禁止事項に抵触する可能性があるので、自己責任のもとで利用してください。

## 使い方

1. `docswell-downloader.py` を開き、変数 `slide_url` の値をダウンロードしたいスライドの URL に変更する
2. 以下のコマンドを実行する

```shell
pip install -r requirements.txt
python docswell-downloader.py
```

結果として、 `output` ディレクトリ内にスライドの PDF ファイルが生成されます。

## ドクセル関係者の方へ

本リポジトリの公開に問題がある場合は、 Issue でその旨をお伝えください。

関係者の GitHub アカウントであることの確認が取れ次第、早急に非公開等の然るべき対応を取らせていただきます。

## License

Copyright (c) Copyright 2022 [@11nu](https://github.com/11nu). All rights reserved.

Licensed under the [MIT](LICENSE.txt) license.
