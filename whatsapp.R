all_data = read.csv("all_messages_sum.csv", header=TRUE)
do <- all_data
library(ggplot2)

do$Date <- as.Date(do$Date,"%d/%m/%Y")

sum_graph <- ggplot(do, aes(Date, Messages)) +
  geom_line()
sum_graph + scale_x_date(date_breaks = "1 month", date_labels = "%b%y") + ggtitle("Number of Whatsapp Messages Sent Between Us")

