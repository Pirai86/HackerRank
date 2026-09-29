def avg_count(response_times):
    avg = 0
    items = []
    count = 0
    if len(response_times) == 0:
        return 0
    else:
        for i, num in enumerate(response_times):
            if i == 0:
                items.append(num)
                continue
            avg = sum(items) / len(items)
            if avg < num:
                count += 1
            items.append(num)
        return count


if __name__ == "__main__":
    response_times_count = int(input().strip())

    response_times = []

    for _ in range(response_times_count):
        response_times_item = int(input().strip())
        response_times.append(response_times_item)

    result = avg_count(response_times)

    print(result)
