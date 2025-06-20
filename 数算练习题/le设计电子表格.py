class Spreadsheet:

    def __init__(self, rows: int):
        self.l=[[0]*26 for _ in range(rows+1)]

    def setCell(self, cell: str, value: int) -> None:
        n=int(cell[1:])
        m=ord(cell[0])-65
        self.l[n][m]=value

    def resetCell(self, cell: str) -> None:
        n=int(cell[1:])
        m=ord(cell[0])-65
        self.l[n][m]=0

    def getValue(self, formula: str) -> int:
        n,m=formula.split('+')
        ans=0
        if ord(n[1])>=65:
            x=int(n[2:])
            y=ord(n[1])-65
            ans+=self.l[x][y]
        else:
            ans+=int(n[1:])
        if ord(m[0])>=65:
            x=int(m[1:])
            y=ord(m[0])-65
            ans+=self.l[x][y]
        else:
            ans+=int(m)
        return ans

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)