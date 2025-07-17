class WordGuessingGame:
    def __init__(self, target_word):
        """
        ターゲットワードでゲームを初期化します。

        Args:
            target_word (str): 推測される単語

        Raises:
            ValueError: ターゲットワードが5文字でない場合
        """
        pass

    def get_unused_letters(self):
        """
        どの推測でも使用されていない文字のセットを返します。

        Returns:
            set: 未使用の文字のセット
        """
        pass

    def guess(self, word):
        """
        推測を行い、Wordleスタイルのフィードバックを取得します。

        フィードバックは文字列のリストです：
        - "correct": 文字が正しい位置にある
        - "present": 文字は単語内にあるが、位置が間違っている
        - "absent": 文字は単語内にない

        Args:
            word (str): 推測された単語

        Returns:
            list: 各文字のフィードバック文字列のリスト

        Raises:
            ValueError: 推測された単語が5文字でない場合
        """
        pass

    def is_solved(self):
        """
        ゲームが解決されたかどうかを確認します。

        Returns:
            bool: 最後の推測が正しければTrue、そうでなければFalse
        """
        pass
