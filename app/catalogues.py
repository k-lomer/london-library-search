from app.catalogue_base.sirsi_dynix import SirsiDynix
from app.catalogue_base.spydus import Spydus


class BarkingAndDagenhamCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/barking-and-dagenham", "Barking and Dagenham", "BARKING_DAGENHAM", "Barking and Dagenham", num_results)


class BrentCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/brent", "Brent", "BRENT", "Brent", num_results)


class CamdenCatalogue(Spydus):
    def __init__(self, num_results):
        super().__init__("https://camden.spydus.co.uk", "Camden", num_results)


class CityOfLondonCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://col.ent.sirsidynix.net.uk/client/rss/hitlist/default", "City of London", "LENDING", "", num_results)


class CityOfWestminsterCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://trib.ent.sirsidynix.net.uk/client/rss/hitlist/wcc", "City of Westminster", "WCC", "", num_results)


class CroydonCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/croydon", "Croydon", "CROYDON", "Croydon", num_results)


class EalingCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/ealing", "Ealing", "EALING", "Ealing", num_results)


class EnfieldCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/enfield", "Enfield", "ENFIELD", "Enfield", num_results)


class HackneyCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/hackney", "Hackney", "HACKNEY", "Hackney", num_results)


class HammersmithAndFulhamCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/lbhf", "Hammersmith and Fulham", "HAMMERSMITHFULHAM", "Hammersmith and Fulham", num_results)


class HarrowCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/harrow", "Harrow", "HARROW", "Harrow", num_results)


class HaveringCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/havering", "Havering", "HAVERING", "Havering", num_results)


class HillingdonCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://hldn.ent.sirsidynix.net.uk/client/rss/hitlist/public", "Hillingdon", "PUBLIC", "", num_results)


class HounslowCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/hounslow", "Hounslow", "HOUNSLOW", "Hounslow", num_results)


class KensingtonAndChelseaCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://trib.ent.sirsidynix.net.uk/client/rss/hitlist/rbkc", "Kensington and Chelsea", "RBKC", "", num_results)


class KingstonUponThamesCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/kingston", "Kingston upon Thames", "KINGSTON", "Royal Borough of Kingston", num_results)


class LewishamCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/lewisham", "Lewisham", "LEWISHAM", "Lewisham", num_results)


class MertonCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://libraries.merton.gov.uk/client/rss/hitlist/merton", "Merton", "MERTON", "Merton", num_results)


class NewhamCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/newham", "Newham", "NEWHAM", "Newham", num_results)


class RedbridgeCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/redbridge", "Redbridge", "REDBRIDGE", "Redbridge", num_results)


class RichmondUponThamesCatalogue(Spydus):
    def __init__(self, num_results):
        super().__init__("https://richmond.spydus.co.uk", "Richmond upon Thames", num_results)


class SouthwarkCatalogue(Spydus):
    def __init__(self, num_results):
        super().__init__("https://southwark.spydus.co.uk", "Southwark", num_results)


class SuttonCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/sutton", "Sutton", "SUTTON", "Sutton", num_results)


class TowerHamletsCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/tower-hamlets", "Tower Hamlets", "TOWER_HAMLETS", "Tower Hamlets", num_results)


class WalthamForestCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk/client/rss/hitlist/walthamforest", "Waltham Forest", "WALTHAM_FOREST", "Waltham Forest", num_results)


catalogues = {
    "Barking and Dagenham": BarkingAndDagenhamCatalogue,
    "Brent": BrentCatalogue,
    "Camden": CamdenCatalogue,
    "City of London": CityOfLondonCatalogue,
    "City of Westminster": CityOfWestminsterCatalogue,
    "Croydon": CroydonCatalogue,
    "Ealing": EalingCatalogue,
    "Enfield": EnfieldCatalogue,
    "Hackney": HackneyCatalogue,
    "Hammersmith and Fulham": HammersmithAndFulhamCatalogue,
    "Harrow": HarrowCatalogue,
    "Havering": HaveringCatalogue,
    "Hillingdon": HillingdonCatalogue,
    "Hounslow": HounslowCatalogue,
    "Kensington and Chelsea": KensingtonAndChelseaCatalogue,
    "Kingston upon Thames": KingstonUponThamesCatalogue,
    "Lewisham": LewishamCatalogue,
    "Merton": MertonCatalogue,
    "Newham": NewhamCatalogue,
    "Redbridge": RedbridgeCatalogue,
    "Richmond upon Thames": RichmondUponThamesCatalogue,
    "Southwark": SouthwarkCatalogue,
    "Sutton": SuttonCatalogue,
    "Tower Hamlets": TowerHamletsCatalogue,
    "Waltham Forest": WalthamForestCatalogue
}
