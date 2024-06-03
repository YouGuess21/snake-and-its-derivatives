# Snake and its derivatives

This repository is for a fun project I took up for myself in summer '24. It might be a good way to learn and explore pygame as well as data structures grids grids, lists, vectors etc.

I would highly like to thank creator of [this.](https://github.com/clear-code-projects/Snake) It has provided me good entry level pygame knowledge and helped me create something to test other stuff on top of snake.

Current progress:
- [x] Snake game: basic snake game in pygame that follows usually rules and can be controlled by user.
- [x] Snake wrap-around: basic snake but walls are not collisions but wrap around (for ex, going out from right, snake comes in from left.)
- [z] Ekans : fun idea by me to start with more than half of board already covered by snake, every time apple is eaten snake reduces in size by one, but snake leaves a block where its tail was, you win when snake vanishes. This is played in wrap-around mode.
- [x] Hamiltonian Cycle solution: Automating snake movement, using hamiltonian cycle that gives guranteed solution. Hamiltonia cycles cover all the vertices (here, all squares on grid) without repeating any vertices and ends on starting node back again. My code of generation of cycle is not the greatest as of now but hey it works!
- [x] A* algorithm: I plan to solve snake using A* or similar algorithm to make snake movement efficient. As of now, I understand that this has to go through many error checks as snake would trap itself on one side of board or within itself, not perfect at all.
- [x] Wrap around A*: works better normal snake A* but only because of added checks while spawning fruit, snake still dies when fruit is inside it's body.
- [x] Ekans A*: Works pretty good with current snake size, and is exactly what it sounds, pretty fun to watch, not perfect yet tho.
- [ ] Reinforcement learning: I have found a good video on youtube that does exactly this... will try it myself too.

I will also try to include more and more interesting stuff I find from various sources. Current suggestions include reinforcement learning.
