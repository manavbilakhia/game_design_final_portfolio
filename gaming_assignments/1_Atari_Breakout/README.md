# <center>Atari Breakout</center>
* Press right key to move the paddle to the right
* Press left key to  move the paddle to the left
* game ends as soon as you hit the last brick or when you are out of lives

* To start the go to the correct directory where the game files are on the terminal
* Copy paste the following command and have fun

<pre><code>python breakout_game.py
</code></pre>

## Revision Notes:

* not a big fan of your `generate_bricks()` function - thre's got to be an easier way.  For starters, the last two lines of every block are identical, so can be moved  out of the blocks entirely.  Some simple math would let you turn it int a much cleaner function.
* why didn't you use circles?  That is worth doing in a revision.
* the assignment was scaffolded in such a way that I expected you to implement your own collision code rather than using the built-in pygame methods.  Could you have implemented your own? Worth revising to show me you can do it.
