def count_squares(points):
    point_set = set(points)
    count = 0
    n = len(points)

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1

            # 两个正方形方向：顺时针和逆时针
            # 旋转向量 90 度
            bx1 = x1 - dy
            by1 = y1 + dx
            dx1 = x2 - dy
            dy1 = y2 + dx

            if (bx1, by1) in point_set and (dx1, dy1) in point_set:
                count += 1

            # 旋转向量 -90 度
            bx2 = x1 + dy
            by2 = y1 - dx
            dx2 = x2 + dy
            dy2 = y2 - dx

            if (bx2, by2) in point_set and (dx2, dy2) in point_set:
                count += 1

    return count // 2  # 每个正方形被算两次
