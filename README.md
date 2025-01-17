# Python Object-Oriented Programming (OOP)

## OOP Introduction

An introductory overview of Object-Oriented Programming, highlighting its principles (Encapsulation, Abstraction, Inheritance, and Polymorphism) and benefits, such as modularity and code reusability.

### Principles of OOP:

- **Encapsulation**: Encapsulation involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit, usually a class. It also includes restricting direct access to some of an object's components to ensure controlled modification and prevent accidental interference.

- **Abstraction**: Abstraction simplifies complexity by hiding unnecessary implementation details and showing only the essential features of an object. This is often achieved using abstract classes and interfaces.

- **Inheritance**: Inheritance allows a class (child class) to acquire the properties and methods of another class (parent class). It facilitates code reusability and establishes a natural hierarchy between classes.

- **Polymorphism**: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types), often implemented using method overriding or interfaces.

## AbstractClass

This file discusses the concept of Abstract Classes in Object-Oriented Programming. Abstract classes are classes that cannot be instantiated directly. They serve as a blueprint for other classes and typically include one or more abstract methods that must be implemented by derived classes.

## class_Method_Alternative

This file explores class methods and their alternatives. Class methods are methods that operate on the class itself rather than on specific instances. They are defined using the `@classmethod` decorator.

# Python Object-Oriented Programming (OOP)

## AbstractClass.py

This file discusses the concept of Abstract Classes in Object-Oriented Programming. Abstract classes are classes that cannot be instantiated directly. They serve as a blueprint for other classes and typically include one or more abstract methods that must be implemented by derived classes.

## class_Method_Alternative

This file explores class methods and their alternatives. Class methods are methods that operate on the class itself rather than on specific instances. They are defined using the `@classmethod` decorator.

## Inheritance

The file delves into inheritance, a fundamental concept in OOP. Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). Different types of inheritance, such as single, multiple, multilevel, and hierarchical inheritance, are also covered.

### Types of Inheritance:

- **Single Inheritance**: A child class inherits from one parent class. This is the simplest form of inheritance.

  ```python
  class Parent:
      def method(self):
          print("This is a method in the Parent class")

  class Child(Parent):
      pass

  obj = Child()
  obj.method()
  ```

- **Multiple Inheritance**: A child class inherits from more than one parent class. This allows the child class to access attributes and methods of multiple parent classes.

  ```python
  class Parent1:
      def method1(self):
          print("This is a method in Parent1")

  class Parent2:
      def method2(self):
          print("This is a method in Parent2")

  class Child(Parent1, Parent2):
      pass

  obj = Child()
  obj.method1()
  obj.method2()
  ```

- **Multilevel Inheritance**: A child class inherits from a parent class, and another class inherits from this child class, forming a chain.

  ```python
  class Grandparent:
      def method(self):
          print("This is a method in the Grandparent class")

  class Parent(Grandparent):
      pass

  class Child(Parent):
      pass

  obj = Child()
  obj.method()
  ```

- **Hierarchical Inheritance**: Multiple child classes inherit from a single parent class.

  ```python
  class Parent:
      def method(self):
          print("This is a method in the Parent class")

  class Child1(Parent):
      pass

  class Child2(Parent):
      pass

  obj1 = Child1()
  obj2 = Child2()
  obj1.method()
  obj2.method()
  ```

- **Hybrid Inheritance**: A combination of two or more types of inheritance, forming a more complex hierarchy.

  ```python
  class Parent:
      def method(self):
          print("This is a method in the Parent class")

  class Child1(Parent):
      pass

  class Child2(Parent):
      pass

  class Grandchild(Child1, Child2):
      pass

  obj = Grandchild()
  obj.method()
  ```

## Instance and Class Variables

This section explains the difference between instance variables (specific to an object) and class variables (shared across all instances of a class). It demonstrates how to define, access, and modify these variables.

## Method Overriding

Method overriding occurs when a subclass provides a specific implementation of a method already defined in its superclass. This file highlights how to override methods and the importance of doing so in certain scenarios.

## Object Introspection

Object introspection is the ability to examine an object’s properties and methods at runtime. This file covers techniques for introspection, such as using the `type`, `dir`, and `getattr` functions.

## Static Method

Static methods are methods that do not operate on an instance or a class directly. They are defined using the `@staticmethod` decorator. This file describes their use cases and how they differ from class methods.

## Super Keyword

The `super` keyword is used to call methods from a superclass. It is particularly useful in the context of method overriding to ensure the parent class’s method is also executed. This file provides practical examples of the `super` keyword in action.

## Operator Overloading

Operator overloading allows the use of standard operators (e.g., +, -, \*, /) with user-defined classes. This file illustrates how to overload operators by implementing special methods like `__add__`, `__sub__`, and `__mul__`.

## Polymorphism

Polymorphism is the ability of a single interface to represent different data types. This section explains how polymorphism is implemented in Python, including examples with functions and methods.
