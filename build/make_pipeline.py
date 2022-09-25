import sys
import os
import shutil
import re

argv = sys.argv
tag = argv[0]

outdir = "../run"

def main():
    # tag の例: v1.2.3
    # 1 -> 抽出処理のバージョン
    # 2 -> 前処理のバージョン
    # 3 -> 訓練処理のバージョン
    print(f"{tag=}")
    m = re.fullmatch(r"v([0-9]+)\.([0-9]+)\.([0-9]+)", tag)
    extraction_ver, preprocess_ver, training_ver = m.groups()

    # パイプラインを作成
    # 簡易のためrun下に資材をまとめて全処理を実行するシェルスクリプトを作成する
    # 本来はパイプライン管理ツールを利用して処理を定義する

    shutils.copytree("../src/workflow", "../run/workflow")

    init = "dataver=$1"
    run_extraction = "python workflow/10_make_analysis_table/main.py --ver " + extraction_ver + " --dataver ${dataver}"
    run_preprocess = "python workflow/20_make_modeling_table/main.py --ver " + preprocess_ver + " --dataver ${dataver}"
    run_training = "python workflow/30_training/main.py"

    run_all = [init, run_extraction, run_preprocess, run_training].join("\n")

    with open("../run/pipeline.sh", "w") as f:
        f.write(run_all)


if __name__ == "__main__":
    main()
