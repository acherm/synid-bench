/*
123333
  Copyright (C) 2014 Sergi Pasoev.

  This pragram is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or (at
  your option) any later version.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program. If not, see <http://www.gnu.org/licenses/>.

  spasoev at gmail.com

*/

#include "pong.h"


//#import <Foundation/Foundation.h>

#define WINDOW_TITLE "Pong"
//#define WINDOW_WIDTH 320
//#define WINDOW_HEIGHT 480
#define FPS 70
#define INITIAL_SPEED 1.1
#define REQUIRED_HITS 5

#define SCORE_PER_HIT 10

int running = 1;
int window_width = 320;
int window_height = 480;

int main(int  argc, char** argv){

  // create window
  SDL_Window *window;
  SDL_Renderer *renderer;

    

  if(SDL_Init(SDL_INIT_VIDEO) >= 0){
  
    SDL_DisplayMode mode;
    SDL_GetDisplayMode(0, 0, &mode);
    //printf("%dx%d\n", mode.w, mode.h);
    window_width = mode.h;
    window_height = mode.w;
  
    
  
    window = SDL_CreateWindow(NULL, 0,
			      0, window_width, window_height,
			      SDL_WINDOW_OPENGL | SDL_WINDOW_SHOWN | SDL_WINDOW_BORDERLESS);
  }

  if(window != 0){
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED |
				  SDL_RENDERER_PRESENTVSYNC);
  }
  /* Create a player */
  Player player;
  player.x = window_width / 2 - PLATE_WIDTH;
  player.y = window_height - PLATE_HEIGHT;
  player.hits = 0;
  player.score = 0;

  
  
  
  
  
  
  //int modes = SDL_GetNumDisplayModes(screen);
  
    
  
  /*
    for (int i = 0; i < modes; i++) {
        SDL_DisplayMode mode;
        SDL_GetDisplayMode(screen, i, &mode);
        printf("%dx%d\n", mode.w, mode.h);
   }*/
  
  
  

  /* Create the enemy! */
  Player enemy;
  enemy.x = window_width / 2 - PLATE_WIDTH;
  enemy.y = 0;
  enemy.hits = 0;
  
  Ball ball;
  ball.x = window_width / 2.0 - BALL_SIZE / 2.0;
  ball.y = window_height / 2.0 - BALL_SIZE / 2.0;
  ball.dx = -INITIAL_SPEED, ball.dy = INITIAL_SPEED;
  ball.size = BALL_SIZE;
  
  while(running){
    handleEvents(&player);
    update(&player, &enemy, &ball);
    render(renderer, &player, &enemy, &ball);
  }

  printf("Game Over\nYour Score: %d\n", player.score * SCORE_PER_HIT);
  return 0;
  clean(window, renderer);
}

void handleEvents(Player *player){
  SDL_Event event;
  while(SDL_PollEvent(&event)){
    switch(event.type){
        case SDL_FINGERDOWN:
        case SDL_FINGERMOTION:
      
                if (player->x + event.tfinger.dx * WINDOW_WIDTH < 0) {
                    player->x = 0;
                } else if((player->x + PLATE_WIDTH) > WINDOW_WIDTH){
                    
                    player->x = WINDOW_WIDTH - PLATE_WIDTH;
                } else {
                    player->x += event.tfinger.dx * window_width;
                }
    
            break;
    case SDL_QUIT:
      running = 0;
      break;   
    case SDL_KEYDOWN:
      switch(event.key.keysym.sym){
      case SDLK_ESCAPE:
	running = 0;
	break;
      case SDLK_q:
	running = 0;
	break;
      }
      break;    
    }
  }

  const Uint8 *state = SDL_GetKeyboardState(NULL);
  if(state[SDL_SCANCODE_RIGHT]){
    if((player->x + PLATE_WIDTH + 2) <= window_width){
      player->x += 3;
    }
  }

  if(state[SDL_SCANCODE_LEFT]){
    if((player->x - 3) >= 0){
      player->x -= 3;
    }
  }
}

void update(Player *player, Player *enemy,  Ball *ball){
  if(ball->x < 0 || ball->x > window_width - ball->size){
    ball->dx = -ball->dx;
  }

  /* Enemy intelligence */
  think(enemy, ball->x, window_width);
  
  if(ball->y < 0 ){
    /* Check if the enemy caught the ball */
    if((ball->x >= enemy->x) && ((ball->x + ball->size) <= (enemy->x + PLATE_WIDTH))){
      ball->dy = -(ball->dy);
      (enemy->hits)++;
    }else{
      /* Enemy missed the ball! */
      player->score++;
      int delay = 90 * abs(ball->dx) + 700;
      SDL_Delay(delay);
      ball->x = window_width / 2.0 - BALL_SIZE / 2.0;
      ball->y = window_height - 22.0 - BALL_SIZE / 2.0;

    }
  }
  
  if(ball->y > window_height - ball->size){
    /* Check if the player caught the ball */
    if((ball->x >= player->x) && ((ball->x + ball->size) <= (player->x + PLATE_WIDTH))){
      ball->dy = -(ball->dy);
      (player->hits)++;
      /* Increase ball speed every fifth hit */
      if((player->hits % REQUIRED_HITS) == 0 ){
	speedUp(ball);
      }
    }else{
      /* Player missed the ball! */
      if(player->score > 0){
	player->score--;
      }
      int delay = 90 * abs(ball->dx) + 700;

      SDL_Delay(delay);
      ball->x = window_width / 2.0 - BALL_SIZE / 2.0;
      ball->y = window_height / 5.0 - BALL_SIZE / 2.0;
    }
  }
  ball->x += ball->dx;
  ball->y += ball->dy;
}

void render(SDL_Renderer *renderer, Player *player, Player *enemy, Ball *ball){
  // show blue background
  SDL_SetRenderDrawColor(renderer, 0x00, 0x00, 0xFF, 0xFF);
  SDL_RenderClear(renderer);
  
  SDL_SetRenderDrawColor(renderer, 255, 255, 255, 0xFF);
  
  SDL_Rect playerRect = {player->x, player->y, PLATE_WIDTH , PLATE_HEIGHT };
  SDL_Rect enemyRect = {enemy->x, enemy->y, PLATE_WIDTH , PLATE_HEIGHT };
  SDL_Rect ballRect = {ball->x, ball->y, ball->size, ball->size};

  SDL_RenderFillRect(renderer, &playerRect);
  SDL_RenderFillRect(renderer, &enemyRect);
  SDL_RenderFillRect(renderer, &ballRect);
  
  SDL_RenderPresent(renderer);
}

void clean(SDL_Window *window, SDL_Renderer *renderer){
  SDL_DestroyWindow(window);
  SDL_DestroyRenderer(renderer);
  SDL_Quit();
}
