"""
Migration description here!
"""
name = "20210405143815"
dependencies = []


def upgrade(db: "pymongo.database.Database"):
    db["recipe"].insert_one({
        "howto": """1) Separate the eggs. 
            2) Whisk the yolks with the sugar. 
            3) Whisk in the milk, cream, and liquor (if using). 
            4) Cover and refrigerate. 
            5) Whisk the egg whites. 
            6)Fold the egg whites into the eggnog. 
            7) Serve the eggnog.
        """,
        "id": "606b39530a7856db1dacc0cf",
        "ingredients": [
            "6 large eggs",
            "1 cup granulated sugar",
            "2 cups whole milk",
            "1 cup heavy cream",
            "1/2 to 1 1/2 cups bourbon, rum, cognac, or a mix (optional)",
            "Freshly grated nutmeg, for serving"
        ],
        "title": "Eggnog"
    })


def downgrade(db: "pymongo.database.Database"):
    db["recipe"].delete_many({})
