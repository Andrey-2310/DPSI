pdf("/home/andrey/IdeaProjects/WalshTransform/plots.pdf")

setwd("/home/andrey/IdeaProjects/WalshTransform")

resultOfProcessing <- function(datasetName, title) {
  result <- read.table(datasetName, stringsAsFactors= F)[, 'V1']
  plot(result, main = title)
  segments(1:length(result), 0, 1:length(result), result, col="red")
  abline(h=0, col="black")
}

resultOfProcessing("original.data", "Data")
resultOfProcessing("disc.data", "DWT")
resultOfProcessing("invdisc.data", "IDWT")
resultOfProcessing("fast.data", "FWT")
resultOfProcessing("invfast.data", "IFWT")