class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res +=str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0 
        while i < len(s):
            # Find the '#' delimiter
            j = i
            while s[j] != '#':
                j += 1
            
            # Get the length (could be multiple digits)
            length = int(s[i:j])
            
            # Move past the '#'
            i = j + 1
            
            # Extract the string
            ans.append(s[i:i + length])
            
            # Move to next encoded string
            i += length
        
        return ans

                    

                
