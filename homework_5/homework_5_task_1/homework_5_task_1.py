from typing import Callable


def caching_fibonacci()-> Callable[[int], int]:    
    """Виклик зовнішньої функції"""
    cache = {}
    def fibonacci(n: int) -> int:                  
        """Виклик внутрішньої функції"""
        if n in cache:
            return cache[n]
        elif n == 1:
            return 1
        elif n <= 0:
            return 0
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
        
    return fibonacci
                               
fib = caching_fibonacci()

print(fib(10))
print(fib(15))
