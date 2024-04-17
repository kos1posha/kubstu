using System;
using System.Collections.Generic;
using System.Linq;

namespace s4_moop_lw_11
{
    public class Page : IPageProvider
    {
        private List<string> _text;
        public Page(string text = "") => _text = text.Split('\n').ToList();
        public void Print() => Console.WriteLine(Content());
        public string Content() => string.Join("\n", _text);
    }
}