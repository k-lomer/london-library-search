from app.catalogue_base.arena import Arena
from app.catalogue_base.prism import Prism
from app.catalogue_base.sirsi_dynix import SirsiDynix
from app.catalogue_base.spydus import Spydus


class BarkingAndDagenhamCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/barking-and-dagenham", "Barking and Dagenham", "BARKING_DAGENHAM", "(Barking and Dagenham)")


class BarnetCatalogue(Prism):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://prism.librarymanagementcloud.co.uk/barnet/", "Barnet")


class BexleyCatalogue(Arena):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://arena.yourlondonlibrary.net/web/bexley", "Bexley", "AUK200102\|18", "BEX")


class BrentCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/brent", "Brent", "BRENT", "(Brent)")


class BromleyCatalogue(Prism):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://prism.librarymanagementcloud.co.uk/bromley/", "Bromley")


class CamdenCatalogue(Spydus):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://camden.spydus.co.uk", "Camden")


class CityOfLondonCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://col.ent.sirsidynix.net.uk/client/rss/hitlist/default", "City of London", "LENDING", "")


class CityOfWestminsterCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://trib.ent.sirsidynix.net.uk/client/rss/hitlist/wcc", "City of Westminster", "WCC", "")


class CroydonCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/croydon", "Croydon", "CROYDON", "(Croydon)", True, False)


class EalingCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/ealing", "Ealing", "EALING", "(Ealing)")


class EnfieldCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/enfield", "Enfield", "ENFIELD", "(Enfield)")


class GreenwichCatalogue(Prism):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://prism.librarymanagementcloud.co.uk/royalgreenwich/", "Greenwich")


class HackneyCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/hackney", "Hackney", "HACKNEY", "(Hackney)")


class HammersmithAndFulhamCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/lbhf", "Hammersmith and Fulham", "HAMMERSMITHFULHAM", "(Hammersmith and Fulham)")


class HaringeyCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/haringey", "Haringey", "LIBRARY	Library	1:HARYY	Hornsey Library (Haringey) || 1:HARTT	Marcus Garvey Library (Haringey) || 1:HARCC	Wood Green Library (Haringey) || 1:HARMM	Muswell Hill Library (Haringey) || 1:HARAA	Alexandra Park Library (Haringey) || 1:HARNN	St. Anns Library (Haringey) || 1:HARSS	Stroud Green Library (Haringey) || 1:HARFF	1:HARFF || 1:HARHLP	Learning Partnership (Haringey) || 1:HARHH	Highgate Library (Haringey) || 1:HARHLS	Home Library Service (Haringey)", "(Haringey)", False)


class HarrowCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/harrow", "Harrow", "HARROW", "(Harrow)")


class HaveringCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/havering", "Havering", "HAVERING", "(Havering)")


class HillingdonCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://hldn.ent.sirsidynix.net.uk/client/rss/hitlist/public", "Hillingdon", "PUBLIC", "")


class HounslowCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/hounslow", "Hounslow", "HOUNSLOW", "Hounslow")


class IslingtonCatalogue(Prism):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://prism.librarymanagementcloud.co.uk/islington/", "Islington")


class KensingtonAndChelseaCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://trib.ent.sirsidynix.net.uk/client/rss/hitlist/rbkc", "Kensington and Chelsea", "RBKC", "")


class KingstonUponThamesCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/kingston", "Kingston upon Thames", "KINGSTON", "(Royal Borough of Kingston)")


class LambethCatalogue(Arena):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://libraries.lambeth.gov.uk", "Lambeth", "AUK000271\|1")


class LewishamCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/lewisham", "Lewisham", "LEWISHAM", "(Lewisham)")


class MertonCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://libraries.merton.gov.uk/client/rss/hitlist/merton", "Merton", "MERTON", "(Merton)")


class NewhamCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/newham", "Newham", "NEWHAM", "(Newham)")


class RedbridgeCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/redbridge", "Redbridge", "REDBRIDGE", "(Redbridge)", True, False)


class RichmondUponThamesCatalogue(Spydus):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://richmond.spydus.co.uk", "Richmond upon Thames")


class SouthwarkCatalogue(Spydus):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://southwark.spydus.co.uk", "Southwark")


class SuttonCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/sutton", "Sutton", "SUTTON", "(Sutton)", True, False)


class TowerHamletsCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/tower-hamlets", "Tower Hamlets", "TOWER_HAMLETS", "(Tower Hamlets)")


class WandsworthCatalogue(Prism):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://prism.librarymanagementcloud.co.uk/wandsworth/", "Wandsworth")


class WalthamForestCatalogue(SirsiDynix):
    def __init__(self, query, num_results):
        super().__init__(query, num_results, "https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/walthamforest", "Waltham Forest", "WALTHAM_FOREST", "(Waltham Forest)")


catalogues = {
    "Barking and Dagenham": BarkingAndDagenhamCatalogue,
    "Barnet": BarnetCatalogue,
    "Bexley": BexleyCatalogue,
    "Brent": BrentCatalogue,
    "Bromley": BromleyCatalogue,
    "Camden": CamdenCatalogue,
    "City of London": CityOfLondonCatalogue,
    "City of Westminster": CityOfWestminsterCatalogue,
    "Croydon": CroydonCatalogue,
    "Ealing": EalingCatalogue,
    "Enfield": EnfieldCatalogue,
    "Greenwich": GreenwichCatalogue,
    "Hackney": HackneyCatalogue,
    "Hammersmith and Fulham": HammersmithAndFulhamCatalogue,
    "Haringey": HaringeyCatalogue,
    "Harrow": HarrowCatalogue,
    "Havering": HaveringCatalogue,
    "Hillingdon": HillingdonCatalogue,
    "Hounslow": HounslowCatalogue,
    "Islington": IslingtonCatalogue,
    "Kensington and Chelsea": KensingtonAndChelseaCatalogue,
    "Kingston upon Thames": KingstonUponThamesCatalogue,
    "Lambeth": LambethCatalogue,
    "Lewisham": LewishamCatalogue,
    "Merton": MertonCatalogue,
    "Newham": NewhamCatalogue,
    "Redbridge": RedbridgeCatalogue,
    "Richmond upon Thames": RichmondUponThamesCatalogue,
    "Southwark": SouthwarkCatalogue,
    "Sutton": SuttonCatalogue,
    "Tower Hamlets": TowerHamletsCatalogue,
    "Waltham Forest": WalthamForestCatalogue,
    "Wandsworth": WandsworthCatalogue
}
