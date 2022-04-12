# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

four_digit_num = str(input("Enter 4 digit number "))

if four_digit_num[0] == four_digit_num[3] and four_digit_num[1] == four_digit_num[2]:
    print("True (palindrome)")
else:
    print("False (not palindrome)")
