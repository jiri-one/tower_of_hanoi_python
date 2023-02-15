import pytest
# internal imports
import towers

NUMBER_OD_DISKS: int = 3
INITIAL_TOWER: list[int] = list(reversed(range(1, NUMBER_OD_DISKS+1)))

def test_move_disk(monkeypatch):
    def init_towers():
        return [INITIAL_TOWER.copy(), [], []]
    
    with monkeypatch.context() as m:
        m.setattr(towers, "towers", init_towers())
        with pytest.raises(IndexError):
            towers.move_disk(2, 1) # from empty to empty tower
    with monkeypatch.context() as m:
        m.setattr(towers, "towers", init_towers())
        towers.move_disk(0, 1) # from first tower to second
    with monkeypatch.context() as m:
        m.setattr(towers, "towers", init_towers())
        towers.move_disk(0, 2) # from first tower to third
