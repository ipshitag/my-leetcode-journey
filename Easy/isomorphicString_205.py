def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    mapping_s_to_t = {}
    mapping_t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in mapping_s_to_t:
            if mapping_s_to_t[char_s] != char_t:
                return False
        else:
            mapping_s_to_t[char_s] = char_t

        if char_t in mapping_t_to_s:
            if mapping_t_to_s[char_t] != char_s:
                return False
        else:
            mapping_t_to_s[char_t] = char_s

    return True

# Example usage:
if __name__ == "__main__":
    s = "egg"
    t = "add"
    print(isIsomorphic(s, t))  # Output: True

    s = "foo"
    t = "bar"
    print(isIsomorphic(s, t))  # Output: False

    s = "paper"
    t = "title"
    print(isIsomorphic(s, t))  # Output: True