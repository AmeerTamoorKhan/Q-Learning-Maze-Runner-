from Maze import gameSetup as gs
GS = gs.GameSetup


class Agent(GS):

    def __init__(self, screen, maze, tilesize):
        GS.__init__(self, screen=screen, maze=maze, tilesize=tilesize )
        self.tilesize = tilesize

    def agent_block(self, dir):
        x, y = gs.GameSetup.agent[0][0]/self.tilesize, gs.GameSetup.agent[0][1]/self.tilesize
        for i in range(len(GS.blocks)):
            X = GS.blocks[i][0]/self.tilesize
            Y = GS.blocks[i][1]/self.tilesize
            if x == X and y == Y:
                if dir == 'R':
                    gs.GameSetup.agent[0][0] = gs.GameSetup.agent[0][0] - self.tilesize
                if dir == 'U':
                    gs.GameSetup.agent[0][1] = gs.GameSetup.agent[0][1] + self.tilesize
                if dir == 'L':
                    gs.GameSetup.agent[0][0] = gs.GameSetup.agent[0][0] + self.tilesize
                if dir == 'D':
                    gs.GameSetup.agent[0][1] = gs.GameSetup.agent[0][1] - self.tilesize

    def agent_enemy_goal(self):
        x, y = gs.GameSetup.agent[0][0] / self.tilesize, gs.GameSetup.agent[0][1] / self.tilesize

        for i in range(len(GS.enemies)):
            X1 = GS.enemies[i][0]/self.tilesize
            Y1 = GS.enemies[i][1]/self.tilesize
            if len(GS.goal)-1 >= i:
                X2 = GS.goal[i][0] / self.tilesize
                Y2 = GS.goal[i][1] / self.tilesize
            if x == X1 and y == Y1:
                return [True, -10]
            elif x == X2 and y == Y2:
                return [False, 10]
        return [True, -1]






