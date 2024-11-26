data(mtcars)

var = names(mtcars)
var

#Send to PDF


pdf("ScatterPlots.pdf")
par(mfrow = c(3,2))

for (i in 3:7){
  plot(mtcars[[1]]~mtcars[[i]], 
       main = paste("Scatter Plot of MPG v.s.", var[3]))
  
}

dev.off()
