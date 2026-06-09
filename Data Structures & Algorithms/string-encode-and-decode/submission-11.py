import base64

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
            
        for idx in range(len(strs)):
            new_str = f"{len(strs[idx])}#{strs[idx]}"
            print(new_str)
            bytes_str = base64.b64encode(new_str.encode('utf-8'))
            encoded_str = bytes_str.decode('utf-8')
            strs[idx] = encoded_str

        return ",".join(strs)            

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        strs = s.split(",")
        for idx in range(len(strs)):
            decoded_bytes = base64.b64decode(strs[idx].encode('utf-8'))
            decoded_str = decoded_bytes.decode('utf-8')
            print(decoded_str)
            new_str = decoded_str.split("#", 1)[1]
            print(new_str)
            strs[idx] = new_str
        return strs