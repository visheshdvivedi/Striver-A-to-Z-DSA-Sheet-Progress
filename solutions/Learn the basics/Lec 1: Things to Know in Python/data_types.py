class Solution:
    def dataTypeSize(self, str):
        data = {
            "Character": 1,
            "Integer": 4,
            "Long": 8,
            "Float": 4,
            "Double": 8
        }
        return data.get(str, 0)