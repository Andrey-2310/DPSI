import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

import static java.lang.Math.PI;
import static java.lang.Math.cos;
import static java.lang.Math.sin;

public class Main {

    private static int N = 8;

    public static void main(String[] args) {
        FFT fastFourierTransform = new FFT();

        Complex[] inputZ = getDataZ();
        Complex[] inputY = getDataY();

        System.out.println("-------Origin data Z----------");
        show(inputZ);
        System.out.println("-------Origin data Y----------");
        show(inputY);

        Complex[] reverseFftForX = fastFourierTransform.fft(inputZ, N, 1);
        Complex[] reverseFftForY = fastFourierTransform.fft(inputY, N, 1);

        Complex[] fftForZ = new Complex[N];
        Complex[] fftForY = new Complex[N];

        for (int i = 0; i < fftForZ.length; i++) {
            fftForZ[FFT.indexReverse(i)] = reverseFftForX[i];
            fftForY[FFT.indexReverse(i)] = reverseFftForY[i];
        }

        System.out.println("----------FFT for Z------------");
        show(fftForZ);
        System.out.println("----------FFT for Y------------");
        show(fftForY);

        Complex[] fftConvResult = Convolution.convFFT(fftForZ, fftForY);
        Complex[] fftCorrResult = Correlation.corrFFT(fftForZ, fftForY);

        System.out.println("-------CONV_FFT multiply result----------");
        show(fftConvResult);
        System.out.println("-------CORR_FFT multiply result----------");
        show(fftCorrResult);

        Complex[] reverseIFFTConvResult = fastFourierTransform.fft(fftConvResult, fftConvResult.length, -1);
        Complex[] reverseIFFTCorrResult = fastFourierTransform.fft(fftCorrResult, fftCorrResult.length, -1);

        Complex[] endConvResult = new Complex[reverseIFFTConvResult.length];
        Complex[] endCorrResult = new Complex[reverseIFFTCorrResult.length];

        for (int i = 0; i < reverseIFFTConvResult.length; i++) {
            endConvResult[FFT.indexReverse(i)] = reverseIFFTConvResult[i].divides(N);
            endCorrResult[FFT.indexReverse(i)] = reverseIFFTCorrResult[i].divides(N);
        }

        Complex[] matrixConv = Convolution.conv(inputZ, inputY);
        Complex[] matrixCorr = Correlation.corr(inputZ, inputY);

        System.out.println("----------END Conv result----------");
        show(endConvResult);
        System.out.println("----------END Conv matrix result----------");
        show(matrixConv);
        System.out.println("----------END Corr result----------");
        show(endCorrResult);
        System.out.println("----------END Corr matrix result----------");
        show(matrixCorr);

        saveToFile("conv.data", matrixConv);
        saveToFile("convfft.data", endConvResult);
        saveToFile("corr.data", matrixCorr);
        saveToFile("corrfft.data", endCorrResult);


    }

    private static void show(Complex[] x) {
        for (Complex aX : x) {
            System.out.println(aX.toString());
        }
    }

    public static Complex[] getData() {
        Complex[] output = new Complex[N];
        for (double i = PI, j = 0; j < N; j++, i += PI / 4) {
            output[(int) j] = new Complex(sin(i) + cos(4 * i), 0);
        }
        return output;
    }

    private static Complex[] getDataZ() {
        Complex[] output = new Complex[N];
        for (int i = 0; i < output.length; i++) {
            output[i] = new Complex(sin(PI / 6 * i), 0);
        }
        return output;
    }

    private static Complex[] getDataY() {
        Complex[] output = new Complex[N];
        for (int i = 0; i < output.length; i++) {
            output[i] = new Complex(cos(PI / 6 * i), 0);
        }
        return output;
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
