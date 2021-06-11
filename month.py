class Month():
    taxBrackets = []

    def __init__(self, date):
        self.date = None
        self.incomesTaxable = {}
        self.incomesNonTaxable = {}
        self.deductions = {}

    @property
    def gross(self):
        return 0

    @property
    def net(self):
        return 0

    def __hash__(self):
        return self.date

    def __str__(self):
        # TODO: Fix
        return f"{self.date} month"

    def __repr__(self):
        # TODO: Fix
        return f"repr {self.date} month"

    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        return self.date < other.date

    def __gt__(self, other):
        return self.date > other.date
