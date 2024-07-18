def calculate_balances(transactions, users):
    balances = {user["_id"]: 0 for user in users}

    for transaction in transactions:
        payor = transaction["payor"]
        amount = transaction["amount"]
        # Assuming equally divided among users except the payor
        split_amount = amount / (len(users) - 1)

        for user in users:
            if user["_id"] != payor:
                balances[payor] += split_amount
                balances[user["_id"]] -= split_amount

    formatted_balances = []
    for user in users:
        formatted_balances.append(
            {"user": user["name"], "balance": balances[user["_id"]]}
        )

    return formatted_balances
