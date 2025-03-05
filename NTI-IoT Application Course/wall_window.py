w, h, d = map(int, input().split())
window_width = w - 2 * d
window_height = h - 2 * d
if window_width <= 0 or window_height <= 0:
    print(0)
else:
    area = window_width * window_height
    print(area)
