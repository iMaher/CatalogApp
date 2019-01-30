from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Categories, Base, CatalogItems, User

engine = create_engine('sqlite:///catalogapp.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(
    name="Maher Malibari",
    email="imaher.it@gmail.com",
    picture="""https://banner2.kisspng.com/20180423/zoq/kisspng-transistor-
            radio-sword-electronic-circuit-
            5ade12d14f58f2.834729861524503249325.jpg""")
session.add(User1)
session.commit()

# Menu for Computers
cat1 = Categories(name="Mac")
session.add(cat1)
session.commit()

item1 = CatalogItems(
    user_id=1,
    name="MacBook",
    description="""The goal with MacBook was to do the impossible engineer a
                full-size experience into the thinnest,lightest Mac notebook
                yet
                .And not only is it compact its more powerful than ever.
                 The new MacBook delivers up to 20 percent faster performance
                 with new seventh-generation Intel Core processors,and faster
                 SSD storage.""",
    categories=cat1)

session.add(item1)
session.commit()


item2 = CatalogItems(user_id=1, name="MacBook Air",
                     description="""The most loved Mac is about to make you
                      fall in love all over again. Available in silver,
                      space gray, and gold, the new thinner and lighter
                       MacBook Air features a brilliant Retina display,
                       Touch ID, the latest-generation keyboard, and a Force
                       Touch trackpad. The iconic wedge is created from 100
                       percent recycled aluminum, making it the greenest Mac
                       ever.1 And with all-day battery life, MacBook Air is
                       your perfectly portable, do-it-all notebook.""",
                     categories=cat1)

session.add(item2)
session.commit()

item3 = CatalogItems(
    user_id=1,
    name="MacBook Pro",
    description="""More power.More performance.More pro.
     With great power comes great capability. MacBook Pro elevates the
      notebook to a whole new level of performance and portability. Wherever
      your ideas take you, you'll get there faster than ever with
      high-performance processors and memory, advanced graphics, blazing-fast
      storage, and more.""",
    categories=cat1)

session.add(item3)
session.commit()


item4 = CatalogItems(user_id=1, name="iMac",
                     description="""A desktop experience that draws
                     you in and keeps you there. This
 is the idea behind today's iMac. And now that idea is more powerful than ever.
  The new iMac is packed with all-new processors, the latest graphics
   technologies, innovative storage, and higher-bandwidth connectivity.
   And it all comes to life on the brightest and most colorful Retina display
   iMac has ever seen. So you get an even more immersive experience - and a
   scintillating new way to take it all in.""",
                     categories=cat1)

session.add(item4)
session.commit()

item5 = CatalogItems(user_id=1, name="iMac Pro",
                     description="""Pros love iMac. So we created one just for
                     you. It's packed with the most powerful graphics and
                     processors ever in a Mac, along with the most advanced
                     storage, memory, and I/O - all behind a breathtaking
                     Retina 5K display in a sleek, all-in-one design. For
                     everyone from photographers to video editors to 3D
                     animators to musicians to software developers to
                     scientists, iMac Pro is ready to turn your biggest ideas
                     into your greatest work.""",
                     categories=cat1)

session.add(item5)
session.commit()

item6 = CatalogItems(
    user_id=1,
    name="Mac Pro",
    description="""Mac has always been built around a singular vision:
     to create machines that are as powerful and functional as they are
      beautiful and intuitive. Mac Pro is a stunning realization of that
       ideal. All the elements that define a pro computer - graphics, storage,
        expansion, processing power, and memory - have been rethought and
         reengineered. So you have the power and performance to bring your
          biggest ideas to life.""",
    categories=cat1)

session.add(item6)
session.commit()

item7 = CatalogItems(user_id=1, name="Mac Mini",
                     description="""In addition to being a great desktop
                     computer, Mac mini powers everything from home automation
                      to giant render farms. And now with eighth-generation
                      Intel quad-core and 6-core processors and Intel UHD
                       Graphics 630, Mac mini has even more compute power
                        for industrial-grade tasks. So whether you're running
                         a live concert sound engine or testing your latest
                          iOS app, Mac mini is the shortest distance between
                           a great idea and a great result.""",
                     categories=cat1)

session.add(item7)
session.commit()


# Menu for Tablets
cat2 = Categories(name="iPad")

session.add(cat2)
session.commit()


item1 = CatalogItems(
    user_id=1,
    name="iPad Pro",
    description="""It's all new, all screen, and all powerful. Completely
     redesigned and packed with our most advanced technology, it will make
      you rethink what iPad is capable of.""",
    categories=cat2)

session.add(item1)
session.commit()

item2 = CatalogItems(
    user_id=1,
    name="iPad Pro 10.5inch",
    description="""It's all new, all screen, and all powerful. Completely
     redesigned and packed with our most advanced technology, it will make
      you rethink what iPad is capable of.""",
    categories=cat2)

session.add(item2)
session.commit()

item3 = CatalogItems(
    user_id=1,
    name="iPad Pro 9.7inch",
    description="""It's all new, all screen, and all powerful. Completely
     redesigned and packed with our most advanced technology, it will make
      you rethink what iPad is capable of.""",
    categories=cat2)

session.add(item3)
session.commit()



item5 = CatalogItems(
    user_id=1,
    name="iPad mini 4",
    description="""There's more to mini than meets the eye. iPad mini 4 puts
     uncompromising performance and potential in your hand. It's thinner and
      lighter than ever before, yet powerful enough to help you take your ideas
       even further.""",
    categories=cat2)

session.add(item5)
session.commit()


# Menu for Phones
cat3 = Categories(name="iPhone")

session.add(cat3)
session.commit()


item1 = CatalogItems(
    user_id=1,
    name="iPhone Xs",
    description="""Welcome to the big screens. Super Retina in two sizes -
     including the largest display ever on an iPhone. Even faster Face ID.
      The smartest, most powerful chip in a smartphone. And a breakthrough
       dual-camera system with Depth Control. iPhone XS is everything you
       love about iPhone. Taken to the extreme.""",
    categories=cat3)

session.add(item1)
session.commit()

item2 = CatalogItems(
    user_id=1,
    name="iPhone XR",
    description="""All-screen design. Longest battery life ever in an iPhone.
    Fastest performance. Water and splash resistant. Studio-quality photos and
    4K video. More secure with Face ID. The new iPhone XR. It's a brilliant
     upgrade.""",
    categories=cat3)

session.add(item2)
session.commit()


# Menu for Watchs
cat4 = Categories(name="Watch")

session.add(cat4)
session.commit()


item1 = CatalogItems(
    user_id=1,
    name="Apple Watch Series 4",
    description="""All new. For a better you. Introducing Apple Watch Series 4.
     Fundamentally redesigned and re-engineered to help you stay even more
      active, healthy, and connected.""",
    categories=cat4)

session.add(item1)
session.commit()

item2 = CatalogItems(
    user_id=1,
    name="Apple Watch Nike+",
    description="""Apple Watch Nike+ is the perfect running partner with the
     Nike Run Club app. But for most people, that's just one facet of their
     training. That's why Nike created the Nike Training Club app to let you
      tap into a world of different workouts and experts. Together they'll help
       you build the endurance and strength to take your fitness to the next
        level.""",
    categories=cat4)

session.add(item2)
session.commit()

item3 = CatalogItems(
    user_id=1,
    name="Apple Watch Hermes",
    description="""A partnership based on parallel thinking, singular vision,
     and mutual regard continues with a fresh new expression. The latest Apple
      Watch Hermes collection showcases boldly colorful leather bands and a
       delightful new watch face designed with Apple. It's the ultimate tool
        for modern life - now with a dash of sophisticated whimsy.""",
    categories=cat4)

session.add(item3)
session.commit()


# Menu for TV
cat5 = Categories(name="Apple TV")

session.add(cat5)
session.commit()


item1 = CatalogItems(
    user_id=1,
    name="Apple TV 4K",
    description="""Cinematic in every sense. Apple TV 4K lets you watch movies
    and shows in amazing 4K HDR - and now it completes the picture with
    immersive sound from Dolby Atmos.1 It streams your favorite channels live.
    Has great content from apps like Netflix, Amazon Prime Video, and ESPN.2
    And thanks to Siri, you can control it all with just your voice.""",
    categories=cat5)

session.add(item1)
session.commit()

item2 = CatalogItems(
    user_id=1,
    name="Apple TV",
    description="""Cinematic in every sense. Apple TV lets you watch movies and
     shows in amazing 4K HDR - and now it completes the picture with immersive
     sound from Dolby Atmos.1 It streams your favorite channels live. Has great
     content from apps like Netflix, Amazon Prime Video, and ESPN.2 And thanks
     to Siri, you can control it all with just your voice.""",
    categories=cat5)

session.add(item2)
session.commit()


# Menu for other's
cat6 = Categories(name="Others")

session.add(cat6)
session.commit()


item1 = CatalogItems(
    user_id=1,
    name="Apple Pencil",
    description="""Introducing the all-new Apple Pencil. Apple Pencil set the
     standard for how drawing, note-taking, and marking up documents should
      feel - intuitive, precise, and magical. The new Apple Pencil takes that
       experience even further. Now you can pair and charge wirelessly and
        change tools, like a pencil to an eraser, with a simple double-tap.
         Go ahead, make your mark.""",
    categories=cat6)

session.add(item1)
session.commit()

item2 = CatalogItems(
    user_id=1,
    name="Smart keyboard",
    description="""Full-size keyboard. Front and back protection. The new Smart
     Keyboard Folio is designed to deliver a great typing experience on a
      full-size keyboard whenever you need it. Its durable, lightweight cover
       protects both the front and back of your new 11-inch or 12.9-inch iPad
        Pro. Simply attach it to your new iPad Pro and type away.""",
    categories=cat6)

session.add(item2)
session.commit()

item3 = CatalogItems(
    user_id=1,
    name="AirPods",
    description="""Just take them out and they're ready to use with all your
    devices. Put them in your ears and they connect instantly. Speak into them
    and your voice sounds clear. Introducing AirPods. Simplicity and
     technology, together like never before. The result is completely
      magical.""",
    categories=cat6)

session.add(item3)
session.commit()

item4 = CatalogItems(
    user_id=1,
    name="HomePod",
    description="""The new sound of home. HomePod is a breakthrough speaker
     that adapts to its location and delivers high-fidelity audio wherever
      it's playing. Together with Apple Music and Siri, it creates an entirely
       new way for you to discover and interact with music at home. And it can
        help you with everyday tasks - and control your smart home - all with
         just your voice.""",
    categories=cat6)

session.add(item4)
session.commit()

print "added menu items!"
