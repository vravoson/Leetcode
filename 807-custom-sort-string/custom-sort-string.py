class Solution:
    def customSortString(self, order: str, s: str) -> str:
        eligible_order = set(order).intersection(set(s))
        if len(eligible_order) == 0:
            return ""
        new_order = "".join([x for x in order if x in eligible_order])
        remaining = []
        seen_dict = dict(zip(list(eligible_order), [0]*len(new_order)))
        for letter in s:
            if not(letter in eligible_order):
                remaining.append(letter)
            elif (letter in seen_dict):
                seen_dict[letter] += 1
        remaining = "".join(remaining)
        res = ""
        for elem in new_order:
            res += elem*seen_dict[elem]
        res += remaining
        return res
        