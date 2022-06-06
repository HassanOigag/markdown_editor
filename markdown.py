def markdown_header():
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

def mardown_link():
        label = input("Label: ")
        url = input("URL: ")
        return f"[{label}]({url})"
def mardown_text(markdown_type):
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

if __name__ == "__main__":
    available_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line"]
    special_commands = ["!help", "!done"]
    markdown = ""
    while True:
        formatter = input("Choose a formatter: ")
        if formatter not in available_formatters + special_commands:
            print("Unknown formatting type or command")
        elif formatter == "!done":
            break
        elif formatter == "!help":
            print("Available formatters:", " ".join(available_formatters))
            print("Special commands:", " ".join(special_commands))
        else:
            if formatter == "header":
                markdown += markdown_header()
                print(markdown)
            elif formatter in ["plain", "bold", "italic", "inline-code"]:
                markdown += mardown_text(formatter)
                print(markdown)
            elif formatter == "new-line":
                markdown += "\n"
                print(markdown)
            elif formatter == "link":
                markdown += mardown_link()
                print(markdown)
