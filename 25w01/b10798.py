"""
241231

input:
ABCDE
abcde
01234
FGHIJ
fghij

output: Aa0FfBb1GgCc2HhDd3IiEe4Jj

input:
AABCDD
afzz
09121
a8EWg6
P5h3kx
"""

inputs = []
for _ in range(5):
    line = input()
    inputs.append(line)

inputs_len = [len(line) for line in inputs]

answer = ""

for col_idx in range(max(inputs_len)):
    for row_idx in range(5):
        if col_idx < inputs_len[row_idx]:
            answer += inputs[row_idx][col_idx]

print(answer)
