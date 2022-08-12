from pprint import pprint

tiesto = {
    "name": "Tiesto",
    "age": 55,
    "equipment": "Pioneer",
    "discography": 20,
    "salary": 30_000,
    "genre": "lite-house",
}
avicci = {
    "name": "Avicci",
    "age": 22,
    "equipment": "Pioneer",
    "discography": 40,
    "salary": 0,
    "genre": "adm",
}
anna = {
    "name": "Anna",
    "age": 24,
    "equipment": "Synth",
    "discography": 3,
    "salary": 3_000,
    "genre": "techno",
}
def validate_dj_data(data):
    if len(data) != 6:
        print("The number of arguments is not correct!")
        return None
    if data[0].isdigit():
        print(f"{data[0]} is digit")
        return None
    for element in [data[1], data[3], data[4]]:
        index = data.index(element)
        if element.isdigit():
            data[index] = int(element)
        else:
            print(f"{element} is not a digit")
            return None
    if not data[5].isalnum():
        print(f"{data[5]} is not an alnum")
        return None
    return data
def add_dj(data):
    user_input = input("Enter new DJ's data: ")
    dj_data = user_input.split(",")
    validated_data = validate_dj_data(dj_data)
    if validated_data is not None:
        new_dj_data = {
            "name": validated_data[0],
            "age": validated_data[1],
            "equipment": validated_data[2],
            "discography": validated_data[3],
            "salary": validated_data[4],
            "genre": validated_data[5],
        }
        data.append(new_dj_data)
        return new_dj_data
def del_dj():
    element = input("Enter DJ's name which you want to delete: ")
    for dj in djs:
        if dj.get("name") == element:
            djs.remove(dj)
            return True
    print(f"{element} is None! Please, enter correct DJ's name: ")
    return False
def update_dj():
    updated = input("Enter DJ's name which you want to update: ")
    is_exist = False
    for dj in djs:
        if dj.get("name") == updated:
            is_exist = True
            curr_dj = dj
            djs.remove(dj)
            param_count = int(input("Input count of change params (1-6)"))
            if param_count < 1 or param_count > 6:
                print("count of params is incorrect")
                break
            else:
                for i in range(1, param_count + 1):
                    param_name = input("Input param name: ")
                    if param_name not in allowed_params:
                        print(f"{param_name} is incorrect parameter name")
                    else:
                        if param_name in ["age", "discography", "salary"]:
                            param_value = int(input("Enter new value: "))
                            curr_dj[param_name] = param_value
                        else:
                            param_value = input("Enter new value: ")
                            curr_dj[param_name] = param_value
            djs.append(curr_dj)
            for dj_1 in djs:
                print(dj_1)
            break
        if not is_exist:
            print(f"{updated} is None! Please, enter correct DJ's name: ")
        
if __name__ == "main":
    djs = [tiesto, avicci, anna]
    allowed_params = ["name", "age", "equipment", "discography", "salary", "genre"]
    allowed_options = "[add/list/names/delete/update/exit]"
    while True:
        desision = input(f"What should I do?{allowed_options}: ")
        if desision == "add":
            print("DJ input format: name,age,equipment,discography,salary,genre")
            new_dj = add_dj(djs)
            if new_dj:
                print(f"DJ {new_dj['name']} is added!")
        elif desision == "list":
            pprint(djs)
        elif desision == "names":
            data = [dj["name"] for dj in djs]
            pprint(data)
        elif desision == "delete":
            deleted_dj = del_dj()
            if deleted_dj:
                print(f"DJ is deleted!")
                print("")
                for dj in djs:
                    print(dj.get("name") + " ")
        elif desision == "update":
            update_dj()
        elif desision == "exit":
            print("Exiting...")
            break
        else:
            print(f"Please use allowed options! {allowed_options}")