# Install pacman only if it's missing, then load packages
if (!requireNamespace("pacman", quietly = TRUE)) install.packages("pacman")
pacman::p_load(tidyverse, readxl)

# Read the Orders tab
orders <- read_excel("GlobalSuperstore.xls", sheet = "Orders")
View(orders)

# US furniture orders only
us_furniture <- orders |>
  filter(Country == "United States", Category == "Furniture")

# Six most frequently occurring states, with total revenue for each
state_revenue <- us_furniture |>
  group_by(State) |>
  summarize(n = n(), Revenue = sum(Sales)) |>
  slice_max(n, n = 6, with_ties = FALSE)

# One row per customer per state: average profit across that customer's orders
customer_profit <- us_furniture |>
  group_by(State, `Customer ID`) |>
  summarize(Profit = mean(Profit), .groups = "drop") |>
  inner_join(state_revenue, by = "State") |>
  mutate(State = fct_reorder(State, Revenue, .desc = TRUE))

# Boxplots overlaid with jitter plots, colored and sorted by state revenue
ggplot(customer_profit, aes(x = State, y = Profit, color = Revenue)) +
  geom_boxplot(outlier.shape = NA) +
  geom_jitter(width = 0.2, alpha = 0.1) +
  scale_color_distiller(palette = "Blues", direction = 1,
                        labels = scales::label_dollar()) +
  labs(
    title = "Average furniture profit per customer, top six US states",
    x = "State (sorted by descending furniture revenue)",
    y = "Average profit per customer",
    color = "State revenue"
  ) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
