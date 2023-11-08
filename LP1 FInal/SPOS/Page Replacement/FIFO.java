
import java.io.*;
import java.util.Scanner;
public class FIFO {

    public static void main(String[] args) throws IOException 
    {
        Scanner sc = new Scanner(System.in);
        int frames, pointer = 0, hit = 0, fault = 0,ref_len;
        int buffer[];
        int reference[];
        int mem_layout[][];
        
        System.out.println("Enter the number of Frames: ");
        frames = sc.nextInt();
        
        System.out.println("Enter the length of the Reference string: ");
        ref_len = sc.nextInt();
        
        reference = new int[ref_len];
        mem_layout = new int[ref_len][frames];
        buffer = new int[frames];
        for(int j = 0; j < frames; j++)
                buffer[j] = -1;
        
        System.out.println("Enter the reference string: ");
        for(int i = 0; i < ref_len; i++)
        {
            reference[i] = sc.nextInt();
        }
        System.out.println();
        for(int i = 0; i < ref_len; i++)
        {
         int search = -1;
         for(int j = 0; j < frames; j++)
         {
          if(buffer[j] == reference[i])
          {
           search = j;
           hit++;
           break;
          } 
         }
         if(search == -1)
         {
          buffer[pointer] = reference[i];
          fault++;
          pointer++;
          if(pointer == frames)
           pointer = 0;
         }
            for(int j = 0; j < frames; j++)
                mem_layout[i][j] = buffer[j];
        }
        
        for(int i = 0; i < frames; i++)
        {
            for(int j = 0; j < ref_len; j++)
                System.out.printf("%3d ",mem_layout[j][i]);
            System.out.println();
        }
        
        System.out.println("The number of Hits: " + hit);
        System.out.println("Hit Ratio: " + (float)((float)hit/ref_len) * 100+" %");
        System.out.println("The number of Faults: " + fault);

        sc.close();
    }
    
}