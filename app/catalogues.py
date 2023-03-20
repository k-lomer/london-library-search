from app.catalogue_base.sirsi_dynix import LlcSirsiDynix, SirsiDynix
from app.catalogue_base.spydus import Spydus


class BarkingAndDagenhamCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Barking and Dagenham", "barking-and-dagenham", "BARKING_DAGENHAM", num_results)


class BrentCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Brent", "brent", "BRENT", num_results)


class CamdenCatalogue(Spydus):
    def __init__(self, num_results):
        super().__init__("https://camden.spydus.co.uk", "Camden", num_results)


class CityOfLondonCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://col.ent.sirsidynix.net.uk", "default", "City of London", num_results)


class CityOfWestminsterCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://trib.ent.sirsidynix.net.uk", "wcc", "City of Westminster", num_results, {"lm": "WCC"})


class CroydonCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Croydon", "croydon", "CROYDON", num_results)


class EalingCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Ealing", "ealing", "EALING", num_results)


class EnfieldCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Enfield", "enfield", "ENFIELD", num_results)


class HackneyCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Hackney", "hackney", "HACKNEY", num_results)


class HammersmithAndFulhamCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Hammersmith and Fulham", "lbhf", "HAMMERSMITHFULHAM", num_results)


class HarrowCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Harrow", "harrow", "HARROW", num_results)


class HaveringCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Havering", "havering", "HAVERING", num_results)


class HillingdonCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://hldn.ent.sirsidynix.net.uk", "public", "Hillingdon", num_results, {"lm": "PUBLIC"})


class HounslowCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Hounslow", "hounslow", "HOUNSLOW", num_results)


class KensingtonAndChelseaCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://trib.ent.sirsidynix.net.uk", "rbkc", "Kensington and Chelsea", num_results, {"lm": "RBKC"})


class KingstonUponThamesCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Kingston upon Thames", "kingston", "KINGSTON", num_results)


class LewishamCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Lewisham", "lewisham", "LEWISHAM", num_results)

class MertonCatalogue(SirsiDynix):
    def __init__(self, num_results):
        super().__init__("https://libraries.merton.gov.uk", "merton", "Merton", num_results, {"lm": "MERTON"})


class NewhamCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Newham", "newham", "NEWHAM", num_results)


class RedbridgeCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Redbridge", "redbridge", "REDBRIDGE", num_results)


class RichmondUponThamesCatalogue(Spydus):
    def __init__(self, num_results):
        super().__init__("https://richmond.spydus.co.uk", "Richmond upon Thames", num_results)


class SouthwarkCatalogue(Spydus):
    def __init__(self, num_results):
        super().__init__("https://southwark.spydus.co.uk", "Southwark", num_results)


class SuttonCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Sutton", "sutton", "SUTTON", num_results)


class TowerHamletsCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Tower Hamlets", "tower-hamlets", "TOWER_HAMLETS", num_results)


class WalthamForestCatalogue(LlcSirsiDynix):
    def __init__(self, num_results):
        super().__init__("Waltham Forest", "walthamforest", "WALTHAM_FOREST", num_results)


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
