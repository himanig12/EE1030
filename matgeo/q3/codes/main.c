#include <stdio.h>
#include"collinear.c"

void generate_points(double k, double points[3][2]) {
    points[0][0] = k + 1; 
    points[0][1] = 2 * k; 
    points[1][0] = 3 * k;
    points[1][1] = 2 * k + 3; 
    points[2][0] = 5 * k - 1; 
    points[2][1] = 5 * k; 
}

int main() {
    FILE *fptr = fopen("points.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    for (double k = -10; k <= 10; k += 0.5) {
        double points[3][2];
        generate_points(k, points);
        
        double det = determinant(points);
        if (det == 0) {
            fprintf(fptr, "%lf %lf %lf %lf %lf %lf\n",
                    points[0][0], points[0][1],
                    points[1][0], points[1][1],
                    points[2][0], points[2][1]);
        }
    }

    fclose(fptr);
    return 0;
}
