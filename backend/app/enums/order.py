import enum


class OrderStatus(enum.Enum):
    ORDER_PLACED = "ORDER_PLACED"
    PREPARING = "PREPARING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
