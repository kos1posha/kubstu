using System;

namespace s4_moop_lw_11
{
    internal static class Program
    {
        public static void Sep() => Console.WriteLine("\n----------------------------------\n");

        public static void Main(string[] args)
        {
            IPageProvider page = new Page(
                "Я помню чудное мгновенье:\n" +
                "Передо мной явилась ты,\n" +
                "Как мимолетное виденье,\n" +
                "Как гений чистой красоты.\n" +
                "В томленьях грусти безнадежной,\n" +
                "В тревогах шумной суеты,\n" +
                "Звучал мне долго голос нежный,\n" +
                "И снились милые черты.\n" +
                "Шли годы. Бурь порыв мятежный\n" +
                "Рассеял прежние мечты,\n" +
                "И я забыл твой голос нежный,\n" +
                "Твои небесные черты.\n" +
                "В глуши, во мраке заточенья\n" +
                "Тянулись тихо дни мои\n" +
                "Без божества, без вдохновенья,\n" +
                "Без слез, без жизни, без любви.\n" +
                "Душе настало пробужденье:\n" +
                "И вот опять явилась ты,\n" +
                "Как мимолетное виденье,\n" +
                "Как гений чистой красоты.\n" +
                "И сердце бьется в упоенье,\n" +
                "И для него воскресли вновь\n" +
                "И божество, и вдохновенье,\n" +
                "И жизнь, и слезы, и любовь."
            );

            int[] steps = { 3, 4, 2, 1 };
            foreach (int step in steps)
            {
                switch (step)
                {
                    case 1:
                        page = new TitledPage(
                            instance: page,
                            title: "К ****\n(К Керн)",
                            titleAlignment: Alignment.Center,
                            separated: false
                        );
                        break;
                    case 2:
                        page = new CommentedPage(
                            instance: page,
                            comment: "Автор: А.С. Пушкин\nНаписано: Не позднее 19 июля 1825",
                            commentAlignment: Alignment.Right,
                            separated: true
                        );
                        break;
                    case 3:
                        page = new IndexedPage(
                            instance: page,
                            indexSeparator: IndexSeparator.Parenthesis,
                            indexSpace: 1,
                            blockLength: 1,
                            startOffset: 0,
                            endOffset: 0
                        );
                        break;
                    case 4:
                        page = new BlockedPage(
                            instance: page,
                            blockSeparator: BlockSeparator.Space,
                            blockLength: 4,
                            blockSpace: 1,
                            startOffset: 0,
                            endOffset: 0
                        );
                        break;
                }
                page.Print();
            }
        }
    }
}