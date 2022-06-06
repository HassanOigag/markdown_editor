def get_markdown_header():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            print("please digits only")
            continue
        if level not in range(1,7):
            print("The level should be within the range of 1 to 6")
        else:
            break
    text = input("Text: ")
    markdown = f"{'#' * level} {text}\n"
    return markdown

def get_markdown_list(list_type):
    list_items = []
    while True:
        try:
            rows = int(input("Number of rows: "))
        except ValueError:
            print("digits please")
            continue
        if rows <= 0:
            print("The number of rows should be greater than zero")
        else:
            break
    for i in range(rows):
        row = input(f"Row #{i + 1}: ")
        list_items.append(row)
    if list_type == "ordered-list":
        markdown = list(map(lambda item: f"{item[0] + 1}. {item[1]}\n", enumerate(list_items)))
    else:
        markdown = list(map(lambda item: f"* {item}\n", list_items))
    return ''.join(markdown)

def get_markdown_link():
        label = input("Label: ")
        url = input("URL: ")
        return f"[{label}]({url})"

def get_markdown_text(markdown_type):
    text = input("Text: ")
    markdown = ""
    if markdown_type == "bold":
        markdown = f"**{text}**"
    elif markdown_type == "italic":
        markdown = f"*{text}*"
    elif markdown_type == "inline-code":
        markdown = f"`{text}`"
    else:
        markdown = text
    return markdown

def save_to_file(markdown):
    with open("output.md", "w") as md:
        md.write(markdown)
    exit()

def get_markdown(formatter):
    if formatter == "header":
        markdown = get_markdown_header()
    elif formatter in ["plain", "bold", "italic", "inline-code"]:
        markdown = get_markdown_text(formatter)
    elif formatter == "new-line":
        markdown = "\n"
    elif formatter == "link":
        markdown = get_markdown_link()
    elif formatter in ["ordered-list", "unordered-list"]:
        markdown = get_markdown_list(formatter)
    return markdown

if __name__ == "__main__":
    available_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list", "unordered-list"]
    special_commands = ["!help", "!done"]
    markdown = ""
    while True:
        formatter = input("Choose a formatter: ")
        if formatter not in available_formatters + special_commands:
            print("Unknown formatting type or command")
        elif formatter == "!done":
            save_to_file(markdown)
        elif formatter == "!help":
            print("Available formatters:", " ".join(available_formatters))
            print("Special commands:", " ".join(special_commands))
        else:
            markdown += get_markdown(formatter)
            print(markdown)
