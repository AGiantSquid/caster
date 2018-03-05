from dragonfly import Function, Choice

from caster.lib import control, alphanumeric2 as alphanumeric
from caster.lib.dfplus.merge.ccrmerger import CCRMerger
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class Alphabet(MergeRule):
    pronunciation = CCRMerger.CORE[0]

    mapping = {
        "[<sky>] <letter>": R(Function(alphanumeric.letters2, extra={"sky", "letter"}), rdescript="Spell"),
    }
    extras = [
        alphanumeric.get_alphabet_choice("letter"),
        Choice("sky",
               {"sky": "sky",
                }),
    ]
    defaults = {
        "sky": "",
    }

control.nexus().merger.add_global_rule(Alphabet())
