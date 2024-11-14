from urllib.request import urlopen


url = "https://www.mit.edu/~ecprice/wordlist.10000"
word_list = urlopen(url).read().decode('utf-8').splitlines()

counters = [0] * 23

print(f"{len(word_list)} words")

avg = 0
beeg_string = ""
for word in word_list:
    beeg_string += word
avg = len(beeg_string) / 10000

print(f"The average word length is {avg}")

for word in word_list:
    counters[len(word)] += 1
print("Length Count")
for i in range(1, len(counters)):
    print(f"{i:>6}  {counters[i]:>4}")



