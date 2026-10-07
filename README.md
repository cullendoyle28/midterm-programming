# CMPSC 202 - Midterm Programming Assignment

Name: *Cullen Doyle*

**Instructions**: Complete the exercise below. Open book, open notes, any tools allowed (except submitting another student's work). Due tonight (10/6) at 11:59pm.

**Submission**: Fork this repository and invite your professor (username: bcmullins) to the repository. To submit, push your code to your forked repository. Make sure to include your name in the README file.

You have been provided with a starter Python file (`midterm_starter.py`). This file contains two fully implemented algorithms that solve the exact same problem: finding if an array contains duplicate values.

The file also contains a `flawed_benchmark()` function. The developer who wrote this benchmark made several severe methodological errors, making the printed timing results completely unreliable for comparing the asymptotic growth of these two algorithms.

**Your tasks**: 

1. Rewrite the `flawed_benchmark()` function to provide a robust empirical comparison of the two algorithms. List the methodological errors in the original benchmark and explain how you fixed them. Your benchmark should demonstrate the scaling behavior of the two algorithms across multiple input sizes.

- The original benchmark was timing the algorithm's runtime while the inputs were being generated. The fix was to create the inputs before the timing starts.
- Since we are comparing both algorithms directly, we want them to have the same list. But, the original benchmark had each algorithm receive a different list, which could interfere with runtime. So, the new benchmark now gives both the same list
- In the original benchmark, random inputs could contain duplicated early which would stop the algorithm before checking the whole list. So, the new benchmark doesn't have duplicates so we can measure the runtime in the worst case.
- Another problem was that only one input size was tested. The updated benchmark tests sizes of 100, 500, 1000, 2000, and 4000 now.
- The algorithms were times only once. In the new benchmark, we're now timing them each 5 times and calculating the average.
- There was no graph being created. So, now we're creating one.

2. Run the empirical comparion and plot the results using a plotting library of your choice (e.g., `matplotlib`, `seaborn`, etc.). Include the plot in your submission called `results.png`. Be sure to label your axes and include a legend.



