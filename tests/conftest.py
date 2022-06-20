"""pytest config."""
import os

from hypothesis import settings

settings.register_profile("slow", settings(max_examples=1000))
settings.register_profile("fast", settings(max_examples=100))

settings.load_profile(os.getenv("HYPOTHESIS_PROFILE", "fast"))
