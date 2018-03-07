class DFT {

    static Complex[] dft(Complex[] x) {
        int N = x.length;
        Complex[] result = new Complex[N];
        for (int i = 0; i < N; i++) {
            result[i] = new Complex(0, 0);
        }

        for (int k = 0; k < N; k++) {
            for (int n = 0; n < N; n++) {

                Complex Wn = new Complex(Math.cos(-2 * Math.PI * k * n / N),
                        Math.sin(-2 * Math.PI * k * n / N));
                result[k] = result[k].plus(x[n].times(Wn));

            }
        }
        return result;

    }

    static Complex[] idft(Complex[] x) {
        int N = x.length;
        Complex[] result = new Complex[N];
        for (int i = 0; i < N; i++) {
            result[i] = new Complex(0, 0);
        }
        for (int k = 0; k < N; k++) {
            for (int n = 0; n < N; n++) {

                Complex Wn = new Complex(Math.cos(2 * Math.PI * k * n / N),
                        Math.sin(2 * Math.PI * k * n / N));
                result[k] = result[k].plus(x[n].times(Wn));

            }
            result[k] = result[k].divides(N);
        }
        return result;
    }

}