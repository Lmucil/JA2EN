# JA2EN
日本語から英語に音声変換できます。

他の主要な言語から英語にもできますが、精度は保証しません。

# 必要な環境、ライブラリ
インターネット

Python3

speech recognition

deep_translator

pyttsx3

keyboard(おそらくデフォルトで入っている)



# 使い方
デフォルトではセミコロン(;)を押すと、pythonファイルが走っている限り、

音声聞き取りが始まります。

# 開発環境
Windows 11 Home

Python 3.7

VSCode

# 仕組み
まずspeech recognitionで音声を日本語として聞き取ります

それを文字としてかきだし、

deep-translateで英語に翻訳します。

