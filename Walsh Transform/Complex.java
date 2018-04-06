public class Complex {

    private final double re;
    private final double im;


    Complex(double real, double imag) {
        re = real;
        im = imag;
    }


    public String toString() {
        if (im == 0) {
            return "(" + re + "+0j)";
        }
        if (re == 0) {
            return "(" + im + "j)";
        }
        if (im < 0) {
            return "(" + re + "-" + (-im) + "j)";
        }
        return "(" + re + " + " + im + "j)";
    }


    public double abs() {
        return Math.hypot(re, im);
    }


    public double phase() {
        return Math.atan2(im, re);
    }


    public Complex plus(Complex b) {
        Complex a = this;
        double real = a.re + b.re;
        double imag = a.im + b.im;
        return new Complex(real, imag);
    }


    public Complex minus(Complex b) {
        Complex a = this;
        double real = a.re - b.re;
        double imag = a.im - b.im;
        return new Complex(real, imag);
    }


    private Complex times(Complex b) {
        Complex a = this;
        double real = a.re * b.re - a.im * b.im;
        double imag = a.re * b.im + a.im * b.re;
        return new Complex(real, imag);
    }

    public Complex times(double d) {

        return new Complex(this.re * d, this.im * d);

    }


    public Complex scale(double alpha) {
        return new Complex(alpha * re, alpha * im);
    }


    public Complex conjugate() {
        return new Complex(re, -im);
    }


    private Complex reciprocal() {
        double scale = re * re + im * im;
        return new Complex(re / scale, -im / scale);
    }


    public double re() {
        return re;
    }

    public double im() {
        return im;
    }


    public Complex divides(Complex b) {
        Complex a = this;
        return a.times(b.reciprocal());
    }

    public Complex divides(int N) {

        Complex a = this;
        return new Complex(a.re / N, a.im / N);

    }

    public static Complex plus(Complex a, Complex b) {
        double real = a.re + b.re;
        double imag = a.im + b.im;
        return new Complex(real, imag);
    }
}