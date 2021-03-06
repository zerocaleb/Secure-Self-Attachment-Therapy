# This script is to test the functionality of the game logic

label game_test:
    scene blank page
    call screen game_test_setup
    $result = _return
    $p = 0
    $c = 0
    
    if result == "attend_go":
        $logic.attend_go()
        $p = 1
        $c = 1
        
    if result == "attend_dontgo":
        $logic.attend_dontgo()
        $p = 1
        
    if result == "ignore_go":
        $logic.ignore_go()
        $c = 1
    
    if result == "ignore_dontgo":
        $logic.ignore_dontgo()
        
    $logic.update_matrix()
    
    if logic.check_win(p, c) and p:
       "you Win!"
    jump game_test

screen game_test_setup:
    hbox xalign 0.5 yalign 0.5 spacing 50:
        vbox spacing 50:
            hbox spacing 10:
                textbutton _(str(round(logic.t[0],1)) + "       " + str(round(logic.t[1],1))) action Return("attend_go")
            
            hbox spacing 10:
                textbutton _(str(round(logic.v[0],1)) + "       " + str(round(logic.v[1],1))) action Return("attend_dontgo")
        
        vbox spacing 50:   
            hbox spacing 10:
                textbutton _(str(round(logic.u[0],1)) + "       " + str(round(logic.u[1],1))) action Return("ignore_go")
    
            hbox spacing 10:
                textbutton _(str(round(logic.w[0],1)) + "       " + str(round(logic.w[1],1))) action Return("ignore_dontgo")
                
label ai_test:
    scene blank page
    python:
        flag = False
        choice = ai.move()
        p = 0
        c = 0
        if choice[0] == "attend":
            p = 1
        if choice[1] == "go":
            c = 1
        if ai.check_win(p, c) and p:
            flag = True
    call screen ai_test_setup
    $result = _return
    
    if(result == "round"):
        jump ai_test
        
    if result == "end":
        while(round(ai.probability_matrix[0],2) != 1.00):
            $choice = ai.move()
        jump ai_test

screen ai_test_setup:
    hbox xalign 0.5 yalign 0.5 spacing 50:
        vbox spacing 50:
            hbox spacing 10:
                textbutton _("AI Move") action Return("round")
                
            hbox spacing 10:
                textbutton _("AI End") action Return("end")
            
            hbox spacing 10:
                textbutton _("Rounds: " + str(ai.get_round())) 

        vbox spacing 50:   
            hbox spacing 10:
                textbutton _("t: " + str(round(ai.ai_logic.t[1],2)))
    
            hbox spacing 10:
                textbutton _("u: " + str(round(ai.ai_logic.u[1],2)))
        
            hbox spacing 10:
                textbutton _("v: " + str(round(ai.ai_logic.v[1],2)))
                
            hbox spacing 10:
                textbutton _("w: " + str(round(ai.ai_logic.w[1],2)))
                
        vbox spacing 50:   
            hbox spacing 10:
                textbutton _("prob_t: " + str(round(ai.probability_matrix[0],2)))
    
            hbox spacing 10:
                textbutton _("prob_u: " + str(round(ai.probability_matrix[1],2)))
        
            hbox spacing 10:
                textbutton _("prob_v: " + str(round(ai.probability_matrix[2],2)))
                
            hbox spacing 10:
                textbutton _("prob_w: " + str(round(ai.probability_matrix[3],2)))
                
            hbox spacing 10:
                textbutton _("ordinal_change: " + str(ai.change))
            
        vbox spacing 50:   
            hbox spacing 10:
                textbutton _("q_t: " + str(round(ai.q_t,4)))
    
            hbox spacing 10:
                textbutton _("q_u: " + str(round(ai.q_u,4)))
        
            hbox spacing 10:
                textbutton _("q_v: " + str(round(ai.q_v,4)))
                
            hbox spacing 10:
                textbutton _("q_w: " + str(round(ai.q_w,4)))
                
        vbox spacing 50:   
            hbox spacing 10:
                textbutton _("t_count: " + str(ai.t_count)) 
    
            hbox spacing 10:
                textbutton _("u_count: " + str(ai.u_count))
                
            hbox spacing 10:
                textbutton _("v_count: " + str(ai.v_count)) 
    
            hbox spacing 10:
                textbutton _("w_count: " + str(ai.w_count)) 
            
            if (flag == True):
                hbox spacing 10:
                    textbutton _("WIN!") 
                    
label ai2_test:
    scene blank page
    python:
        flag = False
        choice = ai2.move()
        p = 0
        c = 0
        if choice[0] == "attend":
            p = 1
        if choice[1] == "go":
            c = 1
        if ai2.check_win(p, c) and p:
            flag = True
    call screen ai2_test_setup
    $result = _return
    
    if(result == "round"):
        jump ai2_test
        
    if result == "end":
        while(round(ai2.p_probability_matrix[0],2) != 1.00):
            $choice = ai2.move()
        jump ai2_test
    
screen ai2_test_setup:
    hbox xalign 0.5 yalign 0.5 spacing 50:
        vbox spacing 50:
            hbox spacing 10:
                textbutton _("AI2 Round") action Return("round")
                
            hbox spacing 10:
                textbutton _("AI2 End") action Return("end")
            
            hbox spacing 10:
                textbutton _("Rounds: " + str(ai2.get_round())) 

        vbox spacing 50:   
            hbox spacing 10:
                textbutton _("t: " + str(round(ai2.ai_logic.t[0],2)) + " | " + str(round(ai2.ai_logic.t[1],2)))
    
            hbox spacing 10:
                textbutton _("u: " + str(round(ai2.ai_logic.u[0],2)) + " | " + str(round(ai2.ai_logic.u[1],2)))
        
            hbox spacing 10:
                textbutton _("v: " + str(round(ai2.ai_logic.v[0],2)) + " | " + str(round(ai2.ai_logic.v[1],2)))
                
            hbox spacing 10:
                textbutton _("w: " + str(round(ai2.ai_logic.w[0],2)) + " | " + str(round(ai2.ai_logic.w[1],2)))
                
        vbox spacing 50:   
            hbox spacing 10:
                textbutton _("p_t: " + str(round(ai2.p_probability_matrix[0],2)))
    
            hbox spacing 10:
                textbutton _("p_u: " + str(round(ai2.p_probability_matrix[1],2)))
        
            hbox spacing 10:
                textbutton _("p_v: " + str(round(ai2.p_probability_matrix[2],2)))
                
            hbox spacing 10:
                textbutton _("p_w: " + str(round(ai2.p_probability_matrix[3],2)))
            
        vbox spacing 50:   
            hbox spacing 10:
                textbutton _("p_o: " + str(round(ai2.c_probability_matrix[0],2)))
    
            hbox spacing 10:
                textbutton _("p_p: " + str(round(ai2.c_probability_matrix[1],2)))
        
            hbox spacing 10:
                textbutton _("p_q: " + str(round(ai2.c_probability_matrix[2],2)))
                
            hbox spacing 10:
                textbutton _("p_y: " + str(round(ai2.c_probability_matrix[3],2)))
                
        vbox spacing 50:   
            hbox spacing 10:
                textbutton _("c_t: " + str(ai2.t_count)) 
    
            hbox spacing 10:
                textbutton _("c_u: " + str(ai2.u_count))
                
            hbox spacing 10:
                textbutton _("c_v: " + str(ai2.v_count)) 
    
            hbox spacing 10:
                textbutton _("c_w: " + str(ai2.w_count)) 
           
            hbox spacing 10:
                textbutton _("p_OC: " + str(ai2.p_change))
            
            if (flag == True):
                hbox spacing 10:
                    textbutton _("WIN!") 
                    
        vbox spacing 50:   
            hbox spacing 10:
                textbutton _("c_o: " + str(ai2.o_count)) 
    
            hbox spacing 10:
                textbutton _("c_p: " + str(ai2.p_count))
                
            hbox spacing 10:
                textbutton _("c_q: " + str(ai2.q_count)) 
    
            hbox spacing 10:
                textbutton _("c_y: " + str(ai2.y_count)) 
                
            hbox spacing 10:
                textbutton _("c_OC: " + str(ai2.c_change))
            
            if (flag == True):
                hbox spacing 10:
                    textbutton _("WIN!") 
        