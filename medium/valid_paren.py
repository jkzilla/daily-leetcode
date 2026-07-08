class Valid:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
    
if __name__ == "__main__":
    valid = Valid()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("{[()]}", True),
        ("{[(])}", False)
    ]

    for s, expected in test_cases:
        result = valid.isValid(s)
        print(f"isValid('{s}') = {result}, expected = {expected}, {'PASS' if result == expected else 'FAIL'}")