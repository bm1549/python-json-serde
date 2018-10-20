class _Absent:

    __INSTANCE = None

    def __new__(cls):
        if _Absent.__INSTANCE is None:
            _Absent.__INSTANCE = super().__new__(cls)
        return _Absent.__INSTANCE

    def __repr__(self) -> str:
        return '<Absent>'

Absent = _Absent()
