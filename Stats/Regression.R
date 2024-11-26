data(mtcars)
mtcars$am.f <- factor(mtcars$am,labels=c("Auto","Manual"))
mtcars$vs.f <- factor(mtcars$vs,labels=c("V-Shape","Straight"))
mtcars$cyl.f <- factor(mtcars$cyl,labels=c("4 Cylinders","6 Cylinders","8 Cylinders"))
mtcars$gear.f <- factor(mtcars$gear,labels=c("3 Gears","4 Gears","5 Gears"))


summary(lm(mpg~wt,data=mtcars))
