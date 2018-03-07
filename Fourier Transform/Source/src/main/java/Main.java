public class Main {

    private static int N = 8;

    public static void main(String[] args) {

        Complex[] input;

        input = getData();

        System.out.println("-------Origin data----------");
        show(input);

        System.out.println("----------FFT----------");

        Complex[] output = FFT.fft(input, N, 1);
        Complex[] correctResult = new Complex[N];

        for (int i = 0; i < output.length; i++) {
            correctResult[FFT.indexReverse(i)] = output[i];
        }
        show(correctResult);

        System.out.println("----------IFFT----------");

        output = FFT.fft(correctResult, N, -1);
        for (int i = 0; i < output.length; i++) {
            correctResult[FFT.indexReverse(i)] = output[i].divides(N);
        }
        show(correctResult);

        System.out.println("----------DFT----------");
        output = DFT.dft(input);
        show(output);
        getAFC(output);
        getPhase(output);

        System.out.println("----------IDFT----------");
        output = DFT.idft(output);

        show(output);

    }

    private static void show(Complex[] x) {
        for (int i = 0; i < x.length; i++)
            System.out.println(x[i].toString());
    }

    private static Complex[] getData() {

        Complex[] output = new Complex[N];
        double PI = 3.14;
        for (double i = PI, j = 0; j < N; j++, i += PI / 4) {
            double a = Math.sin(Math.round(i)) + Math.cos(Math.round(i));

            output[(int) j] = new Complex(a, 0);

        }

        return output;
    }

    private static void getAFC(Complex[] x) {
        System.out.println("-------Amplitude-------");
        for (Complex point : x) {
            System.out.println(point.abs());
        }
    }

    private static void getPhase(Complex[] x) {
        System.out.println("--------Phase--------");
        for (Complex point : x) {
            System.out.println(point.phase());
        }
    }
}