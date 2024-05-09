from enum import Enum

class EnumRules(Enum):
    RULE_S = 'S\s"[^"]*"\s"[^"]*"\s(0[1-9]|1[0-9]|2[0-3]):([0-5][0-9]|00)+\s(0[1-9]|1[0-9]|2[0-3]):([0-5][0-9]|00)(\\n)?$'
    RULE_Q = 'Q\s"[^"]*"\s(0[1-9]|1[0-9]|2[0-3]):([0-5][0-9]|00)(\\n)?$'
    METHODS = ['S', 'Q']
    FILES_SUPPORTED = ['.txt']
