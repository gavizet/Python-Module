""" Simple progress bar program to inititiate us to yield and function generators """
from time import sleep, time
import sys

# Output time in format :
# ETA: 14.67s [ 9%][=> ] 327/3333 | elapsed time 1.33s


def ft_progress(lst):
    """
    Generator function that displays a progress bar with estimated time of
    arrival (ETA) and elapsed time for a given iterable.

    Args:
      lst: The list of elements that we want to iterate over and track progress for.
            It is a range of numbers.
    """
    total_iterations = len(lst)
    bar_len = 20
    start_time = time()
    for count, element in enumerate(lst, 1):
        percentage_completed = count / total_iterations
        # How many '=' we will print to visualize progress. 20 / percentage
        len_progress_bar = int(bar_len * percentage_completed)
        bar_done = "="*len_progress_bar
        # Fill the rest of the bar with spaces for smoother visualization
        bar_left = " "*(bar_len - len_progress_bar)
        # Time passed since we launched the program for the first time
        elapsed_time = time() - start_time
        # Average time it takes to do one full loop of our generator function
        operation_time = elapsed_time / count
        # Time left before end of the progress bar's execution
        eta = operation_time * (total_iterations - count)
        # Print f-string to stdout with a carriage return
        print(
            f"ETA: {eta:.2f}s "
            f"[{percentage_completed:.2%}]"
            f"[{bar_done:s}>{bar_left:s}] "
            f"{count:d}/{total_iterations:d}"
            f" | elapsed time {elapsed_time:.2f}s",
            end="\r", file=sys.stdout, flush=True)
        # Returns our iteratable generator object
        yield element


if __name__ == "__main__":
    RET = 0
    X = range(1000)
    for elem in ft_progress(X):
        RET += (elem + 3) % 5
        sleep(0.01)
    print()
    print(RET)
