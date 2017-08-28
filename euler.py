def is_prime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    p=3
    while p*p<n:
        if n%p==0:
            return False
        p+=2
    return True
print([i for i in range(2,100) if is_prime(i)])
