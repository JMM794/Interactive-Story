def present_text_in_box(text):
    """Display text in a box format."""
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    border = '+' + '-' * (max_length + 2) + '+'

    print(border)
    for line in lines:
        print('| ' + line + ' ' * (max_length - len(line)) + ' |')
    print(border)

text = """01: A, 02: B, 03: C, 04: D, 05: E,
06: F, 07: G, 08: H, 09: I, 10: J,
11: K, 12: L, 13: M, 14: N, 15: O,
16: P, 17: Q, 18: R, 19: S, 20: T,
21: U, 22: V, 23: W, 24: X, 25: Y,
26: Z"""