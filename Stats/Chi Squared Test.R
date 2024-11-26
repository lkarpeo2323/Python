############  Test the effect of Gender on Internet use ##################

data = read.csv("Telemedicine_extract.csv")
names(data)


#######  Run The Test ################
chisq.test(data$Gender, data$InternetUse)
#####################################################

###########  TEST SUMMARY #############
#p-value =  0.8996
#we cannot reject null hypothesis: 
#we do not have evidence that internet use is effected by gender
##################################################################


##############  Produce a bar Plot    #################3

a = table(data$Gender, data$InternetUse)
barplot(a,beside=TRUE,legend=TRUE,args.legend=list(x="topright"))

########################################################
