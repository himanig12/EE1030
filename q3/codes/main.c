#include <stdio.h>
extern int is_collinear(float x1, float y1, float x2, float y2, float x3, float y3);

void find_collinear_k() {
    for (int k = -100; k <= 100; k++) {
        float k_float = (float)k;

        float x1 = k_float + 1, y1 = 2 * k_float;
        float x2 = 3 * k_float, y2 = 2 * k_float + 3;
        float x3 = 5 * k_float - 1, y3 = 5 * k_float;

        if (is_collinear(x1, y1, x2, y2, x3, y3)) {
            printf("Points are collinear when k = %.1f\n", k_float);
        }
    }
}

int main() {
    find_collinear_k();
    return 0;
}
