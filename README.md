Sockets: o que é e como eles funcionam?

Os sockets são portas de entrada para processos de comunicação, isto é, eles permitem que dois processos distintos se comuniquem e, por consequência, geram determinado resultado.
Hoje, as portas de internet estão entre as mais populares. Mesmo com Wi-Fi cada vez mais rápidos, essas portas disponibilizam conexões estáveis e aproveitam 100% do potencial da rede, explicando a então popularidade dessa função.
Ainda assim, poucos usuários entendem como funcionam os sockets. Justamente por isso, hoje a Linux Solutions preparou este artigo e reuniu tudo o que você deve saber sobre este dispositivo de comunicação!

O que são sockets?

Os sockets podem ser definidos como um processo de comunicação que permite dois diferentes processos de conversarem e trocarem informação entre si. Na internet, por exemplo, eles funcionam para gerar uma conexão entre usuário e site.
Mesmo com diferentes aplicações e exemplos, o uso do socket é bastante popular por conta do seu uso diário em páginas da web, que requisitam o uso de socket para melhorar a experiência do usuário.
Do mesmo modo, ao criar um ssh no seu servidor, você recorre aos sockets para realizar e aumentar a eficiência entre os processos.
Vale destacar que esta linguagem entre processos não é recente. Pelo contrário, a primeira aparição se deu em 1983, na versão 4.2 do Berkeley Software Distribution (BSD), sistema operacional que deriva do Unix. Não à toa, este mesmo recurso está presente nas tantas distro Linux.
Hoje é possível encontrar os sockets em formato de API. Neste caso, eles funcionam com mais independência em relação à rede com o propósito das aplicações conversarem com mais agilidade e sem a intervenção do protocolo TCP/IP.
Vale pontuar que a comunicação não chega a ser totalmente independente, afinal ainda é necessário o transporte por meio do protocolo.
Porém, a interface entre os processos acontece em uma porta diferente e torna todo o projeto mais centralizado por limitar a comunicação entre dois processos distintos.

Como funciona um socket de rede?

Os sockets funcionam a partir da arquitetura Client/Server, sendo a mais comuns em diferentes tipos de projetos. Aqui, é necessário ter um cliente e um servidor, e ambos precisam da mesma API do socket.
Para entender melhor, basta considerar um processo de comunicação entre duas pessoas. Toda conversa depende de ao menos duas pessoas. O mesmo vale para aplicações.
Neste contexto, um servidor ssh precisa do seu cliente e assim por diante. Por conta disso, você encontra ssh/sshd; chromium/nginx; ftp/ftpd; etc.
Especialmente no caso das distro Linux, a API realiza leituras a partir do sistema. Ou seja, a linguagem do SO usa, obrigatoriamente, a API para então realizar a leitura dos sockets.
Portanto, o kernel da distro é o único que abre um socket. Indo além disso, ele também faz o controle dos programas em execução que têm ou não o acesso a ler e escrever determinadas aplicações em um socket aberto.
Inclusive, este recurso está entre os principais diferenciais das distro Linux e responsável por garantir que os SOs baseados em Linux sejam mais seguros para diferentes tipos de projetos.
