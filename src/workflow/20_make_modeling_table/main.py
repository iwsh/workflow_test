import argparse
import yaml

# モデリング用データテーブル
# 簡単のため、バージョン情報のみyamlで格納
analysis_table = "../data/analysis_table.yml"
modeling_table = "../data/modeling_table.yml"

parser = argparse.ArgumentParser()
parser.add_argument('--ver')
parser.add_argument('--dataver')

args = parser.parse_args()


def main():
    print("Init: make_modeling_data")
    with open(analysis_table, "r") as f:
        dic_analysis_table = yaml.safe_load(f)
    print(f"analysis data is {dic_analysis_table}")


    vers = get_current_vers(modeling_table)
    if [args.ver, args.dataver] == vers:
        print("use existing modeling_table")
    else:
        update_table(modeling_table)


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


if __name__ == "__main__":
    main()
