def _decorator_(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        count = len(result)
        average = sum(result) / count
        maximum = max(result)
        
        print(f"Numbers read: {result}")
        print(f"Count: {count}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum}")

        return result  
    return wrapper

@_decorator_
def read_num(line):
     numbers = list(int(num) for num in line.strip().split())
     return numbers
 

def printStats(t):  
    with open(t, 'r') as file:
        for line in file:
            read_num(line)
            
printStats('num.txt')
