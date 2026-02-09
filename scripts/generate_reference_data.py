from data_platform.seed import SEED  # noqa
from data_platform.generators.dc import generate_distribution_centers
from data_platform.generators.sku import generate_sku
from data_platform.generators.suppliers import generate_suppliers


def main():
    generate_distribution_centers()
    generate_sku()
    generate_suppliers()
    print('Reference data generated')


if __name__ == '__main__':
    main()