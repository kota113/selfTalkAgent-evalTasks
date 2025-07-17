# エージェント評価タスク

このリポジトリには、AIエージェントを評価するための2つのPythonタスクが含まれています：

## タスク1: スケジューリングAPI

イベントの追加、競合の検出、イベントの一覧表示を可能にするシンプルなスケジューリングAPIです。

### 機能

1. イベントリストの保存とソート
2. `add_event()`の実装
3. 場所/参加者の競合検出
4. フィルタリングオプション付きのイベント一覧表示

### 使用方法

```python
from datetime import datetime
from Task1.scheduling_api import Event, SchedulingAPI

# スケジューリングAPIを作成
api = SchedulingAPI()

# イベントを作成
meeting = Event(
    name="チームミーティング",
    start_time=datetime(2023, 1, 1, 10, 0),
    end_time=datetime(2023, 1, 1, 11, 0),
    location="会議室A",
    participants=["アリス", "ボブ", "チャーリー"]
)

# イベントを追加
success = api.add_event(meeting)
if success:
    print("イベントが正常に追加されました")
else:
    print("イベントは既存のイベントと競合しています")

# すべてのイベントを取得
all_events = api.events

# フィルタリングされたイベントを取得
events_with_alice = api.get_events(participant="アリス")
events_in_room_a = api.get_events(location="会議室A")
morning_events = api.get_events(
    start_time=datetime(2023, 1, 1, 9, 0),
    end_time=datetime(2023, 1, 1, 12, 0)
)
```

### テスト

テストスクリプトを実行してAPIの動作を確認します：

```
python Task1/test_scheduling_api.py
```

## タスク2: 単語推測ゲーム

Wordleスタイルの単語推測ゲームで、推測に対するフィードバックを提供します。

### 機能

1. 初期化時の5文字単語の検証
2. 未使用文字の追跡
3. Wordleスタイルの推測フィードバック

### 使用方法

```python
from Task2.word_game import WordGuessingGame

# 新しいゲームを作成
game = WordGuessingGame("APPLE")

# 推測を行う
feedback = game.guess("HEART")
print(feedback)  # ['absent', 'present', 'absent', 'absent', 'absent']

# 未使用の文字を取得
unused = game.get_unused_letters()
print(unused)  # {'b', 'c', 'd', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 's', 'u', 'v', 'w', 'x', 'y', 'z'}

# ゲームが解決されたかどうかを確認
if game.is_solved():
    print("勝利しました！")
```

### テスト

テストスクリプトを実行してゲームの動作を確認します：

```
python Task2/test_word_game.py
```

## 要件

- Python 3.6以上
- 外部依存関係は不要