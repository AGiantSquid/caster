from dragonfly import Function, Choice

from caster.lib import control, alphanumeric2 as alphanumeric
from caster.lib.dfplus.merge.ccrmerger import CCRMerger
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class Modifiers(MergeRule):
    pronunciation = CCRMerger.CORE[4]

    mapping = {
        "[<mod>] <letter>": R(Function(alphanumeric.modifiers, extra={"mod", "letter"}), rdescript="Spell"),
    }
    extras = [
        alphanumeric.get_alphabet_choice("letter"),

        Choice("mod",
               {
                   "crop": "alt",
                   # "cropshiff": "alt shift",
                   "troll": "ctrl",
                   # "trollshiff": "control shift",
                   # "trollcrop": "control alt",
                }),
    ]
    defaults = {
        "mod": "",
    }

control.nexus().merger.add_global_rule(Modifiers())
