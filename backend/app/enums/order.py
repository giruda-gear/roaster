import enum


class OrderStatus(enum.StrEnum):
    PLACED = "placed"
    PREPARING = "preparing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
