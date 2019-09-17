#include <stdio.h>
#include <SDL.h>

SDL_Window *win;
SDL_Renderer *ren;

void drawsquare(double x, double y, double l) {
	SDL_Rect rect = { x, y, l, l }; // x, y, width, height
	SDL_RenderFillRect(ren, &rect);
	SDL_RenderDrawRect(ren, &rect);
	SDL_RenderPresent(ren);
}

/********Add Recursive drawBoxFractal function here*******/

void main(int argc, char *argv[]) {
	if (SDL_Init(SDL_INIT_EVERYTHING) < 0) {
		printf("SDL could not initializeStack");
	}

	SDL_CreateWindowAndRenderer(300, 300, 0, &win, &ren);
	SDL_SetRenderDrawColor(ren, 255, 255, 255, 255);
	SDL_RenderClear(ren);

	SDL_SetRenderDrawColor(ren, 0, 0, 0, 255);
	
/********Call Recursive drawBoxFractal function here*******/
	
	SDL_Event e;
	do { SDL_PollEvent(&e); } while (e.type != SDL_MOUSEBUTTONDOWN);
} 
// Linux, Mac: gcc task3b.c -o task3b; ./task3b
// Windows: gcc task3b.c -o task3b; task3b

