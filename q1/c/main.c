#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

struct Point {
    float x;
    float y;
};

int main(void) {
    void *handle = dlopen("./section.so", RTLD_LAZY);
    if (!handle) {
        fprintf(stderr, "Failed to load library: %s\n", dlerror());
        return 1;
    }

    struct Point (*section)(float, float, float, float, float, float);
    *(void **)(&section) = dlsym(handle, "section");
    if (!section) {
        fprintf(stderr, "Failed to load section function: %s\n", dlerror());
        dlclose(handle);
        return 1;
    }

    float x1 = -1.0, y1 = 3.0; 
    float x2 = 2.0, y2 = 5.0;
    float m = 3.0, n = 2.0; 

    struct Point sec_point = section(x1, y1, x2, y2, m, n);

    // Print the result
    printf("Section point: (%.2f, %.2f)\n", sec_point.x, sec_point.y);

    // Close the shared library
    dlclose(handle);

    return 0;
}
