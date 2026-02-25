from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def products_cost(self, customer_products: dict) -> float:
        cost = 0.0
        for product, quantity in customer_products.items():
            cost += quantity * self.products[product]
        return cost

    def products_cost_with_command(self, customer_products: dict) -> float:
        cost = 0.0
        total_cost = 0.0
        for product, quantity in customer_products.items():
            cost = quantity * self.products[product]
            total_cost += cost
            if cost.is_integer():
                cost = int(cost)
            print(f"{quantity} {product}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        return total_cost
