using System;

namespace s1_prog_cw_02
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.Write("Введите число: "); string strx = Console.ReadLine(); Console.Write("\n");
            string output = "Число в словесном виде записывается как", erl;
            double x = double.Parse(strx), ipx = Math.Floor(x), fpx = 0;
            if (x < 0) output += " минус";
            x = Math.Abs(double.Parse(strx)) - 1;
            bool des = false, last1 = false, ipx0 = false, fpx0 = false;
            int rankend = 0, numb = 0;
            if (x % 1 > 0) fpx = double.Parse(x.ToString().Split(',')[1]);
            string stripx = Convert.ToString(ipx), strfpx = Convert.ToString(fpx);
            List<string> ranklist = new List<string>();
            if (Math.Abs(x) > 999999999999.9999) { output = "Программа ограничена промежутком от 999 999 999 999,9 999 до -999 999 999 999,9 999. Перезапустите программу и введите другое число."; Console.WriteLine(output); Environment.Exit(0); }
            if ((ipx == 0) && (fpx > 0)) { output = "Число в словесном виде записывается как нуль"; ipx0 = true; }
            if (fpx == 0) fpx0 = true;
            switch (strx)
            {
                case "0": output = "Число в словесном виде записывается как нуль."; Console.WriteLine(output); Environment.Exit(0); break;
                case "0,0": output = "Число в словесном виде записывается как нуль."; Console.WriteLine(output); Environment.Exit(0); break;
                case "-0": output = "Минус нуль? \nСерьёзно? \nТы либо совсем дурачок, либо перед тобой создатель проги понтуется тем, что учел даже такую упоротую фигню. \nДва клоуна..."; Console.WriteLine(output); Environment.Exit(0); break;
                case "-0,0": output = "Минус нуль? \nСерьёзно? \nТы либо совсем дурачок, либо перед тобой создатель проги понтуется тем, что учел даже такую упоротую фигню. \nДва клоуна..."; Console.WriteLine(output); Environment.Exit(0); break;
                case "42": output = "Ответ на главный вопрос жизни, вселенной и всего такого."; Console.WriteLine(output); Environment.Exit(0); break;
                case "69": output = "Noice"; Console.WriteLine(output); Environment.Exit(0); break;
                case "420": output = "Самое время курить травку."; Console.WriteLine(output); Environment.Exit(0); break;
                case "6390": output = "Пароль от моего сердца."; Console.WriteLine(output); Environment.Exit(0); break;
            }
            if (x < 0) { output += " минус"; x = Math.Abs(x); strx = Convert.ToString(Math.Abs(x)); }
            if (x % 1 > 0) { var s = x.ToString().Split(',')[1]; fpx = double.Parse(s); }
            if (ipx0 != true)
            {
                for (; stripx.Length < 12;) stripx = $"0{stripx}";
                for (int i = 0; i <= 9; i += 3) { erl = ""; erl += stripx[i]; erl += stripx[i + 1]; erl += stripx[i + 2]; ranklist.Add(erl); }
                for (int i = 0; i < ranklist.Count; i++)
                {
                    erl = (string)ranklist[i];
                    if (erl == "000") continue;
                    switch (erl[0])
                    {
                        case '1': output += " cто"; rankend = 0; break;
                        case '2': output += " двести"; rankend = 0; break;
                        case '3': output += " триста"; rankend = 0; break;
                        case '4': output += " четыреста"; rankend = 0; break;
                        case '5': output += " пятьсот"; rankend = 0; break;
                        case '6': output += " шестьсот"; rankend = 0; break;
                        case '7': output += " семьсот"; rankend = 0; break;
                        case '8': output += " восемьсот"; rankend = 0; break;
                        case '9': output += " девятьсот"; rankend = 0; break;
                    }
                    switch (erl[1])
                    {
                        case '1':
                            switch (erl[2])
                            {
                                case '0': output += " десять"; rankend = 0; break;
                                case '1': output += " одиннадцать"; rankend = 0; break;
                                case '2': output += " двенадцать"; rankend = 0; break;
                                case '3': output += " тринадцать"; rankend = 0; break;
                                case '4': output += " четырнадцать"; rankend = 0; break;
                                case '5': output += " пятнадцать"; rankend = 0; break;
                                case '6': output += " шестнадцать"; rankend = 0; break;
                                case '7': output += " семнадцать"; rankend = 0; break;
                                case '8': output += " восемнадцать"; rankend = 0; break;
                                case '9': output += " девятнадцать"; rankend = 0; break;
                            }
                            des = true;
                            break;
                        case '2': output += " двадцать"; rankend = 0; break;
                        case '3': output += " тридцать"; rankend = 0; break;
                        case '4': output += " сорок"; rankend = 0; break;
                        case '5': output += " пятьдесят"; rankend = 0; break;
                        case '6': output += " шестьдесят"; rankend = 0; break;
                        case '7': output += " семьдесят"; rankend = 0; break;
                        case '8': output += " восемьдесят"; rankend = 0; break;
                        case '9': output += " девяносто"; rankend = 0; break;
                    }
                    if (des == false)
                        switch (erl[2])
                        {
                            case '1': if ((i == 2) || ((i == 3) && (fpx > 0))) { output += " одна"; if ((i == 3) && (fpx > 0)) last1 = true; rankend = 2; break; } else { output += " один"; rankend = 2; } break;
                            case '2': if ((i == 2) || ((i == 3) && (fpx > 0))) { output += " две"; rankend = 1; } else { output += " два"; rankend = 1; } break;
                            case '3': output += " три"; rankend = 1; break;
                            case '4': output += " четыре"; rankend = 1; break;
                            case '5': output += " пять"; rankend = 0; break;
                            case '6': output += " шесть"; rankend = 0; break;
                            case '7': output += " семь"; rankend = 0; break;
                            case '8': output += " восемь"; rankend = 0; break;
                            case '9': output += " девять"; rankend = 0; break;
                        }
                    switch (i)
                    {
                        case 0: output += " миллиард"; break;
                        case 1: output += " миллион"; break;
                        case 2: output += " тысяч"; break;
                    }
                    if (i < 2)
                        switch (rankend)
                        {
                            case 0: output += "ов"; break;
                            case 1: output += "а"; break;
                        }
                    if (i == 2)
                        switch (rankend)
                        {
                            case 1: output += "и"; break;
                            case 2: output += "а"; break;
                        }
                    rankend = 0;
                    des = false;
                }
            }
            if (fpx0 == true) { output += '.'; Console.WriteLine(output); Environment.Exit(0); }
            else { ranklist.Clear(); if (last1 == false) output += " целых и"; else output += " целая и"; }
            numb = strfpx.Length; last1 = false;
            for (; strfpx.Length < 12;) { strfpx = $"0{strfpx}"; }
            for (int i = 0; i <= 9; i += 3) { erl = ""; erl += strfpx[i]; erl += strfpx[i + 1]; erl += strfpx[i + 2]; ranklist.Add(erl); }
            for (int i = 0; i < ranklist.Count; i++)
            {
                erl = (string)ranklist[i];
                if (erl == "000") continue;
                switch (erl[0])
                {
                    case '1': output += " cто"; rankend = 0; break;
                    case '2': output += " двести"; rankend = 0; break;
                    case '3': output += " триста"; rankend = 0; break;
                    case '4': output += " четыреста"; rankend = 0; break;
                    case '5': output += " пятьсот"; rankend = 0; break;
                    case '6': output += " шестьсот"; rankend = 0; break;
                    case '7': output += " семьсот"; rankend = 0; break;
                    case '8': output += " восемьсот"; rankend = 0; break;
                    case '9': output += " девятьсот"; rankend = 0; break;
                }
                switch (erl[1])
                {
                    case '1':
                        switch (erl[2])
                        {
                            case '0': output += " десять"; rankend = 0; break;
                            case '1': output += " одиннадцать"; rankend = 0; break;
                            case '2': output += " двенадцать"; rankend = 0; break;
                            case '3': output += " тринадцать"; rankend = 0; break;
                            case '4': output += " четырнадцать"; rankend = 0; break;
                            case '5': output += " пятнадцать"; rankend = 0; break;
                            case '6': output += " шестнадцать"; rankend = 0; break;
                            case '7': output += " семнадцать"; rankend = 0; break;
                            case '8': output += " восемнадцать"; rankend = 0; break;
                            case '9': output += " девятнадцать"; rankend = 0; break;
                        }
                        des = true;
                        break;
                    case '2': output += " двадцать"; rankend = 0; break;
                    case '3': output += " тридцать"; rankend = 0; break;
                    case '4': output += " сорок"; rankend = 0; break;
                    case '5': output += " пятьдесят"; rankend = 0; break;
                    case '6': output += " шестьдесят"; rankend = 0; break;
                    case '7': output += " семьдесят"; rankend = 0; break;
                    case '8': output += " восемьдесят"; rankend = 0; break;
                    case '9': output += " девяносто"; rankend = 0; break;
                }
                if (des == false)
                    switch (erl[2])
                    {
                        case '1': if ((i == 2) || (i == 3)) { output += " одна"; if (i == 3) last1 = true; rankend = 2; } else { output += " один"; rankend = 2; } break;
                        case '2': if ((i == 2) || (i == 3)) { output += " две"; rankend = 1; } else { output += " два"; rankend = 1; } break;
                        case '3': output += " три"; rankend = 1; break;
                        case '4': output += " четыре"; rankend = 1; break;
                        case '5': output += " пять"; rankend = 0; break;
                        case '6': output += " шесть"; rankend = 0; break;
                        case '7': output += " семь"; rankend = 0; break;
                        case '8': output += " восемь"; rankend = 0; break;
                        case '9': output += " девять"; rankend = 0; break;
                    }
                switch (i)
                {
                    case 0: output += " миллиард"; break;
                    case 1: output += " миллион"; break;
                    case 2: output += " тысяч"; break;
                }
                if (i < 2)
                    switch (rankend)
                    {
                        case 0: output += "ов"; break;
                        case 1: output += "а"; break;
                    }
                if (i == 2)
                    switch (rankend)
                    {
                        case 1: output += "и"; break;
                        case 2: output += "а"; break;
                    }
                rankend = 0;
                des = false;
            }
            switch (numb)
            {
                case 1: output += " десят"; break;
                case 2: output += " сот"; break;
                case 3: output += " тысячн"; break;
                case 4: output += " десятитысячн"; break;
                case 5: output += " стотысячн"; break;
                case 6: output += " миллионн"; break;
                case 7: output += " десятимиллионн"; break;
                case 8: output += " стомиллионн"; break;
                case 9: output += " миллиардн"; break;
                case 10: output += " десятимиллиардн"; break;
                case 11: output += " стомиллиардн"; break;
                case 12: output += " триллионн"; break;
            }
            switch (last1)
            {
                case false: output += "ых."; break;
                case true: output += "ая."; break;
            }
            Console.WriteLine(output);
        }
    }
}
