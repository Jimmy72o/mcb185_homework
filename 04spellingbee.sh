gunzip -c Code/MCB185/data/dictionary.gz | grep "r" | grep "[ziarcon]" | grep -v "[qwetyupsdfghjklxvbm]" | grep -E ".{4,}"
