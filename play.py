from nim import train, play

ai = train(10000)
#play(ai) 0 goes first, 1 goes second, player who goes second always win
play(ai, 1)
