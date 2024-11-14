import math

def add(float1, float2):
    result = float1 + float2
    if result % 1 >= 0.5:
        result = math.ceil(result)
    else:
        result = math.floor(result)
    if result % 2 > 0:
        result = result + 0.5
    return int(result)

def main():
    float1 = 3.1
    float2 = 9.2
    return add(float1, float2)

if __name__ == "__main__":
    print(main())
