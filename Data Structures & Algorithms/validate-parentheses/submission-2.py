class Solution:
    def isValid(self, s: str) -> bool:

        # base case
        if len(s) % 2 != 0:
            return False

        # store popped (only half the chars)
        popped = [None for _ in range(int(len(s) / 2))]
        pop_pointer = -1

        # start popping
        for top in range(len(s) - 1, -1, -1):
            char = s[top]
            print(f"top char: {char}")

            if char in [')', '}', ']']:
                pop_pointer += 1
                if (pop_pointer > int(len(s) / 2) - 1):
                    return False
                popped[pop_pointer] = char # add to popped array
                print(f"added char to popped array: {popped}")

            else:
                if char == '{' and popped[pop_pointer] == '}':
                    pop_pointer -= 1
                    print(f"found: {{ and pop_pointer is: {pop_pointer}")
                    continue
                elif char == '(' and popped[pop_pointer] == ')':
                    pop_pointer -= 1
                    print(f"found: (( and pop_pointer is: {pop_pointer}")
                    continue
                elif char == '[' and popped[pop_pointer] == ']':
                    pop_pointer -= 1
                    print(f"found: [[ and pop_pointer is: {pop_pointer}")
                    continue
                else:
                    return False
        
        return True