import argparse
import json

def parser_json_object(name, json_obj):
    pass

def parser_json_array():
    pass

def parser_java(name, json_str):
    try:
        bean = json.loads("".join(json_str))
    except:
        exit("illegal json:\n {}".format(json_str))

    bean = json.loads(json_str)
    rst = "class " + name + " {\n"
    for k, v in bean.items():
        if isinstance(v, list):
            rst += "\tpublic List<String> {} = new ArrayList<>();\n".format(k)
        else:
            rst += "\tpublic String {} = \"\";\n".format(k)
    rst += "}"
    return rst

def main():
    parser = argparse.ArgumentParser(description='convert json to bean')
    parser.add_argument('-l', type=str, choices=["java"], help="dist language")
    parser.add_argument('-n', type=str, help='the bean name')
    
    args = parser.parse_args()
    lang = args.l
    name = args.n
    if not lang or not name:
        parser.print_help
        exit(0)

    print("please input the json: ")
    json_content = []
    while True:
        line = input()
        json_content.append(line)
        if line == '':
            break

    json_content = "".join(json_content)
    rst = parser_java(name, json_content)
    print(rst)
    


    