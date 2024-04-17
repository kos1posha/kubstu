using System.Net.Configuration;
using NUnit.Framework;
using s4_moop_lw_10;

namespace s4_moop_lw_10_test
{
    [TestFixture]
    public static class ObserverPatternTest
    {
        [Test]
        public static void UpdateHumanLocation()
        {
            Human human = new Human();
            human.Update(Location.Hall);

            Location expected = Location.Hall;
            Location actual = human.Location;
            
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public static void UpdateHumanAction()
        {
            Human human = new Human();
            human.Update(Action.CleansParrotCell);

            Action expected = Action.CleansParrotCell;
            Action actual = human.Action;
            
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public static void SubscribeCat()
        {
            Human human = new Human();
            Cat cat = new Cat();
            human.Subscribe(cat);

            string expectedReaction = "1 Чувствует единение со своим человеком от факта совместного ничегонеделания.\n";
            string actualReaction = human.Update(Action.Nothing);
            Action expectedAction = Action.Nothing;
            Action actualAction = cat.Action;
            
            Assert.AreEqual(expectedReaction, actualReaction);
            Assert.AreEqual(expectedAction, actualAction);
        }

        [Test]
        public static void SubscribeDog()
        {
            Human human = new Human();
            Dog dog = new Dog();
            human.Subscribe(dog);

            string expectedReaction = "2 Скучает.\n";
            string actualReaction = human.Update(Action.Nothing);
            Action expectedAction = Action.Nothing;
            Action actualAction = dog.Action;
            
            Assert.AreEqual(expectedReaction, actualReaction);
            Assert.AreEqual(expectedAction, actualAction);
        }

        [Test]
        public static void SubscribeCarrot()
        {
            Human human = new Human();
            Carrot carrot = new Carrot();
            human.Subscribe(carrot);

            string expectedReaction = "3 ...\n";
            string actualReaction = human.Update(Action.Nothing);
            Action expectedAction = Action.SaysBadWords;
            Action actualAction = carrot.Action;
            
            Assert.AreEqual(expectedReaction, actualReaction);
            Assert.AreEqual(expectedAction, actualAction);
        }

        [Test]
        public static void SubscribeAll()
        {
            Human human = new Human();
            Cat cat = new Cat();
            human.Subscribe(cat);
            Dog dog = new Dog();
            human.Subscribe(dog);
            Carrot carrot = new Carrot();
            human.Subscribe(carrot);

            string expectedReaction = "1 Чувствует единение со своим человеком от факта совместного ничегонеделания.\n" + 
                                      "2 Скучает.\n" + 
                                      "3 ...\n";
            string actualReaction = human.Update(Action.Nothing);

            Assert.AreEqual(expectedReaction, actualReaction);
        }
    }
}