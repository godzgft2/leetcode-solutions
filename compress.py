#LeetCode: 443. String Compression
#Runtime: 57ms, Beats 63.71%
#Memory: 16.71MB, Beats 11.90%

#Compresses a string by changing repeated characters into the form: ["(char)", "(num of char)"]
#For example, ["a", "a", "a", "b", "b", "c"] would be ["a", "3", "b", "2", "c"]

def compress(self, chars: List[str]) -> int:
    s = ""
    temp = ""
    count = 0
    if len(chars) == 1:
        return
    for i in range(len(chars)):
        if i == 0:
            temp = chars[0]
            count = count + 1
        elif i == len(chars)-1:
            if temp == chars[i]:
                s = s + temp + str(count+1)
            else:
                if count == 1:
                    s = s + temp + chars[i]
                else:
                    s = s + temp + str(count) + chars[i]
        else:
            if chars[i] == temp:
                count = count + 1
            else:
                if count == 1:
                    s = s + temp
                    temp = chars[i]
                    count = 1
                else:
                    s = s + temp + str(count)
                    temp = chars[i]
                    count = 1
    chars.clear()
    for i in range(len(s)):
        chars.append(s[i])
