def candies(n, arr):
    # Write your code here
    aux = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            aux[i] = aux[i-1] + 1
    for i in range((n-1), 0, -1):

        if arr[i] < arr[i-1] and aux[i-1] <= aux[i]:
            aux[i-1] = aux[i] + 1

    return aux







candies(10, [1, 2, 3, 7, 3, 8, 7, 6, 5, 9])