from Building import Building
from Villa import Villa
from Apartment import Apartment
from Asset import Asset

Anthis = Building('Anthis Career Academy', '1200 S Barr St, Fort Wayne, IN 46802', 4, 300, 20)

Anthis.revenue()
Anthis.display()

Avilla = Villa('Avilla', 'Avilla, Indiana 46710', 500, 40)

Avilla.revenue()
Avilla.display()

Lumber = Apartment(300, 20)

Lumber.display()

Asset = Asset('Asset', 'None')

Asset.display()