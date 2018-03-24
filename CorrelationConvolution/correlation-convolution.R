pdf("/home/andrey/IdeaProjects/CorrelationConvolution/plots.pdf")

setwd("/home/andrey/IdeaProjects/CorrelationConvolution")

resultOfProcessing <- function(datasetName) {
  result <- read.table(datasetName, stringsAsFactors= F)[, 'V1']
  plot(result)
  segments(1:length(result), 0, 1:length(result), result, col="red")
  abline(h=0, col="black")
}

execPoints <-seq(from=0, to=7*pi/6, by=pi/6)

getStartPlot <- function(kek, title){
  plot(kek(execPoints), ylab = "y", main = title)
  abline(h=0, col="black")
}

getStartPlot(sin, "y = sin(x)")
getStartPlot(cos, "y = cos(x)")

resultOfProcessing("corr.data")
resultOfProcessing("corrfft.data")
resultOfProcessing("conv.data")
resultOfProcessing("convfft.data")