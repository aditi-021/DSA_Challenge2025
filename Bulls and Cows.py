class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x = 0
        bucket = [0]*10

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                x += 1
            else:
                bucket[int(secret[i])] += 1
                bucket[int(guess[i])] -= 1
        y = len(secret) - x - sum(b for b in bucket if b>0)

        return f'{x}A{y}B'

            
            
    
            


        
