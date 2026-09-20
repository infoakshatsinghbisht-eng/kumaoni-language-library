"""
Kumaoni traditional festivals and cultural celebrations.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class Festival:
    name_kumaoni: str
    name_roman: str
    month: str
    description: str
    rituals: List[str]
    traditional_song_or_couplet: str


FESTIVALS_DATA: Dict[str, Festival] = {
    "harela": Festival(
        name_kumaoni="हरेला",
        name_roman="Harela",
        month="साउन (July)",
        description="A major Himalayan agricultural festival marking the onset of the monsoon and the new crop season, dedicated to Lord Shiva and Goddess Parvati.",
        rituals=[
            "Sowing seeds of 5 to 9 different grains (wheat, barley, maize, mustard, etc.) in small bamboo or clay pots 9-10 days before the festival.",
            "Harvesting the vibrant green yellow shoots on the day of Harela.",
            "Elders blessing family members by placing green Harela stalks behind their ears with the auspicious blessing: 'जी रया, जागि रया, तीष्ट रया...'"
        ],
        traditional_song_or_couplet="जी रया, जागि रया, तीष्ट रया, पनपि रया। हिमाल म ह्युं छन तक, गंगा म पाणि छन तक।"
    ),
    "phool_dei": Festival(
        name_kumaoni="फूलदेई",
        name_roman="Phool Dei",
        month="चैत (March)",
        description="The spring festival of flowers celebrating nature's blossom and the first day of the Hindu solar new year in the hills.",
        rituals=[
            "Young children (Phoolari) gather wild Himalayan spring flowers such as Pyoli (Reinwardtia), Buransh (Rhododendron), and mustard.",
            "Children go house-to-house placing flowers on every doorstep, singing traditional greetings.",
            "Householders bless the children and reward them with sweets, rice, jaggery (gur), and coins."
        ],
        traditional_song_or_couplet="फूल देई, छम्मा देई, दैणी द्वार, भर भकार। यो देली स बारम्बार नमस्कार!"
    ),
    "ghughutiya": Festival(
        name_kumaoni="घुघुतिया / उत्तरायणी",
        name_roman="Ghughutiya / Uttarayani",
        month="माघ (January - Makar Sankranti)",
        description="Celebrated when the sun enters Capricorn (Uttarayana). Deeply tied to folk legends of King Kalyan Chand and crows.",
        rituals=[
            "Deep-frying twisted, sweet dough cookies made of wheat flour and jaggery shaped like spotted doves (ghughute), knives, drums, and flowers.",
            "Threading the sweets into wearable necklaces (ghughut mala) with an orange in the center.",
            "Early morning calling of crows to eat the sweets from children's hands with playful folk chants."
        ],
        traditional_song_or_couplet="काले कौवा काले, घुघुति माला खाले! ले कौवा भात, मकै दे सुनक थात।"
    ),
    "olgia": Festival(
        name_kumaoni="ओलगिया / घी संक्रांति",
        name_roman="Olgia / Ghee Sankranti",
        month="भादौ (August)",
        description="Ancient thanksgiving festival celebrating the peak of crop growth and dairy abundance in the monsoon.",
        rituals=[
            "Artisans, farmers, and family members present traditional gifts (Olga) of fresh harvest, cucumbers, and walnuts to landowners and elders.",
            "Consuming large amounts of freshly churned homemade cow/buffalo ghee, curd, and stuffed urad-dal bedu roti."
        ],
        traditional_song_or_couplet="घी संक्रातिक दिन घी जरूर खाण चाइन।"
    ),
    "nanda_devi": Festival(
        name_kumaoni="नंदा देवी मेला",
        name_roman="Nanda Devi Mela",
        month="भादौ / आसोज (September)",
        description="Historic cultural fair held in Almora, Nainital, Ranikhet, and Bageshwar honoring Goddess Nanda, the divine patron goddess of the Chand kings and Kumaon.",
        rituals=[
            "Creating sacred idols of Goddess Nanda and Sunanda using plantain (banana) tree trunks.",
            "Grand traditional procession, Chholiya dance performances, and immersion rituals."
        ],
        traditional_song_or_couplet="जय माँ नंदा, जय माँ सुनंदा, सुख-समृद्धि दै।"
    ),
}


def get_festival(name: str) -> Optional[Festival]:
    """Retrieve festival information by key (e.g., 'harela', 'phool_dei')."""
    return FESTIVALS_DATA.get(name.lower().replace("-", "_").replace(" ", "_"))


def list_festivals() -> List[Dict]:
    """List all major traditional Kumaoni festivals."""
    return [asdict(f) for f in FESTIVALS_DATA.values()]
