full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name,str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    
    stats = [strength, intelligence, charisma]

    for s in stats:
        if type(s) != int:
            return "All stats should be integers"
        if s < 1:
            return "All stats should be no less than 1"
        if s > 4:
            return "All stats should be no more than 4"

    if sum(stats) != 7:
        return "The character should start with 7 points"
    
    def format_stat(label, value):
        full_dots = '●' * value
        empty_dots = '○' * (10 - value)
        return label + " " + full_dots + empty_dots

    result = (
        name + "\n" +
        format_stat("STR", strength) + "\n" +
        format_stat("INT", intelligence) + "\n" +
        format_stat("CHA", charisma)
    )

    return result
