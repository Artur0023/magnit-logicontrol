from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey
)

from data_platform.db.engine import Base


class DistributionCenter(Base):
    __tablename__ = "distribution_centers"

    dc_id = Column(String, primary_key=True)
    region = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)
    base_sla = Column(Integer, nullable=False)


class SKU(Base):
    __tablename__ = "sku"

    sku_id = Column(String, primary_key=True)
    category = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    shelf_life = Column(Integer, nullable=False)


class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    sku_id = Column(String, ForeignKey("sku.sku_id"), nullable=False)
    dc_id = Column(String, ForeignKey("distribution_centers.dc_id"), nullable=False)
    units_sold = Column(Integer, nullable=False)


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    sku_id = Column(String, ForeignKey("sku.sku_id"), nullable=False)
    dc_id = Column(String, ForeignKey("distribution_centers.dc_id"), nullable=False)
    stock_qty = Column(Integer, nullable=False)


class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    sku_id = Column(String, ForeignKey("sku.sku_id"), nullable=False)
    supplier_id = Column(String, ForeignKey("suppliers.supplier_id"), nullable=False)
    dc_id = Column(String, ForeignKey("distribution_centers.dc_id"), nullable=False)
    qty = Column(Integer, nullable=False)
    delay_days = Column(Integer, nullable=False)
