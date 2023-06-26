class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def mod(stt1,stt2):
            while stt1.startswith(stt2):
                stt1=stt1[len(stt2):]
            return stt1

        if len(str1)<len(str2):
            return self.gcdOfStrings(str2,str1)
        if not str2:
            return str1
        if not str1.startswith(str2):
            return ""
        

        return self.gcdOfStrings(str2,mod(str1,str2))