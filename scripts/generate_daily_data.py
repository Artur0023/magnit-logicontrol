from data_platform.generators.sales import generate_sales
from data_platform.generators.stock import generate_stock
from data_platform.generators.shipments import generate_shipments

def main():
    generate_sales()
    generate_stock()
    generate_shipments()
    print("Daily data generated")

if __name__ == "__main__":
    main()
