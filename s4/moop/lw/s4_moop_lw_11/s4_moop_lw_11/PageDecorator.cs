using System;

namespace s4_moop_lw_11
{
    public abstract class PageDecorator : IPageProvider
    {
        protected readonly IPageProvider _instance;
        protected PageDecorator(IPageProvider instance) => _instance = instance;
        public virtual void Print() => Console.WriteLine(Content());
        public virtual string Content() => _instance.Content();
    }
}