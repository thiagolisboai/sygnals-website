# Política de Privacidade — Sygnals

**Versão:** 1.0
**Última atualização:** 12 de julho de 2026
**Idioma de controle:** Português (Brasil), para titulares e clientes no Brasil.


---

## Sumário

1. [Quem Somos](#1-quem-somos)
2. [Escopo desta Política](#2-escopo-desta-politica)
3. [Dados que Coletamos](#3-dados-que-coletamos)
4. [De Onde Vêm os Dados](#4-de-onde-vem-os-dados)
5. [Para Que Usamos os Dados](#5-para-que-usamos-os-dados)
6. [Bases Legais para o Tratamento](#6-bases-legais-para-o-tratamento)
7. [Legítimo Interesse: Nossa Avaliação](#7-legitimo-interesse-nossa-avaliacao)
8. [Intent Score e Decisões Automatizadas](#8-intent-score-e-decisoes-automatizadas)
9. [Com Quem Compartilhamos Dados](#9-com-quem-compartilhamos-dados)
10. [Transferência Internacional de Dados](#10-transferencia-internacional-de-dados)
11. [Por Quanto Tempo Guardamos os Dados](#11-por-quanto-tempo-guardamos-os-dados)
12. [Segurança da Informação](#12-seguranca-da-informacao)
13. [Aviso a Pessoas Monitoradas ("Engajadores")](#13-aviso-a-pessoas-monitoradas-engajadores)
14. [Seus Direitos como Titular de Dados](#14-seus-direitos-como-titular-de-dados)
15. [Cookies e Tecnologias Similares](#15-cookies-e-tecnologias-similares)
16. [Crianças e Adolescentes](#16-criancas-e-adolescentes)
17. [Alterações a Esta Política](#17-alteracoes-a-esta-politica)
18. [Contato e Encarregado (DPO)](#18-contato-e-encarregado-dpo)

---

## 1. Quem Somos

Esta Política de Privacidade é publicada por **TLA DIGITAL LTDA - ME**, inscrita no CNPJ sob o nº **54.958.502/0001-59**, com sede em **Av. Paulista, 1106, Sala 01, Bela Vista, São Paulo/SP, CEP 01310-914** ("**Sygnals**", "**nós**"), controladora dos dados pessoais tratados conforme aqui descrito, nos termos da Lei nº 13.709/2018 (Lei Geral de Proteção de Dados Pessoais — "**LGPD**").

## 2. Escopo desta Política

Esta Política se aplica a **duas categorias distintas de titulares de dados**, tratadas de forma diferente ao longo deste documento:

- **(a) Clientes e usuários do Sygnals** — pessoas que criam conta, configuram Workspaces e utilizam a plataforma; e
- **(b) Engajadores** — pessoas físicas que interagiram publicamente no LinkedIn (reações, comentários, visitas de perfil, novos seguidores, solicitações de conexão) com um perfil monitorado por um Cliente através do Sygnals, e que **nunca se cadastraram no Sygnals nem têm qualquer relação direta conosco**.

Se você é um Engajador e chegou a esta página a partir de um link enviado por e-mail, por um Cliente do Sygnals, ou por busca direta, vá diretamente à **[Seção 13](#13-aviso-a-pessoas-monitoradas-engajadores)**, escrita especificamente para você.

## 3. Dados que Coletamos

### 3.1. Dados de Clientes (usuários da plataforma)

- Dados de cadastro: nome, e-mail, foto de perfil (via Google OAuth), senha ou método de autenticação.
- Dados de Workspace: nome da empresa, configurações de Signals, integrações configuradas (URLs de webhook, nomes de configuração).
- Dados de faturamento: processados pelo Stripe (não armazenamos dados completos de cartão).
- Dados de uso: interações com a plataforma, logs técnicos, dados de suporte.

### 3.2. Dados de Engajadores (pessoas monitoradas)

Para cada Engajador identificado através de um Signal configurado por um Cliente, podemos tratar:

- **Dados públicos do LinkedIn**: nome, headline/cargo declarado, foto de perfil pública, URL do perfil, localização (país/cidade quando disponível publicamente), conteúdo do comentário público (quando aplicável), tipo de reação, data de postagem/comentário.
- **Dados de conta conectada** (apenas quando o Cliente conecta sua própria conta LinkedIn via Unipile): visitantes de perfil, novos seguidores, timestamp de detecção de seguimento.
- **Atributos inferidos por nós**: cargo e empresa (derivados por parsing do headline público), senioridade (classificação interna baseada no título), função/departamento (classificação interna), região geográfica (derivada do país), e o **Intent Score** (pontuação de 0 a 100 calculada a partir de frequência de engajamento, senioridade inferida, tipo de engajamento e recência — ver Seção 8).

**Não coletamos, e nosso produto é desenhado para nunca inferir**, categorias de dados sensíveis nos termos do art. 5º, II da LGPD (origem racial ou étnica, convicção religiosa, opinião política, filiação sindical, dado referente a saúde ou vida sexual, dado genético ou biométrico).

## 4. De Onde Vêm os Dados

- **De você diretamente** (se você é Cliente): no momento do cadastro e uso da plataforma.
- **De fontes públicas do LinkedIn**, coletadas por meio de provedor terceiro especializado em dados públicos (Apify), sem uso de cookies de sessão do LinkedIn ou extensão de navegador — aplicável a Signals baseados em posts/reações/comentários públicos.
- **De contas do LinkedIn conectadas pelo próprio Cliente**, por meio de provedor terceiro (Unipile), quando o Cliente autoriza acesso à sua própria conta ou conta de Sales Navigator para coleta de sinais como visitantes de perfil e novos seguidores. Essa coleta é autorizada e configurada pelo Cliente, não pelo Engajador.

## 5. Para Que Usamos os Dados

- Operar, manter e melhorar o Serviço.
- Processar Signals configurados pelos Clientes e gerar Perfis de Engajamento.
- Calcular o Intent Score para priorização comercial.
- Entregar dados aos Clientes via tabela, exportação CSV, integração com Clay ou webhook genérico.
- Processar pagamentos e gerenciar assinaturas.
- Cumprir obrigações legais e regulatórias.
- Comunicação de suporte e avisos operacionais.

Não utilizamos dados de Engajadores para fins de publicidade direcionada, venda a terceiros não autorizados pelo Cliente, ou qualquer finalidade além da entrega ao Cliente que configurou o Signal correspondente.

## 6. Bases Legais para o Tratamento

| Categoria de dado | Base legal (LGPD) | Base legal (GDPR, quando aplicável) |
|---|---|---|
| Dados de Cliente (cadastro, uso, faturamento) | Execução de contrato (art. 7º, V) | Execução de contrato (art. 6º, 1, b) |
| Dados de Engajador — coleta pública via Apify | Legítimo interesse (art. 7º, IX) | Legítimo interesse (art. 6º, 1, f) |
| Dados de Engajador — conta conectada via Unipile | Legítimo interesse do Cliente e nosso, como operador (art. 7º, IX) | Legítimo interesse (art. 6º, 1, f) |
| Cumprimento de obrigação legal (ex.: fiscal) | Obrigação legal (art. 7º, II) | Obrigação legal (art. 6º, 1, c) |

## 7. Legítimo Interesse: Nossa Avaliação

Como o Engajador nunca interage diretamente com o Sygnals nem nos concede consentimento, tratamos esses dados com base no **legítimo interesse**, nos termos do art. 7º, IX, c/c art. 10 da LGPD. Antes de lançar esse tratamento, aplicamos um teste de balanceamento em três etapas, seguindo a metodologia do Guia Orientativo de Legítimo Interesse publicado pela Autoridade Nacional de Proteção de Dados (ANPD):

**(a) Finalidade legítima.** O interesse perseguido é concreto e específico: permitir que empresas identifiquem, entre pessoas que já demonstraram publicamente interesse em um tema (ao reagir ou comentar em um post), aquelas com maior probabilidade de terem interesse comercial genuíno — uma prática already estabelecida na indústria de inteligência comercial B2B (ex.: Clay, Trigify e ferramentas similares).

**(b) Necessidade.** Coletamos apenas os dados estritamente necessários para essa finalidade: identificação básica, dados profissionais públicos, e o conteúdo do próprio engajamento (comentário/reação). Não coletamos dados sensíveis, não realizamos coleta contínua e ilimitada — cada Signal é limitado a um perfil específico configurado por um Cliente, com limites de volume por execução.

**(c) Balanceamento com os direitos do titular.** Reconhecemos que o Engajador não tem uma expectativa prévia específica de que seus dados públicos serão processados dessa forma. Por isso, adotamos as seguintes salvaguardas:
- disponibilizamos esta política publicamente, incluindo um **aviso dedicado ao Engajador** (Seção 13), acessível sem necessidade de conta;
- oferecemos um **canal simples de oposição e exclusão**, sem exigir cadastro (ver Seção 13);
- limitamos o tratamento a **dados profissionais**, nunca dados sensíveis;
- o Intent Score e os atributos inferidos servem apenas para priorização comercial pelo Cliente — **não geram decisão automatizada com efeito jurídico relevante ou que afete significativamente o Engajador** (ver Seção 8);
- mantemos um registro interno desta avaliação de legítimo interesse, disponível à ANPD mediante solicitação, nos termos do art. 37 da LGPD.

Reavaliamos este balanceamento sempre que o produto evolui de forma a ampliar o volume, a sensibilidade ou o escopo dos dados tratados.

## 8. Intent Score e Decisões Automatizadas

O Intent Score é uma pontuação de 0 a 100, calculada por regras internas e transparentes com base em quatro fatores: (1) frequência de engajamento nos últimos 30 dias; (2) senioridade inferida a partir do cargo declarado publicamente; (3) tipo de engajamento (comentário pondera mais que reação); e (4) decaimento temporal (engajamentos mais antigos pontuam menos).

Este cálculo **não constitui decisão automatizada com efeitos jurídicos ou impacto significativo** sobre o Engajador, nos termos do art. 20 da LGPD: ele apenas organiza e prioriza, para o Cliente, informações que já são públicas ou às quais o Cliente já tem acesso legítimo, sem gerar qualquer efeito automático (ex.: não bloqueia, nega ou concede acesso a nada; não é usado para decisões de crédito, emprego ou similares). Ainda assim, qualquer titular pode solicitar revisão humana e informações sobre os critérios do Intent Score referentes a si, conforme a Seção 14.

## 9. Com Quem Compartilhamos Dados

Compartilhamos dados com os seguintes subprocessadores, estritamente para viabilizar o Serviço:

| Subprocessador | Finalidade | Localização |
|---|---|---|
| Apify | Coleta de dados públicos do LinkedIn | UE |
| Unipile | Acesso a sinais baseados em conta LinkedIn conectada pelo Cliente | UE |
| MongoDB Atlas | Armazenamento de banco de dados | Conforme região contratada |
| Railway | Hospedagem de backend e workers | EUA |
| Vercel | Hospedagem de frontend | EUA |
| Cloudflare (R2) | Armazenamento de arquivos de exportação CSV | Global (rede Cloudflare) |
| Stripe | Processamento de pagamentos | EUA/Global |
| Resend | Envio de e-mails transacionais | EUA |
| OpenAI | Fallback de classificação de cargo (~5% dos casos, sem dados sensíveis) | EUA |
| Sentry / PostHog | Monitoramento de erros e analytics de produto | EUA/UE |
| Clay / Webhook do Cliente | Entrega dos Perfis de Engajamento, conforme integração configurada pelo próprio Cliente | Conforme configuração do Cliente |

Não vendemos dados pessoais a terceiros. O compartilhamento com o Cliente que configurou o Signal correspondente é a finalidade central do Serviço; a partir da entrega, o Cliente passa a ser controlador independente desses dados (ver Cláusula 15 dos [Termos de Serviço](/legal/terms)).

## 10. Transferência Internacional de Dados

Alguns dos subprocessadores listados na Seção 9 estão localizados fora do Brasil. Quando isso ocorre, utilizamos os mecanismos de transferência internacional previstos na LGPD (art. 33) e regulamentados pela Resolução CD/ANPD nº 19/2024, incluindo cláusulas-padrão contratuais aprovadas pela ANPD, celebradas com os subprocessadores relevantes. Para titulares na União Europeia, aplicamos, quando cabível, as Cláusulas Contratuais Padrão (SCCs) da Comissão Europeia.

## 11. Por Quanto Tempo Guardamos os Dados

- **Dados de Cliente**: enquanto a conta estiver ativa, e por até 90 (noventa) dias após o cancelamento do Workspace, para fins de recuperação de dados e cumprimento de obrigações legais.
- **Dados de Engajadores**: enquanto o Signal correspondente estiver ativo, e por até 30 (trinta) dias após a exclusão de um Signal específico, findos os quais os dados são permanentemente removidos, salvo obrigação legal de retenção por prazo diverso.
- **Solicitações de exclusão de Engajadores** (Seção 13) são atendidas em prazo compatível com a legislação aplicável, tipicamente em até 15 (quinze) dias.

## 12. Segurança da Informação

Adotamos medidas técnicas e organizacionais para proteger os dados pessoais, incluindo: criptografia em repouso (AES-256-GCM para credenciais de webhook, hashing SHA-256 para chaves de API), controle de acesso multi-tenant obrigatório em todos os endpoints, e conexões criptografadas em trânsito (TLS). Nenhum sistema é absolutamente seguro; em caso de incidente de segurança relevante, notificaremos a ANPD e os titulares afetados nos termos do art. 48 da LGPD.

## 13. Aviso a Pessoas Monitoradas ("Engajadores")

> **Esta seção é escrita diretamente para você, se você reagiu, comentou, visitou um perfil ou seguiu alguém no LinkedIn e foi identificado por um Cliente do Sygnals através da nossa plataforma. Você não precisa ter conta no Sygnals para exercer os direitos descritos aqui.**

### O que fazemos com seus dados

Um cliente do Sygnals (uma empresa que faz prospecção comercial B2B) monitora um perfil do LinkedIn — possivelmente o próprio perfil dessa empresa ou de um concorrente/parceiro dela. Quando você reage, comenta, visita um perfil ou segue um perfil monitorado, nosso sistema pode identificar sua interação, coletar os dados públicos associados (nome, cargo declarado, texto do comentário, etc.) e apresentá-los a esse cliente, junto com uma pontuação interna de prioridade comercial (Intent Score).

### Por que isso é permitido

Tratamos esse dado com base no **legítimo interesse** (art. 7º, IX da LGPD), conforme detalhado na Seção 7 acima. Sua interação já era pública no momento em que ocorreu; nós apenas organizamos essa informação pública para fins de prospecção comercial B2B legítima.

### O que você pode fazer

Você pode, a qualquer momento e **sem necessidade de criar conta**:

- **Solicitar acesso** aos dados que temos sobre você;
- **Solicitar a exclusão** dos seus dados de nossa base;
- **Se opor** ao tratamento de seus dados com base em legítimo interesse, nos termos do art. 18, § 2º da LGPD;
- **Solicitar correção** de dados imprecisos.

Para exercer qualquer um desses direitos, envie um e-mail para **[privacidade@sygnals.ai]** com o link do seu perfil do LinkedIn para que possamos localizar seus dados. Responderemos em até 15 (quinze) dias.

### O que não fazemos

Não usamos seus dados para publicidade direcionada, não os vendemos a terceiros não relacionados ao Signal que gerou a coleta, e não tomamos nenhuma decisão automatizada sobre você com efeito jurídico relevante.

## 14. Seus Direitos como Titular de Dados

Nos termos do art. 18 da LGPD (e, quando aplicável, dos artigos correspondentes do GDPR), você tem direito a:

- confirmação da existência de tratamento;
- acesso aos seus dados;
- correção de dados incompletos, inexatos ou desatualizados;
- anonimização, bloqueio ou eliminação de dados desnecessários ou tratados em desconformidade com a lei;
- portabilidade dos dados a outro fornecedor de serviço;
- eliminação dos dados tratados com consentimento (quando aplicável);
- informação sobre entidades públicas e privadas com as quais compartilhamos dados;
- informação sobre a possibilidade de não fornecer consentimento e as consequências da negativa (quando o consentimento for a base legal aplicável);
- revogação do consentimento (quando aplicável);
- **oposição** a tratamento realizado com base em legítimo interesse;
- revisão de decisões tomadas unicamente com base em tratamento automatizado, quando afetarem seus interesses.

Para exercer esses direitos, entre em contato pelo e-mail informado na Seção 18. Você também tem o direito de apresentar reclamação à Autoridade Nacional de Proteção de Dados (ANPD) ou, se aplicável, à autoridade de proteção de dados de seu país.

## 15. Cookies e Tecnologias Similares

Utilizamos cookies estritamente necessários para autenticação e funcionamento da plataforma, além de ferramentas de analytics de produto (PostHog) para entender o uso da aplicação por Clientes autenticados. Não utilizamos cookies de rastreamento publicitário, nem no site institucional, nem na aplicação.

## 16. Crianças e Adolescentes

O Serviço é destinado exclusivamente a uso profissional por maiores de 18 anos, na qualidade de representantes de empresas. Não direcionamos o Serviço a crianças ou adolescentes e não coletamos intencionalmente dados de menores de idade.

## 17. Alterações a Esta Política

Podemos atualizar esta Política periodicamente. Alterações materiais serão comunicadas aos Clientes por e-mail ou aviso na plataforma, com indicação de nova data de vigência. Recomendamos revisão periódica desta página.

## 18. Contato e Encarregado (DPO)

Para exercer seus direitos, esclarecer dúvidas sobre esta Política, ou reportar uma preocupação de privacidade:

**Encarregado de Proteção de Dados (DPO):** [NOME]
**E-mail:** [privacidade@sygnals.ai]
**Endereço:** Av. Paulista, 1106, Sala 01, Bela Vista, São Paulo/SP, CEP 01310-914

Você também pode registrar reclamação junto à Autoridade Nacional de Proteção de Dados (ANPD) em **gov.br/anpd**.
