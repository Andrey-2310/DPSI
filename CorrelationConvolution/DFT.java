import static java.lang.Math.PI;
import static java.lang.Math.cos;
import static java.lang.Math.sin;

public class DFT extends FT{

    public Complex[] dft(Complex[] x) {
        int N = x.length;
        Complex[] result = new Complex[N];
        for (int i = 0; i < N; i++) {
            result[i] = new Complex(0, 0);
        }
        for (int k = 0; k < N; k++) {
            for (int n = 0; n < N; n++) {
                Complex Wn = new Complex(cos(-2 * PI * k * n / N), sin(-2 * PI * k * n / N));
                result[k] = result[k].plus(x[n].times(Wn));
                mulCount++;
                sumCount++;
            }
        }
        System.out.println("");
        return result;
    }

    public static Complex[] idft(Complex[] x) {
        int N = x.length;
        Complex[] result = new Complex[N];
        for (int i = 0; i < N; i++) {
            result[i] = new Complex(0, 0);
        }
        for (int k = 0; k < N; k++) {
            for (int n = 0; n < N; n++) {
                Complex Wn = new Complex(cos(2 * PI * k * n / N), sin(2 * PI * k * n / N));
                result[k] = result[k].plus(x[n].times(Wn));
            }
            result[k] = result[k].divides(N);
        }
        return result;
    }
}