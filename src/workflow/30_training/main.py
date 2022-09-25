import yaml

modeling_table = ../data/modeling_table.yml


def main():
    print("Init: training")
    with open(modeling_table, "r") as f:
        dic_table = yaml.safe_load(f)
    print(f"train with modeling data {dic_table}")


if __name__ = "__main__":
    main()
