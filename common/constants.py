LOG_TYPES = {
    "TRACE": 0,
    "DEBUG": 1,
    "INFO": 2,
    "WARNING": 3,
    "ERROR": 4,
    "CRITICAL": 5,
}

I_LOG_TYPES = {v: k for k, v in LOG_TYPES.items()}

INFRACTION_TYPES = {
    "NOTE": 0,
    "WARN": 1,
    "KICK": 2,
    "MUTE": 3,
    "BAN": 4,
    "MISC": 5,
}

I_INFRACTION_TYPES = {v: k for k, v in INFRACTION_TYPES.items()}
