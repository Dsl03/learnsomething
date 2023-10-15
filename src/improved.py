def max_area(height):
    max_area = 0
    l, r = 0, len(height) - 1

    while l < r:
        h1 = height[l]
        h2 = height[r]
        width = r - l
        current_area = min(h1, h2) * width
        max_area = max(max_area, current_area)

        if h1 < h2:
            l += 1
        else:
            r -= 1

    return max_area
