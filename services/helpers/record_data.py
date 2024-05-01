def record_data(data: dict, comment: str = None) -> None:
    file_path = r'C:\Users\user\PycharmProjects\distance\data\results.txt'

    with open(file_path, 'a') as file:

        if comment is not None:
            file.write(comment)

        for message, data_item in data.items():
            file.write(f"{message}:\n")
            file.write(str(data_item) + "\n")

        file.write("=====================================================================================\n")
