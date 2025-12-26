"""
Hegemon World Cultural Preferences

Loads all 13 cultural preference definitions.
Culture objects define trait preferences for mate selection.
"""

from .dna_culture import Culture

# ============================================================================
# GERMANIC TEMPLATE CULTURES (3)
# ============================================================================

# Culture 1: VALTHIR (Code: No)
# Type: Generic | Expansionism: 1.0 | Template: Germanic
# Description: Traditional Northern culture, resistant to change
VALTHIR = Culture(
    name="Valthir",
    preferences={
        # Physical: Value traditional northern appearance
        0: lambda eyes: 10 if 6 <= eyes <= 9 else 5,  # Blue/Grey eyes preferred
        1: lambda hair: 10 if 5 <= hair <= 7 else 5,  # Blonde/Ash blonde preferred
        3: lambda height: height * 0.8,                # Taller preferred (modest)
        4: lambda build: max(0, build - 4) * 1.2,      # Sturdy/strong build
        
        # Health: Value hardiness and longevity
        8: lambda constitution: constitution * 1.5,     # Constitution important
        10: lambda longevity: longevity * 1.2,          # Value long life
        11: lambda disease: disease * 1.3,              # Disease resistance
        
        # Mental: Value stability and tradition
        19: lambda stability: stability * 1.8,          # Stability VERY important
        17: lambda wisdom: wisdom * 1.5,                # Wisdom valued
        20: lambda willpower: willpower * 1.3,          # Strong will
        
        # Magical: Low priority
        24: lambda magic: magic * 0.3,                  # Magic not valued highly
    },
    mate_selection_pressure=0.75  # Strong traditional preferences
)

# Culture 2: STURMGAARD (Code: Sh)
# Type: Generic | Expansionism: 1.2 | Template: Germanic
# Description: Central Germanic, stable, aware of patterns
STURMGAARD = Culture(
    name="Sturmgaard",
    preferences={
        # Physical: Balanced Germanic traits
        0: lambda eyes: 8 if 4 <= eyes <= 9 else 4,   # Green to Grey eyes
        1: lambda hair: 8 if 2 <= hair <= 8 else 4,   # Brown to Red hair
        4: lambda build: build * 1.0,                  # All builds acceptable
        
        # Health: Value balance
        8: lambda constitution: constitution * 1.3,    # Constitution important
        9: lambda fertility: fertility * 1.4,          # Fertility valued
        
        # Mental: Value intelligence and awareness
        16: lambda intelligence: intelligence * 2.0,   # Intelligence VERY valued
        17: lambda wisdom: wisdom * 1.8,               # Wisdom important
        19: lambda stability: stability * 1.5,         # Stability valued
        23: lambda memory: memory * 1.5,               # Memory important
        
        # Magical: Moderate interest (academic)
        24: lambda magic: magic * 1.2,                 # Some magical interest
    },
    mate_selection_pressure=0.65  # Moderate, thoughtful selection
)

# Culture 3: ELDERMARK (Code: An)
# Type: Generic | Expansionism: 1.8 | Template: Germanic
# Description: Ambitious, expansionist, possibly Strategist-driven
ELDERMARK = Culture(
    name="Eldermark",
    preferences={
        # Physical: Value strength and presence
        3: lambda height: height * 1.5,                # Height important (dominance)
        4: lambda build: build * 1.8,                  # Strong build VERY valued
        5: lambda features: features * 1.5,            # Noble features valued
        
        # Health: Value vigor and fertility
        8: lambda constitution: constitution * 1.8,    # Strong constitution
        9: lambda fertility: fertility * 2.0,          # High fertility (expansion)
        13: lambda healing: healing * 1.3,             # Fast healing (warriors)
        
        # Mental: Value leadership traits
        18: lambda charisma: charisma * 2.0,           # Charisma VERY important
        20: lambda willpower: willpower * 1.8,         # Strong will
        19: lambda stability: stability * 1.2,         # Stability (moderate)
        
        # Magical: Moderate (tools for expansion)
        24: lambda magic: magic * 1.0,                 # Magic as tool
    },
    mate_selection_pressure=0.80  # Strong selection (ambitious culture)
)

# ============================================================================
# LATIN TEMPLATE CULTURES (4)
# ============================================================================

# Culture 4: VERIDIAN (Code: Ro)
# Type: Generic | Expansionism: 1.6 | Template: Latin (Roman)
# Description: Imperial, structured, expansionist
VERIDIAN = Culture(
    name="Veridian",
    preferences={
        # Physical: Value classical beauty and strength
        5: lambda features: features * 1.8,            # Noble features important
        4: lambda build: max(0, build - 3) * 1.5,     # Athletic/strong build
        3: lambda height: height * 1.2,                # Height valued
        
        # Health: Value vigor and endurance
        8: lambda constitution: constitution * 1.8,    # Constitution VERY important
        9: lambda fertility: fertility * 1.6,          # Fertility valued
        12: lambda pain: pain * 1.4,                   # Pain tolerance (military)
        
        # Mental: Value intelligence and leadership
        16: lambda intelligence: intelligence * 1.8,   # Intelligence important
        18: lambda charisma: charisma * 1.8,           # Charisma important
        17: lambda wisdom: wisdom * 1.5,               # Wisdom valued
        20: lambda willpower: willpower * 1.6,         # Strong will
        
        # Magical: Moderate (organized magic systems)
        24: lambda magic: magic * 1.0,                 # Magic as discipline
        25: lambda bloodline: bloodline * 1.3,         # Bloodline matters
    },
    mate_selection_pressure=0.75  # Strong imperial preferences
)

# Culture 5: SOLEMNIUM (Code: Ta)
# Type: Generic | Expansionism: 1.5 | Template: Latin (Italian)
# Description: Artistic, cultured, balanced
SOLEMNIUM = Culture(
    name="Solemnium",
    preferences={
        # Physical: Value beauty and refinement
        5: lambda features: features * 2.0,            # Beauty VERY important
        0: lambda eyes: eyes * 1.2,                    # Expressive eyes valued
        6: lambda voice: voice * 1.5,                  # Beautiful voice
        7: lambda scent: scent * 1.3,                  # Pleasant presence
        
        # Health: Value vitality
        8: lambda constitution: constitution * 1.3,    # Health important
        9: lambda fertility: fertility * 1.5,          # Fertility valued
        
        # Mental: Value creativity and social graces
        22: lambda creativity: creativity * 2.5,       # Creativity HIGHLY valued
        18: lambda charisma: charisma * 2.0,           # Charisma very important
        16: lambda intelligence: intelligence * 1.5,   # Intelligence valued
        
        # Magical: Moderate (artistic magic)
        24: lambda magic: magic * 1.2,                 # Magic as art
    },
    mate_selection_pressure=0.70  # Moderate-strong aesthetic preferences
)

# Culture 6: AURELIAN (Code: Po)
# Type: Hunting | Expansionism: 1.4 | Template: Latin (Iberian)
# Description: Hunting culture, practical, explorers
AURELIAN = Culture(
    name="Aurelian",
    preferences={
        # Physical: Value practical strength
        8: lambda constitution: constitution * 2.0,    # Constitution CRITICAL
        4: lambda build: max(0, build - 3) * 1.5,     # Athletic build
        3: lambda height: height * 1.0,                # Height neutral
        
        # Health: Value survival traits
        11: lambda disease: disease * 1.8,             # Disease resistance important
        13: lambda healing: healing * 1.5,             # Fast healing valued
        12: lambda pain: pain * 1.4,                   # Pain tolerance
        9: lambda fertility: fertility * 1.6,          # Fertility important
        
        # Mental: Value awareness and courage
        17: lambda wisdom: wisdom * 1.8,               # Wisdom (survival)
        20: lambda willpower: willpower * 1.6,         # Willpower important
        16: lambda intelligence: intelligence * 1.2,   # Intelligence valued
        
        # Magical: Low (practical people)
        24: lambda magic: magic * 0.5,                 # Magic not prioritized
    },
    mate_selection_pressure=0.65  # Moderate practical selection
)

# Culture 7: MERIDIAN (Code: Lu)
# Type: Generic | Expansionism: 1.3 | Template: Latin (French)
# Description: Refined, courtly, moderate expansion
MERIDIAN = Culture(
    name="Meridian",
    preferences={
        # Physical: Value elegance and beauty
        5: lambda features: features * 2.2,            # Beauty VERY important
        6: lambda voice: voice * 1.8,                  # Voice important
        7: lambda scent: scent * 1.5,                  # Presence valued
        0: lambda eyes: eyes * 1.3,                    # Expressive eyes
        
        # Health: Value grace over raw strength
        8: lambda constitution: constitution * 1.2,    # Health moderate
        9: lambda fertility: fertility * 1.4,          # Fertility valued
        
        # Mental: Value wit and social intelligence
        18: lambda charisma: charisma * 2.5,           # Charisma HIGHLY valued
        16: lambda intelligence: intelligence * 1.8,   # Intelligence important
        22: lambda creativity: creativity * 1.8,       # Creativity valued
        17: lambda wisdom: wisdom * 1.2,               # Wisdom moderate
        
        # Magical: Moderate (courtly magic)
        24: lambda magic: magic * 1.3,                 # Magic appreciated
        25: lambda bloodline: bloodline * 1.8,         # Bloodline VERY important
    },
    mate_selection_pressure=0.72  # Strong courtly preferences
)

# ============================================================================
# BERBER TEMPLATE CULTURE (1)
# ============================================================================

# Culture 8: QASRIDAN (Code: Be)
# Type: Hunting | Expansionism: 1.6 | Template: Berber
# Description: Desert hunters, adaptable, resilient
QASRIDAN = Culture(
    name="Qasridan",
    preferences={
        # Physical: Value endurance over raw strength
        8: lambda constitution: constitution * 2.2,    # Constitution CRITICAL
        4: lambda build: 15 - abs(build - 7),          # Lean build preferred (7±2)
        3: lambda height: height * 0.8,                # Height less important
        
        # Health: Value desert survival traits
        11: lambda disease: disease * 2.0,             # Disease resistance VERY important
        14: lambda metabolism: 12 - abs(metabolism - 6), # Moderate metabolism preferred
        15: lambda toxin: toxin * 1.8,                 # Toxin resistance important
        9: lambda fertility: fertility * 1.8,          # High fertility valued
        10: lambda longevity: longevity * 1.5,         # Long life valued
        
        # Mental: Value wisdom and endurance
        17: lambda wisdom: wisdom * 2.0,               # Wisdom VERY important
        20: lambda willpower: willpower * 1.8,         # Willpower important
        16: lambda intelligence: intelligence * 1.3,   # Intelligence valued
        
        # Magical: Low (practical survival focus)
        24: lambda magic: magic * 0.4,                 # Magic not emphasized
    },
    mate_selection_pressure=0.68  # Strong practical selection
)

# ============================================================================
# SLAVIC TEMPLATE CULTURES (2)
# ============================================================================

# Culture 9: ZVEZDAN (Code: Sl)
# Type: Nomadic | Expansionism: 2.2 | Template: Slavic
# Description: Nomadic, high expansion, mobile
ZVEZDAN = Culture(
    name="Zvezdan",
    preferences={
        # Physical: Value hardiness
        8: lambda constitution: constitution * 2.0,    # Constitution VERY important
        4: lambda build: max(0, build - 4) * 1.3,     # Strong build valued
        3: lambda height: height * 1.2,                # Height valued
        
        # Health: Value endurance and fertility
        9: lambda fertility: fertility * 2.2,          # Fertility CRITICAL (expansion)
        11: lambda disease: disease * 1.6,             # Disease resistance
        13: lambda healing: healing * 1.4,             # Fast healing
        10: lambda longevity: longevity * 1.3,         # Longevity valued
        
        # Mental: Value courage and adaptability
        20: lambda willpower: willpower * 1.8,         # Willpower important
        17: lambda wisdom: wisdom * 1.4,               # Wisdom valued
        19: lambda stability: stability * 1.3,         # Stability valued
        
        # Magical: Moderate (shamanistic traditions)
        24: lambda magic: magic * 0.8,                 # Some magical tradition
    },
    mate_selection_pressure=0.62  # Moderate (nomadic flexibility)
)

# Culture 10: YAROSLAV (Code: So)
# Type: Nomadic | Expansionism: 2.3 | Template: Slavic
# Description: Nomadic, highest Slavic expansion, aggressive
YAROSLAV = Culture(
    name="Yaroslav",
    preferences={
        # Physical: Value warrior traits
        8: lambda constitution: constitution * 2.2,    # Constitution CRITICAL
        4: lambda build: build * 1.8,                  # Strong build VERY valued
        3: lambda height: height * 1.5,                # Height important
        
        # Health: Value vigor and fertility
        9: lambda fertility: fertility * 2.5,          # Fertility HIGHEST priority
        12: lambda pain: pain * 1.8,                   # Pain tolerance important
        13: lambda healing: healing * 1.6,             # Fast healing
        11: lambda disease: disease * 1.4,             # Disease resistance
        
        # Mental: Value courage and strength of will
        20: lambda willpower: willpower * 2.0,         # Willpower VERY important
        18: lambda charisma: charisma * 1.5,           # Charisma (leadership)
        19: lambda stability: stability * 1.2,         # Stability moderate
        
        # Magical: Low (warrior focus)
        24: lambda magic: magic * 0.5,                 # Magic not prioritized
    },
    mate_selection_pressure=0.70  # Strong warrior selection
)

# ============================================================================
# FUSION CULTURE (1)
# ============================================================================

# Culture 11: SUNDRAKAR (Code: Eu)
# Type: Nomadic | Expansionism: 3.0 | Template: Germanic + Berber Fusion
# Description: Highest expansion, aggressive hybrid culture
SUNDRAKAR = Culture(
    name="Sundrakar",
    preferences={
        # Physical: Hybrid vigor - value adaptability
        8: lambda constitution: constitution * 2.5,    # Constitution HIGHEST priority
        4: lambda build: max(0, build - 5) * 1.5,     # Strong/athletic build
        3: lambda height: height * 1.3,                # Height valued
        
        # Health: Value extreme survivability
        9: lambda fertility: fertility * 2.8,          # Fertility EXTREME (3.0 expansion)
        11: lambda disease: disease * 2.0,             # Disease resistance critical
        13: lambda healing: healing * 1.8,             # Fast healing important
        12: lambda pain: pain * 1.8,                   # Pain tolerance important
        15: lambda toxin: toxin * 1.5,                 # Toxin resistance (desert)
        
        # Mental: Value aggression and adaptability
        20: lambda willpower: willpower * 2.2,         # Willpower VERY important
        16: lambda intelligence: intelligence * 1.5,   # Intelligence (tactics)
        19: lambda stability: stability * 1.0,         # Stability neutral (chaotic)
        
        # Magical: Moderate (hybrid traditions)
        24: lambda magic: magic * 1.0,                 # Magic neutral
    },
    mate_selection_pressure=0.78  # Strong selection (aggressive expansion)
)

# ============================================================================
# SPECIAL CULTURES (2)
# ============================================================================

# Culture 12: KHANHTHIEN (Code: Vi)
# Type: Generic | Expansionism: 2.3 | Template: East Asian
# Description: High expansion, philosophical, aware of "game of heaven"
KHANHTHIEN = Culture(
    name="Khanhthien",
    preferences={
        # Physical: Value balance and harmony
        5: lambda features: features * 1.5,            # Refined features
        4: lambda build: 12 - abs(build - 6),          # Balanced build preferred
        0: lambda eyes: 8 if eyes <= 3 else 4,        # Dark eyes preferred
        1: lambda hair: 10 if hair <= 2 else 3,       # Dark hair preferred
        
        # Health: Value longevity and health
        8: lambda constitution: constitution * 1.6,    # Constitution important
        10: lambda longevity: longevity * 2.0,         # Longevity VERY valued
        9: lambda fertility: fertility * 1.8,          # Fertility important
        11: lambda disease: disease * 1.5,             # Disease resistance
        
        # Mental: Value wisdom and balance
        17: lambda wisdom: wisdom * 2.5,               # Wisdom HIGHEST priority
        16: lambda intelligence: intelligence * 2.0,   # Intelligence VERY important
        19: lambda stability: stability * 1.8,         # Stability important
        23: lambda memory: memory * 1.6,               # Memory valued
        
        # Magical: High (philosophical understanding)
        24: lambda magic: magic * 1.8,                 # Magic important (philosophy)
        30: lambda prophecy: prophecy * 1.5,           # Prophecy valued ("game of heaven")
    },
    mate_selection_pressure=0.73  # Strong philosophical selection
)

# Culture 13: WILDLANDS
# Type: Unknown | Expansionism: N/A
# Description: Uninhabited - not a true culture, no preferences
WILDLANDS = Culture(
    name="Wildlands",
    preferences={},  # No preferences (uninhabited)
    mate_selection_pressure=0.0  # No selection
)

# ============================================================================
# CULTURE REGISTRY FOR HEGEMON WORLD
# ============================================================================

HEGEMON_CULTURES = {
    # Germanic Template (3)
    'valthir': VALTHIR,
    'sturmgaard': STURMGAARD,
    'eldermark': ELDERMARK,
    
    # Latin Template (4)
    'veridian': VERIDIAN,
    'solemnium': SOLEMNIUM,
    'aurelian': AURELIAN,
    'meridian': MERIDIAN,
    
    # Berber Template (1)
    'qasridan': QASRIDAN,
    
    # Slavic Template (2)
    'zvezdan': ZVEZDAN,
    'yaroslav': YAROSLAV,
    
    # Fusion (1)
    'sundrakar': SUNDRAKAR,
    
    # Special (2)
    'khanhthien': KHANHTHIEN,
    'wildlands': WILDLANDS,
}

# Exclude Wildlands from active cultures (it's uninhabited)
ACTIVE_CULTURES = {k: v for k, v in HEGEMON_CULTURES.items() if k != 'wildlands'}
