using System;

interface ITarget { void Request(); }

class Client
{
    static void Main()
    {
        var target = new ObjectAdapter();
        target.Request();

        var target2 = ClassAdapter.Create();
        
    }
}

class ClassAdapter : Adaptee, ITarget
{
    private ClassAdapter() { }
    public void Request() => Operation();
    public static ITarget Create() => new ClassAdapter();
}

class ObjectAdapter : ITarget
{
    Adaptee adaptee = new Adaptee();
    public void Request() => adaptee.Operation();
}

class Adaptee
{
    public void Operation() => Console.WriteLine("Adaptee.Operation() called");
}