using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Virtue.EVM.Lab5._1
{
    class Program
    {
        static Queue<CPTask> qsp = new Queue<CPTask>();
        class CPTask
        {
            public double TimeTask;
            public int TypeTask;
            public CPTask(double timeTask, int typeTask)
            {
                this.TimeTask = timeTask;
                this.TypeTask = typeTask;
            }
        }
        static double ModelWithCommonMemory(Queue<CPTask> tasks, int processors, int controlTask)
        {
            Queue<CPTask> copiesTasks = new Queue<CPTask>(tasks);
            double[] workingProcessors = new double[processors];
            CPTask currentTask = null;
            double minimalTask = 0;
            int taskDone = 0;
            int controlProcessor = 0;
            double totalTime = 0;
            double controlTime = 0;
            while (copiesTasks.Count != 0)
            {
                totalTime += minimalTask;
                for (int i = 0; i < processors; ++i)
                {
                    if (workingProcessors[i] == 0)
                    {
                        ++taskDone;
                        if (taskDone == controlTask)
                        {
                            controlProcessor = i;
                        }
                        currentTask = copiesTasks.Dequeue();
                        workingProcessors[i] = currentTask.TimeTask;
                    }
                    else
                    {
                        workingProcessors[i] -= minimalTask;
                    }
                    if (taskDone >= controlTask && i == controlProcessor && workingProcessors[i] == 0) //проеверка на выполнение контрольной
                    {
                        controlTime = totalTime;
                    }
                }
                minimalTask = workingProcessors.Min();
                if (minimalTask == 0)
                {
                    double[] temp = new double[processors];
                    workingProcessors.CopyTo(temp, 0);
                    Array.Sort(temp);
                    for (int j = 0; j < processors; ++j)
                    {
                        if (temp[j] > 0)
                        {
                            minimalTask = temp[j];
                            break;
                        }
                    }
                }
            }
            return controlTime;
        }




        /// <summary>
        ///
        /// </summary>

        static int procCount = 5; //количество процессоров
        static int[] procs = new int[procCount]; //массив длин задач на процессорах
        static Queue<int>[] qs = new Queue<int>[procCount]; //массив очередей для каждого процессора
        static Random rnd = new Random();
        static void AddSomeWork()
        {
            //вероятность прихода заявки 2/3.
            //если заявка не пришла, сразу же выходим
            if (rnd.Next(3) == 0) return;
            //генерируем длительность заявки и ее тип
            int work = rnd.Next(1, 10);
            int type = rnd.Next(procCount);
            Console.WriteLine("Принята заявка длиной {0}", work);
            //если процессор данного типа не занят,
            //сразу кидаем на него эту заявку
            //иначе просто ставим ее в очередь к этому процессору
            CPTask cp = new CPTask(work, type);
            qsp.Enqueue(cp);
            if (procs[type] <= 0)
            {
                procs[type] = work;
                Console.WriteLine("Отправлена на процессор {0}", type);
            }
            else
            {
                Console.WriteLine("Поставлена в очередь к процессору {0}", type);
                qs[type].Enqueue(work);
            }
        }
        //проверка на то, что все заявки были обработаны
        static bool AllWorkDone()
        {
            foreach (Queue<int> q in qs) if (q.Count != 0) return false;
            foreach (int proc in procs) if (proc > 0) return false;
            return true;
        }
        static void Main(string[] args)
        {
            for (int i = 0; i < procCount; i++)
            {
                procs[i] = 0;
                qs[i] = new Queue<int>();
            }
            int ticks;
            //для начала сгенерируем некоторое количество работы
            for (int i = 0; i < 10; i++) AddSomeWork();
            //ждем окончания обработки всех заявок
            for (ticks = 0; !AllWorkDone(); ticks++)
            {
                //моделируем случайное событие прихода случайной заявки
                AddSomeWork();
                for (int i = 0; i < procCount; i++)
                {
                    //если процессор занят задачей,
                    //отнимаем от времени ее выполнения единицу.
                    //и тут же проверяем, не выполнилась ли задача
                    if (procs[i] != -1 && --procs[i] == 0)
                    {
                        //добавляем задачу из очереди, если еще остались
                        if (qs[i].Count() != 0) procs[i] = qs[i].Dequeue();
                        //отключаем процессор, очередь закончилась.
                        else procs[i] = -1;
                    }
                }
            }
            Console.WriteLine("Время работы модели МПС с индивидуальной памятью: {0}", ticks);
            Console.WriteLine("Время работы модели МПС с общей памятью: " + ModelWithCommonMemory(qsp, 5, 10));
            Console.ReadKey();
        }
    }
}