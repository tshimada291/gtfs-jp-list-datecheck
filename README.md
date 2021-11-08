# gtfs-jp-list-datecheck
GTFS/GTFS-JP固定URLデータ　日付チェック

日本国内で公開されているGTFS / GTFS-JP データのうち、固定URLで公開されている静的データの更新日をチェックします。
* 毎朝1回、リスト（GTFS_fixedURL.csv）に登録されている登録URLを自動でチェックし、結果を GTFS_fixedURL_LastModified.csv に書き込みします。
  * 2021.11現在、10:30～40ごろに更新確定
* URLで指定されているデータのファイル情報を取得し、Last-Modified（最終更新日）に記載されている日付をcsvファイルとして返します。
  * 取得日時はGMT（グリニッジ標準時）となっています。（＋9時間でJST（日本標準時））
  * 以下の場合は日付欄が空欄となっています。
    * Last-Modifiedがない場合やファイル情報が取得できない場合
    * .zipで終わっていないURLの場合（自動更新型の配信システム、一部のストレージサービスなど）
  * 必ずしもファイル自体の更新日を表すとは限りません。あくまで参考としてください。

## URL
https://tshimada291.github.io/gtfs-jp-list-datecheck/GTFS_fixedURL_LastModified.csv

## License
[cc0](https://creativecommons.org/publicdomain/zero/1.0/deed.ja)（プログラム、生成データともに）
