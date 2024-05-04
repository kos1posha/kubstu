tables = {
    'categories': [
        '"title" TEXT NOT NULL UNIQUE',
        '"description" TEXT NOT NULL',
    ],
    'products': [
        '"code" TEXT NOT NULL UNIQUE',
        '"title" TEXT NOT NULL',
        '"category_id" INTEGER NOT NULL REFERENCES "Categories"',
        '"on_storage_count" INTEGER NOT NULL',
        '"weight" INTEGER NOT NULL',
        '"price" INTEGER NOT NULL',
        '"description" TEXT NOT NULL',
        '"has_complectation" INTEGER NOT NULL',
    ],
    'income_history': [
        '"datetime" TEXT NOT NULL',
        '"product_code" TEXT NOT NULL',
        '"product_title" TEXT NOT NULL',
        '"product_category" TEXT NOT NULL',
        '"product_price" TEXT NOT NULL',
        '"count" INTEGER NOT NULL',
    ],
    'outcome_history': [
        '"datetime" TEXT NOT NULL',
        '"product_code" TEXT NOT NULL',
        '"product_title" TEXT NOT NULL',
        '"product_category" TEXT NOT NULL',
        '"product_price" TEXT NOT NULL',
        '"count" INTEGER NOT NULL',
    ]
}
