float area_of_triangle(float x_1, float y_1, float x_2, float y_2, float x_3, float y_3) {
    return x_1 * (y_2 - y_3) + x_2 * (y_3 - y_1) + x_3 * (y_1 - y_2);
}
int is_collinear(float x_1, float y_1, float x_2, float y_2, float x_3, float y_3) {
    float area = area_of_triangle(x_1, y_1, x_2, y_2, x_3, y_3);
    return area == 0 ? 1 : 0;
}
