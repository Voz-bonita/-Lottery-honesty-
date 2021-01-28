# install.packages("readxl")
library(readxl)
file <- "Lotofac_hist.xlsx"
data <- read_xlsx(file, sheet = "Plan1")
data.tab <- as.table(data$Obs_value, data$Exp_value)

chisq_obs <- chisq.test(data.tab)$statistic
p.value <- chisq.test(data.tab)$p.value

chisq_critical <- qchisq(0.95, 24)

if (chisq_obs[[1]] > chisq_critical) {
  print("Denie null hypothesis")
} else {
  print("Accept null hypothesis")
}
