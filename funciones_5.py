# Pasar un numero arbitrario de argumentos

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nCreando una pizza con los siguientes ingredientes:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza(
    'mushrooms',
    'green peppers',
    'extra cheese')