username = ["ahmed","majeed"];
password = [123,456]
while True :
    x = raw_input("press R to Register or L to login ");
    print x
    if x == "L":
        name = raw_input(" name");
        print "password :"
        pasw = input();
        i = 0;
        while i < 2:
            if username[i] == name :
                index = i ;
                if password[index] == pasw :
                    print("Correct");
                    break;
    elif x == "R":
        check = False;
        name = raw_input(" Enter username");
        i = 0;
        while i < len(username):
            if username[i] == name:
                print "The username is exist "
                check = True;
                break;
            i += 1;
        if not check:
            username.append(name);
            pasw = input("password :");
            password.append(pasw);
