import heapq
from dataclasses import dataclass

@dataclass
class Group:
    sum: int

with open('2022/day1/input.txt') as f:
    lines = f.read().splitlines()

queue = []
current_sum = 0

for line in lines:
    if not line:
        heapq.heappush(queue, current_sum)
        current_sum = 0
    else:
        current_sum += int(line)

largest = heapq.nlargest(1, queue)
print(sum(largest))

largest = heapq.nlargest(3, queue)
print(sum(largest))
