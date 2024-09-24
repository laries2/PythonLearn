#USED TO EXPRESS IF A GIVEN LOGICAL CONDITION IS TRUE OR FALSE

a = 3
b= 5
# if a>b:
#     print("a is greater than b")

# if True:
#     print("a is greater than b")

state= a>b
print(state)

if state:
    print("a is greater than b")
else:
    print("b is greater than a")


def grant_access(ID_is_valid, has_gate_pass):
    return ID_is_valid and has_gate_pass


access = grant_access(True, False)
print(access)



