public class Correlation {
    public static Complex[] corr(Complex[] signalZ, Complex[] signalY) {
        Complex[] result = new Complex[signalZ.length];

        for (int i = 0; i < result.length; i++) {
            result[i] = new Complex(0, 0);
        }

        for (int i = 0; i < signalZ.length; i++) {
            for (int j = 0; j < signalZ.length; j++) {
                int index = i + j;

                if (index >= signalZ.length) {
                    index = -signalZ.length + index;
                }
                result[i] = result[i].plus(signalZ[j].times(signalY[index]));
            }
        }

        return result;
    }

    public static Complex[] corrFFT(Complex[] signalZ, Complex[] signalY) {
        Complex[] result = new Complex[signalZ.length];

        for (int i = 0; i < signalZ.length; i++) {
            Complex temp = signalZ[i].conjugate();
            result[i] = temp.times(signalY[i]);
        }

        return result;
    }
}