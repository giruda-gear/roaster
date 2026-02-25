### 📝 Order & Roasting Process
[ ] User Auth
[ ] Create Order: Insert data into the orders table with PENDING status.

[ ] Deduct Inventory: Deduct green bean inventory from bean_inventories.

[ ] Aggregate Demand: Check if the sum of specific beans in PENDING status within the orders table exceeds the threshold (e.g., 10kg).

[ ] Roasting Instruction: If the threshold is exceeded, bulk update the status of those orders to IN_ROASTING. (Ready for Kafka event transmission to the roasting department).
