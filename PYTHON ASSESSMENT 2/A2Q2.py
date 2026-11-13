otp = "1234"
attempts = 0

while attempts < 3:
    entered = input("Enter OTP: ")

    if entered == "":
        print("Blank entry! Try again.")
        continue

    attempts += 1

    if entered == otp:
        print("OTP Verified Successfully")
        break
    else:
        print("Wrong OTP")

else:
    print("Account Locked for 30 Minutes")


# Using for loop
for i in range(3):
    entered = input("Enter OTP: ")

    if entered == "":
        continue

    if entered == otp:
        print("OTP Verified Successfully")
        break
    else:
        pass

else:
    print("Account Locked for 30 Minutes")
