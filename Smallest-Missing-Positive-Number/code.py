def findSmallestPositiveMissingNumber(order_nums) -> int:
    n = len(order_nums)

    for i in range(n):
        while (
            1 <= order_nums[i] <= n and order_nums[order_nums[i] - 1] != order_nums[i]
        ):
            order_nums[i], order_nums[order_nums[i] - 1] = (
                order_nums[order_nums[i] - 1],
                order_nums[i],
            )

    for i in range(n):
        if order_nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    orderNumberCount = int(input().strip())

    order_nums = []

    for _ in range(orderNumberCount):
        order_num_item = int(input().strip())
        order_nums.append(order_num_item)

    result = findSmallestPositiveMissingNumber(order_nums)

    print(result)
