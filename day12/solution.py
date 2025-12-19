# Advent of Code 2025 - Day 12
# Solution Credit: https://topaz.github.io/paste/#XQAAAQD5BQAAAAAAAAARiEJGPfQWNG6xo4rUnrU/FzgTXmJOWQF53DaV6F4jcQsRQpNT4KyGWX5hUaw6B9k53WIygUgvNBvQkRGPG+IKInbVYAc6btJ6/GVnvPET2y6kPmce5FE9LN4xK31P4no3KH3ViU6LJXG+coYQrHm+vHWznE8NijgRTytN6G6s+/g/p/4z0nXxu9Vq8maihzjX3fx6OTqeDCdPYUFnaWDmpwLxda1IRtc5t/oUzk9WZa0C+WXypUQDZ1VCn/XYMjXa2GnN0wQsdU8i3kbPp9tPMKzhbbNu8AoVaIui/oEpsCNuo0l5ojCIpxEFhEYkxvbSb/FlOIsyRIpC+Kzo7jyhF27nBBzKXqKrPoew+HjqpNHCSX5rHbGL4njhh8/0oKJ686D1QV/gK/1/chjPWYcVEj1h6rqCjqJrI2mctDLgGbUDNW2I7NxfkntYw0KO4kpaAjpzDjjmlvDjqzJkq6Z4CWavspGbomg6UPUUSN9KG5CBA6jsb9UCHcHcp1EaPSswQR/FUChKV0q1p0iMDewsKcuM9yVADohrGAGrOhgPQCHg51Rk1jqr0UsiZlkzjlxaI6MyXlZloiz0d927CES81C9W+kvqhWbSqFXYciAMCrUhclj/RE7cxOMZpB5EHAU8zdZdtzCo4l+50/6BEWg+Qg6hInlID7qJR6VYLjOUQB+HO6XiLcjT99Dkl+yeM1ePbQf8bFOhv0aiQP+gJrpUKC7HCsT7QfXzQRFNM7fR1DNBCOosAZQQ69lVcTPdBXvMzdAg9IPDByQzYF07kMRBB5RV1HtPzCd18K0utJZ30FBwlgSuyycFUamkOhspnToDAtzG8TLe6qtLRKgY7v/duHv9

lines = open("input.txt").read().strip().split("\n")

regions = []

last_shape = None
for line in lines:
    line = line.strip()
    if not line:
        continue
    elif "#" in line or "." in line:
        continue
    elif ":" in line:
        parts = line.split(":")
        if parts[1].strip() == "":
            continue
        else:
            w, h = map(int, parts[0].split("x"))
            counts = list(map(int, parts[1].strip().split()))
            regions.append(((w, h), counts))

# Part 1
def part1():
    count = 0
    for (w, h), counts in regions:
        total_area = w * h
        if 9 * sum(counts) <= total_area:
            count += 1
    print(count)

# Part 2
def part2():
    print("Merry Christmas!")

if __name__ == "__main__":
    part1()
    part2()