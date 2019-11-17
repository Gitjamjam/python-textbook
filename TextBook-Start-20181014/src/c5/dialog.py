# ダイアログを表示するために必要なモジュール
import tkinter.messagebox as mb

# ダイアログを表示
ans = mb.askyesno("タイトル", "これはメッセージです")

if ans == True:
    # OKボタンがあるだけのダイアログを表示
    mb.showinfo("同意", "OKです")
else:
    mb.showinfo("拒否", "NGです")
