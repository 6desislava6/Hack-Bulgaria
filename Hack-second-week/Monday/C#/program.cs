using System;
using System.Text;

public class HelloWorld
{
    static public void Main ()
    {
        Console.WriteLine ("What is the answer to The Ultimate Question of Life, the Universe, and Everything?");
        string num = Console.ReadLine();

        byte[] bytesToEncode = Encoding.UTF8.GetBytes (num);
        string encodedText = Convert.ToBase64String (bytesToEncode);

        Console.WriteLine("Now let's see if you gave me the right answer!");
        Console.WriteLine(encodedText);
    }

}
