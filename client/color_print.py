
def red_text(text):
    print("\033[31m{}\033[0m" .format(text))
def green_text(text):
    print("\033[32m{}\033[0m" .format(text))
def yellow_text(text):
    print("\033[33m{}\033[0m" .format(text))
def blue_text(text):
    print("\033[34m{}\033[0m" .format(text))


if __name__ == "__main__":
    red_text('test')
    print('test')