#Figure Out if weights are different

data = read.csv("t-Test.csv")

t.test(data$Weight~data$University, data=data)
