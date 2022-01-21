# gtfs-jp-list-datecheck
GTFS/GTFS-JP固定URLデータ　日付チェック

日本国内で公開されているGTFS / GTFS-JP データのうち、固定URLで公開されている静的データの更新日をチェックします。
* 毎朝1回、リスト（GTFS_fixedURL.csv）に登録されているURLを自動でチェックし、結果を GTFS_fixedURL_LastModified.csv に書き込みします。
  * 2021.12現在、毎朝4:30～40ごろに内容確定
* URLで指定されているデータのファイル情報を取得し、Last-Modified（最終更新日）プロパティに記載されている日付をcsvファイルとして返します。
  * 取得日時はJST（日本標準時）に変換してあります。（2022/1/22更新分より）
  * 以下の場合は日付欄が空欄となっています。
    * ファイルにLast-Modifiedプロパティがない場合
    * ファイル情報が取得できない場合（配信サーバ側の制限など）
  * 必ずしも対象ファイル自体の更新日を表すとは限りません。あくまで参考としてください。

## URL
https://tshimada291.github.io/gtfs-jp-list-datecheck/GTFS_fixedURL_LastModified.csv

## License
[cc0](https://creativecommons.org/publicdomain/zero/1.0/deed.ja)（プログラム、生成データともに）

## History
* 2021.11.05 運用開始
* 2021.12.13 チェック開始時間変更（JST 9:00 → 4:00）
* 2022.01.21 JST対応
