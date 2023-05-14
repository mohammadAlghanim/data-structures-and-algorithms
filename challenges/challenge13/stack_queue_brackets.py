from challenges.stack_and_queue.Stack import Stack
"""
    Validate a string of brackets to ensure they are well-formed.

    Parameters:
    s (str): The string of brackets to validate.

    Returns:
    bool: True if all brackets are well-formed and balanced (i.e., every opening bracket has a corresponding closing bracket),
    False otherwise.
"""
def validate_brackets(s):
    Brackets = {'(': ')', '{': '}', '[': ']'}
    stack = Stack()
    if not s:  # check if the string is empty
        return False
    for i in s:
        if i in Brackets:
            # If the character is an open bracket, push it onto the stack
            stack.push(i)
        elif i in Brackets.values():
            # If the character is a closing bracket, check if it matches the topmost open bracket on the stack
            if stack.is_empty():
                return False
            Open_Bracket = stack.pop()
            if i != Brackets[Open_Bracket]:
                return False
    
    # If all brackets are well-formed, the stack should be empty
    return stack.is_empty()

s= "(){dfbzf}[]"
print(validate_brackets(s))