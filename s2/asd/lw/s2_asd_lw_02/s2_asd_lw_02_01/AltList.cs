using System;
using System.Collections.Generic;
using System.Text;

namespace s2_asd_lw_02_01
{
    class AltList
    {
        private int[] Body;
        public int Length = 0;
        public AltList() { }
        public AltList(int[] body)
        {
            Body = body;
            Length = body.Length;
        }
        public int GetValue(int index) => Body[index];
        public void Show()
        {
            for (int i = 0; i < Length; i++) Console.WriteLine(GetValue(i));
        }
        public void Add(int value)
        {
            int[] newBody = new int[++Length];
            for (int i = 0; i < Length - 1; i++) newBody[i] = Body[i];
            newBody[Length - 1] = value;
            Body = newBody;
        }
        public void AddTo(int value, int index)
        {
            if (index > Length - 1) throw new Exception("Exception: Index out of range");
            int[] newBody = new int[++Length];
            for (int i = 0; i < index; i++) newBody[i] = Body[i];
            newBody[index++] = value;
            for (int i = index; i < Length; i++) newBody[i] = Body[i - 1];
            Body = newBody;
        }
        public void Remove()
        {
            int[] newBody = new int[--Length];
            for (int i = 0; i < Length; i++) newBody[i] = Body[i];
            Body = newBody;
        }
        public void RemoveTo(int index)
        {
            int[] newBody = new int[--Length];
            for (int i = 0; i < index; i++) newBody[i] = Body[i];
            for (int i = index; i < Length; i++) newBody[i] = Body[i + 1];
            Body = newBody;
        }
    }
}
