//3610 minimum-number-of-primes-to-sum-to-target

class Solution {

    public int minNumberOfPrimes(int n, int m) {
        // --- Step 1: Generate primes up to 'n' using Sieve of Eratosthenes ---
        // 'primes' boolean array: primes[i] will be true if 'i' is prime, false otherwise.
        // The sieve limit is 'n' because any prime larger than 'n' cannot be used to form sum 'n'.
        boolean[] isPrimeSieve = new boolean[n + 1];
        Arrays.fill(isPrimeSieve, true); // Assume all numbers are prime initially

        // 0 and 1 are not prime numbers
        if (n >= 0) isPrimeSieve[0] = false;
        if (n >= 1) isPrimeSieve[1] = false;

        // Apply Sieve of Eratosthenes: Mark multiples of primes as non-prime
        for (int i = 2; i * i <= n; i++) {
            if (isPrimeSieve[i]) { // If 'i' is prime
                // Mark all multiples of 'i' (starting from i*i) as not prime
                for (int j = i * i; j <= n; j += i) {
                    isPrimeSieve[j] = false;
                }
            }
        }

        // --- Step 2: Collect the first 'm' prime numbers (up to 'n') ---
        // 'reqPrimes' will store the actual prime numbers we can use as "coins".
        Set<Integer> reqPrimes = new HashSet<>();
        int primesFoundCount = 0; // Counter for how many primes from the first 'm' we've added

        // Iterate from 2 up to 'n' to find primes
        for (int i = 2; i <= n; i++) {
            if (isPrimeSieve[i]) { // If 'i' is prime
                primesFoundCount++; // Increment count of primes found
                reqPrimes.add(i);   // Add the prime to our set of available primes

                // Optimization/Edge Case: If 'n' itself is a prime and it's among the first 'm' primes,
                // then 1 mutation is enough.
                if (n == i) {
                    return 1;
                }
            }
            // Stop collecting primes once we have found the first 'm' primes.
            // Note: This correctly limits the primes to the 'first m' that are also <= n.
            if (primesFoundCount == m) {
                break;
            }
        }

        // --- Step 3: Dynamic Programming for Minimum Coin Change ---
        // 'dp[i]' stores the minimum number of primes needed to sum up to 'i'.
        int[] dp = new int[n + 1];
        // Initialize all sums as unreachable (Integer.MAX_VALUE)
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0; // Base case: 0 primes needed to sum to 0

        // Iterate through each available prime number (our "coin")
        for (int prime : reqPrimes) {
            // Iterate through possible sums from 'prime' up to 'n'.
            // This order allows each prime to be used multiple times (unbounded knapsack).
            for (int currentSum = prime; currentSum <= n; currentSum++) {
                // Check if the subproblem (currentSum - prime) was reachable
                if (dp[currentSum - prime] != Integer.MAX_VALUE) {
                    // Update dp[currentSum] with the minimum of:
                    // 1. Its current value (from previous primes or existing path)
                    // 2. 1 (for using the current 'prime') + dp[currentSum - prime] (min primes for remaining sum)
                    dp[currentSum] = Math.min(dp[currentSum], 1 + dp[currentSum - prime]);
                }
            }
        }

        // --- Step 4: Return the result ---
        // If dp[n] is still Integer.MAX_VALUE, it means 'n' cannot be formed
        // by the given prime numbers.
        return dp[n] == Integer.MAX_VALUE ? -1 : dp[n];
    }
}

// TC:

// O(n log log n)    → for sieve
// + O(n)            → to collect m primes
// + O(m * n)        → for DP

// = O(n log log n + m * n)

// SC:

// O(n) for sieve
// + O(m) for prime set
// + O(n) for dp

// = O(n)
