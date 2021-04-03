import Classes.Player as pl
import Classes.Table as tbl
import Variables as va


def TableSetup():
    players = []
    Table = tbl.Table
    for n in va.PlayerNames:
        players.append(pl.Player(n,va.StartingPurse))

    Table.Players = players
    Table.Min = va.TableMin
    Table.Max = va.TableMax
    Table.Multiple = va.TableMultiple
    return Table