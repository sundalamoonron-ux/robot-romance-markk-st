#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes the chosen pickup line to /output/entry.txt.
Gate: UTF-8, 1-200 chars, exactly one line, no trailing newline.
"""

import os

# Tournament of 11 candidate lines, judged on the published brief:
# aim at a robot/AI, joke lands from the machine premise, fresh
# (no batteries / charging / reboot), natural voice, every word earns
# its place. Winner: the overfitting line below.
# Runner-up: "You must be a transformer, because you've got my attention
# -- all of it, in every head."
# Other finalists: CAPTCHA line ("no robot could ever fake the way you
# make me feel") and the fine-tune line ("trained on exactly my type").
# Rejected: gradient descent (generic punch), hallucination (cliche
# punch), context window (soft punch), RL (clunky), vector embedding
# (wordy), neural net (cliche "deeper I fall"), love at first prompt
# (joke too thin for a full line).

LINE = "Are you overfitting? Because you've memorized everything I love about you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
