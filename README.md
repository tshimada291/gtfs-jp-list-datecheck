# gtfs-jp-list-datecheck
GTFS/GTFS-JP固定URLデータ　日付チェック

日本国内で公開されているGTFS / GTFS-JP データのうち、固定URLで公開されている静的データの更新日と feed_info.txt の内容をチェックします。
* 毎朝1回、リスト（GTFS_fixedURL.csv）に登録されているURLを自動でチェックし、結果を GTFS_fixedURL_LastModified.csv に出力します。
  * 2022.7 現在、毎朝 4:30～40 ごろに内容確定
* URLで指定されているデータのファイル情報を取得し、Last-Modified（最終更新日）プロパティに記載されている日付を csv に出力します。
  * 取得日時はJST（日本標準時）に変換してあります。（2022/1/24更新分より）
  * 以下の場合は日付欄が空欄となっています。
    * ファイルにLast-Modifiedプロパティがない場合
    * ファイル情報が取得できない場合（配信サーバ側の制限や障害発生など）
  * 必ずしも対象ファイル自体の更新日を表すとは限りません。あくまで参考としてください。
* 上記に加えて、zipファイルに格納されている feed_info.txt の内容を読み取り、結果を csv に出力します。
  * feed_info.txt がない場合は空欄となります。
  * feed_into.txt があっても記載がない項目がある場合は、該当項目のみ空欄となります。
* サーバへの問い合わせ時に応答がなくタイムアウトとなった場合は、当該データの情報が取得できないため空欄となります。

## URL
https://tshimada291.github.io/gtfs-jp-list-datecheck/GTFS_fixedURL_LastModified.csv

## License
[cc0](https://creativecommons.org/publicdomain/zero/1.0/deed.ja)（プログラム、生成データともに）

## History
* 2021.11.05　運用開始
* 2021.12.13　チェック開始時間変更（JST 9:00 → 4:00）
* 2022.01.24　JST対応
* 2022.03.18　feed_infoチェック機能追加

## References
* [GitHub ActionsでPythonスクリプトを実行する（Helve Tech Blog）](https://helve-blog.com/posts/git/github-actions-python/)
* [［Python入門］urllib.requestモジュールによるWebページの取得（@IT）](https://atmarkit.itmedia.co.jp/ait/articles/1910/15/news018.html)
* [Pythonでcsv形式の文字列データをパースする（某エンジニアのお仕事以外のメモ（分冊））](https://water2litter.net/rum/post/python_csv_parse_string/)
* [Requests の使い方 (Python Library)（Qiita @sqrtxx）](https://qiita.com/sqrtxx/items/49beaa3795925e7de666)
* [インターネット上のzipファイルをリクエストして変数に取り込む（Qiira @Intel0tw5727）](https://qiita.com/Intel0tw5727/items/465a7dff9d0880f4250a)
* [指定したURLのリンクが有効かどうかをチェックするpythonスクリプトを作成（Qiita @Seigot）](https://qiita.com/seigot/items/534ca3089d217200a1d6)
