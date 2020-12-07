


def cleanString_withLambdaFunc(s):
    """ 
    :type s: str
    :rtype: bool
    """
    # remove spaces and make all letters lowercase
    s = "".join(s.split()).lower()
    # remove characters
    func = lambda s, char: s.replace(char, "")
    if not s.isalnum():
        s = func(s, ":")
        s = func(s, ",")
    
    return s

print(cleanString_withLambdaFunc("A man, a plan, a canal: Panama"))