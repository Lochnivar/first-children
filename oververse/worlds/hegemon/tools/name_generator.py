"""
Cultural Name Generator for Hegemon World

Generates culturally appropriate first names and family names
based on culture, and assigns them to burgs (cities).
"""

import random
from typing import List, Dict, Tuple, Optional
from pathlib import Path
import json

try:
    from .hegemon_cultures import ACTIVE_CULTURES, HEGEMON_CULTURES
except ImportError:
    import sys
    from pathlib import Path
    tools_dir = Path(__file__).parent
    sys.path.insert(0, str(tools_dir.parent))
    from tools.hegemon_cultures import ACTIVE_CULTURES, HEGEMON_CULTURES


# ============================================================================
# CULTURAL NAME PATTERNS
# ============================================================================

# First name elements (syllables/roots) by culture template
CULTURAL_FIRST_NAMES = {
    # Germanic Template
    'germanic': {
        'male': [
            # Valthir, Sturmgaard, Eldermark patterns
            'Aethel', 'Alaric', 'Baldric', 'Conrad', 'Dietrich', 'Erik', 
            'Friedrich', 'Gunther', 'Hakon', 'Ingvar', 'Jurgen', 'Karl',
            'Leif', 'Magnus', 'Odin', 'Ragnar', 'Siegfried', 'Thorin',
            'Ulrich', 'Werner', 'Bjorn', 'Gunnar', 'Harald', 'Ivar',
            'Rolf', 'Stein', 'Torvald', 'Vidar', 'Wulf', 'Einar'
        ],
        'female': [
            'Astrid', 'Birgit', 'Dagmar', 'Elsa', 'Freya', 'Gudrun',
            'Helga', 'Ingrid', 'Jorunn', 'Kara', 'Liv', 'Maren',
            'Nora', 'Olga', 'Ragna', 'Sigrid', 'Thora', 'Ursula',
            'Vera', 'Wendy', 'Ylva', 'Astrid', 'Brita', 'Erika',
            'Greta', 'Hilda', 'Kirsten', 'Lena', 'Marta', 'Solveig'
        ],
        'surname_patterns': [
            # Germanic surname patterns: -son, -sen, von X, -berg, -gard
            '{firstname}son', '{firstname}sen', 'von {place}',
            '{place}berg', '{place}gard', '{place}heim', '{place}stad',
            'the {trait}', '{element}hammer', '{element}blade'
        ],
        'place_elements': [
            'Nord', 'Sud', 'Ost', 'West', 'Berg', 'Hof', 'Wald', 'See',
            'Fjord', 'Stein', 'Eisen', 'Gold', 'Silber', 'Wolf', 'Adler'
        ],
        'trait_words': [
            'Bold', 'Brave', 'Wise', 'Strong', 'Swift', 'Stout', 'Proud'
        ]
    },
    
    # Latin Template
    'latin': {
        'male': [
            # Veridian, Solemnium, Aurelian, Meridian patterns
            'Aurelius', 'Caius', 'Decimus', 'Fabius', 'Gaius', 'Julius',
            'Lucius', 'Marcus', 'Quintus', 'Titus', 'Valerius', 'Publius',
            'Antonius', 'Claudius', 'Cornelius', 'Flavius', 'Horatius',
            'Marius', 'Octavius', 'Severus', 'Vibius', 'Cassius',
            'Dominic', 'Emilio', 'Giovanni', 'Lorenzo', 'Marco', 'Nico'
        ],
        'female': [
            'Aurelia', 'Claudia', 'Cornelia', 'Flavia', 'Julia', 'Livia',
            'Marcia', 'Octavia', 'Portia', 'Valeria', 'Lucia', 'Tullia',
            'Antonia', 'Fausta', 'Helena', 'Iulia', 'Sulpicia', 'Titia',
            'Dominica', 'Emilia', 'Giovanna', 'Lorenza', 'Marcella', 'Nicoleta'
        ],
        'surname_patterns': [
            # Latin patterns: -ius, -us, -anus, de X, di X
            '{firstname}ius', '{firstname}us', '{firstname}anus',
            'de {place}', 'di {place}', '{place}ensis', '{place}anus',
            'the {trait}ius', '{element}manus'
        ],
        'place_elements': [
            'Castra', 'Villa', 'Roma', 'Nova', 'Alta', 'Magna', 'Parva',
            'Fluvius', 'Mons', 'Mare', 'Silva', 'Campus', 'Portus'
        ],
        'trait_words': [
            'Magnus', 'Pius', 'Sapiens', 'Fortis', 'Celer', 'Prudens'
        ]
    },
    
    # Berber Template
    'berber': {
        'male': [
            # Qasridan patterns
            'Amir', 'Hakim', 'Jabir', 'Karim', 'Malik', 'Nasir',
            'Omar', 'Rashid', 'Salim', 'Tariq', 'Umar', 'Yasin',
            'Zahir', 'Abdul', 'Farid', 'Hamza', 'Idris', 'Khalil',
            'Layth', 'Mansur', 'Nadir', 'Qasim', 'Rami', 'Sadiq'
        ],
        'female': [
            'Aaliyah', 'Amira', 'Fatima', 'Jamila', 'Khadija', 'Layla',
            'Mariam', 'Nadia', 'Safa', 'Zara', 'Zahra', 'Aisha',
            'Dina', 'Halima', 'Iman', 'Jamilah', 'Khalida', 'Lina',
            'Malika', 'Noor', 'Rahma', 'Samira', 'Yasmin', 'Zainab'
        ],
        'surname_patterns': [
            # Berber patterns: al-X, ibn X, -i, -an
            'al {place}', 'ibn {firstname}', '{place}i', '{place}an',
            'the {trait}', '{element}i', '{element}an'
        ],
        'place_elements': [
            'Al', 'Bahr', 'Jabal', 'Sahra', 'Wadi', 'Qasr', 'Dar',
            'Ras', 'Qaryat', 'Ain', 'Bir', 'Hajar', 'Raml'
        ],
        'trait_words': [
            'Alim', 'Hakim', 'Karim', 'Malik', 'Nasir', 'Salim'
        ]
    },
    
    # Slavic Template
    'slavic': {
        'male': [
            # Zvezdan, Yaroslav patterns
            'Boris', 'Dmitri', 'Igor', 'Ivan', 'Mikhail', 'Nikolai',
            'Pavel', 'Sergei', 'Vladimir', 'Yuri', 'Alexei', 'Andrei',
            'Dmitry', 'Fyodor', 'Grigori', 'Konstantin', 'Lev', 'Maxim',
            'Oleg', 'Pyotr', 'Roman', 'Stepan', 'Viktor', 'Yaroslav',
            'Zvezdan', 'Bogdan', 'Dragan', 'Ilya', 'Jovan', 'Luka'
        ],
        'female': [
            'Anastasia', 'Daria', 'Elena', 'Irina', 'Katarina', 'Mariya',
            'Natalia', 'Olga', 'Sofia', 'Tatiana', 'Valeria', 'Yelena',
            'Aleksandra', 'Darya', 'Ekaterina', 'Galina', 'Ivana', 'Jelena',
            'Ksenia', 'Lyudmila', 'Marina', 'Nadezhda', 'Svetlana', 'Vera',
            'Yaroslava', 'Zvezdana', 'Bogdana', 'Dragana', 'Jovana', 'Luka'
        ],
        'surname_patterns': [
            # Slavic patterns: -ov, -ev, -in, -ski, -ich
            '{firstname}ov', '{firstname}ev', '{firstname}in',
            '{place}ski', '{place}ev', '{place}ov', '{place}in',
            '{trait}ov', '{element}ov', '{element}ski'
        ],
        'place_elements': [
            'Novo', 'Staraya', 'Krasno', 'Bel', 'Chern', 'Zelen',
            'Gorod', 'Grad', 'Pol', 'Les', 'Reka', 'More', 'Gora'
        ],
        'trait_words': [
            'Bogdan', 'Bratislav', 'Dragomir', 'Jaroslav', 'Miroslav', 'Vladislav'
        ]
    },
    
    # Fusion (Sundrakar)
    'fusion': {
        'male': [
            # Hybrid Germanic + Berber
            'Khalid', 'Ragnar', 'Amir', 'Bjorn', 'Hakim', 'Gunther',
            'Malik', 'Siegfried', 'Tariq', 'Erik', 'Nasir', 'Karl',
            'Omar', 'Thorin', 'Rashid', 'Magnus', 'Salim', 'Dietrich'
        ],
        'female': [
            'Aaliyah', 'Astrid', 'Fatima', 'Freya', 'Jamila', 'Helga',
            'Layla', 'Ingrid', 'Mariam', 'Gudrun', 'Nadia', 'Elsa',
            'Safa', 'Sigrid', 'Zara', 'Thora', 'Amira', 'Kara'
        ],
        'surname_patterns': [
            # Hybrid patterns
            '{firstname}son al {place}', 'ibn {firstname} {place}berg',
            '{place}heim ibn {firstname}', '{element}hammer al {place}'
        ],
        'place_elements': [
            'Khar', 'Sund', 'Rak', 'Brand', 'Grim', 'Khal', 'Mal', 'Nas'
        ],
        'trait_words': [
            'Grim', 'Khal', 'Rak', 'Brand', 'Sund'
        ]
    },
    
    # Special (Khanhthien - East Asian)
    'east_asian': {
        'male': [
            'An', 'Bao', 'Chen', 'Dao', 'Feng', 'Guang', 'Hao', 'Jian',
            'Kai', 'Liang', 'Ming', 'Ning', 'Qi', 'Rong', 'Shan', 'Tao',
            'Wei', 'Xiang', 'Yong', 'Zheng', 'Chang', 'Dong', 'Fang',
            'Gang', 'Hong', 'Jin', 'Kang', 'Lin', 'Long', 'Ping'
        ],
        'female': [
            'Ai', 'Bai', 'Chun', 'Dan', 'Fang', 'Gui', 'Hua', 'Jing',
            'Lan', 'Mei', 'Ning', 'Qing', 'Rui', 'Shan', 'Ting', 'Wei',
            'Xia', 'Yan', 'Zhen', 'An', 'Bing', 'Cai', 'Di', 'E',
            'Fei', 'Hong', 'Jia', 'Ke', 'Li', 'Ming'
        ],
        'surname_patterns': [
            # East Asian: Single character or compound
            '{firstname}', '{place}', '{element}{element}',
            '{firstname} {element}', '{place} {element}'
        ],
        'place_elements': [
            'An', 'Bai', 'Chen', 'Dong', 'Feng', 'Gang', 'He', 'Jiang',
            'Kang', 'Liang', 'Ming', 'Ning', 'Qing', 'Shan', 'Tian', 'Wei'
        ],
        'trait_words': [
            'An', 'Bao', 'Feng', 'Guang', 'Hao', 'Jian', 'Ming', 'Wei'
        ]
    },
}


# Map culture keys to templates
CULTURE_TO_TEMPLATE = {
    # Germanic
    'valthir': 'germanic',
    'sturmgaard': 'germanic',
    'eldermark': 'germanic',
    
    # Latin
    'veridian': 'latin',
    'solemnium': 'latin',
    'aurelian': 'latin',
    'meridian': 'latin',
    
    # Berber
    'qasridan': 'berber',
    
    # Slavic
    'zvezdan': 'slavic',
    'yaroslav': 'slavic',
    
    # Fusion
    'sundrakar': 'fusion',
    
    # Special
    'khanhthien': 'east_asian',
}


def generate_first_name(culture_key: str, gender: str = None) -> str:
    """
    Generate a culturally appropriate first name
    
    Args:
        culture_key: Culture key (e.g., 'valthir', 'veridian')
        gender: 'male' or 'female' (random if None)
        
    Returns:
        First name string
    """
    template = CULTURE_TO_TEMPLATE.get(culture_key, 'germanic')
    
    if template not in CULTURAL_FIRST_NAMES:
        template = 'germanic'  # Fallback
    
    if gender is None:
        gender = random.choice(['male', 'female'])
    
    names = CULTURAL_FIRST_NAMES[template][gender]
    return random.choice(names)


def generate_family_name(culture_key: str, 
                         place_name: Optional[str] = None,
                         founder_first_name: Optional[str] = None) -> str:
    """
    Generate a culturally appropriate family name
    
    Args:
        culture_key: Culture key
        place_name: Optional place name to incorporate
        founder_first_name: Optional founder's first name
        
    Returns:
        Family name string
    """
    template = CULTURE_TO_TEMPLATE.get(culture_key, 'germanic')
    
    if template not in CULTURAL_FIRST_NAMES:
        template = 'germanic'
    
    patterns = CULTURAL_FIRST_NAMES[template]['surname_patterns']
    pattern = random.choice(patterns)
    
    # Replace placeholders
    place_elements = CULTURAL_FIRST_NAMES[template]['place_elements']
    trait_words = CULTURAL_FIRST_NAMES[template]['trait_words']
    
    if place_name is None:
        place_name = random.choice(place_elements)
    
    if founder_first_name is None:
        founder_first_name = random.choice(CULTURAL_FIRST_NAMES[template]['male'])
    
    element = random.choice(place_elements)
    trait = random.choice(trait_words)
    
    # Replace pattern placeholders
    name = pattern.format(
        firstname=founder_first_name,
        place=place_name,
        element=element,
        trait=trait
    )
    
    # Clean up common issues
    name = name.replace('  ', ' ').strip()
    
    return name


def generate_full_name(culture_key: str, 
                      gender: str = None,
                      place_name: Optional[str] = None) -> Tuple[str, str, str]:
    """
    Generate a full name (first name, family name, full name)
    
    Args:
        culture_key: Culture key
        gender: 'male' or 'female' (random if None)
        place_name: Optional place name for family name
        
    Returns:
        Tuple of (first_name, family_name, full_name)
    """
    first_name = generate_first_name(culture_key, gender)
    family_name = generate_family_name(culture_key, place_name, first_name)
    full_name = f"{first_name} {family_name}"
    
    return (first_name, family_name, full_name)


def assign_names_to_burgs(states_dir: str = None):
    """
    Assign culturally appropriate names to all burgs
    
    Reads burg data from state folders and assigns names based on culture.
    Updates burg files with generated names.
    
    Args:
        states_dir: Path to states directory (default: looks in azgaar-data)
    """
    if states_dir is None:
        tools_dir = Path(__file__).parent
        states_dir = tools_dir.parent / 'azgaar-data' / 'states'
    
    states_dir = Path(states_dir)
    
    if not states_dir.exists():
        raise ValueError(f"States directory not found: {states_dir}")
    
    # Load culture mapping from burgs.json files
    # Each burg has a culture index that we need to map to culture names
    
    # First, get culture index -> name mapping from cultures
    culture_index_map = _load_culture_index_map()
    
    # Process each state
    for state_dir in sorted(states_dir.iterdir()):
        if not state_dir.is_dir() or state_dir.name == 'README.md':
            continue
        
        burgs_json_path = state_dir / 'burgs.json'
        if not burgs_json_path.exists():
            continue
        
        print(f"Processing {state_dir.name}...")
        
        # Load burgs
        with open(burgs_json_path, 'r', encoding='utf-8') as f:
            burgs = json.load(f)
        
        # Assign names to each burg
        for burg in burgs:
            # Get culture index
            culture_index = burg.get('culture', 0)
            culture_key = culture_index_map.get(culture_index, 'valthir')
            
            # Generate names for burg
            # Use burg name as place name for family name generation
            burg_place_name = burg.get('name', '').split()[0] if burg.get('name') else None
            
            # Generate ruling family name
            ruling_family_name = generate_family_name(culture_key, burg_place_name)
            
            # Generate prominent families (3-5 families)
            num_families = random.randint(3, 5)
            prominent_families = [
                generate_family_name(culture_key, burg_place_name)
                for _ in range(num_families)
            ]
            
            # Store in burg data
            burg['ruling_family'] = ruling_family_name
            burg['prominent_families'] = prominent_families
            
            # Generate founder name (first ruler)
            founder_gender = random.choice(['male', 'female'])
            founder_first, founder_family, founder_full = generate_full_name(
                culture_key, founder_gender, burg_place_name
            )
            burg['founder'] = {
                'first_name': founder_first,
                'family_name': founder_family,
                'full_name': founder_full,
                'gender': founder_gender
            }
        
        # Save updated burgs
        with open(burgs_json_path, 'w', encoding='utf-8') as f:
            json.dump(burgs, f, indent=2, ensure_ascii=False)
        
        print(f"  Assigned names to {len(burgs)} burgs")
    
    print("\nName assignment complete!")


def _load_culture_index_map() -> Dict[int, str]:
    """
    Load mapping from culture index to culture key
    
    Returns:
        Dict mapping culture index -> culture key
    """
    # Try to load from cultures master list or JSON
    tools_dir = Path(__file__).parent
    cultures_json_path = tools_dir.parent / 'azgaar-data' / '10-cultures.json'
    
    culture_index_map = {}
    
    if cultures_json_path.exists():
        with open(cultures_json_path, 'r', encoding='utf-8') as f:
            cultures = json.load(f)
        
        # Map index to culture name, then to culture key
        for i, culture in enumerate(cultures):
            if isinstance(culture, dict):
                culture_name = culture.get('name', '').lower()
                # Map name to key
                for key, cult_obj in ACTIVE_CULTURES.items():
                    if cult_obj.name.lower() == culture_name:
                        culture_index_map[i] = key
                        break
                else:
                    # Fallback mapping
                    culture_index_map[i] = 'valthir'
            else:
                culture_index_map[i] = 'valthir'
    else:
        # Fallback: use default mapping
        # This is approximate - should be updated with actual data
        default_mapping = {
            0: 'wildlands',
            1: 'qasridan',
            2: 'meridian',
            3: 'valthir',
            4: 'zvezdan',
            5: 'aurelian',
            6: 'sturmgaard',
            7: 'veridian',
            8: 'solemnium',
            9: 'eldermark',
            10: 'yaroslav',
            11: 'khanhthien',
            12: 'sundrakar',
        }
        culture_index_map = default_mapping
    
    return culture_index_map


def generate_burg_families_master_list(states_dir: str = None) -> Dict:
    """
    Generate master list of all families by burg
    
    Args:
        states_dir: Path to states directory
        
    Returns:
        Dictionary mapping state -> burg -> families
    """
    if states_dir is None:
        tools_dir = Path(__file__).parent
        states_dir = tools_dir.parent / 'azgaar-data' / 'states'
    
    states_dir = Path(states_dir)
    master_list = {}
    
    for state_dir in sorted(states_dir.iterdir()):
        if not state_dir.is_dir():
            continue
        
        state_name = state_dir.name
        burgs_json_path = state_dir / 'burgs.json'
        
        if not burgs_json_path.exists():
            continue
        
        with open(burgs_json_path, 'r', encoding='utf-8') as f:
            burgs = json.load(f)
        
        master_list[state_name] = {}
        
        for burg in burgs:
            burg_name = burg.get('name', 'Unknown')
            master_list[state_name][burg_name] = {
                'ruling_family': burg.get('ruling_family'),
                'prominent_families': burg.get('prominent_families', []),
                'founder': burg.get('founder'),
                'culture': burg.get('culture')
            }
    
    return master_list


if __name__ == "__main__":
    # Test name generation
    print("Testing name generation:")
    for culture_key in ['valthir', 'veridian', 'qasridan', 'zvezdan', 'khanhthien']:
        first, family, full = generate_full_name(culture_key)
        print(f"{culture_key}: {full}")
    
    # Assign names to burgs
    print("\nAssigning names to burgs...")
    assign_names_to_burgs()



