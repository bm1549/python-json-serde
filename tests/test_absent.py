from json_serde._utils import Absent, _Absent


def test_absent():
    assert None is not Absent
    assert _Absent() is Absent
    assert '' is not Absent
    assert False is not Absent
