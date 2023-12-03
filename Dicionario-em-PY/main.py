from random import randrange

'''arthur = {
  "nome":"Arthur Nogueira Oliveira",
  "jogos_favoritos":["LOL","MK","For Honor","FIFA"],
  "idade": 16,
  "linguagens":["C#","Python","HTML","CSS","JS"],
  "game_engines":["Unity","GameMaker","Unreal"],
  "desing_softwares":["Aseprite","PH"]
}'''



pessoas = ["Arthur","Júnior","João Pedro", "Vitor", "Rafael", "João Alfredo"]

jogos = [{
  "nome": "MK",
  "estilo": "luta",
  "modos": ["historia","vs bot","online","torres"]
},{
  "nome": "CS:GO",
  "estilo": "FPS",
  "modos": ["Braço direito","ranked","casual","mata mata"]
},{
  "nome": "Brawlhalla",
  "estilo": "luta",
  "modos": ["vs bot","2v2","1v1"]
},{
  "nome": "LOL",
  "estilo": "moba",
  "modos": ["normal","aram","urf","ranked"]
},{
  "nome": "FIFA",
  "estilo": "futebol",
  "modos": ["UT","Carreira","Online"]
},{
  "nome": "Paladins",
  "estilo": "FPS",
  "modos": ["cerco","mata mata","ranked"]
}]

qual_jogo = randrange(0,len(jogos))
qual_modo1 = randrange(0,4)
qual_modo2 = randrange(0,3)

if (qual_jogo == 0 or qual_jogo == 1 or qual_jogo == 3):
  print(f"{pessoas[randrange(0,len(pessoas))]} vai jogar {jogos[qual_jogo]['nome']} estilo {jogos[qual_jogo]['estilo']} modo {jogos[qual_jogo]['modos'][qual_modo1]}")

elif (qual_jogo == 2 or qual_jogo == 4 or qual_jogo == 5):
  print(f"{pessoas[randrange(0,len(pessoas))]} vai jogar {jogos[qual_jogo]['nome']} estilo {jogos[qual_jogo]['estilo']} modo {jogos[qual_jogo]['modos'][qual_modo2]}")


