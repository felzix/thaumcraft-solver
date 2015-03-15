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

        ('gelum', ('ignis', 'perditio')),
        ('lux', ('aer', 'ignis')),
        ('motus', ('aer', 'ordo')),
        ('potentia', ('ordo', 'ignis')),
        ('saxum', ('terra', 'terra')),
        ('vacuos', ('aer', 'perditio')),
        ('victus', ('agua', 'terra')),

        ('bestia', ('motus', 'victus')),
        ('fames', ('victus', 'vacuos')),
        ('iter', ('motus', 'terra')),
        ('limus', ('victus', 'agua')),
        ('mortuus', ('victus', 'perditio')),
        ('permutatio', ('perditio', 'ordo')),
        ('praecantatio', ('vacuos', 'potentia')),
        ('sano', ('victus', 'victus')),
        ('tempestas', ('aer', 'agua')),
        ('tenebrae', ('vacuos', 'lux')),
        ('vinculum', ('motus', 'perditio')),
        ('vitreus', ('terra', 'ordo')),
        ('volatus', ('aer', 'motus')),
        ('tempus', ('vacuos', 'ordo')),

        ('metallum', ('terra', 'vitreus')),
        ('alienis', ('vacuos', 'tenebrae')),
        ('auram', ('praecantatio', 'aer')),
        ('corpus', ('mortuus', 'bestia')),
        ('exanimis', ('motus', 'mortuus')),
        ('herba', ('victus', 'terra')),
        ('infernus', ('ignis', 'praecantatio')),
        ('spiritus', ('victus', 'mortuus')),
        ('venenum', ('agua', 'perditio')),
        ('vitium', ('praecantatio', 'perditio')),

        ('arbor', ('aer', 'herba')),
        ('cognitio', ('ignis', 'spiritus')),
        ('desidia', ('spiritus', 'vinculum')),
        ('luxuria', ('fames', 'corpus')),
        ('sensus', ('aer', 'spiritus')),

        ('humanus', ('bestia', 'cognitio')),

        ('instrumentum', ('humanus', 'ordo')),  # as of 4.1.0g
        ('lucrum', ('humanus', 'fames')),
        ('messis', ('herba', 'humanus')),  # as of 4.1.0g
        ('perfodio', ('humanus', 'terra')),

        ('fabrico', ('humanus', 'instrumentum')),
        ('gula', ('fames', 'vacuos')),
        ('invidia', ('sensus', 'fames')),
        ('machina', ('motus', 'instrumentum')),
        ('meto', ('messis', 'instrumentum')),  # as of 4.1.0g
        ('pannus', ('instrumentum', 'bestia')),
        ('telum', ('instrumentum', 'ignis')),
        ('tutamen', ('instrumentum', 'terra')),

        ('ira', ('telum', 'ignis')),
    ])


def process(source_name, destination_name, depth):
    aspects = make_aspect_list()
    graph = AspectGraph(aspects)
    source_aspect = graph.get_aspect(source_name)
    destination_aspect = graph.get_aspect(destination_name)
    return graph.all_paths(source_aspect, destination_aspect, depth)


def main():
    source_name = argv[1]
    destination_name = argv[2]
    depth = int(argv[3])
    paths = process(source_name, destination_name, depth)
    for path in paths:
        print ' -> '.join(['{:<12}'.format(source_name)] + ['{:<12}'.format(aspect) for aspect in path])


if __name__ == '__main__':
    main()
