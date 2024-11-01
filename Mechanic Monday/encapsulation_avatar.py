
class Avatar:
    def __init__(self, name):
        self.name = name
        self._avatar_state = False # Private Attribute

    def enter_avatar_state(self):
        self._avatar_state = True
        return f"{self.name} has entered the Avatar State!"
    
    def leave_avatar_state(self):
        self._avatar_state = False
        return f"{self.name} has exited the Avatar State!"
    
aang = Avatar("Aang")
aang_gets_angry = aang.enter_avatar_state()
print(aang_gets_angry)

aang_calms_down = aang.leave_avatar_state()
