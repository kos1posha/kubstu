using System;
using System.Collections.Generic;
using System.Text;

namespace s2_asd_lw_04
{
    class BinaryTree
    {
        public int? Data { get; private set; }
        public BinaryTree Left { get; private set; }
        public BinaryTree Right { get; private set; }
        private bool Dispose = false;
        public BinaryTree() { }
        public BinaryTree(int? data)
        {
            Data = data;
        }
        public BinaryTree(int?[] branches)
        {
            foreach (int? branch in branches) Add(branch);
        }
        public BinaryTree(List<int?> branches)
        {
            foreach (int? branch in branches) Add(branch);
        }
        public void Add(int? data)
        {
            if (Data == null) Data = data;
            else if (Data < data)
            {
                if (Left != null) if (!Left.Dispose)
                        Left.Add(data);
                    else Left = new BinaryTree(data);
                else Left = new BinaryTree(data);
            }
            else if (Data > data)
            {
                if (Right != null) if (!Right.Dispose)
                        Right.Add(data);
                    else Right = new BinaryTree(data);
                else Right = new BinaryTree(data);
            }
            else return;
        }
        public void DelNegLeafs()
        {
            int lr = 0;
            if (Left != null)
                if (!Left.Dispose)
                    Left.DelNegLeafs();
                else lr++;
            else lr++;
            if (Right != null)
                if (!Right.Dispose)
                    Right.DelNegLeafs();
                else lr++;
            else lr++;
            if (lr == 2 && Data < 0)
            {
                Data = null;
                Dispose = true;
            }
        }
        public void Show(string space = "")
        {
            if (Data != null) Console.WriteLine(space + new string(' ', Data >= 0 ? 1 : 0) + Data);
            if (Right != null) Right.Show("<l " + space);
            if (Left != null) Left.Show("<r " + space);
        }
    }
}
