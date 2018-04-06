public class Transform {

    private int N = 8;
    private Complex[] x;
    private int[][] hadamard;

    Transform(Complex[] x) {
        this.x = x;
        fillHadamard();
    }

    public Complex[] fastTransform(Complex[] x, int N) {

        if (N == 1) {
            return new Complex[]{x[0]};
        }

        Complex[] y1, y2;

        Complex[] x1 = new Complex[N / 2];
        Complex[] x2 = new Complex[N / 2];

        for (int j = 0; j < N / 2; j++) {

            x1[j] = x[j].plus(x[j + N / 2]);
            x2[j] = x[j].minus(x[j + N / 2]);


        }
        y1 = fastTransform(x1, N / 2);
        y2 = fastTransform(x2, N / 2);

        Complex[] result = new Complex[y1.length + y2.length];
        for (int i = 0; i < y1.length; i++) {

            result[i] = y1[i];
            result[i + result.length / 2] = y2[i];

        }

        return result;
    }


    public Complex[] inverseFastTransform(Complex[] x, int N) {

        if (N == 1) {
            return new Complex[]{x[0]};
        }

        Complex[] x1 = new Complex[N / 2];
        Complex[] x2 = new Complex[N / 2];

        for (int j = 0; j < N / 2; j++) {

            x1[j] = x[j];
            x2[j] = x[j + N / 2];

        }
        x1 = inverseFastTransform(x1, N / 2);
        x2 = inverseFastTransform(x2, N / 2);

        Complex[] result = new Complex[N];
        for (int i = 0; i < N / 2; i++) {

            result[i] = x1[i].plus(x2[i]);
            result[i + N / 2] = x1[i].minus(x2[i]);

        }
        return result;
    }


    public Complex[] discreteTransform() {

        Complex[] result = new Complex[N];
        for (int i = 0; i < N; i++) {
            result[i] = new Complex(0, 0);
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                result[i] = result[i].plus(x[j].times(hadamard[i][j]));
            }
        }
        for (int i = 0; i < N; i++) {
            result[i] = result[i].divides(N);
        }

        return result;
    }

    public Complex[] inverseDiscreteTransform(Complex[] result) {
        Complex[] inverse_result = new Complex[N];
        for (int i = 0; i < N; i++) {
            inverse_result[i] = new Complex(0, 0);
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                inverse_result[i] = inverse_result[i].plus(result[j]
                        .times(hadamard[i][j]));

            }
        }
        return inverse_result;

    }


    private void fillHadamard() {
        hadamard = new int[N][N];
        hadamard[0][0] = 1;
        for (int k = 1; k < N; k += k) {
            for (int i = 0; i < k; i++) {
                for (int j = 0; j < k; j++) {
                    hadamard[i + k][j] = hadamard[i][j];
                    hadamard[i][j + k] = hadamard[i][j];
                    hadamard[i + k][j + k] = hadamard[i][j] * (-1);
                }
            }
        }

    }

}