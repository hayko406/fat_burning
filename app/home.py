import streamlit as st

st.header('Калькулятор процента жира')
current_weight = st.number_input('твой текущий вес', step=5)
current_fat = st.number_input('твой текущий процент жира', step=1)
desired_fat = 100 - st.number_input('какой процент жира ты хочешь', step=1)

but = st.button('посчитать сколько мне нужно весить для этого')

if current_fat>=100 or current_fat<0 or desired_fat<0:
    st.header("неправильный процент жира")
else:
    if but:
        muscles = 100 - current_fat
        fat_muscles_diff = 100/muscles
        desired_fat_muscles_diff = 100/desired_fat

        diff = fat_muscles_diff/desired_fat_muscles_diff

        necessary_weight = current_weight/diff

        add=''
        if current_weight-necessary_weight>4:
            add='. Ты на столько никогда не похудеешь, свинья'
        st.header(f'для этого тебе нужно весить {round(necessary_weight,2)} кг'+add)
