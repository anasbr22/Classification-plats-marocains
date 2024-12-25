import pandas as pd

# Données des plats
dish_data = {
    "pastilla": {
        "ingredients": "Chicken, almonds, cinnamon, sugar, eggs, pastry sheets.",
        "nutrition": {
            "calories": "300 kcal",
            "protein": "25g",
            "carbs": "20g",
            "fat": "15g",
        },
        "other_info": "A traditional Moroccan dish, typically served for festive occasions.",
    },
    "poulet mhamer": {
        "ingredients": "Chicken, onions, saffron, garlic, olive oil, cumin.",
        "nutrition": {
            "calories": "450 kcal",
            "protein": "30g",
            "carbs": "15g",
            "fat": "25g",
        },
        "other_info": "A flavorful Moroccan dish known for its rich spices and tender chicken.",
    },
    "rfissa": {
        "ingredients": "Chicken, lentils, fenugreek, onions, spices, bread.",
        "nutrition": {
            "calories": "500 kcal",
            "protein": "35g",
            "carbs": "45g",
            "fat": "10g",
        },
        "other_info": "A traditional dish often served during special occasions like celebrations.",
    },
    "taktouka": {
        "ingredients": "Tomatoes, bell peppers, onions, garlic, olive oil, cumin.",
        "nutrition": {
            "calories": "150 kcal",
            "protein": "3g",
            "carbs": "15g",
            "fat": "10g",
        },
        "other_info": "A healthy, vegetarian dish made with roasted vegetables.",
    },
    "couscous btfaya": {
        "ingredients": "Couscous, lamb, chickpeas, carrots, onions, spices.",
        "nutrition": {
            "calories": "600 kcal",
            "protein": "40g",
            "carbs": "50g",
            "fat": "25g",
        },
        "other_info": "A classic Moroccan dish, often served for big family meals.",
    },
    "couscous legumes": {
        "ingredients": "Couscous, zucchini, carrots, pumpkin, onions, chickpeas.",
        "nutrition": {
            "calories": "450 kcal",
            "protein": "12g",
            "carbs": "60g",
            "fat": "15g",
        },
        "other_info": "A vegetarian version of couscous with mixed vegetables.",
    },
    "hrira": {
        "ingredients": "Tomatoes, lentils, chickpeas, beef, spices, coriander.",
        "nutrition": {
            "calories": "350 kcal",
            "protein": "20g",
            "carbs": "40g",
            "fat": "10g",
        },
        "other_info": "A Moroccan soup, typically served during Ramadan to break the fast.",
    },
    "tajine legume": {
        "ingredients": "Vegetables, chickpeas, tomatoes, onions, olive oil, spices.",
        "nutrition": {
            "calories": "200 kcal",
            "protein": "8g",
            "carbs": "30g",
            "fat": "10g",
        },
        "other_info": "A hearty vegetarian stew cooked in a traditional clay pot.",
    },
    "tajine lham barkouk": {
        "ingredients": "Lamb, dried fruit, onions, spices, almonds.",
        "nutrition": {
            "calories": "550 kcal",
            "protein": "35g",
            "carbs": "30g",
            "fat": "25g",
        },
        "other_info": "A delicious and rich dish with tender lamb and sweet fruit.",
    }
}

# Transformation des données en un format approprié pour Excel
records = []
for dish, data in dish_data.items():
    record = {
        "Dish": dish,
        "Ingredients": data["ingredients"],
        "Calories": data["nutrition"]["calories"],
        "Protein": data["nutrition"]["protein"],
        "Carbs": data["nutrition"]["carbs"],
        "Fat": data["nutrition"]["fat"],
        "Other Info": data["other_info"]
    }
    records.append(record)

# Création d'un DataFrame pandas
df = pd.DataFrame(records)

# Sauvegarde du DataFrame dans un fichier Excel
df.to_excel("dish_data.xlsx", index=False, engine='openpyxl')

print("Fichier Excel généré : dish_data.xlsx")
