def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()

def get_num_words(text: str) -> int:
    return len(text.split()) 

def get_character_dict(text: str) -> dict:
    char_count = {}
    for character in text:
        if character.lower() not in char_count:
            char_count[character.lower()] = 1
        else:
            char_count[character.lower()] += 1
    return char_count

def get_stats_list(char_count: dict) -> list:
    stat_list = []
    for key, value in char_count.items():
        stat_list.append({"character": key, "num": value})
    return sorted(stat_list, reverse=True, key=lambda i: i['num']) # lambda function grabs 'num' key in dict

def print_stats(file_path: str) -> str:
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    stats_list = get_stats_list(get_character_dict(text))

    stats = f"""
\t============ BOOKBOT ============
\tAnalyzing book found at {file_path}...
\t----------- Word Count ----------
\tFound {num_words} total words
\t--------- Character Count -------
    """
    for item in stats_list:
        if item['character'].isalpha():
            stats += f"\t{item['character']}: {item['num']}\n"
    
    stats += "\t============= END ==============="

    return stats