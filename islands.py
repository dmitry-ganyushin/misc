class Solution:
    """Algorithms: Solve 'Connected Cells' Using DFS"""
    def __init__(self, m):
        self.matrix = m

    def get_region_size(self, row, col):
        if row < 0 or col < 0 or row >=len(self.matrix) or col >= len(self.matrix[0]):
            return 0
        if self.matrix[row][col] == 0:
            return 0
        
        # mark that we visited it already
        self.matrix[row][col] = 0
        size = 1
        for r in [row-1, row, row+1]:
            for c in [col-1, col, col+1]:
                size += self.get_region_size(r, c)
                    
        return size

    def get_biggest_region(self):
        max_region = 0
        islands=[]
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[0])):
                if self.matrix[r][c] == 1:
                    size = self.get_region_size(r,c)
                    islands.append(size)  
                    max_region = max(max_region, size)
                    
        return islands


def main():
    test_matrix = [[0,0,0,1,1,0,0], [0,1,0,0,1,1,0], [1,1,0,1,0,0,1], [0,0,0,0,0,1,0],[1,1,0,0,0,0,0], [0,0,0,1,0,0,0]]
    
    for r in test_matrix:
        print(r)

    sol = Solution(test_matrix)
    print(sol.get_biggest_region())


if __name__== "__main__":
    main()

