#include <stdio.h>
extern int is_collinear(float x_1, float y_1, float x_2, float y_2, float x_3, float y_3);

void find_collinear_k() {
    for (int k = -100; k <= 100; k++) {
        float k_float = (float)k;

        float x_1 = k_float + 1, y_1 = 2 * k_float;
        float x_2 = 3 * k_float, y_2 = 2 * k_float + 3;
        float x_3 = 5 * k_float - 1, y_3 = 5 * k_float;

        if (is_collinear(x_1, y_1, x_2, y_2, x_3, y_3)) {
            printf("Points are collinear when k = %.1f\n", k_float);
        }
    }
}

int main() {
    find_collinear_k();
    return 0;
}
