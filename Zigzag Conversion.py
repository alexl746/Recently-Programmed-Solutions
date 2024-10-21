#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (Runs in 31 ms, beats 78% of submissions)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
class Solution(object):
    def convert(self, s, numRows):
        array_2d = [[] for _ in range(numRows)]
        finished = False
        counter = -1
        while finished == False:
            for i1 in range(numRows):
                counter += 1
                array_2d[i1].append(s[counter])
                if counter == len(s)-1:
                    finished = True
                    break
            if finished == True:
                break
            height = numRows-2
            while height > 0:
                counter += 1
                array_2d[height].append(s[counter])
                height -= 1
                if counter == len(s)-1:
                    finished = True
                    break
        answer = ""
        for n in range(numRows):
          for n1 in range(len(array_2d[n])):
                answer += str(array_2d[n][n1])
        return answer
