import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String[] roadNodesEdges = scanner.nextLine().split(" ");
        int roadNodes = Integer.parseInt(roadNodesEdges[0].trim());
        int roadEdges = Integer.parseInt(roadNodesEdges[1].trim());

        int[][] dist = new int [roadNodes + 1][roadNodes + 1];
        for(int i =0;i<=roadNodes;i++){
            Arrays.fill(dist[i], Integer.MAX_VALUE);
            dist[i][i] = 0;
        }
        int roadFrom, roadTo, roadWeight;
        for (int i = 0; i < roadEdges; i++) {
            String[] roadFromToWeight = scanner.nextLine().split(" ");
            roadFrom = Integer.parseInt(roadFromToWeight[0].trim());
            roadTo = Integer.parseInt(roadFromToWeight[1].trim());
            roadWeight = Integer.parseInt(roadFromToWeight[2].trim());
            dist[roadFrom][roadTo] = roadWeight;
        }
        
        for (int k=1; k <= roadNodes; k++) {
            for (int i=1; i <= roadNodes; i++) {
                if (dist[i][k] != Integer.MAX_VALUE){
                  for (int j=1; j <= roadNodes; j++) {
                    if (dist[k][j]!= Integer.MAX_VALUE && dist[i][j] > dist[i][k] + dist[k][j]){
                        dist[i][j]  = dist[i][k] + dist[k][j];
                    }
                  }                   
                }

            }
        }

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        
        String s = ""; 
        for (int qItr = 0; qItr < q; qItr++) {
            String[] xy = scanner.nextLine().split(" ");

            int x = Integer.parseInt(xy[0]);

            int y = Integer.parseInt(xy[1]);
            
            int r = dist[x][y];
            if (r == Integer.MAX_VALUE) 
                System.out.println("-1"); 
            else 
                System.out.println(String.valueOf(dist[x][y]));
        }

        scanner.close();
    }
}
