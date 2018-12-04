import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
from discord import Game
 
 
Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()
 
 
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='testbot'))
    print('Ready, Freddy') 
 
 
@client.event
async def on_message(message):
    





    if message.content == '!ralseihola':
        await client.send_message(message.channel, random.choice(['https://ibb.co/BfR94WG','https://ibb.co/BnzpMrf','https://ibb.co/kJ1cSzF','https://ibb.co/mtcRyc6']))
    if message.content == '!ralseihi':
        await client.send_message(message.channel, random.choice(['https://ibb.co/BfR94WG','https://ibb.co/BnzpMrf','https://ibb.co/kJ1cSzF','https://ibb.co/mtcRyc6']))
    if message.content == '!ralseiadios':
        await client.send_message(message.channel, random.choice(['https://ibb.co/ZgmsVmS','https://ibb.co/fXSC4HS','https://ibb.co/ZXc7Drk']))
    if message.content == '!ralseibye':
        await client.send_message(message.channel, random.choice(['https://ibb.co/ZgmsVmS','https://ibb.co/fXSC4HS','https://ibb.co/ZXc7Drk']))
    if message.content == '!ralseihelp':
        await client.send_message(message.channel, random.choice(['https://ibb.co/yktvyYy']))
    if message.content == '!rhelp':
        await client.send_message(message.channel, random.choice(['https://ibb.co/yktvyYy']))
    if message.content == '!ralseihelp2':
        await client.send_message(message.channel, random.choice(['https://ibb.co/F8Mjr9D']))
    if message.content == '!rhelp2':
        await client.send_message(message.channel, random.choice(['https://ibb.co/F8Mjr9D']))
    if message.content == '!rhelp3':
        await client.send_message(message.channel, random.choice(['https://ibb.co/JQcgRCz']))
    if message.content == '!ralseihelp3':
        await client.send_message(message.channel, random.choice(['https://ibb.co/JQcgRCz']))
    if message.content == '!tellstory':
        await client.send_message(message.channel, random.choice(['https://www.youtube.com/watch?v=qiagtspfoZY']))
    if message.content == '!tellgun':
        await client.send_message(message.channel, random.choice(['hhttps://www.youtube.com/watch?v=a7MObuHcKp0']))
    if message.content == '!tellincident':
        await client.send_message(message.channel, random.choice(['https://www.youtube.com/watch?v=tLj57khiTl4']))
    if message.content == '!playsans':
        await client.send_message(message.channel, random.choice(['https://jcw87.github.io/c2-sans-fight/']))
    if message.content == '!playraider':
        await client.send_message(message.channel, random.choice(['http://xproger.info/projects/OpenLara/']))
    if message.content == '!playmcommand':
        await client.send_message(message.channel, random.choice(['https://my.ign.com/atari/missile-command']))
    if message.content == '!playtetris':
        await client.send_message(message.channel, random.choice(['https://tetris.com/play-tetris']))
    if message.content == '!rcook':
        await client.send_message(message.channel, random.choice(['https://ibb.co/x5rYdFy','https://ibb.co/2g0wmQy','https://ibb.co/ypY2syy','https://ibb.co/qNFKhnQ']))
    if message.content == '!rcook':
        await client.send_message(message.channel, random.choice(['https://viruji.andaluciainformacion.es/wp-content/uploads/2018/09/pizza-3000274_960_720.jpg','https://www.cocinavital.mx/wp-content/uploads/2017/08/lasana-napolitana.jpg','https://cocina-casera.com/wp-content/uploads/2012/12/espaguetis-bolonesa.jpg','https://digitaldeleon.com/wp-content/uploads/2018/08/digitaldeleon-com-2018-08-31-11-2609-776852-640x350.jpg','https://www.cscassets.com/recipes/wide_cknew/wide_24792.jpg','https://www.handletheheat.com/wp-content/uploads/2014/02/Homemade-Crepes-01-Square-550x550.jpg','https://cocina-casera.com/wp-content/uploads/2015/11/paella-mixta-receta-casera.jpeg','https://singularityhub.com/wp-content/uploads/2018/08/homemade-grilled-hamburger-on-plate-red_shutterstock_135216374.jpg','http://www.carnevillamaria.com/blog/wp-content/uploads/2016/03/filetes-rusos-carne-villa-maria-online.jpg','https://search.chow.com/thumbnail/1280/800/www.chowstatic.com/assets/models/promotions/photos/29385/original/spanish-horchata-recipe-chowhound.jpg','https://upload.wikimedia.org/wikipedia/commons/3/31/Ice_Cream_dessert_02.jpg','https://www.hogarmania.com/archivos/201105/sandwich-mixto-xl-848x477x80xX.jpg','https://i.ytimg.com/vi/B806Innc068/maxresdefault.jpg','http://as01.epimg.net/deporteyvida/imagenes/2018/05/07/portada/1525714597_852564_1525714718_noticia_normal.jpg','https://www.simplyrecipes.com/wp-content/uploads/2016/07/2016-08-12-BLT-Salad-3.jpg','https://img.delicious.com.au/5PiJMQy-/w759-h506-cfill/del/2015/12/cornetti-italian-croissants-24713-1.jpg','https://static01.nyt.com/images/2018/02/21/dining/00RICEGUIDE8/00RICEGUIDE8-threeByTwoMediumAt2X.jpg','https://st.depositphotos.com/1328914/3359/i/950/depositphotos_33591071-stock-photo-tacos.jpg','https://losandes.com.ar/uploads/2018/09/image5bafd801b6f9e.jpg','https://images.theconversation.com/files/111932/original/image-20160218-1252-1gu3108.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=496&fit=clip']))
    if message.content == '!rcook':
        await client.send_message(message.channel, random.choice(['https://ibb.co/DVcSgCB','https://ibb.co/hXy5rDy','https://ibb.co/RjScv0y']))
    if message.content == '!rmalo':
        await client.send_message(message.channel, random.choice(['https://ibb.co/094gKjS','https://ibb.co/P9r8kqX','https://ibb.co/k13602P']))
    if message.content == '!rbueno':
        await client.send_message(message.channel, random.choice(['https://ibb.co/NNYP0wj','https://ibb.co/w0KKnNv','https://ibb.co/qWtmsFb']))
    if message.content == '!rbake':
        await client.send_message(message.channel, random.choice(['hhttps://ibb.co/0mS7QrM','https://ibb.co/8n3p388']))
    if message.content == '!rbake':
        await client.send_message(message.channel, random.choice(['https://i.pinimg.com/236x/72/62/5f/72625f8fedc4a5cb2c70d0a936c9e098.jpg',]))
    if message.content == '!rchiste':
        await client.send_message(message.channel, random.choice(['https://ibb.co/wzqBmpr','https://ibb.co/5B0W1Y9','https://ibb.co/FKT38tR','https://ibb.co/jL8tgqR','https://ibb.co/kXd6Y8q']))
    if message.content == '!rjojo':
        await client.send_message(message.channel, random.choice(['https://pics.me.me/fix-that-spaghetti-im-gonna-35381196.png','https://i.kym-cdn.com/entries/icons/facebook/000/018/329/duwang_(1).jpg','https://pics.me.me/stand-masteri-speedwagon-istand-name-speedwagon-ucabil-the-perfect-stando-31840297.png','https://pm1.narvii.com/6531/2e318d6a27412e1ec60440c606fbcdd20f604fe6_hq.jpg','https://ih0.redbubble.net/image.434260546.2457/throwpillow,small,750x1000-bg,f8f8f8.u1.jpg','https://img.memecdn.com/kakoyin-and-dio-talk-about-art_o_5684563.jpg','https://i.kym-cdn.com/photos/images/newsfeed/000/750/827/519.jpg','https://i.kym-cdn.com/photos/images/newsfeed/001/167/460/698.jpg','https://i.pinimg.com/originals/6c/aa/2e/6caa2e86580bf7d01b89d716eefcc119.png','https://i.pinimg.com/originals/b0/44/28/b04428cc89b133d94a0ce140e85934b3.jpg','https://vignette.wikia.nocookie.net/jjba/images/6/6c/Jotaro_yells_at_Josuke.png/revision/latest?cb=20160715205903','http://i.imgur.com/yOV27jy.png','https://i.kym-cdn.com/photos/images/newsfeed/001/128/851/f4b.jpg','https://i.kym-cdn.com/photos/images/original/000/624/276/3ee.gif','https://media3.giphy.com/media/1Erx4cu7f9IBi/giphy.gif','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-mEZqu3nhUZpx_KS-x72194__URwq5P7OZYICWE_D9EXcQNYJug','https://i.pinimg.com/originals/9a/80/6e/9a806e9140dd1d414cf55bbd880a2a10.png','https://i.kym-cdn.com/photos/images/newsfeed/001/195/600/cd6.png','https://i.imgur.com/mJak8qN.jpg','https://vignette.wikia.nocookie.net/jjba/images/f/fe/43f.jpg/revision/latest?cb=20130130073453','https://i.ytimg.com/vi/DRMPQvLvJx4/maxresdefault.jpg']))
    if message.content == '!rhug':
        await client.send_message(message.channel, random.choice(['https://pre00.deviantart.net/05c7/th/pre/i/2018/307/a/3/hug_ralsei_by_xyronii-dcr2la2.png','https://pre00.deviantart.net/1c84/th/pre/i/2018/311/d/f/deltarune_kris_and_ralsei_hug_by_htpencil13-dcrej43.png','https://orig00.deviantart.net/651c/f/2018/319/1/1/hug_ralsei__by_misakarin-dcs1jyt.png','https://a.wattpad.com/cover/168389643-352-k991697.jpg','https://pre00.deviantart.net/b262/th/pre/f/2018/307/f/7/hug_ralsei_by_s1ug-dcr2rwr.png','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWHNz5Q1PeXC9M_Qp5HyC9FByd75BT2NFHHHIM-AWKW4sKDXkJXeveRBA','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvhK2PnHhO7MRsmz6pnnew4VRqvttxf1i3xCDL_fdm95hK-YbR','https://scontent-lax3-1.cdninstagram.com/vp/5267d578ebdb9e05784e5443a86269e8/5C6D0010/t51.2885-15/e35/s480x480/44238835_824511427719110_2939012261303334_n.jpg','https://i.ytimg.com/vi/PJaW4AeoI5A/maxresdefault.jpg','https://ibb.co/PZKZ0NG']))
    if message.content == '!rsing':
        await client.send_message(message.channel, random.choice(['https://files.gamebanana.com/img/ico/sprays/5bec40db9c258.gif']))
    if message.content == '!rsing':
        await client.send_message(message.channel, random.choice(['Espero que te guste como canto!']))
    if message.content == '!rangry':
        await client.send_message(message.channel, random.choice(['https://pbs.twimg.com/media/DsgCFGhW0AA3bKM.jpg']))
    if message.content == '!rbored':
        await client.send_message(message.channel, random.choice(['https://pbs.twimg.com/profile_images/1059672657950621698/plrqftoY.jpg']))
    if message.content == '!rshy':
        await client.send_message(message.channel, random.choice(['https://static.tvtropes.org/pmwiki/pub/images/ralsei.png']))
    if message.content == '!rhappy':
        await client.send_message(message.channel, random.choice(['https://preview.redd.it/jy0krbkgjmv11.png?width=227&auto=webp&s=131907ae7675e3c925949f1cb12d0cfc0fabb0da']))
    if message.content == '!rwhat':
        await client.send_message(message.channel, random.choice(['https://img.fireden.net/v/thumb/1541/05/1541051168252s.jpg']))
    if message.content == '!rdelete':
        await client.send_message(message.channel, random.choice(['https://i.redd.it/t0m9cw7fxxw11.jpg','https://files.facepunch.com/forum/upload/213180/a9c908e8-82b2-41b7-98a4-1b379fb5570d/ralsei%20delet%20this.png','https://i.redd.it/7tp9zjwmpqw11.jpg']))
    if message.content == '!rwork':
        await client.send_message(message.channel, random.choice(['https://i.pinimg.com/originals/fc/79/38/fc793861b3db611edabec65edcaaa3c3.gif']))
    if message.content == '!rwork':
        await client.send_message(message.channel, random.choice(['Beep Boop Beep Beep Boop Beep']))  
    if message.content == '!rhit':
        await client.send_message(message.channel, random.choice(['https://i.kym-cdn.com/photos/images/original/001/428/856/516.gif']))
    if message.content == '!rclap':
        await client.send_message(message.channel, random.choice(['https://i.redd.it/ji4xmsvhrsw11.gif']))
    if message.content == '!rdance':
        await client.send_message(message.channel, random.choice(['https://orig00.deviantart.net/3e9a/f/2018/309/7/6/76c38c8dae8ba3d15d3554d06bd4ecd5-dcrb2l0.gif','https://66.media.tumblr.com/731c6087aa0820765e953ac78b827518/tumblr_phz0jizEsn1v04u6vo2_500.gif','https://media1.tenor.com/images/929f74fa9c1a2028456b6f9d60596b54/tenor.gif?itemid=12823779']))
    if message.content == '!rjojodance':
        await client.send_message(message.channel, random.choice(['https://i.kym-cdn.com/photos/images/original/001/434/357/bce.gif']))
    if message.content == '!rmeme':
        await client.send_message(message.channel, random.choice(['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8l8OGlHfmc1XU-XC-QXFQyXNZjaKB0DhGHv3EIEPBNQp47aumrg','https://i.kym-cdn.com/photos/images/original/001/428/163/89b.png','https://hugelolcdn.com/i/558531.jpg','https://external-preview.redd.it/tG8G80gJ95B0yAxUqOR5FrLF-iNGHP8DeA2n3nVUMo4.jpg?s=2c402a307ff0eddf0948521db1eae14dedab402e','https://pbs.twimg.com/media/Drf3RvBU0AAIQXC.jpg','https://preview.redd.it/tatpnmxg59x11.png?width=300&auto=webp&s=cc479faf34ca88f5e2348be439ebdb329dca3ad8','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRrJg6oNoqbJe2LB0FlrwZ0jnrdnzEvR9L-SiJovTLBrRAWAv0EgneWCgI','https://pbs.twimg.com/media/Dsj5w3YU0AAQRJQ.jpg','https://i.kym-cdn.com/photos/images/newsfeed/001/434/872/190.png','https://i.kym-cdn.com/photos/images/original/001/427/569/01d.gif','https://scontent-amt2-1.cdninstagram.com/vp/7cf5e0ca535b044a1ca7a1759edcc7dd/5C6AADCE/t51.2885-15/e35/c35.0.429.429/44485523_348831652350338_1706431970991345663_n.jpg','https://scontent-amt2-1.cdninstagram.com/vp/7cf5e0ca535b044a1ca7a1759edcc7dd/5C6AADCE/t51.2885-15/e35/c35.0.429.429/44485523_348831652350338_1706431970991345663_n.jpg','https://preview.redd.it/h8roay4tzgx11.jpg?width=480&auto=webp&s=af0a5753495ba7f190f03303327a5a466b6ddb29','https://i.imgur.com/zUJCOaq.png','https://ibb.co/rM6dZfF','https://scontent-amt2-1.cdninstagram.com/vp/7cf5e0ca535b044a1ca7a1759edcc7dd/5C6AADCE/t51.2885-15/e35/c35.0.429.429/44485523_348831652350338_1706431970991345663_n.jpg']))
    if message.content == '!rgive':
        await client.send_message(message.channel, random.choice(['https://i.pinimg.com/originals/e4/3b/3a/e43b3acd5df1dac947e1eccb0b57e31d.jpg','https://i.pinimg.com/originals/51/a8/a7/51a8a7d817b802c1c45c7b354735b847.jpg','https://i.pinimg.com/originals/46/84/9c/46849cf225e6daaac77fa5e152a0509a.jpg','https://66.media.tumblr.com/5a9cfbd6b83d636af8fd6b495ea51819/tumblr_phsg96QdzG1uzzuc5o1_1280.png',]))
    if message.content == '!rcute':
        await client.send_message(message.channel, random.choice(['https://pre00.deviantart.net/5f70/th/pre/i/2018/324/3/a/ralsei_take_off_his_hat_by_sansurichin-dcsfyy0.png','https://i.pinimg.com/originals/27/2c/c8/272cc81a6213a77204ef67dc1197a6fe.gif','https://i.kym-cdn.com/photos/images/newsfeed/001/430/229/3b7','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0FiSD63lSCgje4fIzD7VxRqkhjCxBk5VfQc3F4gpbNAq9t_h7p5J8_tk','https://preview.redd.it/lsho7ax9umx11.jpg?width=978&auto=webp&s=bcebae7e7ccd01b48c10a1042e71e2bde40ef6b3','https://i.ytimg.com/vi/-nT-3Ud16ao/maxresdefault.jpg','https://orig00.deviantart.net/d742/f/2018/308/b/2/ralsei_by_artist_squared-dcr7p5g.gif','https://memestatic.fjcdn.com/large/pictures/24/b4/24b429_6802893.jpg',]))
    if message.content == '!rheh':
        await client.send_message(message.channel, random.choice(['https://i.redd.it/7ilk9uha4jx11.png']))
    if message.content == '!rheh':
        await client.send_message(message.channel, random.choice(['Heh Heh Heh']))
    if message.content == '!rfluffy':
        await client.send_message(message.channel, random.choice(['https://i.pinimg.com/originals/41/aa/58/41aa58ab8b2e3ca5740ce6b6f97fdafc.gif','https://i.kym-cdn.com/photos/images/original/001/428/074/f91.jpg','https://i.imgur.com/RMZPHQZ.jpg']))
    if message.content == '!rcheer':
        await client.send_message(message.channel, random.choice(['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSo7sUZxA_fKzuWJPhb8iPqOfMiAAL5YhyxfgqK3_hRCkSNDrU3']))
    if message.content == '!rdelta':
        await client.send_message(message.channel, random.choice(['https://i.kym-cdn.com/photos/images/original/001/427/776/63b.gif']))
    if message.content == '!rrune':
        await client.send_message(message.channel, random.choice(['https://thumbs.gfycat.com/GrayFrequentAlaskajingle-small.gif']))
    if message.content == '!r???':
        await client.send_message(message.channel, random.choice(['https://i.imgur.com/oOF8IXq.gif?noredirect']))
    if message.content == '!repic':
        await client.send_message(message.channel, random.choice(['https://i.redd.it/dn5w5bsp5tv11.jpg']))
    if message.content == '!rthot':
        await client.send_message(message.channel, random.choice(['https://i.pinimg.com/236x/35/e1/74/35e174321552479d2bc1cea180f8d59a.jpg']))
    if message.content == '!rping':
        await client.send_message(message.channel, random.choice(['https://ibb.co/SxbZ8gK']))
    if message.content == '!ralsei que tal el dia':
        await client.send_message(message.channel, random.choice(['hhttps://ibb.co/sWyC6m0','https://ibb.co/7yYzdLY']))
    if message.content == '!ralsei que tal el dia?':
        await client.send_message(message.channel, random.choice(['hhttps://ibb.co/sWyC6m0','https://ibb.co/7yYzdLY']))
    if message.content == '!ralsei te quiero':
        await client.send_message(message.channel, random.choice(['https://ibb.co/FsKQ8N5']))
    if message.content == '!ralsei te quiero mucho':
        await client.send_message(message.channel, random.choice(['https://ibb.co/qDPgdWZ']))
    if message.content == '!ralsei que tal el dia':
        await client.send_message(message.channel, random.choice(['hhttps://ibb.co/sWyC6m0','https://ibb.co/7yYzdLY']))
    if message.content == '!ralsei que tal el dia?':
        await client.send_message(message.channel, random.choice(['hhttps://ibb.co/sWyC6m0','https://ibb.co/7yYzdLY']))
    if message.content == '!ralsei gracias':
        await client.send_message(message.channel, random.choice(['https://ibb.co/r2FrKkN']))
    if message.content == '!ralsei abrazame':
        await client.send_message(message.channel, random.choice(['https://ibb.co/rfgnfPv','https://ibb.co/RSnzzqH','https://ibb.co/B3K42bZ','https://ibb.co/jVQv35X','https://ibb.co/0BvzBb2']))
    if message.content == '!rabrazame':
        await client.send_message(message.channel, random.choice(['https://ibb.co/rfgnfPv','https://ibb.co/RSnzzqH','https://ibb.co/B3K42bZ','https://ibb.co/jVQv35X','https://ibb.co/0BvzBb2']))
    if message.content == '!rfag':
        await client.send_message(message.channel, random.choice(['https://www.youtube.com/watch?v=PNups4pAPr8']))
    if message.content == '!reaster':
        await client.send_message(message.channel, random.choice(['https://ibb.co/CJDBfXC']))
    if message.content == '!regg':
        await client.send_message(message.channel, random.choice(['https://ibb.co/MD8vvkm']))







    if message.content == '!rcredits':
        await client.send_message(message.channel, random.choice(['https://ibb.co/gt85JPF']))



client.run(os.getenv('TOKEN'))


