from src.cmd_mal import search_again, search_mal, get_user_input, print_mal_dict, mal_get_all_info
from src.maltocsv import export_to_csv

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