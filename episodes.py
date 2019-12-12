# IN THIS FILE WE IMPLEMENT THE GAME AND RUN THE EPISODES
from env import *

# STORING REWARDS IN A LIST
episode_rewards=[]

for episode in range(TOT_EPISODES):
    player=agent()
    v_b=villain_bullets()
    tot_dodged=0
    if episode%SHOW_EVERY==0:
        print(f"On episode number {episode}, epsilon value is {epsilon}")
        print(f"Mean for last {SHOW_EVERY} episodes : {np.mean(episode_rewards[-SHOW_EVERY:])}")
        show = True

    else:
        show=False

    episode_rew=0
    for i in range(200): #MAX 200 STEPS ONLY (IT WON'T REALLY REACH 200 ANYWAYS)
        obs=(player.pos, v_b.observed_bullet, tot_dodged)
        if np.random.random() > epsilon:
            action=np.argmax(q_table[obs])
        else:
            action=np.random.randint(0,3)  # for exploration
        player.action(action)
        v_b.move()

        #rewarding
        if player.pos==v_b.final_bullet:
            reward=-ENEMY_PENALTY
        elif tot_dodged==DODGE_GOAL-1:
            reward=ALL_DODGE_REWARD
        else:
            if v_b.final_bullet != -1:
                reward=DODGE_REWARD
                tot_dodged+=1
            else:
                reward=-MOVE_PENALTY
        
        new_obs=(player.pos,v_b.observed_bullet, tot_dodged)
        max_future_q=np.max(q_table[new_obs])
        current_q=q_table[obs][action]

        if reward==ALL_DODGE_REWARD:
            new_q=ALL_DODGE_REWARD
        else:
            # calculating the new Q-value using the equation
            new_q=(1-LR)*current_q+LR*(reward+DISCOUNT*max_future_q)

        q_table[obs][action]=new_q #updating the particular Q-value


        if show:        # To render one episode of the game
            game=np.zeros((GAME_LENGTH, GAME_WIDTH, 3), dtype=np.uint8)
            game[GAME_LENGTH-1][player.pos]=d[AGENT]
            c=1
            for b in v_b.bullet_pos:
                if b!=-1:
                    game[GAME_LENGTH-c][b]=d[BULLET]
                c+=1
            game[0][v_b.vil_pos]=d[SHOOTER]
            img = Image.fromarray(game, 'RGB')  
            img = img.resize((250, 400))  # resizing to see the game properly
            draw = ImageDraw.Draw(img)
            draw.text((0, 0),f"Epidsode:{episode}",(255,255,255))
            cv2.imshow("image", np.array(img))
            if reward == ALL_DODGE_REWARD or reward == -ENEMY_PENALTY:  # to wait for sometime if it gets hit or dodges all bullets
                if cv2.waitKey(500) & 0xFF == ord('q'):
                    break
            else:
                if cv2.waitKey(200) & 0xFF == ord('q'):
                    break

        episode_rew += reward
        if reward == ALL_DODGE_REWARD or reward == -ENEMY_PENALTY: # ending the episode if goal reached or hit by bullet
            break
    
    episode_rewards.append(episode_rew)
    epsilon *= EPS_DECAY # updating the epsilon value



# FOR GRAPHING
moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')

plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel(f"Average reward at every {SHOW_EVERY} episodes")
plt.xlabel("Episode Number")
plt.show()


