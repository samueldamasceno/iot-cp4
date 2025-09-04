// Felipe Prometti - rm555174
// Iris Tavares - rm557728
// Samuel Damasceno - rm558876

#include <string.h>
void score(double * input, double * output) {
    double var0[2];
    if (input[0] <= 0.5596950054168701) {
        if (input[3] <= 0.07973000034689903) {
            memcpy(var0, (double[]){1.0, 0.0}, 2 * sizeof(double));
        } else {
            if (input[3] <= 0.1634950041770935) {
                if (input[0] <= 0.3059450052678585) {
                    memcpy(var0, (double[]){1.0, 0.0}, 2 * sizeof(double));
                } else {
                    memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
                }
            } else {
                memcpy(var0, (double[]){1.0, 0.0}, 2 * sizeof(double));
            }
        }
    } else {
        if (input[2] <= 0.6169399917125702) {
            memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
        } else {
            memcpy(var0, (double[]){1.0, 0.0}, 2 * sizeof(double));
        }
    }
    memcpy(output, var0, 2 * sizeof(double));
}
