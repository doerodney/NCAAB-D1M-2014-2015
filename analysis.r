setwd("c:/github/doerodney/NCAAB-D1M-2014-2015")

df = read.csv("dataframe.csv", header=TRUE)

summary(df)

# margin of victory
df$mov = df$win_points_scored - df$loss_points_scored


