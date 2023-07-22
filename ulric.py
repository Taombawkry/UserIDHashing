import hashlib

#hud - Hashed User Data 


def conv(input_data):
    hash_object = hashlib.sha256(input_data.encode())
    return hash_object.hexdigest()

def save_to_file(data):
    with open("hud.txt", "a") as file:
        file.write(data + "\n")

def main():
    hud_list = []
    hud_dict = {}

    while True:
        user_input = input("Enter New User Name (or 'exit' to stop): ")

        if user_input.lower() == "exit":
            break

        hashed_value = conv(user_input)
        hud_list.append(hashed_value)
        hud_dict[user_input] = hashed_value

        save_to_file(hashed_value)

    print("\nHashed datal ist: ")
    print(hud_list)

    print("\nHashed data dictionary: ")
    for key, value in hud_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()


#                               Taombawkry                  '''     '''
