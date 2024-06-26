from .players.elves.elf_ranger import ElfRanger
from .players.elves.druid import Druid
from .players.dwarves.dwarf_warrior import DwarfWarrior
from .players.dwarves.dwarf_blacksmith import DwarfBlacksmith


usage = [DwarfBlacksmith, DwarfWarrior, Druid, ElfRanger]


def calculate_team_total_rating(team: list["ElfRanger", "Druid"]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list["DwarfBlacksmith", "DwarfWarrior"]) \
        -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
