/* 2D Environment Simulator - Env2d.cpp
   Author: Prof. Joao Alberto Fabro - UTFPR - Curitiba - PR - Brazil
   e-mail: fabro at utfpr.edu.br
   Course: Intelligent Systems - CSI30
   Version 1.0 - 20/03/2019
   
---------------HOW TO COMPILE AND EXECUTE ---------------------------------
   Compiling instructions: $ g++ Env2d.cpp -o Env2d
   In order to execute:    $ ./Env2d

---------------HOW TO SPECIFY THE ENVIRONMENT -----------------------------
   It is necessary to have a file "Env.txt" in the same folder, with the following structure:
   - First Line: a single integer, representing the number of rows(n_rows) of the environment;
   - Second Line: a single integer, representing the number of columns(n_cols) of the environment;
   - A sequence of 'n_rows' lines, each with 'n_cols' symbols from:
	- Character '.' representing free positions in the grid;
	- Character '*' representing positions in the grid with obstacles;
	- Character 'x' representing the 'goal' position of the 'robot';
	- One of the following characters, representing the robot's initial position and orientation:
			- Character '>' if the robot is facing EAST;
			- Character '^' if the robot is facing NORTH;
			- Character '<' if the robot is facing WEST;
			- Character 'v' if the robot is facing SOUTH;

-------------- HOW TO USE THE PROGRAM -------------------------------
Use the keyboard to control the movements of the 'robot':
	- key 'w' or 'W' to order the robot to "go forward";
	- key 'a' or 'A' to order the robot to "turn counterclockwise 45 degrees";
	- key 'd' or 'D' to order the robot to "turn clockwise 45 degrees";
*/


#include <stdio.h>
#include <termios.h>
#include <unistd.h>
#include <fcntl.h>
 
#define ROBOT       26
#define WALL        27
#define TARGET	    28
#define NONE        -1
 
#define MAX_ROWS    20
#define MAX_COLS    20
 
#define EAST		0
#define NORTHEAST	1
#define NORTH		2
#define NORTHWEST       3
#define WEST		4
#define SOUTHWEST       5
#define SOUTH		6
#define SOUTHEAST	7

#define CLOCKWISE    100
#define COUNTERCLOCK 101

int kbhit(void);

class Robot {
  public:
    int getX() { return locX; }
    int getY() { return locY; }
    int getFacing() { return facing; }
    void setFacing(int f) { facing = f; }
    void setLocation(int x, int y){locX=x;locY=y;};
    int move(int direction){
	if(direction==EAST) 	       locY++;
	else if(direction==SOUTHEAST) {locY++;locX++;}
	else if(direction==WEST)       locY--;
	else if(direction==SOUTHWEST) {locY--;locX++;}
	else if(direction==SOUTH)             locX++;
	else if(direction==NORTHWEST) {locY--;locX--;}
	else if(direction==NORTH)             locX--;
	else if(direction==NORTHEAST) {locY++;locX--;}
	};
    void print_state()
	{
		printf("Robot position: X=%d, Y=%d, facing:",locX, locY);
		if(facing==NORTH) 	printf(" NORTH\n");
		if(facing==EAST) 	printf(" EAST\n");
		if(facing==SOUTH) 	printf(" SOUTH\n");
		if(facing==WEST) 	printf(" WEST\n");
		if(facing==NORTHEAST) 	printf(" NORTHEAST\n");
		if(facing==NORTHWEST) 	printf(" NORTHWEST\n");
		if(facing==SOUTHEAST) 	printf(" SOUTHEAST\n");
		if(facing==SOUTHWEST) 	printf(" SOUTHWEST\n");
        };

  private:
    int locX;
    int locY;
    int facing;
};


class Environment {
 private:
    int n_rows, n_cols;
    int Matrix[MAX_ROWS][MAX_COLS];
 public: 
    void scan_state();
    void scan_state_from_file();
    void print_state();
    void move_robot(int direction);
    void rotate_robot(int clock_or_counterclock_90_degrees);
};

  Environment Env1; 
  Robot Rob1; 

int main( void )
{ char ch; int a;

  // scan the state of the environment
  Env1.scan_state_from_file();
 
  // print the state of the environment
  Env1.print_state();


  printf("Use the arrow keys or : w(go ahead), a(turn counterclockwise), d(turn clockwise), q(quit):\n");
  while(1)
  {a=kbhit();
   if(a!=0)
   { 
   ch = getchar();
//   printf("Command=%d\n",ch);

   // ch== 119 means 'w', ch == 87 means 'W'
   if((ch==119) || (ch==87)) Env1.move_robot(Rob1.getFacing());

   // ch== 97 means 'a', ch == 65 means 'A'
   if((ch==97) || (ch==65))Env1.rotate_robot(COUNTERCLOCK);

   // ch== 100 means 'd', ch == 68 means 'D'
   if((ch==100) || (ch==68))Env1.rotate_robot(CLOCKWISE);

   if (ch == '\033') { // if the first value is esc
    getchar(); // skip the [
    switch(getchar()) { // the real value
        case 'A':
            // code for arrow up
	    Env1.move_robot(Rob1.getFacing());
            break;
//        case 'B':
            // code for arrow down
//            break;
        case 'C':
            // code for arrow right
	    Env1.rotate_robot(CLOCKWISE);
            break;
        case 'D':
            // code for arrow left
	    Env1.rotate_robot(COUNTERCLOCK);
            break;
    } //end of switch(getchar())
   } //end of if (ch == '\033')

   // ch== 113 means 'q', ch == 81 means 'Q', to QUIT
   if((ch==113)||(ch==81)) break;
   Env1.print_state();
   sleep(0.2);
   } // end of if(a!=0)
 } // end of while(1)

/*  Env1.rotate_robot(CLOCKWISE);
 
  Env1.print_state();
  
  Env1.move_robot(SOUTH);
  Env1.move_robot(SOUTH);
  Env1.rotate_robot(COUNTERCLOCK);
  Env1.move_robot(EAST);
 
  Env1.print_state();

  Env1.move_robot(EAST);
 
  Env1.print_state();
  Env1.move_robot(EAST);
 
  Env1.print_state();
  Env1.move_robot(EAST);
 
  Env1.print_state();
  Env1.move_robot(EAST);
 
  Env1.print_state();
  Env1.move_robot(EAST);
 
  Env1.print_state();

  Env1.move_robot(EAST);
 
  Env1.print_state();
  Env1.move_robot(SOUTH);
 
  Env1.print_state();

  ch=getchar();
*/
  return 0;
}


void Environment::scan_state_from_file()
{
int r,c;
char url[]="Env.txt";
char ch;
FILE *arq;
	
arq = fopen(url, "r");
if(arq == NULL)
    printf("Error, it is not possible to open the Env.txt file!\n");
fscanf(arq, "%d\n", &n_rows);
fscanf(arq, "%d\n", &n_cols);
for(r=0;r<n_rows;r++)
	{
    	for(c=0;c<n_cols;c++)
    	{ 
    		ch=fgetc(arq);
	 //     printf("%d,%d = %c\t",r,c,ch);
		if ( ch == '*' ) {
			Matrix[r][c] = WALL;
     			}
		else if ( ch == 'x' ) {
			Matrix[r][c] = TARGET;
     			}
		else if ( ch == '^' ) {
			Matrix [r][c] = ROBOT;
			Rob1.setLocation(r,c);
			Rob1.setFacing(NORTH);
			}
		else if ( ch == '>' ) {
			Matrix [r][c] = ROBOT;
			Rob1.setLocation(r,c);
			Rob1.setFacing(EAST);
     			}
		else if ( ch == 'v' ) {
			Matrix [r][c] = ROBOT;
			Rob1.setLocation(r,c);
			Rob1.setFacing(SOUTH);
			}
		else if ( ch == '<' ) {
			Matrix [r][c] = ROBOT;
			Rob1.setLocation(r,c);
			Rob1.setFacing(WEST);
			}
		else {
			Matrix [r][c] = NONE;
			}//end of if...else
		}//end of for(c)
	fscanf(arq,"\n");// to cath the new line
	}//end of for(r)
fclose(arq);
}	
 
void Environment::scan_state()
{
  int ch;
  int r,c;
 
  
  printf("Number of Lines:");
  scanf("%d\n", &n_rows);
  printf("Number of Columns:");
  scanf("%d\n", &n_cols);
  for(r=0;r<n_rows;r++)
   {
    for(c=0;c<n_cols;c++)
    { 
    
     ch=getchar();
//     printf("%d,%d = %c\t",r,c,ch);
     if ( ch == '*' ) {
      Matrix[r][c] = WALL;
     }
     else if ( ch == 'x' ) {
      Matrix[r][c] = TARGET;
     }
     else if ( ch == '^' ) {
      Matrix [r][c] = ROBOT;
      Rob1.setLocation(r,c);
      Rob1.setFacing(NORTH);
     }
     else if ( ch == '>' ) {
      Matrix [r][c] = ROBOT;
      Rob1.setLocation(r,c);
      Rob1.setFacing(EAST);
     }
     else if ( ch == 'v' ) {
      Matrix [r][c] = ROBOT;
      Rob1.setLocation(r,c);
      Rob1.setFacing(SOUTH);
     }
     else if ( ch == '<' ) {
      Matrix [r][c] = ROBOT;
      Rob1.setLocation(r,c);
      Rob1.setFacing(WEST);
     }
     else {
      Matrix [r][c] = NONE;
     }//end of if...else
    }//end of for(c)
    scanf("\n");// to cath the new line
   }//end of for(r)
}
 
 
void Environment::print_state()
{

int r,c;
 printf("    ");
 for(int i=0;i<n_cols;i++) 
   printf("  %d ",i);
 printf("\n");
 printf("    ");
 for(int i=0;i<n_cols;i++) 
   printf("+---");
 printf("+\n");
 for( r=0; r < n_rows ; r++ ) 
 {
 printf("  %d ",r);
   for( c=0; c < n_cols; c++ ) {
      if (Matrix[r][c] == WALL) 
       {
        printf( "|***" );
       }

      if (Matrix[r][c] == TARGET) 
       {
        printf( "| X " );
       }

      if (Matrix[r][c] == NONE) 
       {
        printf( "|   " );
       }

      if ( Matrix[r][c] == ROBOT ) 
       {
        if (Rob1.getFacing() == NORTH) 
        {
          printf("| ^ ");
        }
        else if (Rob1.getFacing() == NORTHEAST) 
        {
          printf("| / ");
        }
        else if (Rob1.getFacing() == EAST) 
        {
          printf("| > ");
        }
        else if (Rob1.getFacing() == SOUTHEAST) 
        {
          printf("| \\ ");
        }
        else if (Rob1.getFacing() == SOUTH) 
        {
          printf("| v ");
        }
        else if (Rob1.getFacing() == SOUTHWEST) 
        {
          printf("| %% ");
        }
        else if (Rob1.getFacing() == WEST) 
        {
          printf("| < ");
        }        
	else if (Rob1.getFacing() == NORTHWEST) 
        {
          printf("| # ");
        }//end of if(Rob1...)else
      }//end of if(Matrix....)
 
   }//end of for(c)
   printf( "|\n" );
   printf("    ");
   for(int i=0;i<n_cols;i++) 
     printf("+---");
   printf("+\n");
 }//end of for(r)
 Rob1.print_state();
}


void Environment::move_robot(int direction)
{
	if ((direction == NORTH) && (Rob1.getFacing() == NORTH) && (Matrix[Rob1.getX()-1][Rob1.getY()]!=WALL) && (Rob1.getX() > 0)) 
	{
		Matrix[Rob1.getX()][Rob1.getY()] = NONE;
		Matrix[Rob1.getX()-1][Rob1.getY()] = ROBOT;
		Rob1.move(NORTH);
	}
	else
	if ((direction == NORTHWEST) && (Rob1.getFacing() == NORTHWEST) && (Matrix[Rob1.getX()-1][Rob1.getY()-1]!=WALL) && (Rob1.getX() > 0) && (Rob1.getY() > 0)) 
	{
		Matrix[Rob1.getX()][Rob1.getY()] = NONE;
		Matrix[Rob1.getX()-1][Rob1.getY()-1] = ROBOT;
		Rob1.move(NORTHWEST);
	}
       else
	if ((direction == SOUTH) && (Rob1.getFacing() == SOUTH) && (Matrix[Rob1.getX()+1][Rob1.getY()]!=WALL) && (Rob1.getX() < n_rows-1)) 
	{
		Matrix[Rob1.getX()][Rob1.getY()] = NONE;
		Matrix[Rob1.getX()+1][Rob1.getY()] = ROBOT;
		Rob1.move(SOUTH);
	}
	else
	if ((direction == SOUTHEAST) && (Rob1.getFacing() == SOUTHEAST) && (Matrix[Rob1.getX()+1][Rob1.getY()+1]!=WALL) && (Rob1.getX() < n_rows-1) && (Rob1.getY() < n_cols-1)) 
	{
		Matrix[Rob1.getX()][Rob1.getY()] = NONE;
		Matrix[Rob1.getX()+1][Rob1.getY()+1] = ROBOT;
		Rob1.move(SOUTHEAST);
	}        
	else
	if ((direction == EAST) && (Rob1.getFacing() == EAST) && (Matrix[Rob1.getX()][Rob1.getY()+1]!=WALL) && (Rob1.getY() < n_cols-1)) 
	{
		Matrix[Rob1.getX()][Rob1.getY()] = NONE;
		Matrix[Rob1.getX()][Rob1.getY()+1] = ROBOT;
		Rob1.move(EAST);
	}
	else
	if ((direction == SOUTHWEST) && (Rob1.getFacing() == SOUTHWEST) && (Matrix[Rob1.getX()+1][Rob1.getY()-1]!=WALL) && (Rob1.getX() < n_rows-1) && (Rob1.getY() >0)) 
	{
		Matrix[Rob1.getX()][Rob1.getY()] = NONE;
		Matrix[Rob1.getX()+1][Rob1.getY()-1] = ROBOT;
		Rob1.move(SOUTHWEST);
	}        
        else
	if ((direction == WEST) && (Rob1.getFacing() == WEST) && (Matrix[Rob1.getX()][Rob1.getY()-1]!=WALL) && (Rob1.getY() > 0)) 
	{
		Matrix[Rob1.getX()][Rob1.getY()] = NONE;
		Matrix[Rob1.getX()][Rob1.getY()-1] = ROBOT;
		Rob1.move(WEST);
	}
	else
	if ((direction == NORTHEAST) && (Rob1.getFacing() == NORTHEAST) && (Matrix[Rob1.getX()-1][Rob1.getY()+1]!=WALL) && (Rob1.getX() >0) && (Rob1.getY() < n_cols-1)) 
	{
		Matrix[Rob1.getX()][Rob1.getY()] = NONE;
		Matrix[Rob1.getX()-1][Rob1.getY()+1] = ROBOT;
		Rob1.move(NORTHEAST);
	} 

}

void Environment::rotate_robot(int clock_or_counterclock_90_degrees)
{
int local_facing;
   if(clock_or_counterclock_90_degrees == CLOCKWISE)
   {
	local_facing = Rob1.getFacing();
	local_facing--;
	if(local_facing<0) local_facing = 7;
	Rob1.setFacing(local_facing);
/*     if(Rob1.getFacing()==SOUTH) Rob1.setFacing(WEST);
     else
     if(Rob1.getFacing()==WEST) Rob1.setFacing(NORTH);
     else
     if(Rob1.getFacing()==NORTH) Rob1.setFacing(EAST);
     else
     if(Rob1.getFacing()==EAST) Rob1.setFacing(SOUTH);
*/   }
   else
   if(clock_or_counterclock_90_degrees == COUNTERCLOCK)
   {
	local_facing = Rob1.getFacing();
	local_facing++;
	if(local_facing>7) local_facing = 0;
	Rob1.setFacing(local_facing);
   }
/*     if(Rob1.getFacing()==SOUTH) Rob1.setFacing(EAST);
     else
     if(Rob1.getFacing()==EAST) Rob1.setFacing(NORTH);
     else
     if(Rob1.getFacing()==NORTH) Rob1.setFacing(WEST);
     else
     if(Rob1.getFacing()==WEST) Rob1.setFacing(SOUTH);
   }
*/}

     
    int kbhit(void)
    {
      struct termios oldt, newt;
      int ch;
      int oldf;
     
      tcgetattr(STDIN_FILENO, &oldt);
      newt = oldt;
      newt.c_lflag &= ~(ICANON | ECHO);
      tcsetattr(STDIN_FILENO, TCSANOW, &newt);
      oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
      fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);
     
      ch = getchar();
     
      tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
      fcntl(STDIN_FILENO, F_SETFL, oldf);
     
      if(ch != EOF)
      {
        ungetc(ch, stdin);
        return 1;
      }
     
      return 0;
    }


