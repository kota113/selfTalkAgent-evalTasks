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
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.participants = participants

    def __str__(self):
        """イベントの文字列表現を返します。"""
        return f"{self.name} at {self.location} from {self.start_time} to {self.end_time}"


class SchedulingAPI:
    def __init__(self):
        """空のイベントリストを初期化します。"""
        self.events = []

    def add_event(self, event):
        """
        既存のイベントと競合しない場合、スケジュールにイベントを追加します。

        Args:
            event (Event): 追加するイベント

        Returns:
            bool: イベントが正常に追加された場合はTrue、競合があった場合はFalse
        """
        # 競合をチェック
        if self._has_conflict(event):
            return False

        # イベントを追加
        self.events.append(event)

        # 開始時間でイベントをソート
        self.events.sort(key=lambda e: e.start_time)

        return True

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
        for event in self.events:
            # 時間の重複をチェック
            if (new_event.start_time < event.end_time and 
                new_event.end_time > event.start_time):

                # 場所の競合をチェック
                if new_event.location == event.location:
                    return True

                # 参加者の競合をチェック
                for participant in new_event.participants:
                    if participant in event.participants:
                        return True

        return False

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
        filtered_events = self.events.copy()

        if start_time:
            filtered_events = [e for e in filtered_events if e.start_time >= start_time]

        if end_time:
            filtered_events = [e for e in filtered_events if e.end_time <= end_time]

        if location:
            filtered_events = [e for e in filtered_events if e.location == location]

        if participant:
            filtered_events = [e for e in filtered_events if participant in e.participants]

        return filtered_events
