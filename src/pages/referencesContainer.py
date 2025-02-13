import streamlit as st
import utils
import amplitude
import pages.snippet as tm
import pages.header as he
import pages.footer as foo

def main():
    """ 
    This is a function that returns the "References" session

    Parameters: 
        session_state (type): section dataset
              
    """
    utils.localCSS("localCSS.css")
    he.genHeader("Sobre")
    utils.main_title(title="<b>Fontes e Referências</b>", subtitle="<br>")
    st.write(
        f"""
        <div class="conteudo main-padding">
            <div class="table-responsive">
            <table>
                <thead>
                    <tr>
                        <th>Título</th>
                        <th>Fonte</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td> Estratégias de reabertura das escolas durante a COVID-19 </td>
                        <td> <a href="https://publications.iadb.org/pt/estrategias-de-reabertura-das-escolas-durante-covid-19">
                            BID
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td> Orientações para Retomada Segura das Atividades Presenciais nas Escolas de Educação Básica no Contexto da Pandemia da COVID-19 </td>
                        <td> <a href="http://antigo.saude.gov.br/images/pdf/2020/September/18/doc-orientador-para-retomada-segura-das-escolas-no-contexto-da-covid-19.pdf">
                            Ministério da Saúde
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td> Manual sobre Biossegurança para Reabertura de Escolas no Contexto da COVID-19 </td>
                        <td> <a href="https://portal.fiocruz.br/sites/portal.fiocruz.br/files/documentos/manualreabertura.pdf">
                            Fiocruz
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td> Guia de Implementação de Protocolos de Retorno das Atividades Presenciais nas Escolas de Educação Básica </td>
                        <td> <a href="https://www.gov.br/mec/pt-br/assuntos/GuiaderetornodasAtividadesPresenciaisnaEducaoBsica.pdf">
                            Ministério da Educação
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td> Considerations for school-related public health measures in the context of COVID-19 </td>
                        <td> <a href="https://apps.who.int/iris/handle/10665/334294">
                            Organização Mundial da Saúde
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td> Manual de Protocolos de Saúde </td>
                        <td> <a href="http://www.educacao.am.gov.br/wp-content/uploads/2020/07/PROTOCOLOS-DE-SAuDE02.pdf">
                            Governo do Estado do Amazonas
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td> Ferramenta de Planejamento e Cálculo de Custos de Preparações Alcoólicas para a Higiene das Mãos </td>
                        <td> <a href="https://proqualis.net/sites/proqualis.net/files/FerramentadePlanejamentoeClculodeCustosgrfica.pdf">
                            Proqualis
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td> Segurança do paciente em serviços de saúde: limpeza e desinfecção de superfícies </td>
                        <td> <a href="https://www20.anvisa.gov.br/segurancadopaciente/images/documentos/ManualLimpezaeDesinfeccaofinal.pdf">
                            ANVISA
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td> NOTA TÉCNICA Nº 47/2020/SEI/GIALI/GGFIS/DIRE4/ANVISA <br> Uso de luvas e máscaras em estabelecimentos da área de alimentos no contexto do enfrentamento ao COVID-19 </td>
                        <td> <a href="https://www.gov.br/anvisa/pt-br/arquivos-noticias-anvisa/310json-file-1">
                            ANVISA
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td> Appendix A – Risk-assessment for determining environmental cleaning method and frequency </td>
                        <td> <a href="https://www.cdc.gov/hai/prevent/resource-limited/risk-assessment.html">
                            Centers for Disease Control and Prevention
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
            </div>
        </div>
        """,
        unsafe_allow_html = True,
    )
    tm.genGuia()
    foo.genFooter()
    
if __name__ == "__main__":
    main()
