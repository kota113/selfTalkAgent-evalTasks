class Event:
    def __init__(self, name, start_time, end_time, location, participants):
        """
        指定されたパラメータでイベントを初期化します。

        Args:
            name (str): イベントの名前
            start_time (datetime): イベントの開始時間
            end_time (datetime): イベントの終了時間
            location (str): イベントの場所
            participants (list): 参加者のリスト
        """
        pass

    def __str__(self):
        """イベントの文字列表現を返します。"""
        pass


class SchedulingAPI:
    def __init__(self):
        """空のイベントリストを初期化します。"""
        pass

    def add_event(self, event):
        """
        既存のイベントと競合しない場合、スケジュールにイベントを追加します。

        Args:
            event (Event): 追加するイベント

        Returns:
            bool: イベントが正常に追加された場合はTrue、競合があった場合はFalse
        """
        pass

    def _has_conflict(self, new_event):
        """
        新しいイベントが既存のイベントと競合するかどうかを確認します。

        競合は以下の場合に発生します：
        1. 同じ場所が重複する時間に予約されている
        2. 同じ参加者が重複するイベントに予定されている

        Args:
            new_event (Event): 競合をチェックするイベント

        Returns:
            bool: 競合がある場合はTrue、そうでない場合はFalse
        """
        pass

    def get_events(self, start_time=None, end_time=None, location=None, participant=None):
        """
        オプションでパラメータによってフィルタリングされたイベントのリストを取得します。

        Args:
            start_time (datetime, optional): この時間以降に開始するイベントをフィルタリング
            end_time (datetime, optional): この時間以前に終了するイベントをフィルタリング
            location (str, optional): この場所でのイベントをフィルタリング
            participant (str, optional): この参加者を含むイベントをフィルタリング

        Returns:
            list: 条件に一致するイベントのリスト
        """
        pass
