import os


Dir_path = r"C:\\Python\\すっきりわかるPython入門\\Chapter5" #ファイルパス
start_num = 0  #連番の最初の値  0だとChapter0から
end_num = 35    #連番の最後の値  35だとChapter35まで生成される

def gen_PythonFile(dir, start_code, end_code):
    os.makedirs(dir, exist_ok=True)  # ディレクトリが存在しない場合に作成する

    for code_number in range(start_code, end_code + 1):
        filename = f"Code{code_number}.py"
        file_path = os.path.join(dir, filename)
        open(file_path, "w").close()  

#実行
gen_PythonFile(Dir_path, start_num, end_num)
