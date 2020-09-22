from collections import defaultdict

from docutils.parsers.rst import directives

from docutils import nodes
from docutils.parsers.rst import Directive, Parser

from sphinx import addnodes
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain
from sphinx.domains import Index
from sphinx.roles import XRefRole
from sphinx.util.nodes import make_refnode


class dimension(nodes.Admonition, nodes.Element):
    pass

class QuantityDirective(ObjectDescription):
    """A custom directive that describes a recipe."""

    has_content = True
    required_arguments = 1

    option_spec = {
        'dimensions': directives.unchanged_required,
        'symbol': directives.unchanged,
    }

    def handle_signature(self, sig, signode):

        # paragraph_node = nodes.paragraph(text='Hello World!')
        text = '\n'.join(self.content)
        # Create the admonition node, to be populated by `nested_parse`.
        admonition_node = nodes.admonition()
        admonition_node += addnodes.desc_name(self.arguments[0], self.arguments[0])

        dimensions = self.options['dimensions'].split(",")
        paramlist = addnodes.desc_parameterlist()
        parser = Parser()
        for dimension in dimensions:
            superscript = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")
            data = dimension.split("^")
            if len(data)>1:
                data[1] = data[1].replace("{","").replace("}","").translate(superscript)
            paramnode = addnodes.desc_parameter(text="".join(data))
            paramlist += paramnode
        
        content_node = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset,
                                content_node)

        admonition_node += paramlist
        #admonition_node += content_node
        
        signode += admonition_node #addnodes.desc_name(text=sig)
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        signode['ids'].append('dimensions' + '-' + sig)
        if 'noindex' not in self.options:
            ingredients = [
                x.strip() for x in self.options.get('dimensions').split(',')]

            recipes = self.env.get_domain('physics')
            recipes.add_quantity(sig, ingredients)


class DimensionIndex(Index):
    """A custom index that creates an ingredient matrix."""

    name = 'dimension'
    localname = 'Dimension Index'
    shortname = 'Dimension'

    def generate(self, docnames=None):
        content = defaultdict(list)

        quantities = {name: (dispname, typ, docname, anchor)
                   for name, dispname, typ, docname, anchor, _
                   in self.domain.get_objects()}
        quantity_dimensions = self.domain.data['quantity_dimensions']
        dimensions_quantity= defaultdict(list)

        # flip from recipe_ingredients to ingredient_recipes
        for quantity_name, dimensions in quantity_dimensions.items():
            for dimension in dimensions:
                dimensions_quantity[dimension].append(quantity_name)

        # convert the mapping of ingredient to recipes to produce the expected
        # output, shown below, using the ingredient name as a key to group
        #
        # name, subtype, docname, anchor, extra, qualifier, description
        for dimension, quantity_names in dimensions_quantity.items():
            for quantity_name in quantity_names:
                dispname, typ, docname, anchor = quantities[quantity_name]
                content[dimension].append(
                    (dispname, 0, docname, anchor, docname, '', typ))

        # convert the dict to the sorted list of tuples expected
        content = sorted(content.items())

        return content, True


class QuantityIndex(Index):
    """A custom index that creates an recipe matrix."""

    name = 'quantity'
    localname = 'Quantity Index'
    shortname = 'Quantity'

    def generate(self, docnames=None):
        content = defaultdict(list)

        # sort the list of recipes in alphabetical order
        recipes = self.domain.get_objects()
        recipes = sorted(recipes, key=lambda recipe: recipe[0])

        # generate the expected output, shown below, from the above using the
        # first letter of the recipe as a key to group thing
        #
        # name, subtype, docname, anchor, extra, qualifier, description
        for name, dispname, typ, docname, anchor, _ in recipes:
            content[dispname[0].lower()].append(
                (dispname, 0, docname, anchor, docname, '', typ))

        # convert the dict to the sorted list of tuples expected
        content = sorted(content.items())

        return content, True


class QuantityDomain(Domain):

    name = 'physics'
    label = 'Quantity Sample'
    roles = {
        'ref': XRefRole()
    }
    directives = {
        'quantity': QuantityDirective,
    }
    indices = {
        QuantityIndex,
        DimensionIndex
    }
    initial_data = {
        'quantities': [],  # object list
        'quantity_dimensions': {},  # name -> object
    }

    def get_full_qualified_name(self, node):
        return '{}.{}'.format('recipe', node.arguments[0])

    def get_objects(self):
        for obj in self.data['quantities']:
            yield(obj)

    def resolve_xref(self, env, fromdocname, builder, typ, target, node,
                     contnode):
        match = [(docname, anchor)
                 for name, sig, typ, docname, anchor, prio
                 in self.get_objects() if sig == target]

        if len(match) > 0:
            todocname = match[0][0]
            targ = match[0][1]

            return make_refnode(builder, fromdocname, todocname, targ,
                                contnode, targ)
        else:
            print('Awww, found nothing')
            return None

    def add_quantity(self, signature, dimensions):
        """Add a new recipe to the domain."""
        name = '{}.{}'.format('quantity', signature)
        anchor = 'quantity-{}'.format(signature)

        self.data['quantity_dimensions'][name] = dimensions
        # name, dispname, type, docname, anchor, priority
        self.data['quantities'].append(
            (name, signature, 'Quantity', self.env.docname, anchor, 0))


def setup(app):
    app.add_domain(QuantityDomain)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
