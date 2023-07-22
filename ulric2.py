import hashlib
from timeit import default_timer as timer

def sha256_hash(input_data):
    hash_object = hashlib.sha256(input_data.encode())
    return hash_object.hexdigest()

def save_to_file(hashed_values):
    with open("hud.txt", "a") as file:
        for data in hashed_values:
            file.write(data + "\n")

def main():
    hud_list = []
    hud_dict = {}
    hashed_values_to_write = []

    while True:
        user_input = input("Enter New User Name (or 'exit' to stop): ")

        if user_input.lower() == "exit":
            break

        if user_input in hud_dict:
            hashed_value = hud_dict[user_input]
        else:
            hashed_value = sha256_hash(user_input)
            hud_dict[user_input] = hashed_value
            hashed_values_to_write.append(hashed_value)

        hud_list.append(hashed_value)

    save_to_file(hashed_values_to_write)

    print("\nHashed data list:")
    print(hud_list)

    print("\nHashed data dictionary:")
    for key, value in hud_dict.items():
        print(f" {key} : {value}")

if __name__ == "__main__":
    start = timer()
    main()
    stop = timer()
    timer = f"Time: {stop - start}s"
    print(timer)

#                               Taombawkry                  '''   9  '''
