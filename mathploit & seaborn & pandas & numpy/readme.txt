datasets : 1 melb_data.csv

rapport le travail des Machines Learning sur le dataset
Etape 1 : Définition du problème
ici le problème est de prédire le prix des logements de Melbourse.
Etape 2 : Collecte des données.
    Le datasets est déjà dispinible.
Etape 3 : EDA
Lorsqu'on essaie de voir le dataframe : [13580 rows x 21 columns]
    Liste des colonnes:
        Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG',
               'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
               'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude',
               'Longtitude', 'Regionname', 'Propertycount'],
              dtype='object')
Structure des colonnes (type) :
                                Suburb type object
                                Address type object
                                Rooms type int64
                                Type type object
                                Price type float64
                                Method type object
                                SellerG type object
                                Date type object
                                Distance type float64
                                Postcode type float64
                                Bedroom2 type float64
                                Bathroom type float64
                                Car type float64
                                Landsize type float64
                                BuildingArea type float64
                                YearBuilt type float64
                                CouncilArea type object
                                Lattitude type float64
                                Longtitude type float64
                                Regionname type object
                                Propertycount type float64
