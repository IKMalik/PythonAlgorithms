def fib(n):

  memo = {}
  return _fib(n, memo)

def _fib(n, memo):

  if n in memo:
    return memo[n]
  if n <= 2:
    fib_res = 1
  else:
    fib_res = _fib(n-1, memo) + _fib(n-2, memo)
    memo[n] = fib_res
  
  return fib_res


print(fib(5))
