from app.players.player import Player
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: list[Player]) -> int:
    rating = 0
    for player in players:
        rating += player.get_rating()

    return rating


def elves_concert(elves: list[ElfRanger, Druid]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[DwarfWarrior, DwarfBlacksmith]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
