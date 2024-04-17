using System;
using System.Collections.Generic;

namespace s2_asd_lw_01_04
{
    class Deque
    {
        private Stack<int> Front = new Stack<int>();
        private Stack<int> Back = new Stack<int>();
        private Stack<int> GetFrontRev()
        {
            Stack<int> frontMid = new Stack<int>();
            Stack<int> front = new Stack<int>();
            while (Front.Count > 0)
            {
                frontMid.Push(Front.Peek());
                front.Push(Front.Pop());
            }
            while (front.Count > 0) Front.Push(front.Pop());
            return frontMid;
        }
        private Stack<int> FrontRev => GetFrontRev();
        private Stack<int> GetBackRev()
        {
            Stack<int> backMid = new Stack<int>();
            Stack<int> back = new Stack<int>();
            while (Front.Count > 0)
            {
                backMid.Push(Back.Peek());
                back.Push(Back.Pop());
            }
            while (back.Count > 0) Back.Push(back.Pop());
            return backMid;
        }
        private Stack<int> BackRev => GetBackRev();
        public bool Empty => ((Front.Count == 0) && (Back.Count == 0));
        public int FrontPop()
        {
            if (Empty) throw new Exception("Exception: Stack is empty.");
            if (Front.Count != 0) return Front.Pop();
            return BackRev.Pop();
        }
        public int BackPop()
        {
            if (Empty) throw new Exception("Exception: Stack is empty.");
            if (Back.Count != 0) return Back.Pop();
            return FrontRev.Pop();
        }
        public void FrontPush(int frontPush)
        {
            Front.Push(frontPush);
        }
        public void BackPush(int backPush)
        {
            Back.Push(backPush);
        }
        public int FrontPeek()
        {
            if (Empty) throw new Exception("Exception: Stack is empty.");
            if (Front.Count != 0) return Front.Peek();
            return BackRev.Peek();
        }
        public int BackPeek()
        {
            if (Empty) throw new Exception("Exception: Stack is empty.");
            if (Back.Count != 0) return Back.Peek();
            return FrontRev.Peek();
        }
        public void Clear()
        {
            Front.Clear();
            Back.Clear();
        }
    }
}
