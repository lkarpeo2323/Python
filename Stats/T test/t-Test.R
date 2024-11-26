#Figure Out if weights are different

college = read.csv("t-Test.csv")

t.test(college$Weight~college$University, data=college)
