def StackEmpty(S)
    if S.top == 0
        return TRUE
    else return FALSE

def push(S,x)
    S.top = S.top + 1
    S[S.top] = x

def pop(S)
    if StackEmpty(S)
        error "Stack Underflow"
    else S.top = S.top - 1
        return S[S.top+1]

