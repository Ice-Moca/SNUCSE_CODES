def sum(a, b):
    return  a+b

def safe_sum(a, b):
    if   type(a) != type(b) :
         print("더할수 있는 것이 아닙니다")
         return
    else :
            result = sum(a, b)
    return result
    
print( "Current executing module:",  __name__ )

if __name__ == "__main__":
    print( safe_sum('a', 1) )
    print( safe_sum(1, 4) )
    print( safe_sum(10, 10.4) )
