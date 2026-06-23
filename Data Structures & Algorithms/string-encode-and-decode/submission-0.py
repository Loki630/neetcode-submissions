class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_msg = ""
        for item in strs:
            encoded_msg += "-" + item
        return encoded_msg
    def decode(self, s: str) -> List[str]:
        return [item for item in s.split("-")[1::]]
