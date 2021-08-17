# Laboratorio de Pruebas - Semana 1-2
# Tema: Centro Comercial Unaleño
# Autor: Pablo Jose Torres Mojica

def get_product_details():
    product_name = input()
    unit_cost = abs(int(input()))
    retail_price = abs(int(input()))  # precio de venta al público
    stock = abs(int(input()))

    return {'Product Name': product_name,
            'Unit Cost': unit_cost,
            'Retail Price': retail_price,
            'Stock': stock}


def get_profit(product):
    return product['Stock'] * (product['Retail Price'] - product['Unit Cost'])


def print_details(product):
    print(f"""Producto: {product['Product Name']}
    \rCU: ${product['Unit Cost']}
    \rPVP: ${product['Retail Price']}
    \rUnidades Disponibles: {product['Stock']}
    \rGanancia: ${product['Profit']}""")


def main():
    product = get_product_details()
    product['Profit'] = get_profit(product)
    print_details(product)


if __name__ == '__main__':
    main()
