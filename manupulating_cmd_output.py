import curses
from curses import wrapper
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_YELLOW)
    blue_white = curses.color_pair(1)
    red_yellow = curses.color_pair(3)
    for i in range(100):
        stdscr.clear()
        color = blue_white
        if(i%2 == 0):
            color = red_yellow
        stdscr.addstr(f"Number: {i}", color)
        time.sleep(0.1)

        # stdscr.addstr(5, 10, "Yes", blue_white | curses.A_REVERSE)
        # stdscr.addstr(5, 30, "Yes", red_yellow)
        stdscr.refresh()
    stdscr.getch()


wrapper(main)
