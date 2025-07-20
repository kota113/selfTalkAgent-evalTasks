# タスク1: スケジューリングAPI

このタスクでは、イベントの追加、競合の検出、イベントの一覧表示を可能にするシンプルなスケジューリングAPIを実装します。

## 要件

### Event クラス

`Event` クラスは以下のパラメータで初期化する必要があります：

- `name` (str): イベントの名前
- `start_time` (datetime): イベントの開始時間
- `end_time` (datetime): イベントの終了時間
- `location` (str): イベントの場所
- `participants` (list): 参加者のリスト

また、イベントの文字列表現を返す `__str__` メソッドを実装する必要があります。

### SchedulingAPI クラス

`SchedulingAPI` クラスは以下のメソッドを実装する必要があります：

1. `__init__()`: 空のイベントリストを初期化します。

2. `add_event(event)`: 既存のイベントと競合しない場合、スケジュールにイベントを追加します。
   - 引数: `event` (Event) - 追加するイベント
   - 戻り値: `bool` - イベントが正常に追加された場合は True、競合があった場合は False

3. `_has_conflict(new_event)`: 新しいイベントが既存のイベントと競合するかどうかを確認します。
   競合は以下の場合に発生します：
   - 同じ場所が重複する時間に予約されている
   - 同じ参加者が重複するイベントに予定されている
   - 引数: `new_event` (Event) - 競合をチェックするイベント
   - 戻り値: `bool` - 競合がある場合は True、そうでない場合は False

4. `get_events(start_time=None, end_time=None, location=None, participant=None)`: オプションでパラメータによってフィルタリングされたイベントのリストを取得します。
   - 引数:
     - `start_time` (datetime, optional): この時間以降に開始するイベントをフィルタリング
     - `end_time` (datetime, optional): この時間以前に終了するイベントをフィルタリング
     - `location` (str, optional): この場所でのイベントをフィルタリング
     - `participant` (str, optional): この参加者を含むイベントをフィルタリング
   - 戻り値: `list` - 条件に一致するイベントのリスト

## テスト

テストスクリプトを実行してAPIの動作を確認します：

```
python Task1/test_scheduling_api.py
```