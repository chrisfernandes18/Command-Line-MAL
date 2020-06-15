from src.mal_cmd import  get_user_input, search_mal, print_mal_dict
from src.mal_csv import export_to_csv
from src.mal_dict import mal_get_all_info

def main(flag):
    while True:
        link, title = search_mal(get_user_input(flag))
        if link == None:
            continue
        mal_dict = mal_get_all_info(link, title)
        print_mal_dict(mal_dict)
        flag = export_to_csv(mal_dict)
    return 0

if __name__ == "__main__":
    main(0)
