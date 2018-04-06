import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

import static java.lang.Math.cos;
import static java.lang.Math.sin;
import static java.lang.Math.PI;
import static java.lang.Math.round;

public class Main {

    private static int N = 8;

    public static void main(String[] args) {
        // TODO Auto-generated method stub

        Complex[] x = getData();
        Transform transform = new Transform(x);

        System.out.println("-----------Original data-----------");
        print(x);
        saveToFile("original.data", x);

        Complex[] result;
        System.out.println("-----------Discrete transform-----------");
        result = transform.discreteTransform();
        print(result);
        saveToFile("disc.data", result);

        System.out.println("-----------Inverse Discrete transform-----------");
        result = transform.inverseDiscreteTransform(result);
        print(result);
        saveToFile("invdisc.data", result);

        System.out.println("-----------Fast transform-----------");
        result = transform.fastTransform(x, N);

        for (int i = 0; i < result.length; i++) {
            result[i] = result[i].divides(N);
        }
        print(result);
        saveToFile("fast.data", result);

        System.out.println("-----------Inverse Fast transform-----------");
        result = transform.inverseFastTransform(result, N);
        print(result);
        saveToFile("invfast.data", result);
    }

    private static Complex[] getData() {
        Complex[] output = new Complex[N];
        for (double i = PI, j = 0; j < N; j++, i += PI / 4) {
            double a = sin(round(i)) + cos(round(i));
            output[(int) j] = new Complex(a, 0);
        }
        return output;
    }

    private static void print(Complex[] x) {
        for (Complex aX : x) {
            System.out.println(aX.toString());
        }
    }

    private static void saveToFile(String fileName, Complex[] data) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            for (Complex item : data) {
                writer.write(String.valueOf(item.re()) + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}