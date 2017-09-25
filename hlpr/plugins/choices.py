from djchoices import ChoiceItem, DjangoChoices


class CategoryChoices(DjangoChoices):
    """
    Choice Items for possible plugin categories
    """

    admin_commands = ChoiceItem('admin_commands', 'Admin Commands')
    fun_commands = ChoiceItem('fun_commands', 'Fun Commands')
    gameplay = ChoiceItem('gameplay', 'Gameplay')
    general_purpose = ChoiceItem('general_purpose', 'General Purpose')
    server_management = ChoiceItem('server_management', 'Server Management')
    statistical = ChoiceItem('statistical', 'Statistical')
    technical_development = ChoiceItem('technical_development', 'Technical/Development')


class ModChoices(DjangoChoices):
    """
    Choice Items for possible half life mods.
    """

    amx_mod_x = ChoiceItem('amx_mod_x', 'AMX Mod X')
    metamod = ChoiceItem('metamod', 'MetaMod')
    sourcemod = ChoiceItem('sourcemod', 'SourceMod')


class GameChoices(DjangoChoices):
    """
    Choice Items for games
    """

    age_of_chivalry = ChoiceItem('age_of_chivalry', 'Age of Chivalry')
    alien_swarm = ChoiceItem('alien_swarm', 'Alien Swarm')
    any = ChoiceItem('any', 'Any')
    battlegrounds_2 = ChoiceItem('battlegrounds_2', 'Battlegrounds 2')
    counter_strike_go = ChoiceItem('csgo', 'Counter-Strike: GO')
    counter_strike_source = ChoiceItem('css', 'Counter-Strike: Source')
    day_of_defeat_source = ChoiceItem('dods', 'Day of Defeat: Source')
    day_of_infamy = ChoiceItem('day_of_infamy', 'Day of Infamy')
    dino_d_day = ChoiceItem('dino_d_day', 'Dino D-Day')
    dystopia = ChoiceItem('dystopia', 'Dystopia')
    empires = ChoiceItem('empires', 'Empires')
    fortress_forever = ChoiceItem('fortress_forever', 'Fortress Forever')
    half_life_2_deathmatch = ChoiceItem('HL2DM', 'Half-Life 2 Deathmatch')
    left_4_dead = ChoiceItem('l4d', 'Left 4 Dead')
    neotokyo = ChoiceItem('neotokyo', 'Neotokyo')
