#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.parsing import tatsumasu
from tatsu.util import re, generic_main  # noqa


KEYWORDS = {}


class CalcBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        namechars='',
        **kwargs
    ):
        super(CalcBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class CalcParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        left_recursion=True,
        parseinfo=False,
        keywords=None,
        namechars='',
        buffer_class=CalcBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(CalcParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
            **kwargs
        )

    @tatsumasu()
    def _start_(self):  # noqa
        self._expression_()
        self._check_eof()

    @tatsumasu()
    def _expression_(self):  # noqa
        with self._choice():
            with self._option():
                self._addition_()
            with self._option():
                self._subtraction_()
            with self._option():
                self._term_()
            self._error('no available options')

    @tatsumasu()
    def _addition_(self):  # noqa
        self._term_()
        self.name_last_node('left')
        self._token('+')
        self.name_last_node('op')
        self._cut()
        self._expression_()
        self.name_last_node('right')
        self.ast._define(
            ['left', 'op', 'right'],
            []
        )

    @tatsumasu()
    def _subtraction_(self):  # noqa
        self._term_()
        self.name_last_node('left')
        self._token('-')
        self.name_last_node('op')
        self._cut()
        self._expression_()
        self.name_last_node('right')
        self.ast._define(
            ['left', 'op', 'right'],
            []
        )

    @tatsumasu()
    def _term_(self):  # noqa
        with self._choice():
            with self._option():
                self._multiplication_()
            with self._option():
                self._division_()
            with self._option():
                self._unary_()
            self._error('no available options')

    @tatsumasu()
    def _multiplication_(self):  # noqa
        self._unary_()
        self.name_last_node('left')
        self._token('*')
        self.name_last_node('op')
        self._cut()
        self._term_()
        self.name_last_node('right')
        self.ast._define(
            ['left', 'op', 'right'],
            []
        )

    @tatsumasu()
    def _division_(self):  # noqa
        self._unary_()
        self.name_last_node('left')
        self._token('/')
        self.name_last_node('op')
        self._cut()
        self._term_()
        self.name_last_node('right')
        self.ast._define(
            ['left', 'op', 'right'],
            []
        )

    @tatsumasu()
    def _unop_(self):  # noqa
        with self._group():
            with self._choice():
                with self._option():
                    self._token('*')
                with self._option():
                    self._token('-')
                with self._option():
                    self._token('+')
                with self._option():
                    self._token('~')
                with self._option():
                    self._token('!')
                with self._option():
                    self._token('--')
                with self._option():
                    self._token('++')
                self._error('expecting one of: ! * + ++ - -- ~')
        self.name_last_node('op')
        self._unary_()
        self.name_last_node('right')
        self.ast._define(
            ['op', 'right'],
            []
        )

    @tatsumasu()
    def _postop_(self):  # noqa
        with self._choice():
            with self._option():
                self._post_wrap_()
                self.name_last_node('left')
                with self._group():
                    with self._choice():
                        with self._option():
                            self._token('++')
                        with self._option():
                            self._token('--')
                        self._error('expecting one of: ++ --')
                self.name_last_node('op')
                self._constant('a')
                self.name_last_node('type')
            with self._option():
                self._post_wrap_()
                self.name_last_node('left')
                self._token('[')
                self._cut()
                self._expression_()
                self.name_last_node('op')
                self._token(']')
                self._constant('b')
                self.name_last_node('type')
            self._error('no available options')
        self.ast._define(
            ['left', 'op', 'type'],
            []
        )

    @tatsumasu()
    def _post_wrap_(self):  # noqa
        with self._choice():
            with self._option():
                self._factor_()
            with self._option():
                self._postop_()
            self._error('no available options')

    @tatsumasu()
    def _unary_(self):  # noqa
        with self._choice():
            with self._option():
                self._post_wrap_()
            with self._option():
                self._unop_()
            self._error('no available options')

    @tatsumasu()
    def _factor_(self):  # noqa
        with self._choice():
            with self._option():
                self._number_()
            with self._option():
                self._subexpression_()
            self._error('no available options')

    @tatsumasu()
    def _subexpression_(self):  # noqa
        self._token('(')
        self._expression_()
        self.name_last_node('@')
        self._token(')')

    @tatsumasu()
    def _number_(self):  # noqa
        self._pattern(r'\d+')


class CalcSemantics(object):
    def start(self, ast):  # noqa
        return ast

    def expression(self, ast):  # noqa
        return ast

    def addition(self, ast):  # noqa
        return ast

    def subtraction(self, ast):  # noqa
        return ast

    def term(self, ast):  # noqa
        return ast

    def multiplication(self, ast):  # noqa
        return ast

    def division(self, ast):  # noqa
        return ast

    def unop(self, ast):  # noqa
        return ast

    def postop(self, ast):  # noqa
        return ast

    def post_wrap(self, ast):  # noqa
        return ast

    def unary(self, ast):  # noqa
        return ast

    def factor(self, ast):  # noqa
        return ast

    def subexpression(self, ast):  # noqa
        return ast

    def number(self, ast):  # noqa
        return ast


def main(filename, startrule, **kwargs):
    with open(filename) as f:
        text = f.read()
    parser = CalcParser()
    return parser.parse(text, startrule, filename=filename, **kwargs)


if __name__ == '__main__':
    import json
    from tatsu.util import asjson

    ast = generic_main(main, CalcParser, name='Calc')
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(asjson(ast), indent=2))
    print()
