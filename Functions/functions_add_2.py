import math

def add(float1, float2):
    result = float1 + float2
    math.ceil(result)
    if result % 2 > 0:
        result = result + 0.5
    return int(result)

def main():
    float1 = float(input("Enter a float: "))
    float2 = float(input("Enter a float: "))
    return add(float1, float2)
    
print(main())
#supposed to add this

if __name__ == "__main__":
    main()