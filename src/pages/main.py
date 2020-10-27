import streamlit as st
import yaml
import utils
import os
import pandas as pd
from ipywidgets import AppLayout, GridspecLayout


def genHeroSection(title1: str, title2: str, subtitle: str, header: bool):

    if header:
        header = """<a href="https://coronacidades.org/" target="blank" class="logo-link"><span class="logo-header" style="font-weight:bold;">corona</span><span class="logo-header" style="font-weight:lighter;">cidades</span></a>"""
    else:
        header = """<br>"""

    st.write(
        f"""
        <div class="container row">
            <div class="col">
                {header}
                <span class="hero-container-product main-blue-span">{title1}</span>
                <br>
                <span class="hero-container-product main-blue-span">{title2}</span>
                <br><br>
            </div>
            <div class="col">
                <br><br><br>
                <span class="hero-container-question main-grey-span">Controle a Covid-19 e promova aulas presenciais seguras na rede pública.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def read_data(country, config, endpoint):
    # if os.getenv("IS_LOCAL") == "TRUE":
    #     api_url = config[country]["api"]["local"]
    # else:
    #     api_url = config[country]["api"]["external"]
    api_url = config[country]["api"]["local"]
    url = api_url + endpoint
    df = pd.read_csv(url)
    return df


@st.cache(suppress_st_warning=True)
def get_data(config):
    df = read_data("br", config, "br/cities/safeschools/main")
    return df


def genSelectBox(df, session_state):
    st.write(
        f"""
        <div class="container main-padding">
            <div class="text-title-section"> Selecione sua rede </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    session_state.state_id = st.selectbox("Estado", utils.filter_place(df, "state"))
    session_state.city_name = st.selectbox(
        "Município", utils.filter_place(df, "city", state_id=session_state.state_id)
    )
    session_state.administrative_level = st.selectbox(
        "Nível de Administração",
        utils.filter_place(df, "administrative_level", state_id=session_state.state_id),
    )


def genPlanContainer():
    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section">Planeje                
                <p>Acesse ferramentas e conteúdos para planejar uma reabertura organizada e segura.</p>
            </div><br>
            <div class="left-margin">
                <div class="row">
                <div class="col">
                    <div class="text-title-section minor-padding"> <img src="https://via.placeholder.com/60"> Protocolos</div>
                    <div class="minor-padding"><b>O que é?</b> Lista de orientações para preparar sua estrutura sanitária e planejar rotinas seguras dentro e fora da sala de aula.</div>
                </div>
                <div class="col">
                    <div class="text-title-section  minor-padding"> <img src="https://via.placeholder.com/60"> Passo a passo</div>
                    <div class="minor-padding"><b>O que é?</b> Saiba quais etapas seguir para retomar as atividades presenciais na escola de sua rede.</div>
                </div>
            </div>
            </div><br>
            <div class="subtitle-section"> Régua de protocolo </div>
                <div class="minor-padding">Entenda quais protocolos adotar de acordo com o nível de alerta da Covid-19 em seu local.</div>
            <div class="minor-padding">
                <img src="https://via.placeholder.com/300">
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def genSimulationResult(number_students, number_teachers, number_classroms):

    st.write(
        f"""
        <div class="container main-padding">
            <div>
                <div class="subtitle-section minor-padding"> RESULTADO DA SIMULAÇÃO </div>
                <div class="row main-padding">
                    <div class="col">
                        <div class="card-simulator blue-bg">
                            <div class="card-title-section primary-span">EQUITATIVO</div>
                            <div class="text-small">Todos os alunos têm aula presencial ao menos 1 vez por semana.</div>
                            <div class="bold">
                                <img src="https://via.placeholder.com/30">
                                <span class="card-number">250</span> alunos retonam às aulas
                            </div>
                            <div class="bold">
                                <img src="https://via.placeholder.com/30">
                                <span class="card-number">100</span> professores retornam
                            </div>
                            <br>
                        </div>
                        <div class="card-simulator blue-bg minor-padding">
                            <div class="card-title-section primary-span">Materiais para compra</div>
                            <br>
                            <div class="bold">
                                <img src="https://via.placeholder.com/30">
                                <span class="card-number">350</span> máscaras
                            </div>
                            <div class="bold">
                                <img src="https://via.placeholder.com/30">
                                <span class="card-number">3</span> termômetros
                            </div>
                            <div class="bold">
                                <img src="https://via.placeholder.com/30">
                                <span class="card-number">4.2</span> litros de álcool em gel
                            </div>
                        </div> 
                    </div>
                    <div class="col">
                        <div class="card-simulator dark-blue-bg light-span">
                            <div class="card-title-section">PRIORITÁRIO</div>
                            <div class="text-small">Máximo de alunos retorna 5 vezes por semana.</div>
                            <br>
                        </div>
                        <div class="card-simulator primary-blue-bg minor-padding">
                            <div class="card-title-section light-span">Materiais para compra</div>
                            <br>
                        </div>
                    </div>
                </div>
            </div>            
            <div class="minor-padding">
                <div class="minor-padding blue-bg" style="border-radius:5px;">
                    <div style="padding:10px;">
                        <img src="https://via.placeholder.com/40"> <b>Veja mais materiais necessários para compra 
                        <a href="https://docs.google.com/spreadsheets/d/15ib2NCdwPbLllofuqf9epKCAQK_hvY1Q8rdp6hHko_U/edit?ts=5f889510#gid=0">
                        aqui</a>.</b>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def genSimulationContainer(df, session_state):
    st.write(
        f"""
        <div class="container main-padding">
            <div class="subtitle-section"> Simule o retorno </div>
                <div class="minor-padding">Analise qual o modelo de retorno mais adequado para sua realidade e calcule os recursos necessários para a retomada. 
                Abaixo trazemos 2 possíveis modelos:</div>
                <div class="minor-padding">
                    <div class="text-title-section minor-padding">Entenda os modelos de retorno </div>
                    <br><div class="row" style="grid-gap: 1rem; padding: 0rem 1rem 0rem;">
                        <div class="col blue-bg card-simulator" style="border-radius:30px;">
                            <div class="two-cols-icon-text">
                                <div class="card-title-section">EQUITATIVO</div>
                                <div class="text-subdescription">
                                    <b>Todos os alunos têm aula presencial ao menos 1 vez por semana.</b>
                                    <p></p>
                                    O modelo prioriza que os alunos voltem para a escola de forma igualitária, 
                                    mesmo que somente um dia na semana. Atividades podem ser de reforço ou conteúdo.
                                </div>
                            </div>
                        </div>
                        <div class="col light-blue-bg light-span card-simulator" style="border-radius:30px">
                        <div class="two-cols-icon-text">
                            <div class="card-title-section">PRIORITÁRIO</div>
                            <div class="text-subdescription">
                                <b>Número limitado de alunos retorna 5 vezes por semana.</b>
                                <p></p>
                                O modelo prioriza o tempo que o aluno passa na escola, mesmo que para uma quantidade menor de alunos. 
                                Atividades podem ser de reforço ou conteúdo.
                            </div>
                        </div>
                        </div>
                    </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        f"""<br>
            <div class="text-title-section minor-padding">Defina seu modelo de retorno</div><br>
            <div>
                <div class="text-padding bold">1) Para qual etapa de ensino você está planejando?</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    # TODO: colocar por estado somente também
    # if city_name:
    data = df[
        (df["city_name"] == session_state.city_name)
        & (df["administrative_level"] == session_state.administrative_level)
    ]

    education_phase = st.selectbox("", data["education_phase"].sort_values().unique())

    data = data[data["education_phase"] == education_phase]

    st.write(
        f"""
            <br><div class="text-padding bold">2) Utilize os filtros para os dados do Censo Escolar (2019):</div>
        """,
        unsafe_allow_html=True,
    )

    if "Rural" in data["school_location"].drop_duplicates().values:
        rural = ["Rural" if st.checkbox("Apenas escolas rurais") else "Todos"][0]

        data = data[(data["school_location"] == rural)]

    if "Sim" in data["school_public_water_supply"].drop_duplicates().values:
        water_supply = [
            "Sim" if st.checkbox("Apenas escolas com água encanada") else "Todos"
        ][0]

        data = data[(data["school_public_water_supply"] == water_supply)]

    st.write(
        f"""
        <div class="main-padding bold">3) Ou informe seus dados abaixo:</div><br>
        </div>
        """,
        unsafe_allow_html=True,
    )

    number_students = st.number_input(
        "Qual total de alunos da sua rede?",
        format="%d",
        value=data["number_students"].values[0],
        step=1,
    )

    number_teachers = st.number_input(
        "Qual total de professores da sua rede?",
        format="%d",
        value=data["number_teachers"].values[0],
        step=1,
    )

    number_classroms = st.number_input(
        "Qual total de sala de aulas na sua rede?",
        format="%d",
        value=data["number_classroms"].values[0],
        step=1,
    )

    st.write(
        f"""
        <div class="main-padding bold">4) Escolha as condições de retorno:</div><br>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    perc_students = st.slider(
        "Percentual de alunos realizando atividades presenciais:", 0, 100, 100, 10
    )
    number_students = int(perc_students * number_students / 100)

    st.write(
        f"<i>Valor selecionado: {str(perc_students)}% dos alunos</i> - {str(number_students)} alunos no total.<br><hr>",
        unsafe_allow_html=True,
    )

    perc_teachers = st.slider(
        "Percentual de professores realizando atividades presenciais:", 0, 100, 100, 10
    )
    number_teachers = int(perc_teachers * number_teachers / 100)

    st.write(
        f"<i>Valor selecionado: {str(perc_teachers)}% dos alunos</i> - {str(number_teachers)} professores no total.<br><hr>",
        unsafe_allow_html=True,
    )

    max_students = st.slider("Máximo de alunos por sala:", 0, 20, 20, 1)

    st.write(
        f"<i>Valor selecionado: {max_students} alunos por sala</i><br>",
        unsafe_allow_html=True,
    )

    if st.button("SIMULAR RETORNO"):
        if st.button("Esconder"):
            pass
        genSimulationResult(number_students, number_teachers, number_classroms)

    utils.stylizeButton(
        name="SIMULAR RETORNO",
        style_string="""box-sizing: border-box;border-radius: 15px; width: 150px;padding: 0.5em;text-transform: uppercase;font-family: 'Oswald', sans-serif;background-color:  #0097A7;font-weight: bold;text-align: center;text-decoration: none;font-size: 18px;animation-name: fadein;animation-duration: 3s;margin-top: 1.5em;""",
        session_state=session_state,
    )


def genPrepareContainer():
    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section">Prepare 
            <p>Durante a reabertura, avalie se a sua unidade escolar está cumprindo todos os protocolos.</p>
            </div>
                <div class="left-margin">
                <div class="text-title-section minor-padding"> <img src="https://via.placeholder.com/60"> Ferramenta de verificação</div>
                <div class="minor-padding"><b>O que é?</b> Preencha o formulário para conferir a adequação da sua unidade aos protocolos e receber orientações.</div>
                <div>
                <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def genMonitorContainer():
    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section">Monitore
                <p>Após a reabertura, monitore a Covid-19 e saiba o que fazer com o sugrimento de casos.</p>
            </div>
            <div class="left-margin">
                <div class="text-title-section minor-padding"> <img src="https://via.placeholder.com/60"> Plano de contigência</div>
                <div class="minor-padding"><b>Há casos de Covid na escola?</b> Monte seu plano de ação a partir do fluxograma abaixo e implemente um sistema de monitoramento a partir da ferramenta.</div>
                <div>
                <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
                </div>
                <div class="text-title-section main-padding"> <img src="https://via.placeholder.com/60"> Ferramenta de notificação</div>
                <div class="minor-padding">lorem ipsum.</div>
                <div>
                <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def genFooterContainer():
    st.write(
        f"""
        <div class="container">
            <div class="text-title-footer main-padding"> Realizado por </div>
            <br>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main(session_state):
    utils.localCSS("style.css")
    genHeroSection(
        title1="Escola", title2="Segura", subtitle="{descrição}", header=True,
    )
    config = yaml.load(open("config/config.yaml", "r"), Loader=yaml.FullLoader)
    data = get_data(config)
    genSelectBox(data, session_state)
    genPlanContainer()
    genSimulationContainer(data, session_state)
    genPrepareContainer()
    genMonitorContainer()
    genFooterContainer()


if __name__ == "__main__":
    main()
