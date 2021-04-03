import Setups.TableSetup as tbl
import Games
from Variables import Rounds

Table = tbl.TableSetup()
Results = Games.Craps(Table,Rounds)
print(Results)
