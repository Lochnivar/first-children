"""
Trait Definitions

This module contains the TRAIT_DEFINITIONS dictionary defining all 32 traits,
their possible values, dominance hierarchies, and markers.

Extracted from HEGEMON-DIALOG.md
"""

# Each trait has 16 possible values (4 bits = 0-15)
# We define what each value means and dominance hierarchy

TRAIT_DEFINITIONS = {
    # ========== PHYSICAL TRAITS (Quartets 0-7) ==========
    0: {
        'name': 'Eye Color',
        'values': {
            0b0000: {'name': 'Dark Brown', 'dominance': 10, 'marker': False},
            0b0001: {'name': 'Brown', 'dominance': 10, 'marker': False},
            0b0010: {'name': 'Hazel', 'dominance': 8, 'marker': False},
            0b0011: {'name': 'Light Hazel', 'dominance': 8, 'marker': False},
            0b0100: {'name': 'Green', 'dominance': 5, 'marker': False},
            0b0101: {'name': 'Sea Green', 'dominance': 5, 'marker': False},
            0b0110: {'name': 'Blue', 'dominance': 3, 'marker': False},
            0b0111: {'name': 'Ice Blue', 'dominance': 3, 'marker': False},
            0b1000: {'name': 'Grey', 'dominance': 2, 'marker': False},
            0b1001: {'name': 'Steel Grey', 'dominance': 2, 'marker': False},
            0b1010: {'name': 'Violet', 'dominance': 1, 'marker': True},  # Royal marker
            0b1011: {'name': 'Deep Violet', 'dominance': 1, 'marker': True},
            0b1100: {'name': 'Amber', 'dominance': 1, 'marker': False},
            0b1101: {'name': 'Gold', 'dominance': 1, 'marker': False},
            0b1110: {'name': 'Red', 'dominance': 1, 'marker': True},  # Demonic/cursed?
            0b1111: {'name': 'Black', 'dominance': 1, 'marker': True},  # Void-touched
        }
    },
    
    1: {
        'name': 'Hair Color',
        'values': {
            0b0000: {'name': 'Black', 'dominance': 10, 'marker': False},
            0b0001: {'name': 'Dark Brown', 'dominance': 10, 'marker': False},
            0b0010: {'name': 'Brown', 'dominance': 8, 'marker': False},
            0b0011: {'name': 'Light Brown', 'dominance': 8, 'marker': False},
            0b0100: {'name': 'Auburn', 'dominance': 6, 'marker': False},
            0b0101: {'name': 'Dark Blonde', 'dominance': 5, 'marker': False},
            0b0110: {'name': 'Blonde', 'dominance': 3, 'marker': False},
            0b0111: {'name': 'Ash Blonde', 'dominance': 3, 'marker': False},
            0b1000: {'name': 'Red', 'dominance': 4, 'marker': False},
            0b1001: {'name': 'Copper Red', 'dominance': 4, 'marker': False},
            0b1010: {'name': 'White', 'dominance': 2, 'marker': False},
            0b1011: {'name': 'Platinum', 'dominance': 1, 'marker': True},  # Elder blood
            0b1100: {'name': 'Silver', 'dominance': 1, 'marker': True},  # Dragon blood
            0b1101: {'name': 'Gold', 'dominance': 1, 'marker': True},  # Divine blood
            0b1110: {'name': 'Blue-Black', 'dominance': 1, 'marker': True},  # Fey blood
            0b1111: {'name': 'Starlight', 'dominance': 1, 'marker': True},  # Celestial
        }
    },
    
    2: {
        'name': 'Skin Tone',
        'values': {
            0b0000: {'name': 'Deep Ebony', 'dominance': 10, 'marker': False},
            0b0001: {'name': 'Dark Brown', 'dominance': 10, 'marker': False},
            0b0010: {'name': 'Brown', 'dominance': 9, 'marker': False},
            0b0011: {'name': 'Medium Brown', 'dominance': 8, 'marker': False},
            0b0100: {'name': 'Olive', 'dominance': 7, 'marker': False},
            0b0101: {'name': 'Tan', 'dominance': 6, 'marker': False},
            0b0110: {'name': 'Medium', 'dominance': 5, 'marker': False},
            0b0111: {'name': 'Fair', 'dominance': 4, 'marker': False},
            0b1000: {'name': 'Pale', 'dominance': 3, 'marker': False},
            0b1001: {'name': 'Porcelain', 'dominance': 2, 'marker': False},
            0b1010: {'name': 'Alabaster', 'dominance': 1, 'marker': True},  # Vampire/undead?
            0b1011: {'name': 'Bronze', 'dominance': 5, 'marker': False},
            0b1100: {'name': 'Copper', 'dominance': 5, 'marker': False},
            0b1101: {'name': 'Golden', 'dominance': 1, 'marker': True},  # Divine touched
            0b1110: {'name': 'Blue-tinted', 'dominance': 1, 'marker': True},  # Elemental
            0b1111: {'name': 'Ashen', 'dominance': 1, 'marker': True},  # Cursed
        }
    },
    
    3: {
        'name': 'Height',
        'values': {i: {
            'name': f"{48 + i*3} inches ({int((48 + i*3)/12)}'{(48 + i*3)%12}\")",
            'dominance': 5,  # Additive trait, dominance less relevant
            'marker': i >= 13  # Very tall (6'5"+) is notable
        } for i in range(16)}
    },
    
    4: {
        'name': 'Build',
        'values': {
            0b0000: {'name': 'Emaciated', 'dominance': 5, 'marker': False},
            0b0001: {'name': 'Frail', 'dominance': 5, 'marker': False},
            0b0010: {'name': 'Thin', 'dominance': 5, 'marker': False},
            0b0011: {'name': 'Slender', 'dominance': 5, 'marker': False},
            0b0100: {'name': 'Slight', 'dominance': 5, 'marker': False},
            0b0101: {'name': 'Average', 'dominance': 5, 'marker': False},
            0b0110: {'name': 'Athletic', 'dominance': 5, 'marker': False},
            0b0111: {'name': 'Muscular', 'dominance': 5, 'marker': False},
            0b1000: {'name': 'Stocky', 'dominance': 5, 'marker': False},
            0b1001: {'name': 'Broad', 'dominance': 5, 'marker': False},
            0b1010: {'name': 'Heavy', 'dominance': 5, 'marker': False},
            0b1011: {'name': 'Powerful', 'dominance': 5, 'marker': True},
            0b1100: {'name': 'Massive', 'dominance': 5, 'marker': True},
            0b1101: {'name': 'Giant', 'dominance': 5, 'marker': True},
            0b1110: {'name': 'Colossal', 'dominance': 5, 'marker': True},
            0b1111: {'name': 'Titanic', 'dominance': 5, 'marker': True},
        }
    },
    
    5: {
        'name': 'Facial Features',
        'values': {
            0b0000: {'name': 'Very Plain', 'dominance': 5, 'marker': False},
            0b0001: {'name': 'Plain', 'dominance': 5, 'marker': False},
            0b0010: {'name': 'Ordinary', 'dominance': 5, 'marker': False},
            0b0011: {'name': 'Common', 'dominance': 5, 'marker': False},
            0b0100: {'name': 'Unremarkable', 'dominance': 5, 'marker': False},
            0b0101: {'name': 'Average', 'dominance': 5, 'marker': False},
            0b0110: {'name': 'Pleasant', 'dominance': 5, 'marker': False},
            0b0111: {'name': 'Attractive', 'dominance': 5, 'marker': False},
            0b1000: {'name': 'Handsome', 'dominance': 5, 'marker': False},
            0b1001: {'name': 'Beautiful', 'dominance': 5, 'marker': False},
            0b1010: {'name': 'Striking', 'dominance': 5, 'marker': True},
            0b1011: {'name': 'Noble', 'dominance': 5, 'marker': True},
            0b1100: {'name': 'Regal', 'dominance': 5, 'marker': True},
            0b1101: {'name': 'Otherworldly', 'dominance': 5, 'marker': True},
            0b1110: {'name': 'Angelic', 'dominance': 5, 'marker': True},
            0b1111: {'name': 'Divine', 'dominance': 5, 'marker': True},
        }
    },
    
    6: {
        'name': 'Voice',
        'values': {
            0b0000: {'name': 'Harsh', 'dominance': 5, 'marker': False},
            0b0001: {'name': 'Rough', 'dominance': 5, 'marker': False},
            0b0010: {'name': 'Gruff', 'dominance': 5, 'marker': False},
            0b0011: {'name': 'Deep', 'dominance': 5, 'marker': False},
            0b0100: {'name': 'Low', 'dominance': 5, 'marker': False},
            0b0101: {'name': 'Average', 'dominance': 5, 'marker': False},
            0b0110: {'name': 'Pleasant', 'dominance': 5, 'marker': False},
            0b0111: {'name': 'Melodious', 'dominance': 5, 'marker': False},
            0b1000: {'name': 'Rich', 'dominance': 5, 'marker': False},
            0b1001: {'name': 'Resonant', 'dominance': 5, 'marker': False},
            0b1010: {'name': 'Commanding', 'dominance': 5, 'marker': True},
            0b1011: {'name': 'Hypnotic', 'dominance': 5, 'marker': True},
            0b1100: {'name': 'Silver-tongued', 'dominance': 5, 'marker': True},
            0b1101: {'name': 'Enchanting', 'dominance': 5, 'marker': True},
            0b1110: {'name': 'Spellbinding', 'dominance': 5, 'marker': True},
            0b1111: {'name': 'Voice of Power', 'dominance': 5, 'marker': True},
        }
    },
    
    7: {
        'name': 'Scent',
        'values': {
            0b0000: {'name': 'Foul', 'dominance': 5, 'marker': False},
            0b0001: {'name': 'Unpleasant', 'dominance': 5, 'marker': False},
            0b0010: {'name': 'Sour', 'dominance': 5, 'marker': False},
            0b0011: {'name': 'Musty', 'dominance': 5, 'marker': False},
            0b0100: {'name': 'Earthy', 'dominance': 5, 'marker': False},
            0b0101: {'name': 'Neutral', 'dominance': 5, 'marker': False},
            0b0110: {'name': 'Clean', 'dominance': 5, 'marker': False},
            0b0111: {'name': 'Pleasant', 'dominance': 5, 'marker': False},
            0b1000: {'name': 'Floral', 'dominance': 5, 'marker': False},
            0b1001: {'name': 'Sweet', 'dominance': 5, 'marker': False},
            0b1010: {'name': 'Honey-like', 'dominance': 5, 'marker': False},
            0b1011: {'name': 'Exotic', 'dominance': 5, 'marker': True},
            0b1100: {'name': 'Intoxicating', 'dominance': 5, 'marker': True},
            0b1101: {'name': 'Divine Perfume', 'dominance': 5, 'marker': True},
            0b1110: {'name': 'Ozone/Lightning', 'dominance': 5, 'marker': True},
            0b1111: {'name': 'Otherworldly', 'dominance': 5, 'marker': True},
        }
    },
    
    # ========== HEALTH TRAITS (Quartets 8-15) ==========
    8: {
        'name': 'Constitution',
        'values': {i: {
            'name': ['Dying', 'Terminal', 'Sickly', 'Frail', 'Weak', 'Below Average', 
                    'Average', 'Healthy', 'Robust', 'Strong', 'Very Strong', 'Exceptional',
                    'Heroic', 'Legendary', 'Mythic', 'Immortal'][i],
            'dominance': 5,
            'marker': i >= 12
        } for i in range(16)}
    },
    
    9: {
        'name': 'Fertility',
        'values': {i: {
            'name': ['Sterile', 'Nearly Sterile', 'Very Low', 'Low', 'Below Average', 'Average',
                    'Above Average', 'High', 'Very High', 'Exceptional', 'Remarkable', 'Extraordinary',
                    'Legendary', 'Mythic', 'Divine', 'Godlike'][i],
            'dominance': 5,
            'marker': i <= 2 or i >= 13  # Both extremes notable
        } for i in range(16)}
    },
    
    10: {
        'name': 'Longevity',
        'values': {i: {
            'name': f"{40 + i*5} years expected",
            'dominance': 5,
            'marker': i >= 13  # 105+ years
        } for i in range(16)}
    },
    
    11: {
        'name': 'Disease Resistance',
        'values': {i: {
            'name': ['None', 'Terrible', 'Very Poor', 'Poor', 'Weak', 'Below Average',
                    'Average', 'Good', 'Strong', 'Very Strong', 'Exceptional', 'Remarkable',
                    'Heroic', 'Legendary', 'Immune', 'Divine'][i],
            'dominance': 5,
            'marker': i >= 13
        } for i in range(16)}
    },
    
    12: {
        'name': 'Pain Tolerance',
        'values': {i: {
            'name': ['None', 'Terrible', 'Very Low', 'Low', 'Below Average', 'Average',
                    'Above Average', 'Good', 'High', 'Very High', 'Exceptional', 'Remarkable',
                    'Heroic', 'Legendary', 'Unflinching', 'Divine'][i],
            'dominance': 5,
            'marker': i >= 13
        } for i in range(16)}
    },
    
    13: {
        'name': 'Healing Rate',
        'values': {i: {
            'name': ['Never Heals', 'Terrible', 'Very Slow', 'Slow', 'Below Average', 'Average',
                    'Above Average', 'Good', 'Fast', 'Very Fast', 'Exceptional', 'Remarkable',
                    'Regeneration', 'Rapid Regen', 'Wolverine', 'Divine'][i],
            'dominance': 5,
            'marker': i >= 12
        } for i in range(16)}
    },
    
    14: {
        'name': 'Metabolism',
        'values': {i: {
            'name': ['Starvation', 'Very Slow', 'Slow', 'Below Average', 'Average', 'Above Average',
                    'Fast', 'Very Fast', 'Hyperactive', 'Extreme', 'Supernatural', 'Legendary',
                    'Mythic', 'Phoenix', 'Elemental', 'Godlike'][i],
            'dominance': 5,
            'marker': i >= 13 or i <= 1
        } for i in range(16)}
    },
    
    15: {
        'name': 'Toxin Resistance',
        'values': {i: {
            'name': ['None', 'Terrible', 'Very Poor', 'Poor', 'Weak', 'Below Average',
                    'Average', 'Good', 'Strong', 'Very Strong', 'Exceptional', 'Remarkable',
                    'Heroic', 'Legendary', 'Immune', 'Processes Poison'][i],
            'dominance': 5,
            'marker': i >= 13
        } for i in range(16)}
    },
    
    # ========== MENTAL TRAITS (Quartets 16-23) ==========
    16: {
        'name': 'Intelligence',
        'values': {i: {
            'name': ['Profound Disability', 'Severe Disability', 'Moderate Disability', 'Mild Disability',
                    'Below Average', 'Average', 'Above Average', 'Bright', 'Very Bright', 'Gifted',
                    'Highly Gifted', 'Genius', 'Exceptional Genius', 'Supergenius', 'Transcendent', 'Divine Mind'][i],
            'dominance': 5,
            'marker': i >= 11
        } for i in range(16)}
    },
    
    17: {
        'name': 'Wisdom',
        'values': {i: {
            'name': ['Foolish', 'Reckless', 'Naive', 'Inexperienced', 'Below Average', 'Average',
                    'Above Average', 'Wise', 'Very Wise', 'Sage', 'Very Sage', 'Oracle',
                    'Prophet', 'Seer', 'Mystic', 'All-Knowing'][i],
            'dominance': 5,
            'marker': i >= 11
        } for i in range(16)}
    },
    
    18: {
        'name': 'Charisma',
        'values': {i: {
            'name': ['Repulsive', 'Off-putting', 'Unlikeable', 'Awkward', 'Below Average', 'Average',
                    'Above Average', 'Charming', 'Very Charming', 'Magnetic', 'Very Magnetic', 'Inspiring',
                    'Legendary', 'Mythic', 'Mesmerizing', 'Divine Presence'][i],
            'dominance': 5,
            'marker': i >= 11
        } for i in range(16)}
    },
    
    19: {
        'name': 'Mental Stability',
        'values': {i: {
            'name': ['Insane', 'Severe Madness', 'Madness', 'Unstable', 'Very Unstable', 'Unstable',
                    'Below Average', 'Average', 'Stable', 'Very Stable', 'Rock Solid', 'Unshakeable',
                    'Iron Will', 'Adamantine', 'Unbreakable', 'Divine Clarity'][i],
            'dominance': 5,
            'marker': i <= 3 or i >= 12  # Both extremes notable
        } for i in range(16)}
    },
    
    20: {
        'name': 'Willpower',
        'values': {i: {
            'name': ['None', 'Terrible', 'Very Weak', 'Weak', 'Below Average', 'Average',
                    'Above Average', 'Strong', 'Very Strong', 'Exceptional', 'Remarkable', 'Heroic',
                    'Legendary', 'Mythic', 'Indomitable', 'Divine'][i],
            'dominance': 5,
            'marker': i >= 12
        } for i in range(16)}
    },
    
    21: {
        'name': 'Empathy',
        'values': {i: {
            'name': ['Psychopath', 'Sociopath', 'Cold', 'Callous', 'Detached', 'Below Average',
                    'Average', 'Empathetic', 'Very Empathetic', 'Compassionate', 'Very Compassionate',
                    'Deeply Empathetic', 'Empath', 'True Empath', 'Psychic Empathy', 'Divine Love'][i],
            'dominance': 5,
            'marker': i <= 1 or i >= 13
        } for i in range(16)}
    },
    
    22: {
        'name': 'Creativity',
        'values': {i: {
            'name': ['None', 'Very Limited', 'Limited', 'Below Average', 'Average', 'Above Average',
                    'Creative', 'Very Creative', 'Highly Creative', 'Exceptional', 'Remarkable', 'Genius',
                    'Visionary', 'Revolutionary', 'Transformative', 'World-Changing'][i],
            'dominance': 5,
            'marker': i >= 11
        } for i in range(16)}
    },
    
    23: {
        'name': 'Memory',
        'values': {i: {
            'name': ['None', 'Terrible', 'Very Poor', 'Poor', 'Below Average', 'Average',
                    'Above Average', 'Good', 'Very Good', 'Excellent', 'Exceptional', 'Eidetic',
                    'Perfect Recall', 'Total Recall', 'Akashic', 'Omniscient'][i],
            'dominance': 5,
            'marker': i >= 11
        } for i in range(16)}
    },
    
    # ========== MAGICAL/SPECIAL TRAITS (Quartets 24-31) ==========
    24: {
        'name': 'Magical Aptitude',
        'values': {i: {
            'name': ['None', 'Trace', 'Minimal', 'Low', 'Below Average', 'Average',
                    'Above Average', 'Talented', 'Gifted', 'Very Gifted', 'Exceptional', 'Prodigy',
                    'Archmage Potential', 'Legendary', 'Mythic', 'Godlike'][i],
            'dominance': 5,
            'marker': i >= 10
        } for i in range(16)}
    },
    
    25: {
        'name': 'Bloodline Power',
        'values': {i: {
            'name': ['None', 'Trace', 'Weak', 'Minor', 'Below Average', 'Average',
                    'Above Average', 'Strong', 'Very Strong', 'Powerful', 'Very Powerful', 'Exceptional',
                    'Ancient Blood', 'Elder Blood', 'First Blood', 'Divine Blood'][i],
            'dominance': 5,
            'marker': i >= 12
        } for i in range(16)}
    },
    
    26: {
        'name': 'Divine Favor',
        'values': {i: {
            'name': ['Cursed', 'Forsaken', 'Shunned', 'Disfavored', 'Below Average', 'Average',
                    'Above Average', 'Favored', 'Blessed', 'Very Blessed', 'Chosen', 'Champion',
                    'Exalted', 'Saint', 'Demigod', 'Avatar'][i],
            'dominance': 5,
            'marker': i <= 2 or i >= 13
        } for i in range(16)}
    },
    
    27: {
        'name': 'Dragon Affinity',
        'values': {i: {
            'name': ['None', 'Trace', 'Minimal', 'Weak', 'Minor', 'Below Average',
                    'Average', 'Above Average', 'Strong', 'Very Strong', 'Dragon-touched', 'Dragonkin',
                    'Dragonblood', 'Dragonheart', 'Dragon Soul', 'True Dragon'][i],
            'dominance': 5,
            'marker': i >= 10
        } for i in range(16)}
    },
    
    28: {
        'name': 'Fey Affinity',
        'values': {i: {
            'name': ['None', 'Trace', 'Minimal', 'Weak', 'Minor', 'Below Average',
                    'Average', 'Above Average', 'Strong', 'Very Strong', 'Fey-touched', 'Fey-kissed',
                    'Fey-blooded', 'Changeling', 'True Fey', 'Archfey'][i],
            'dominance': 5,
            'marker': i >= 10
        } for i in range(16)}
    },
    
    29: {
        'name': 'Elemental Affinity',
        'values': {i: {
            'name': ['None', 'Trace', 'Minimal', 'Weak', 'Minor', 'Below Average',
                    'Average', 'Above Average', 'Strong', 'Very Strong', 'Elemental-touched', 'Elemental-born',
                    'Elemental-blooded', 'Elemental-kin', 'Elemental Soul', 'True Elemental'][i],
            'dominance': 5,
            'marker': i >= 10
        } for i in range(16)}
    },
    
    30: {
        'name': 'Prophecy Resonance',
        'values': {i: {
            'name': ['None', 'Trace', 'Minimal', 'Weak', 'Minor', 'Below Average',
                    'Average', 'Above Average', 'Strong', 'Notable', 'Significant', 'Prophesied',
                    'Fated', 'Destined', 'Chosen One', 'Nexus of Fate'][i],
            'dominance': 5,
            'marker': i >= 11
        } for i in range(16)}
    },
    
    31: {
        'name': 'Shadow Affinity',
        'values': {i: {
            'name': ['None', 'Trace', 'Minimal', 'Weak', 'Minor', 'Below Average',
                    'Average', 'Above Average', 'Strong', 'Very Strong', 'Shadow-touched', 'Shadow-kin',
                    'Shadow-blooded', 'Void-walker', 'Shadow Lord', 'Living Shadow'][i],
            'dominance': 5,
            'marker': i >= 10
        } for i in range(16)}
    },
}

