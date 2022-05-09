import time
# set UserId and PW
userId = "somestring"
passWrd = "someOtherString"
######################################################
# Check to see if Micro Service is ready("waiting...")
######################################################
with open("loginUser.txt", "r") as userLoggingIn:
    user = userLoggingIn.read().split(" ")

    # print(f"in Read....   {user}")
    while user[0] != "waiting...":
        time.sleep(1)
        user = userLoggingIn.read().split()
        # print(user)

userLoggingIn.close()
outstring = userId + " " + passWrd

######################################################
# write UserID and UserPW into the login file to launch the MicroService Action
######################################################

with open("loginUser.txt", "w") as loger:
    loger.write(outstring)
    loger.close()
######################################################
# read the MicroService Communication file to see results of Login Attempt
######################################################
time.sleep(1)
with open("validUserResponse.txt", "r") as errorCheck:
    errorMsg = errorCheck.read().split(" ")
    if errorMsg[0] == userId:
        #verifyAge(userId)# Other Microservice call
        print(f"Welcome {userId}, you are now logged in!")
        pwInvalid = False
    elif errorMsg[0] == "Invalid":
        print(f"Sorry that Password is invalid, Please try again.")
    else:
        #verifyAge(userId)# Other Microservice call
        print(f" ...Welcome New User: {userId}")
        pwInvalid = False
    errorCheck.close()