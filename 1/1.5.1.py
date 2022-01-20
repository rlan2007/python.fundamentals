class MoneyBox:
    value = 0
    capacity = 0
    def __init__(self, capacity):
        # ����������� � ���������� � ����������� �������
        self.capacity = capacity

    def can_add(self, v):
        # True, ���� ����� �������� v �����, False �����
        if self.value + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        # �������� v ����� � �������
        if self.can_add(v):
            self.value += v



