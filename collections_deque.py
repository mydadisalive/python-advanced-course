from collections import deque

# Create a deque
queue = deque()

# Add elements to the deque
queue.append('Task 1')
queue.append('Task 2')
queue.append('Task 3')

# Remove elements from the deque
completed_task = queue.popleft()
print(f"Completed task: {completed_task}")
