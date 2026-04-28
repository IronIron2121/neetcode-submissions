class Solution:

    def encode(self, strs: List[str]) -> str:
        print(len(strs))
        return "_%_".join(strs) + '_%_' if len(strs) > 0 else ''

    def decode(self, s: str) -> List[str]:
        print("S == ", s)
        return s.split("_%_")[:-1] if s != '' else []