class FFT {
    private static final int MAX_LENGHT = 3;

    static Complex[] fft(Complex[] x, int N, int dir) {

        if (N == 1) {
            return new Complex[]{x[0]};
        }

        Complex[] y1, y2;

        Complex[] x1 = new Complex[N / 2];
        Complex[] x2 = new Complex[N / 2];

        Complex Wn = new Complex(Math.cos(2 * Math.PI / N), dir * Math.sin(2
                * Math.PI / N));
        Complex w = new Complex(1, 0);
        for (int j = 0; j < N / 2; j++) {

            x1[j] = x[j].plus(x[j + N / 2]);
            x2[j] = x[j].minus(x[j + N / 2]).times(w);
            w = w.times(Wn);

        }
        y1 = FFT.fft(x1, N / 2, dir);
        y2 = FFT.fft(x2, N / 2, dir);

        Complex[] result = new Complex[y1.length + y2.length];
        for (int i = 0; i < y1.length; i++) {

            result[i] = y1[i];
            result[i + result.length / 2] = y2[i];

        }

        return result;
    }

    static int indexReverse(int index) {
        StringBuilder value = new StringBuilder(Integer.toBinaryString(index));

        int zeroesCount = MAX_LENGHT - value.length();

        for (int i = 0; i < zeroesCount; i++) {
            value.insert(0, '0');
        }

        for (int i = 0, j = value.length() - 1; i < value.length() / 2; i++, j--) {
            char tmp = value.charAt(i);
            value.setCharAt(i, value.charAt(j));
            value.setCharAt(j, tmp);
        }

        return Integer.parseInt(value.toString(), 2);
    }
}