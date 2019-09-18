from collections import deque
expression = "{[]})"
TOKENS=[["{", "}"], ["(", ")"], ["[", "]"]]

def is_open_term(c):
    for t in TOKENS:
        if t[0] == c:
            return True
    return False

def matches(c1, c2):
    for t in TOKENS:
        if t[0] == c1 and t[1] == c2:
            return True
    return False

def is_balanced(expresssion):
    stack = deque()
    for c in expression:
        if is_open_term(c):
            stack.append(c)
        elif len(stack) == 0 or not matches(stack.pop(), c):
            return False
    return len(stack)==0

def main():
    if (is_balanced(expression)):
        print("*********Balanced*********")
    else:
        print("*********Not balanced*****")



if __name__ == "__main__":
    main()