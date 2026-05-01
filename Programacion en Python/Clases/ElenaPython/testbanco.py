#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import bancodef


class TeleBancoTest(unittest.TestCase):
    def test_teleConsulta(self):
        mi_tele_banco = banco.TeleBanco('127.0.0.1', 5000)
        mi_tele_terminal = banco.TeleTerminal('127.0.0.1', 5000)

        mi_tele_terminal.ejecutar_orden("crear Cliente1 123123X CC0987654321 700 3")
        mi_tele_terminal.ejecutar_orden("crear Cliente2 123121X CC0987654322 0 2")

        saldo1 = mi_tele_terminal.ejecutar_orden("consulta CC0987654321")
        saldo2 = mi_tele_terminal.ejecutar_orden("consulta CC0987654322")

        self.assertEqual("700", saldo1)
        self.assertEqual("0", saldo2)


if __name__ == "__main__":
    unittest.main()