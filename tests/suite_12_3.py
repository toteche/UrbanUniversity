import unittest
import RunnerTest
import TournamentTest

calcST = unittest.TestSuite()

calcST.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
calcST.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentCorrectnessTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)

if __name__ == '__main__':
    unittest.main()