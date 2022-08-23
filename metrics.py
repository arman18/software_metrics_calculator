

import ast
import collections
import math

from radon.visitors import  HalsteadVisitor


Halstead = collections.namedtuple("Halstead", "total functions")


def h_visit_src(code):
    ast_node = ast.parse(code)
    visitor = HalsteadVisitor.from_ast(ast_node)
    total = halstead_visitor_report(visitor)
    functions = [
        (v.context, halstead_visitor_report(v))
        for v in visitor.function_visitors
    ]

    return Halstead(total, functions)


def halstead_visitor_report(visitor):
    """Return a HalsteadReport from a HalsteadVisitor instance."""
    h1, h2 = visitor.distinct_operators, visitor.distinct_operands
    N1, N2 = visitor.operators, visitor.operands
    h = h1 + h2
    N = N1 + N2
    volume = N * math.log(h, 2) if h != 0 else 0
    difficulty = (h1 * N2) / float(2 * h2) if h2 != 0 else 0
    effort = difficulty * volume
    return (
        h1,
        h2,
        N1,
        N2,
        h,
        N,
        volume,
        difficulty,
        effort
    )

