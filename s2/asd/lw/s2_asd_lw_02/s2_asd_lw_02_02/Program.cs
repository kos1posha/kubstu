using System;

namespace s2_asd_lw_02_02
{
    class Program
    {
        static void Main(string[] args)
        {

            int[] unpuckedDeck = new int[10] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            Random r = new Random();
            for (int i = unpuckedDeck.Length - 1; i >= 1; i--)
            {
                int j = r.Next(i + 1);
                int temp = unpuckedDeck[j];
                unpuckedDeck[j] = unpuckedDeck[i];
                unpuckedDeck[i] = temp;
            }
            AltQueue deck = new AltQueue(unpuckedDeck), firstPlayer = new AltQueue(), secondPlayer = new AltQueue();
            while (deck.Length > 0)
            {
                switch (r.Next(2))
                {
                    case 0:
                        if (firstPlayer.Length != 5) firstPlayer.Add(deck.Get());
                        else secondPlayer.Add(deck.Get());
                        break;
                    case 1:
                        if (secondPlayer.Length != 5) secondPlayer.Add(deck.Get());
                        else firstPlayer.Add(deck.Get());
                        break;
                }
            }
            //deck.Show(); Console.WriteLine(); firstPlayer.Show(); Console.WriteLine(); secondPlayer.Show();
            int turn = 1;
            while ((firstPlayer.Length > 0) && (secondPlayer.Length > 0))
            {
                Console.WriteLine($"{turn}) fP: [{firstPlayer.Peek}] sP: [{secondPlayer.Peek}]");
                turn++;
                if ((firstPlayer.Peek == 0) && (secondPlayer.Peek == 9))
                {
                    Console.WriteLine("fP > sP");
                    firstPlayer.Add(secondPlayer.Get());
                    firstPlayer.Add(firstPlayer.Get());
                    continue;
                }
                if ((firstPlayer.Peek == 9) && (secondPlayer.Peek == 0))
                {
                    Console.WriteLine("fP < sP");
                    secondPlayer.Add(firstPlayer.Get());
                    secondPlayer.Add(secondPlayer.Get());
                    continue;
                }
                if (firstPlayer.Peek > secondPlayer.Peek)
                {
                    Console.WriteLine("fP > sP");
                    firstPlayer.Add(secondPlayer.Get());
                    firstPlayer.Add(firstPlayer.Get());
                }
                else
                {
                    Console.WriteLine("fP < sP");
                    secondPlayer.Add(firstPlayer.Get());
                    secondPlayer.Add(secondPlayer.Get());
                }
                Console.Write($"fP: "); firstPlayer.Show(); Console.WriteLine();
                Console.Write($"sP: "); secondPlayer.Show(); Console.WriteLine();
            }
        }
    }
}
