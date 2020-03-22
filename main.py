from src.cmd_mal import search_again, search_mal, get_user_input, print_mal_dict, mal_get_all_info

def main(flag):
    link, title = search_mal(get_user_input(flag))
    
    if link == None:
        quit()
    
    mal_dict = mal_get_all_info(link, title)
    print_mal_dict(mal_dict)
    search_again()
    return 0


if __name__ == "__main__":
    main(0)