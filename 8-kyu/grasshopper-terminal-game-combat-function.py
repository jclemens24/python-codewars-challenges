def combat(health, damage):
    return health - damage if health - damage > 0 else 0


def combat_v2(health, damage):
    return max(0, health - damage)