import timeit

from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search

def time_search(text, pattern):
    kmp_time = timeit.timeit(lambda: kmp_search(text, pattern), number = 10)
    bm_time = timeit.timeit(lambda: boyer_moore_search(text, pattern), number=10)
    rk_time = timeit.timeit(lambda: rabin_karp_search(text, pattern), number=10)
    return f"{kmp_time: ^25}|{bm_time:^25}|{rk_time:^25}|"

if __name__ == "__main__":
    with open("article1.txt", "r", encoding = "utf8") as f:
        article1 = f.read()
        true_pattern = "швидкий час пошуку"
        false_pattern = "сніг іде"
        print(f"{'text':^15}|{'pattern':^15}|{'kmp':^25}|{'boyer_moore':^25}|{'rabin_karp':^25}|")
        print(f"{'-'*110}")
        print(f"{'article1':^15}|{'true':^15}|{time_search(article1, true_pattern)}")
        print(f"{'-'*95:>110}")
        print(f"{'':^15}|{'false':^15}|{time_search(article1, false_pattern)}")
        print(f"{'-'*110}")
    with open("article2.txt", 'r', encoding ="utf8") as f2:
        article2 = f2.read()
        true_pattern2 = "діаграми рішень"
        print(f"{'article2':^15}|{'true':^15}|{time_search(article2, true_pattern2)}")
        print(f"{'-'*95:>110}")
        print(f"{'':^15}|{'false':^15}|{time_search(article2, false_pattern)}")

   