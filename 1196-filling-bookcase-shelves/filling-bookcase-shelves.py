class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        @cache
        def f(book, currWidth, height, shelfWidth):
            if len(book) == 1:
                if book[0][0] + currWidth > shelfWidth:
                    return height + book[0][1]
                else:
                    return max(height, book[0][1])
            else:
                b = book[0]
                if b[0] + currWidth > shelfWidth: # no space on the shelf
                    return height + f(book[1:], b[0], b[1], shelfWidth) # create a new one
                else:
                    return min(height + f(book[1:], b[0], b[1], shelfWidth)
                               ,f(book[1:], currWidth + b[0], max(height, b[1]), shelfWidth))

        
        res = f(tuple(map(tuple,books)), 0, 0, shelfWidth)
        
        return res
                
            
            

        