"""
Configuration constants for DNA Simulation

This module contains configuration constants and trait definitions for the DNA simulation system.
"""

# ============================================================================
# CONFIGURATION CONSTANTS
# ============================================================================

# Total number of traits
NUM_TRAITS = 32

# Trait category ranges
PHYSICAL_TRAITS = list(range(0, 8))
HEALTH_TRAITS = list(range(8, 16))
MENTAL_TRAITS = list(range(16, 24))
MAGICAL_TRAITS = list(range(24, 32))

# Numeric traits (use averaging for equal dominance)
NUMERIC_TRAITS = [3, 8, 9, 10, 11, 12, 13, 14, 15]

# Key traits for breeding analysis
KEY_TRAITS = [0, 1, 19, 24, 25, 26]  # Eyes, Hair, Stability, Magic, Bloodline, Divine

# Default mutation rate
DEFAULT_MUTATION_RATE = 0.01

# Genetic similarity thresholds for inbreeding warnings
SEVERE_INBREEDING_THRESHOLD = 0.75
SIGNIFICANT_INBREEDING_THRESHOLD = 0.50
MODERATE_INBREEDING_THRESHOLD = 0.25

