float area_of_triangle(float x1, float y1, float x2, float y2, float x3, float y3) {
    return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);
}
int is_collinear(float x1, float y1, float x2, float y2, float x3, float y3) {
    float area = area_of_triangle(x1, y1, x2, y2, x3, y3);
    return area == 0 ? 1 : 0;
}
