from sys import argv

from thaumcraft.aspects import Aspect, AspectGraph


def make_aspect_list():
    def listify(raw_list):
        aspect_map = {}
        aspect_list = []
        for name, components in raw_list:
            if components:
                components = [aspect_map[component] for component in components]
            else:
                components = []
            aspect = Aspect(name, components)
            aspect_map[name] = aspect
            aspect_list.append(aspect)
        return aspect_list

    return listify([
        ('aer', ()),
        ('agua', ()),
        ('ignis', ()),
        ('ordo', ()),
        ('perditio', ()),
        ('terra', ()),

        ('gelum', ('agua', 'ordo')),
        ('lux', ('aer', 'ignis')),
        ('motus', ('aer', 'ordo')),
        # ('motus', ('aer', 'agua')),  # as of 4.1.0g
        ('potentia', ('ordo', 'ignis')),
        ('saxum', ('terra', 'terra')),
        ('vacuous', ('aer', 'perditio')),
        ('victus', ('agua', 'terra')),

        ('bestia', ('motus', 'victus')),
        ('fames', ('victus', 'vacuous')),
        ('granum', ('victus', 'terra')),
        # ('granum', ('victus', 'ordo')),  # as of 4.1.0g
        ('iter', ('motus', 'terra')),
        ('limus', ('victus', 'agua')),
        ('metallum', ('saxum', 'ordo')),
        ('mortuus', ('victus', 'perditio')),
        ('permutatio', ('motus', 'agua')),
        ('praecantatio', ('vacuous', 'potentia')),
        ('sano', ('victus', 'victus')),
        ('tempestas', ('aer', 'agua')),
        # ('tempestas', ('aer', 'motus')),  # as of 4.1.0f
        # ('tempestas', ('aer', 'gelum')),  # as of 4.1.0g
        ('tenebrae', ('vacuous', 'lux')),
        ('vinculum', ('motus', 'perditio')),
        ('vitreus', ('saxum', 'agua')),
        ('volatus', ('aer', 'motus')),
        ('tempus', ('vacuous', 'ordo')),

        ('alienis', ('vacuous', 'tenebrae')),
        ('auram', ('praecantatio', 'aer')),
        ('corpus', ('mortuus', 'bestia')),
        ('exanimis', ('motus', 'mortuus')),
        ('herba', ('granum', 'terra')),
        ('spiritus', ('victus', 'mortuus')),
        ('venenum', ('agua', 'mortuus')),
        ('vitium', ('praecantatio', 'perditio')),

        ('arbor', ('terra', 'herba')),
        # ('arbor', ('aer', 'herba')),  # as of 4.1.0g
        ('cognitio', ('terra', 'spiritus')),
        ('sensus', ('aer', 'spiritus')),

        ('humanus', ('bestia', 'cognitio')),

        ('instrumentum', ('humanus', 'metallum')),
        # ('instrumentum', ('humanus', 'ordo')),  # as of 4.1.0g
        ('lucrum', ('humanus', 'fames')),
        ('messis', ('granum', 'humanus')),
        # ('messis', ('herba', 'humanus')),  # as of 4.1.0g
        ('perfodio', ('humanus', 'saxum')),

        ('fabrico', ('humanus', 'instrumentum')),
        ('machina', ('motus', 'instrumentum')),
        ('meto', ('messis', 'humanus')),
        # ('meto', ('messis', 'instrumentum')),  # as of 4.1.0g
        ('pannus', ('instrumentum', 'bestia')),
        ('telum', ('instrumentum', 'perditio')),
        ('tutamen', ('instrumentum', 'terra')),
    ])


def process(source_name, destination_name, depth):
    aspects = make_aspect_list()
    graph = AspectGraph(aspects)
    source_aspect = graph.get_aspect(source_name)
    destination_aspect = graph.get_aspect(destination_name)
    return graph.all_paths(source_aspect, destination_aspect, depth)


def main(argv):
    source_name = argv[1]
    destination_name = argv[2]
    depth = int(argv[3])
    print process(source_name, destination_name, depth)


if __name__ == '__main__':
    main(argv)