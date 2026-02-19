def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name please."
        except KeyError:
            return "Contact not found."

    return inner


@input_error
def add_contact(args, users_dict):
    name, phone = args
    users_dict[name] = phone
    return "Contact added."


@input_error
def change_contact(args, users_dict):
    name, new_phone = args
    users_dict[name]
    users_dict[name] = new_phone
    return "Contact updated."


@input_error
def show_phone(args, users_dict):
    name = args[0]
    phone = users_dict[name]
    return phone


@input_error
def show_all(users_dict):
    all_users_visibility = []
    if not users_dict:
        return "No contacts."
    for name, phone in users_dict.items():
        joint_str = f"{name}: {phone}"
        all_users_visibility.append(joint_str)
    return "\n".join(all_users_visibility)


def main():
    print("Welcome to the assistant bot!")
    users_dict = {}
    while True:
        user_input = input("Enter a command: ")
        if not user_input.split():
            continue
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "add":
            result_add_contact = add_contact(args, users_dict)
            print(result_add_contact)
        elif command == "change":
            result_change_cont = change_contact(args, users_dict)
            print(result_change_cont)
        elif command == "phone":
            result_show_ph = show_phone(args, users_dict)
            print(result_show_ph)
        elif command == "all":
            result_show_all = show_all(users_dict)
            print(result_show_all)

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
