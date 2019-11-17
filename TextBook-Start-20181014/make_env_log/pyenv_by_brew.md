
# python3 をいれる
## 参考
- https://prog-8.com/docs/python-env

# バージョン確認
- `python --version`
- 現在のバージョンは

```
$ python --version
Python 2.7.10
```

- 3系をいれていく

# brewでpyenvを入れる
- `pyenv -v`
- 結果は

```
$ pyenv -v
zsh: command not found: pyenv
```

まだ入ってない
## 入れていく

- `brew install pyenv`

### インストール後
```
[~]
$ pyenv -v
pyenv 1.2.13

```
- 入りました

### pyenvパス設定　
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

# Pythonのインストール
## インストールリスト
```
pyenv install --list
```
インストールできるものを確認  
3.7.4をいれましょう

### pyenvでダウンロード
```
pyenv install 3.7.4
```
- pythonをダウンロードしているので、少し長い

## pyenvのダウンロード済みリスト
- `pyenv versions`
- 確認してみましょう

```
$ pyenv versions
* system (set by /Users/jamac/.pyenv/version)
  3.7.4
```

- `3.7.4`がダウンロード済みです


## 使用Python設定
- いつも使用するpythonを設定しましょう
- `pyenv global 3.7.4`

### バージョン確認
- `python --version`
- 結果は

```
[~]
$ python --version
Python 2.7.10
```
- はいらない

# トラブルシュート
- パス確認

```
[~]
$ which python
/usr/bin/python
````

## pyenv init
- 参考；https://github.com/pyenv/pyenv#homebrew-on-mac-os-x
- `pyenv init` を使ってみる
- できない
- `pyenv rehash` も使って、もう一度、`pyenv init` を使ってみる

```
python --version
Python 3.7.4
```
- はいりました。今はなにも知らなくてもいいでしょう

```
$ which python
/Users/jamac/.pyenv/shims/python

```
- いまはなにも知らなくていいでしょう。

### 3系が使えるようになりました
