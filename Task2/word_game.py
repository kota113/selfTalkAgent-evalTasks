class WordGuessingGame:
    def __init__(self, target_word):
        """
        ターゲットワードでゲームを初期化します。

        Args:
            target_word (str): 推測される単語

        Raises:
            ValueError: ターゲットワードが5文字でない場合
        """
        if not isinstance(target_word, str) or len(target_word) != 5:
            raise ValueError("ターゲットワードは正確に5文字でなければなりません")

        self.target_word = target_word.lower()
        self.guesses = []
        self.all_letters = set("abcdefghijklmnopqrstuvwxyz")
        self.used_letters = set()

    def get_unused_letters(self):
        """
        どの推測でも使用されていない文字のセットを返します。

        Returns:
            set: 未使用の文字のセット
        """
        return self.all_letters - self.used_letters

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
        if not isinstance(word, str) or len(word) != 5:
            raise ValueError("推測された単語は正確に5文字でなければなりません")

        word = word.lower()
        self.guesses.append(word)

        # 推測からすべての文字を使用済み文字セットに追加
        for letter in word:
            self.used_letters.add(letter)

        # フィードバックを生成
        feedback = []

        # 最初のパス：正しい文字をマーク
        target_remaining = list(self.target_word)
        for i, letter in enumerate(word):
            if letter == self.target_word[i]:
                feedback.append("correct")
                # この文字をターゲットで使用済みとしてマーク
                target_remaining[i] = None
            else:
                # 今はプレースホルダー
                feedback.append(None)

        # 2番目のパス：存在するか存在しない文字をマーク
        for i, letter in enumerate(word):
            if feedback[i] is not None:
                continue  # すでに正しいとマークされている文字をスキップ

            if letter in target_remaining:
                feedback[i] = "present"
                # この文字をターゲットで使用済みとしてマーク
                target_remaining[target_remaining.index(letter)] = None
            else:
                feedback[i] = "absent"

        return feedback

    def is_solved(self):
        """
        ゲームが解決されたかどうかを確認します。

        Returns:
            bool: 最後の推測が正しければTrue、そうでなければFalse
        """
        if not self.guesses:
            return False

        return self.guesses[-1] == self.target_word
