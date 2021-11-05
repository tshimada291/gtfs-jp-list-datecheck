# gtfs-jp-list-datecheck
GTFS/GTFS-JP固定URLデータ　日付チェック

日本国内で公開されているGTFS / GTFS-JP データのうち、固定URLで公開されている静的データの更新日をチェックします。
* URLで指定されているデータのファイル情報を取得し、Last-Modified（最終更新日）に記載されている日付をcsvファイルとして返します。
  * 取得日時はGMT（グリニッジ標準時）となっています。（＋9時間でJST（日本標準時））
  * Last-Modifiedがない場合やファイル情報が取得できない場合は空欄となっています。（.zipで終わっていないURLのデータについては空欄となっています。）
  * 必ずしもファイルの更新日を表すとは限りません。あくまで参考としてください。

## URL
https://tshimada291.github.io/gtfs-jp-list-datecheck/GTFS_fixedURL_LastModified.csv
