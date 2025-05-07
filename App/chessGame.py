class Chess:
    def __init__(self):
        self.gameON = False
        self.playerTurn = None
        self.board = {}
        self.rows = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for i in self.rows:
            a = {}
            for e in range(8):
                a[e] = " "
            self.board[i] = a
    
    def creat_game(self):
        if self.gameON == True:
            return
        self.gameON = True
        #pawns
        for a in self.rows:
            self.board[a][1] = ["black", "pawn", 0]
            self.board[a][-2] = ["white", "pawn", 0]
            
        #rocks
        self.board["A"][0] = ["black", "rock", 0]
        self.board["H"][0] = ["black", "rock", 0]
        self.board["A"][-1] = ["white", "rock", 0]
        self.board["H"][-1] = ["white", "rock", 0]
        
        #knights
        self.board["B"][0] = ["black", "knight"]
        self.board["G"][0] = ["black", "knight"]
        self.board["B"][-1] = ["white", "knight"]
        self.board["G"][-1] = ["white", "knight"]
        
        #bishops
        self.board["C"][0] = ["black", "bishop"]
        self.board["F"][0] = ["black", "bishop"]
        self.board["C"][-1] = ["white", "bishop"]
        self.board["F"][-1] = ["white", "bishop"]
        
        #queen
        self.board["D"][0] = ["black", "queen"]
        self.board["D"][-1] = ["white", "queen"]
        
        #king
        self.board["D"][0] = ["black", "king", 0]
        self.board["D"][-1] = ["white", "king", 0]
        
        self.playerTurn = "white"
        
    def isPositionEmpty(self, position):
        return self.board[position[0]][position[1]]==" "
        
    def legal_moves(self, piece, current_position):
        """returns an array of a piece's legal moves.
        """
        a = []
        if piece[1] == "pawn":
            for x in range(1, 3-piece[2]):
                p = [current_position[0], current_position[1]+x]
                if self.isPositionEmpty(p):
                    a.append(p)
                else:
                    break
            left = chr(ord(current_position[0])-1)
            right = chr(ord(current_position[0])+1)
            if "A" <= left < "H":
                if not self.isPositionEmpty([right, current_position[1]+1]) and self.board[right][current_position[1]+1][0]!=piece[0]:
                    a.append([right, current_position[1]+1])
            if "A" <= right <= "H":
                if not self.isPositionEmpty([left, current_position[1]+1]) and self.board[left][current_position[1]+1][0]!=piece[0]:
                    a.append([left, current_position[1]+1])
        elif piece[1] == "rock":
            horizontal = "A"
            vertical = 0
            while horizontal <= "H":
                p = [horizontal, current_position[1]]
                if self.isPositionEmpty(p) or self.board[p[0]][p[1]][0]!=piece[0]:
                    a.append(p)
                horizontal = chr(ord(horizontal)+1)
            while vertical <= 7:
                p = [current_position[0], vertical]
                if self.isPositionEmpty(p) or self.board[p[0]][p[1]][0]!=piece[0]:
                    a.append(p)
                vertical += 1
        return a
                    
            
        
    def move_piece(self, piece, current_position, new_position):
        """move a chess piece from 'current_position' to 'new_position'.

        Args:
            piece (array):['black', 'queen']
            current_position (array): exemple ['D', 3]
            new_position (array): exemple ['D', 4]
        """
        if current_position == new_position:
            return -1
        if piece[0] != self.playerTurn:
            return -2
        
        
        
        