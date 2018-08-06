def banner(message: str, border: str='-'):
    message_lines = []
    max_line_length = 0

    for message_line in message.split('\n'):
        message_lines.append(message_line)
        if len(message_lines[-1]) > max_line_length:
            max_line_length = len(message_lines[-1])

    border_line = border * max_line_length
    border_line = border_line[0:max_line_length]

    print(border_line)
    for message_line in message_lines:
        print(message_line)
    print(border_line)


if __name__ == "__main__":
    banner("Banner function, default")
    banner("Banner function with '\*/*'\nAlso in multi-line flavor!", '\*/*')
