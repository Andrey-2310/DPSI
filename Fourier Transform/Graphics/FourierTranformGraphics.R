pdf("/home/andrey/Documents/R/Fourier/plots.pdf")

x=seq(-10,10,0.1)
y <- sin(x) + cos(x)
plot(x, y, type = "l", main="y=sin(x)+cos(x)")
abline(h=0, col="black")


fourierData <- read.table("/home/andrey/Documents/R/Fourier/DFT.data", sep = ",", stringsAsFactors= F)

afcData <- sqrt(fourierData[,'V1']^2 + fourierData[,'V2']^2)
plot(afcData, xlab = "frequency", ylab = "amplitude", main = "FT: afc")
segments(1:length(afcData), 0, 1:length(afcData), afcData, col="red")

pfcData <- atan(fourierData[,'V2']/fourierData[,'V1'])
plot(ffcData,  xlab = "frequency", ylab = "phase", main = "FT: pfc")
segments(1:length(pfcData), 0, 1:length(pfcData), pfcData, col="red")
abline(h=0, col="black")

inverseFourierData <- read.table("/home/andrey/Documents/R/Fourier/IDFT.data", sep = ",", stringsAsFactors= F)
plot(inverseFourierData[,'V1'], main = "IFT")
abline(h=0, col="black")



fastFourierData <- read.table("/home/andrey/Documents/R/Fourier/DFFT.data", sep = ",", stringsAsFactors= F)

afcFData <- sqrt(fastFourierData[,'V1']^2 + fastFourierData[,'V2']^2)
plot(afcFData,  xlab = "frequency", ylab = "amplitude", main = "FFT: afc")
segments(1:length(afcFData), 0, 1:length(afcFData), afcFData, col="red")

pfcFData <- atan(fastFourierData[,'V2']/fastFourierData[,'V1'])
plot(pfcFData, xlab = "frequency", ylab = "phase", main = "FFT: pfc")
segments(1:length(pfcFData), 0, 1:length(pfcFData), pfcFData, col="red")
abline(h=0, col="black")

inverseFastFourierData <- read.table("/home/andrey/Documents/R/Fourier/IFDFT.data", sep = ",", stringsAsFactors= F)
plot(inverseFastFourierData[,'V1'], main = "IFFT")
abline(h=0, col="black")

dev.off()

