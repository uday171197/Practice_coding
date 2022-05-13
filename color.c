/*
Question 8: Graph Coloring

Write a function to count the number of solutions of the coloring problem with V regions and m
colors. You should use the global variable "count" in the template file for this purpose.

int graphColoring(int** graph, int m, int* color, int v)

You may need to create and initialize the memory for this question.

///////////////////////////////////////////////////////////////////////////////////////////////

Sample Input:

3
4
0 1 1 1
1 0 1 0
1 1 0 1
1 0 1 0

///////////////////////////////////////////////////////////////////////////////////////////////

Sample Output:

Enter number of colors:
Enter number of regions:
Input the adjacency matrix:
There is/are total 6 solution(s)

///////////////////////////////////////////////////////////////////////////////////////////////
*/

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of vertices in the graph
int count = 0; // count the number of solutions
int V;         // number of regions

/* A utility function to print solution */
void printSolution(int *color)
{
    printf(
        "Solution Exists:"
        " Following are the assigned colors \n");
    for (int i = 0; i < V; i++)
        printf(" %d ", color[i]);
    printf("\n");
}

/*  A utility function to check if
    the current color assignment
    is dafe for vertex v i.e. checks
    whether the edge exists or not
*/
int isSafe(int v, int *graph, int *color, int c)
{
    for (int i = 0; i < V; i++)
        if (graph[v][i] && c == color[i])
            return 0;
    return 1;
}

/* A recursive utility function to solve m coloring problem */
int graphColoringUtil(int **graph, int m, int *color, int v)
{
    /* base case: If all vertices are assigned a color then
       return 1 */
    printf("%d", V);
    if (v == V)
        return 1;

    /* Consider this vertex v and try different colors */
    for (int c = 1; c <= m; c++)
    {
        /* Check if assignment of color c to v is fine*/
        if (isSafe(v, graph, color, c))
        {
            color[v] = c;

            /* recur to assign colors to rest of the vertices */
            if (graphColoringUtil(graph, m, color, v + 1) == 1)
                return 1;

            /* If assigning color c doesn't lead to a solution
               then remove it */
            color[v] = 0;
        }
    }

    /* If no color can be assigned to this vertex then return 0 */
    return 0;
}

/* This function solves the m Coloring problem using Backtracking.
  It mainly uses graphColoringUtil() to solve the problem. It returns
  0 if the m colors cannot be assigned, otherwise return 1 and
  prints assignments of colors to all vertices. Please note that there
  may be more than one solutions, this function prints one of the
  feasible solutions.*/
int graphColoring(int **graph, int m)
{
    // Initialize all color values as 0. This initialization is needed
    // correct functioning of isSafe()
    int color[V];
    for (int i = 0; i < V; i++)
        color[i] = 0;

    // Call graphColoringUtil() for vertex 0
    if (graphColoringUtil(graph, m, color, 0) == 0)
    {
        printf("Solution does not exist");
        return 0;
    }

    // Print the solution
    printSolution(color);
    return 1;
}


int main()
{
    /* Create following graph and test whether it is 3 colorable
      (3)---(2)
       |   / |
       |  /  |
       | /   |
      (0)---(1)
    */

   int m;
   int **graph;
   printf("Enter number of colors: \n");
   scanf("%d", &m);

   printf("Enter number of regions: \n");
   scanf("%d", &V);

    (*graph)[V] = malloc(sizeof(int[V][V]));

    

    printf("Input the adjacency matrix\n");
    for (int i = 0; i < V; i++)
        for (int j=0; j<V; j++)
            scanf("%d", &graph[i][j]);

    graphColoring(graph, m);
    return 0;
}