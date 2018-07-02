from dragonfly import (Grammar, AppContext, Dictation, Key, Repeat)

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class SublimeRule(MergeRule):
    pronunciation = "sublime"

    mapping = {
        "go to line":
            R(Key("c-g"), rdescript="Sublime: Go To Line"),
        "go to symbol":
            R(Key("c-r"), rdescript="Sublime: Go To Symbol"),
        "go to word":
            R(Key("c-semicolon"), rdescript="Sublime: Go To Word"),
        "uppercase":
            R(Key("control:down, k, u, control:up"),
              rdescript="Sublime: Transform Upper"),
        "lowercase":
            R(Key("control:down, k, l, control:up"),
              rdescript="Sublime: Transform Lower"),
        "outdent":
            R(Key("c-rbrace"), rdescript="Sublime: Outdent"),
        "comment line":
            R(Key("c-slash"), rdescript="Sublime: Comment Line"),
        "comment block":
            R(Key("cs-slash"), rdescript="Sublime: Comment Block"),
        "full screen":
            R(Key("f11"), rdescript="Sublime: Fullscreen"),
        "set bookmark":
            R(Key("c-f2"), rdescript="Sublime: Set Bookmark"),
        "next bookmark":
            R(Key("f2"), rdescript="Sublime: Next Bookmark"),
        "prior bookmark":
            R(Key("s-f2"), rdescript="Sublime: Prior Bookmark"),
        "fold":
            R(Key("ac-lbrace"), rdescript="Sublime: Fold"),
        "unfold":
            R(Key("ac-rbrace"), rdescript="Sublime: Unfold"),
        "open file":
            R(Key("c-p"), rdescript="Sublime: Open File"),
        "new file":
            R(Key("c-n"), rdescript="Sublime: New File"),
        "delete line [<n>]":
            R(Key("cs-k"), rdescript="Sublime: Delete Line or # Lines Below") *
            Repeat(extra="n"),
    }
    extras = [
        IntegerRefST("n", 1, 1000),
    ]
    defaults = {"n": 1}


#---------------------------------------------------------------------------

context = AppContext(executable="sublime_text")
grammar = Grammar("Sublime", context=context)

if settings.SETTINGS["apps"]["sublime"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(SublimeRule())
    else:
        rule = SublimeRule(name="sublime")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()
