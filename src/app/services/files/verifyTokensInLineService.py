import re

from domain.enum.enumProcessorMessages import EnumProcessorMessages
from domain.enum.enumRules import EnumRules

def verifyTokensInLineService(line):
    if line[0] in EnumRules.METHODS.value:
        if line[0] == 'Q':
            if not re.match(EnumRules.RULE_Q.value, line):
                return False
        if line[0] == 'S':
            if not re.match(EnumRules.RULE_S.value, line):
                return False
    return True
