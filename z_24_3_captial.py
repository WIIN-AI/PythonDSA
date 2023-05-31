
string_in = "wiinai kkumar"

if string_in.upper() == string_in:
    print("Valid")
elif string_in.lower() == string_in:
    print("Valid")
elif string_in.title() == string_in:
    print("Valid")
else :
    print(string_in.title())
    print("INVALID WORD FORMAT...")
