﻿using System;
using System.Collections.Generic;
using System.Text;

namespace OldestFamilyMember
{
    class Person
    {
        public Person() { }
        public Person(string name, int age)
        {
            this.Name = name;
            this.Age = age;
        }

        public string Name { get; set; }

        public int Age { get; set; }
    }
}
