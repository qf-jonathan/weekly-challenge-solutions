from unittest import TestCase, main
from unittest.mock import patch
from solution import solution
from io import StringIO


class TestFizzBuzz(TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_solution(self, m_out):
        solution()
        self.assertEqual(
            m_out.getvalue(),
            (
                "1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\n"
                "fizzbuzz\n16\n17\nfizz\n19\nbuzz\nfizz\n22\n23\nfizz\nbuzz\n26\n"
                "fizz\n28\n29\nfizzbuzz\n31\n32\nfizz\n34\nbuzz\nfizz\n37\n38\n"
                "fizz\nbuzz\n41\nfizz\n43\n44\nfizzbuzz\n46\n47\nfizz\n49\nbuzz\n"
                "fizz\n52\n53\nfizz\nbuzz\n56\nfizz\n58\n59\nfizzbuzz\n61\n62\n"
                "fizz\n64\nbuzz\nfizz\n67\n68\nfizz\nbuzz\n71\nfizz\n73\n74\n"
                "fizzbuzz\n76\n77\nfizz\n79\nbuzz\nfizz\n82\n83\nfizz\nbuzz\n86\n"
                "fizz\n88\n89\nfizzbuzz\n91\n92\nfizz\n94\nbuzz\nfizz\n97\n98\n"
                "fizz\nbuzz\n"
            ),
        )


if __name__ == "__main__":
    main()
