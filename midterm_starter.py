import time

# =======================================================
# DO NOT MODIFY THE ALGORITHM IMPLEMENTATIONS
# =======================================================

def find_duplicates_slow(data):
    """An O(n^2) algorithm to find duplicates."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def find_duplicates_fast(data):
    """An O(n) algorithm to find duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


# =======================================================
# YOUR TASK: FIX THE BENCHMARKING SCRIPT BELOW
# =======================================================

def flawed_benchmark():
    """
    This benchmarking function contains several methodological errors.
    Rewrite this function to properly and fairly compare the two algorithms to demonstrate their scaling behavior.
    """
    input_sizes = (100, 500, 1000, 2000, 4000)
    trials = 5
    slow_times = []
    fast_times = []
    datasets = {}

    for n in input_sizes:
        datasets[n] = list(range(n))

    for n in input_sizes:
        data = datasets[n]
        slow_trial_times = []
        fast_trial_times = []

        for _ in range(trials):
            start = time.perf_counter()
            find_duplicates_slow(data)
            end = time.perf_counter()
            slow_trial_times.append(end - start)

            start = time.perf_counter()
            find_duplicates_fast(data)
            end = time.perf_counter()
            fast_trial_times.append(end - start)

        slow_average = sum(slow_trial_times) / len(slow_trial_times)
        fast_average = sum(fast_trial_times) / len(fast_trial_times)
        slow_times.append(slow_average)
        fast_times.append(fast_average)
        print(
            f"n={n:>5}: slow={slow_times[-1]:.6f}s, "
            f"fast={fast_times[-1]:.6f}s"
        )

    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 5))
    plt.loglog(input_sizes,slow_times,marker="o",label="find_duplicates_slow (quadratic, O(n^2))",)
    plt.loglog(input_sizes,fast_times,marker="o",label="find_duplicates_fast (linear, O(n))",)
    plt.xlabel("Input size (n)")
    plt.ylabel("Average execution time (seconds)")
    plt.title("Duplicate-finding algorithm scaling: O(n^2) vs. O(n)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("results.png", dpi=150)
    plt.close()

    return {
        "input_sizes": list(input_sizes),
        "slow_times": slow_times,
        "fast_times": fast_times,
    }


if __name__ == "__main__":
    flawed_benchmark()