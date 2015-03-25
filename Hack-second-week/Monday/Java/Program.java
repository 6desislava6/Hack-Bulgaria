public class Program
{
  public static void main(String[] args)
  {
    if(args.length >= 2)
    {
        System.out.println("Okay, okay");
        System.out.println("Here is the answer:");
        System.out.println(new StringBuilder("gnimmargorp detneiro tcejbo").reverse().toString());
    } else {
        System.out.println("Hi there!");
        System.out.println("To get the answer from me, you should call me with atleast two arguments.!");
        System.out.println("Because I say so.");
    }
  }
}
