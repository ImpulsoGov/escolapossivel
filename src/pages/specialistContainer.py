import streamlit as st


def genSpecialistContainer():
    """ 
    This is a function that returns the "Specialist" session
              
    """
    '''st.write(
        f"""
        <div class="container">
                <div class="left-margin card-plan">
                        <div style="margin:10px">
                            <div class="left-margin">
                                <div class="text-title-section minor-padding"> 
                                Encontro com o <span class="bold main-orange-span">especialista </span></div>
                                <div class="minor-padding main-black-span"><br>
                                Realizamos, semanalmente, um encontro online com <b>Wanderson de Oliveira</b>, 
                                epidemiologista e ex-secretário nacional de vigilância em saúde, para solucionar dúvidas da 
                                gestão pública sobre o processo de retomada de atividades presenciais na rede de ensino. 
                                <div class="main-padding" align="center" style="padding-bottom: 10px;">
                                    <a href="https://forms.gle/MrkuQ9H4WwEYjbw98" target=_blank>
                                    <button class="button"; style="border-radius: .25rem;">inscreva-se ></button><br>
                                    </a><br>
                                </div>
                            </div>
                        </div>
                </div>
        </div>
        """,
        unsafe_allow_html=True,
    )'''
    st.write(
        f"""
        <div class="conteudo upper-padding">
            <div class="card-plan" style="width:100%;">
                <div style="margin:10px">
                    <div>
                        <div style="word-break: break-word; font-size:1.5em;">
                        Encontro com o <span style="color:#ff9147;"><b>especialista</b></span>
                        </div>
                        <div><br>
                            Em dezembro, realizamos uma série de encontros com <b>Wanderson Oliveira</b>, 
                            ex-secretário nacional de vigilância em saúde, para falar sobre uma reabertura planejada da 
                            rede pública de ensino. 
                            Você pode conferir um resumo das discussões e tirar suas dúvidas sobre o assunto.
                            <div align="center" style="padding-bottom: 10px;">
                                <a href="https://coronacidades.org/encontro-online-da-escola-segura-discute-reabertura-responsavel-e-gradual-da-rede-publica-diante-da-covid/" target=_blank>
                                <button class="button"; style="border-radius: .25rem;">tire suas dúvidas ></button><br>
                                </a><br>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()


