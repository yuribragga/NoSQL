from utils.utils import get_purchase, get_user

def delete_purchase(db, purchase_id):
    try:
        purchase = get_purchase(db, purchase_id)
        if purchase is None:
            print("Compra não encontrada")
            return
            
        user = get_user(db, purchase.get('user_id'))
        if user is None:
            print("Comprador não encontrado")
            return

        # Remove purchase from user's purchases list
        user_compras = user.get('compras', [])
        user_compras = [compra for compra in user_compras if compra.get("id") != purchase_id]

        # Update user document
        user_collection = db.get_collection("user")
        user_collection.update_one(
            {"_id": user.get('_id')},
            {"$set": {"compras": user_compras}}
        )

        # Delete purchase document
        purchases_collection = db.get_collection("purchase")
        purchases_collection.delete_one({"_id": purchase_id})

        print(f"Compra com ID {purchase_id} deletada com sucesso!")
        return

    except Exception as e:
        print(f"Erro ao deletar a compra: {e}")

