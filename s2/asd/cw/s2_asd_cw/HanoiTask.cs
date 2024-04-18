using System;
using System.Collections.Generic;
using System.Text;

namespace s2_asd_cw
{
    class HanoiTask
    {
        int Height;
        public bool Mode;
        public int Turn = 1;
        public bool Done => RightTower.Count == Height;
        Stack<int> LeftTower = new Stack<int>();
        Stack<int> CenterTower = new Stack<int>();
        Stack<int> RightTower = new Stack<int>();
        public HanoiTask(int height, bool mode)
        {
            Height = height;
            Mode = mode;
            for (int i = Height; i > 0; i--)
                LeftTower.Push(i);
        }
        public void View()
        {
            Console.WriteLine();
            Stack<int> left = new Stack<int>(new Stack<int>(LeftTower)),
                       center = new Stack<int>(new Stack<int>(CenterTower)),
                       right = new Stack<int>(new Stack<int>(RightTower));
            for (int i = Height; i > 0; i--)
                Console.WriteLine("  " + RingView(left, i) + RingView(center, i) + RingView(right, i));
        }
        string RingView(Stack<int> tower, int i)
            => tower.Count == i ?
            new string(' ', Height - tower.Peek()) +
            new string('[', tower.Peek() - tower.Peek().ToString().Length + 1) +
            $"{tower.Peek()}" +
            new string(']', tower.Peek()) +
            new string(' ', Height - tower.Pop())
            :
            new string(' ', Height * 2 + 1);
        public int Replace(string replace)
        {
            Stack<int> tower1 = new Stack<int>(), tower2 = new Stack<int>();
            switch (replace[0])
            {
                case '1': tower1 = LeftTower; break;
                case '2': tower1 = CenterTower; break;
                case '3': tower1 = RightTower; break;
                default: return 0;
            }
            switch (replace[1])
            {
                case '1': tower2 = LeftTower; break;
                case '2': tower2 = CenterTower; break;
                case '3': tower2 = RightTower; break;
                default: return 0;
            }
            if (!tower2.TryPeek(out int t2Peek)) t2Peek = 1025;
            if (Mode)
            {
                if (!tower1.TryPeek(out int t1Peek)) return -1;
                if (t1Peek < t2Peek) tower2.Push(tower1.Pop());
                else return -2;
            }
            else
            {
                if (!tower1.TryPeek(out int t1Peek)) { tower1.Push(tower2.Pop()); return 1; }
                if (t1Peek < t2Peek) tower2.Push(tower1.Pop());
                else tower1.Push(tower2.Pop());
            }
            return 1;
        }
    }
}
