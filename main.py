def get_user_input():
    name = input("Enter your USERNAME PLEASE: ")
    print("Commit#1")
    length = float(input("Enter rectangle Length: "))
    width = float(input("Enter rectangle Width : "))
    return name, length, width

if __name__ == "__main__":
    user_name, user_length, user_width = get_user_input()
    print("I_MAster")
    print("user_name, user_length, user_width")
    print("Area of rectangle:", calculate_area(6, 3))