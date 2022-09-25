import argparse
import yaml

# 分析用データテーブル
# 簡単のため、バージョン情報のみyamlで格納
analysis_table = ../data/analysis_table.yml

parser = argparse.ArgumentParser()
parser.add_argument('--ver')
parser.add_argument('--dataver')

args = parser.parse_args()


def main():
    print("Init: make_amalysis_data")
    vers = get_current_vers(analysis_table)
    if [args.ver, args.dataver] == vers:
        print("use existing analysis_table")
    else:
        update_table(analysis_table)


def get_current_vers(table):
    with open(table, "r") as f:
        dic_table = yaml.safe_load(f)
    vers = [dic_table["code_ver"], dic_table["data_ver"]]
    return vers


def update_table(table):
    dic_table = {
        "code_ver": args.ver,
        "data_ver": args.dataver,
    }
    with open(table, "w") as f:
        yaml.dump(dic_table, f, default_flow_style=False)


if __name__ = "__main__":
    main()
