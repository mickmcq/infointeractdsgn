% HCIN 620 Information and Interaction Design
% Supplemental Notes
% Spring 2015

# Day 01 prototyping tools

You volunteered the names of prototyping tools you've used.

- Axure
- Indigo Studio
- Balsamiq
- Visio
- Flash Catalyst
- Dreamweaver
- Actionscript

One kind of prototyping tool you may have thought too rudimentary to mention would be any graphics package with layering, such as Photoshop or Sketchbook Pro. You can use different layers in the same file to represent transitions from one app state to another. The advantage of using a tool like this is that you may already know the tool and won't waste time on it, instead spending your time on developing your ideas.

# Day 01 Missing from Syllabus

Peer evaluations will count! Your projects will be graded as groups but you will submit anonymous peer evaluations that may affect individual grades.

Also, the ad hoc group work will be evaluated, in part, on what you put into your notebook. Thus, two people in the same group could receive different grades for the differing quality of their notebooks.

# Day 01 introductions

Everyone gave names they prefer to be called by and told a little of their past and future with HCI. Feel free to give me an update for your section.

## Naina

### past
undergrad in bio; worked in biotech; stumbled into hci; doing a project designing an interface to db

### future
user centered design in edu companies

## Jai

### past
undergrad in cs; did motion capture and augmented reality interface

### future
develop innovative tech ... medical

## Shreya

### past
undergrad cs: web app developer backend

### future
accessibility and google glass; maybe research

## Kasmira

### past
graphic design, print media

### future
research, ux designer

## Abdullah

### past
bus admin econ; now research asst

### future
improve web phone apps

## Brian

### past
psych, it help desk;

### future
ux design, gaming company

## Katherine

### past
psych, took crosslisted hci class, web design, app devel

### future
ux design for gaming company or possibly robotics

## Ashley

### past
imaging sci; developed training tool for disaster mgt through ARCGis and Python

### future
eLearning for disaster management, social media and disaster management

## Anthony

### past
systems engr, sw devel, saw many projects where users had problems managers didn't notice

### future
ux design, iot (internet of things)

## Hongbo

### past
info security, bus mgt, sys engr, games

### future
imagineer at Disney; but first a startup

## Alice

### past
multimedia telcom, image processing robot, multimedia system design, drawing for 12 years

### future
combination of drawing ui graphic design

## Ziyan

### past
mathematics no experience in hci (computational mathematics)

### future
smart home, small devices (Christopher Alexander)

## Yebai

### past
telecomm in past, saw projects bad in design

### future
virtual reality, user interface design

## Alessandra

### past
software engineer, proj mgr for decade, delivered projects to customers who were upset by interfaces

### future
will work with different mindset same field

## Tiago

### past
cs software dev for 6 yrs; embedded, mobile

### future
research with digital fabrication

## Raghu

### past
cs engr, banking sw maint; implemented front and back end

### future
mobile dev and website dev

## Nathan

### past
cs engr, ui engineer for 6 years, web and mobile for consumer devices, augmented reality, brainwave computing, worked with SixthSense (Pranav Mistry, head of Samsung design in India)

### future
founder of startup and chief of design

## Goudam

### past
instr and control engr, cisco sw engr, web and mobile apps, gesture recognition devel

### future
ceo of own company, working as dev on gesture recognition

## KLN

### past
cs sw dev for insurance, on oracle frameworks web content mgt;

### future
improve ui design, be a good web devel

## Matt

### past
operations IT long time networking sys admin supporting users who can't use software; did gaming hci ui design

### future
gaming maybe , also linguist so language learning tools

# Day 01 Todo list

- Start reading Holtzblatt (2005), Rapid
  Contextual Design, Chapters 7 and 8
- Get a 5 $\times$ 8 in notebook
- Start forming teams---form a duo with someone
  like you, then put together two dissimilar duos
- Please don't take it personally when Mick
  disses products from your friends at BigCo---he'll say anything to get a laugh

# Day 02

## Definitions
We need working definitions of the words in the course title and description, even though these words are notoriously resistant to definition.

## A. Information

Defining information is the subject of a lot of fighting among people who get paid by the word. Some valuable information about information can be found in a dictionary.

\lstset{language=generic}

```
From The Collaborative International Dictionary of English v.0.48 [gcide]:

  Information \In`for*ma"tion\, n. [F., fr. L. information
     representation, conception. See {Inform}, v. t.]
     1. The act of informing, or communicating knowledge or
        intelligence.
        [1913 Webster]
              The active informations of the intellect.
                --South.
        [1913 Webster]

     2. Any fact or set of facts, knowledge, news, or
        advice, whether communicated by others or
        obtained by personal study and investigation;
        any datum that reduces uncertainty about the
        state of any part of the world;
        intelligence; knowledge derived from reading,
        observation, or instruction.
        [1913 Webster +PJC]
              Larger opportunities of information.
                --Rogers.
        [1913 Webster]
              He should get some information in the
              subject he intends to handle.
                --Swift.
        [1913 Webster]

     3. (Law) A proceeding in the nature of a prosecution
        for some offense against the government,
        instituted and prosecuted, really or nominally,
        by some authorized public officer on behalf of
        the government. It differs from an indictment in
        criminal cases chiefly in not being based on the
        finding of a grand jury. See {Indictment}.
        [1913 Webster]

     4. (Information Theory) A measure of the number of
        possible choices of messages contained in a
        symbol, signal, transmitted message, or other
        information-bearing object; it is usually
        quantified as the negative logarithm of the
        number of allowed symbols that could be
        contained in the message; for logarithms to the
        base 2, the measure corresponds to the unit of
        information, the hartley, which is log210, or
        3.323 bits; called also {information content}.
        The smallest unit of information that can be
        contained or transmitted is the bit,
        corresponding to a yes-or-no decision.

     5. (Computers) Useful facts, as contrasted with
        raw data; as, among all this data, there must
        be some interesting information.
        [PJC]

From WordNet (r) 3.0 (2006) [wn]:

  information
      n 1: a message received and understood
           [syn: {information}, {info}]
        2: knowledge acquired through study or
           experience or instruction
        3: formal accusation of a crime
        4: a collection of facts from which
           conclusions may be drawn;
           "statistical data"
           [syn: {data}, {information}]
        5: (communication theory) a numerical measure
           of the uncertainty of an outcome; "the signal
           contained thousands of bits of information"
           [syn: {information}, {selective information},
            {entropy}]

From The Free On-line Dictionary of Computing
     (20 July 2014) [foldoc]:

  information

     <data> The result of applying {data processing} to
     {data}, giving it context and meaning.  Information
     can then be further processed to yield {knowledge}.

     People or computers can find patterns in data to
     perceive information, and information can be used
     to enhance {knowledge}.  Since knowledge is
     prerequisite to wisdom, we always want more data
     and information.  But, as modern societies verge
     on {information overload}, we especially need
     better ways to find patterns.

     1234567.89 is data.

     "Your bank balance has jumped 8087% to $1234567.89"
     is information.

     "Nobody owes me that much money" is knowledge.

     "I'd better talk to the bank before I spend it,
     because of what has happened to other people"
     is wisdom.

     (2007-09-10)
```

Of particular note in the above definitions is that people define information according to their work. Claude Shannon popularized the notion of information as a message received and understood because that notion served his development of information theory, which underlies the field of network communication.

Some pundits like to posit a hierarchy of data, information, knowledge, and wisdom to support their work in a field called knowledge management. This field was popular about a dozen years ago and its influence had waned by the time the last definition above had been added to the Free Dictionary of Computing.

## B. Interaction

If we do the same dictionary exercise with the word Interaction,
we'll find that it has a little more
substance.  It means reciprocal action or influence and
that is something we can work with---how the computer and the human influence each other. Reciprocity is a key to understanding and influencing interaction.
## C. Design
Design
is one of the best of all possible words.  I
always like to look up words in the dictionary, but not
many have the power of the word design.  It's no
accident that it is chosen by propagandists in the
Intelligent Design wars.  It's a very powerful word.
It's all about making conscious choices.
Some definitions you will find in dictionaries include

a plan or drawing produced to show the
look and function or workings of a building, garment, or
other object before it is built or made


## Exercise:Draw a face

Draw two horizontal lines to divide your notebook page into three parts, so each part is about 2 and half inches high.

Step 1 is to draw a human face in left-facing profile in the top third of the page. It is important to do this before looking at steps 2 and 3. Looking at those steps will affect how you do this step, so quit reading this now and draw the face!

Step 2 is to first make sure you have already drawn a face in left-facing profile before reading further. Quit reading! Draw that face in the upper third of your page. Are you sure you've drawn it? Really? Okay, then, step 2 is to draw another face in the middle third of the page but, this time, make one change. Carefully plan this head so that the eye is halfway between the top of the skull and the chin.

Step 3 is to draw a third human face in left-facing profile in the bottom third of the page. This time, use a dime and a half dollar as aids. (This exercise was conceived in an era when half dollar coins were common---your teacher can supply an appropriately sized disk as a substitute.)


\begin{center}
\includegraphics[
  width=0.89\linewidth]
{dimeHalfDollar.jpg}
\end{center}



# Day 03

## More Intros
These are from online students, Steven and Nicole. It is possible I received one from Nicole but can not find it at this time.

## Steven

### past
Automation Technician, Electrical/Mechanical Engineering

## future
Researcher, user centered design in 3D printing and Drone technology

# Audience

## Academic Communities

The topic has been studied by three main academic
communities, human factors in engineering schools, human
computer interaction in computer science schools, and
management information systems in business schools.
Each of the three has specialized to some extent but
there are overlaps.

*Human factors* is usually the experimental study of how
people operate complex machines like automobiles, ships,
nuclear reactors, and aircraft. Since the researchers
who identify themselves this way are usually funded by
the military, they emphasize military applications
although their findings are usually applicable to some
degree outside the military.

*Human computer interaction* was, until recently,
primarily the study of one person
interacting with one computer system. This field began
with the study of users of expensive computers
performing specialized work tasks. During this period,
the field mainly studied how the user interface affected
some measure of productivity, usually in laboratory
studies. The second period of human
computer interaction research studied how people
interact casually with computers. This involved field
studies with very small groups of participants (formerly
called users) and very limited conclusions, appropriate
to the increased pace of change in user interfaces.

It's easier to identify past epochs than current ones.
It appears that human computer interaction has diverged
into two areas in the current era but the distinction is
harder to be certain of without the advantage of years
of hindsight. The two current branches appear to be
*ubiquitous computing* and *computing communities*.

*Ubiquitous computing* is an old term referring to computers
embedded in other devices and able to communicate with each
other. When first coined by Marc Weiser around 1991 (see
@Weiser1991), the term meant anything that was not a desktop
computer and concerned a small, well-defined community. Today,
almost no interaction between computers and people can be
defined with respect to only a desktop computer, rendering the
original definition moot. Now it seems to encompass all
computing.

*Community computing* is not a broadly used term by
itself. I am using it here to refer to the change in focus
from a single person (formerly a user) to many people
forming a community. Two types of communities exist,
communities that occur in computer networks and
communities that exist in the physical world. Since the
latter may share sewers, electrical utilities,
telecommunications utilities, roads, schools, local
governments, and other aspects of physical
infrastructure, it differs greatly from a network-only
community such as Facebook.

Communities that can function remotely, such as
Facebook, are the focus of study of Social Network
Analysis and Data Science, closely related fields whose
work is enabled by monitoring electronic communication
networks.

Communities that exist in physical space, such as
neighborhoods and cities, are obviously the subject of
study of architects, social workers, and people in many
other disciplines. Recently, many of these researchers
and their sponsors have aligned with computer scientists
identified with human computer interaction.

*Management Information Systems* a discipline professed in some
business schools, has long been concerned with the adoption and
diffusion of technological innovation in productive
organizations. This concern has led to many psychological
studies of groups of users of information systems in
organizations.

## Industrial and Government Communities

\begin{quotation}
\noindent
You want me to deprioritize
my current reports until you advise
of a status upgrade?

\medskip

\noindent
Make these your primary
action items.
\end{quotation}
\hfill ---dialog from *Fight Club*, 1999





### Suppliers of IT

Who are suppliers of IT in 2015? How do you measure? Public awareness? Market Capitalization? What industry codes are applicable?


### Customers of IT

This group can best be defined by students.

## Exercise: Picking up a Key

From *Making Comics* 1993, by Scott McCloud.
Chapter 1.  On page 13 is a
five-sentence story, told in 8 panels.  The character is
supposed to be a man.  Change the character to a woman
or creature or a different man.  Change the last
sentence (about the lion) to a different ending.  Choose
your own number of panels, anywhere from 7 to 9 panels.
Tell the story your own way. The five sentences are (1) A man is walking. (2) He finds a key on the ground. (3) He takes it with him, then he comes to a locked door. (4) He unlocks the door. (5) Then a hungry lion jumps out.

# Day 04

Today, the main activity will be to reflect on the pictures you drew on two previous days. The exercise today will be a take-home exercise---one of very few we can not complete in class because it requires you to visit a certain location during the exercise. We can also discuss the first milestone and the course content survey.

## Issues with first two exercises

Please do not create zip files. If I ask you to put a picture into a dropbox, please do not enclose it in a zip file. If you put a series of pictures into different files, please number the files, e.g., 01pickingUpAKey.jpg, 02pickingUpAKey.jpg, 03pickingUpAKey.jpg.

Your name and a lot of numbers will be automatically added to your file name. There is no reason for you to include your name in the file name. There is no reason to include your email address in the file name. A sequence number and the name of the exercise, preferrably with NO SPACES in the name, will work best. Your name really only needs to appear on the first page of the notebook. It should not be too challenging to read your name.

The pictures this time were all in acceptable file formats. I can work with jpg, png, pdf, tif, and some other formats. I can NOT accept doc, docx, ppt, pptx, xls, xlsx, bmp, wmf and some other formats. If you must use an adobe format such as psd, please be aware that I do not necessarily have the ability to read it---I have some versions of adobe software on some computers, but if I can't read it immediately, I will just give it a zero. This is so I can spend more time on things more relevant to class than trying to read proprietary file formats.

The current date should appear on at least the first page and preferrably all the pages, handwritten in your notebook in tiny characters. This is the date on which you did the work, not other dates like dates of handing things in. If you find yourself picking up in the middle of a page on a different day, you should be able to subtly indicate that by including a thin horizontal line and the new date written in tiny characters.

As we look through the pictures, you will notice that some have remarkably small file sizes. If you have any options in transmitting your pictures to me, please opt for the largest possible file size. It will help with interpreting details in the picture. If you notice a lot of camera shake, please try to retake the photo, perhaps bracing the camera against a solid object or slamming the exposure button with slightly less hammerhead force.

## Critiques

Critiquing design choices and implementations is among the most difficult and important activities any designer practices. And I do mean practices. You can only be good at this through practice. You can only practice with other people. Young people often overestimate their talent for this activity and fail to learn and apply techniques.

We can approach critiques in several ways. The way we will approach them today is to just jump right in and try. In golf, a pro once told me that so much is going on that you have to have a swing thought for every swing. You can not possibly bring everything you know to bear, at least not consciously. You have to pick one or two things you need to think about right now.

Each time you offer or receive a critique, you may find yourself in the same position as the golfer. You can read and discuss and think about the critical process but you can not think about too many things at once. So let's start with a few things likely to come up during this critique.

## Domination

Some students abhor silence. If I ask people to answer a question, studies show it takes students an average of at least 45 seconds to formulate an answer. Some students squirm during that 45 seconds and wind up answering every question. These very few students, usually only one or two per class, get a lot of experience speaking in class, but others do not. It is often better to allow the uncomfortable moment to continue than to be the student who speaks most in class.

## Parochialism

You may be surprised to find out about the diversity of user experience and the variety of reasons for design choices. Students often say that *no one* does this or *no one* wants that. Often, students supply anecdotes showing how everyone does things one way. Plenty of research shows that anecdotal evidence is more persuasive than statistical evidence. It should be easy to peruse a blog that covers new products like *Engadget* and see in the comments that every new product was designed by idiots who have no idea what is going on in the world. It is even possible to dig through tweets from celebrities to show enthusiastic greetings for failed products and damning criticism of what later turned out to be game-changers.

## THINK acronym

My eight-year-old's class is being inculcated with the admonition to THINK before speaking, asking if what they propose to say is true, helpful, inspiring of confidence, necessary, and kind. I would be happy if I could just figure out the helpful, necessary, and kind parts.

A famous quote, popularized by William S. Burroughs in *Naked Lunch* and in the game *Assassin's Creed*, and sometimes attributed to 11th Century thinker Hassan Sabbah, says *Nothing is true; everything is permitted*. Some discussions of the meaning of this have to do with our shifting perceptions of truth. We can not learn everything all at once. Sometimes we use scaffolding to be discarded after we use it. This includes a lot of assertions that are helpful but not true.

For example, you may have been told to sit with a straight spine. This has the helpful effect of distributing and reducing stress on the muscles that support your head. On the other hand, no one has a straight spine. The s-shaped curve of the spine is a remarkable shock absorber and to straighten it would mean disaster for your physical well-being.

From time to time, you have to think more carefully about what will be helpful to say rather than what will be immutably true. You can not always tell immediately what will be helpful. Sometimes you have to listen and watch very carefully to see the effect of what you say. Have you ever told someone to calm down? If not, let me warn you that such an admonition usually has the opposite effect.

## Exercise: Redesign a Widget

For this exercise, define a widget to be an object on a
device that permits the user of the device to change its
state in some way, such as the ubiquitous five way
rocker switch on recent cell phones or the wheel on an
iPod.  Find a real widget in one of the following
contexts and redesign it: automobile, department store,
kitchen, parking lot, public transit (these are
overtly physical contexts, as distinct from cultural or
other contexts).  Present it to the class and receive
critiques from other students.

Work in a small group to produce a picture in your notebook as the focus
of your presentation.  The picture should include (1) a
rendering of the widget as you found it, (2) a rendering
of the widget as you redesigned it, (3) some text
explaining the problem, (4) some text explaining why the
redesign is a solution to that problem, (5) directions
for interacting with the redesigned widget, and (6) a
list of other real widgets that are similar due to
either human interaction or system input.

Put your picture into the dropbox more than an hour before the next class, i.e., by 2:30PM EST, 10 Feb. This will allow the instructor to assemble the pictures into a pdf.

Critique the work of other students according to three
criteria, selection, solution, and craft.  Selection
means to critique the selection of the particular
widget.  Question whether it really is a widget and
whether it warrants redesign.  Solution means to
evaluate whether the redesign really does improve the
widget.  Craft means to critique the visual appeal of
the poster.  Question the picture as a communication
design.

(This exercise was developed by John Zimmerman at CMU.)


# Another Intro

## Nicole

I have a M.S. in psychology and specialize in research and experimental design.  I also have some decent artistic ability.

# protocol & verbal analysis

Let's contrast protocol analysis
described by @Ericsson1984
vs.
verbal analysis
described by @Chi1997.

protocol $\rightarrow$ *think-aloud process*

The main idea in Ericsson (1984) is to elicit
information from a person *while* they accomplish
a task by asking them to think aloud about the
information they attend to while solving problems, but
not to describe or explain.

verbal $\rightarrow$ *knowledge representation*

@Chi1997 contrasts protocol analysis with an
approach designed to elicit the structure of knowledge
of the problem solver, rather than the problem solving
process.

The output of protocol analysis $\rightarrow$
 *process map*

The output of verbal analysis $\rightarrow$
 *knowledge map*

\section{contextual inquiry}

There is plenty of material in Holtzblatt (@Holtzblatt2005) for
developing a contextual inquiry.
I can tell you
frankly that I look closely at the quality of the
affinity diagrams
for evidence of effective work on this milestone.

## Three ways to study users

Spinuzzi (@Spinuzzi2000) compares contextual inquiry with other
approaches, so you can see why we emphasize contextual
inquiry and what we might do instead (ethnography or
participatory design).

## Contextual inquiry

The key sentence in the article
suggests using contextual inquiry to make radical
changes in a short time frame. It relies on an
underlying work structure that reduces the amount of
time you have to spend to understand the workplace, so
it's not suitable for completely alien work processes.

## Participatory design

Participatory design works well for incremental changes
and empowering users.

## Ethnography

Ethnography works best if a great deal of time (both
client time and designer time) is available and a
detailed understanding is required.  The classic example
of this in information technology is Stephen Barley's
studies of technology adoption by radiologists. Barley
obtained an MD in the course of his study.

## Contextual inquiry

*Spinuzzi (2000) on contextual inquiry*

- radical changes
- reliance on underlying structure
- minimal client time

## Ethnography

*Spinuzzi (2000) on ethnography*

- radical changes
- only choice in exotic workplace
- maximal client time

## Participatory design

*Spinuzzi (2000) on participatory design*

- incremental changes
- empowers users
- maximal client time

## Contextual design

Holtzblatt 2005
describes the most commonly used of the above three methods.
It's the most common for a chain of reasons. First,
the reliance on an underlying work structure minimizes the
need for client time, always an attractive feature in a
resource-constrained workplace. Second, the direct manipulation of
the underlying work structure means that existing design
artifacts can be sidestepped and radical changes are 
possible without time-consuming study and modification of
existing design artifacts.

## Popularity of contextual design

Because contextual inquiry and its umbrella, contextual
design, have been so successful and so inexpensive to
implement, you are more likely to participate in it in the
workplace than in any other design method.
One hallmark of contextual design you may experience is the
method's reliance on extremely large numbers of post-it
notes containing atomic observations about the subject work.

## Contextual design process

A team conducting a contextual inquiry typically immerses
itself in a mass of these post-it notes, following a
structured
method for grouping and regrouping the notes to make sense
of the subject work and to organize the observations of the
client participants to reveal the essential characteristics
that will inform the new design.

## Immersion

Beyer and Holtzblatt's (@Beyer1999) picture of immersion follows.

\begin{center}
  \includegraphics[width=4.0in]{affinity.pdf}
\end{center}

## Affordance

- that aspect of a thing you can interact with that
suggests how to interact with it
- can be done well or poorly
- central concept for individual user
- often skeuomorphic
- flat design opposes notion of need for affordance

## Flat design risks

\begin{center}
  \includegraphics[width=4.0in]{flatdesigndanger.png}
\end{center}

[dangers-of-flat-design](http://blog.uxpin.com/2526/5-dangers-of-flat-design/)

## Bad door

\begin{center}
  \includegraphics[width=4.0in]{Door-Pull.jpg}
\end{center}

## Bad and less bad door

\begin{center}
  \includegraphics[width=4.0in]{PushPullDoors.jpg}
\end{center}

## Anti-ADA door

\begin{center}
  \includegraphics[width=4.0in]{AffordancesBig.jpg}
\end{center}

## Bad dryer

\begin{center}
  \includegraphics[width=4.0in]{affordance.jpg}
\end{center}

## Bad iPad

\begin{center}
  \includegraphics[width=4.0in]{NiceIpad1.png}
\end{center}

## Bad iPad's ancestor

\begin{center}
  \includegraphics[width=4.0in]{darkhorse.jpg}
\end{center}

# Day 07. Tuesday, 17 Feb

## Milestone 1 Critiques

I'm going to make my individual critiques available to everyone because they apply to everyone. If I did not say something to you directly, please see if you think the criticism I gave to another group may also apply to you. I don't want to repeat the same criticisms. Also, I find that it is sometimes easier for students to see where they could improve by looking at the work of others. It is natural to react defensively to criticism of your work and to want to explain why you did it a certain way. If you look at criticism applied to other work and think about how it *might* apply to your work, you may be able to work with it more effectively.

## A common question

Students often come to me after receiving a grade of less than a hundred percent and ask what they did wrong. Even after I have provided critiques of the class work in general and have raised the issues I have seen in the questioning student's work about some other work. Still they walk up to me after class and say, what did I do wrong?

It's a tough question to answer. There are several things to say about it. 
I'd like to devote a few words to each aspect of it.

First, there is the notion that it should be easy to obtain a perfect score if you simply learn the eccentricities of the teacher and cater to them. Do you see perfection in the world? Are there hundreds of companies succeeding at making smartphones? Cars? Anything? Ask yourself whether you have ever given a negative review on a website. Judging by the number of negative reviews I have seen, not only has everyone on the planet given one but some have given more than their share! If you submit your work to the public, will the public give you a perfect score? And yet, in graduate school, teachers are encouraged to grade A as acceptable, B as bad, and C as catastrophic. It seems almost as if students feel entitled to a good grade by virtue of doing something.

Second, there is the question of the difference between your work and perfection. When you ask me this question, I feel as if you have not listened to the critiques given or you have dismissed them as not applicable to your work. Can I tell you some step you could complete to make your work perfect? Can I provide a box to check that will improve your work? What will happen to your work if I make it more to my taste? Teams at the CHI Student Design Competition under my coaching have competed very successfully against teams following checklists from other coaches. Let me provide you with the benefit of my experience.

The preceding point should suggest that you need to gain insight, not instructions. The only instructions most of you need right now are very very simple. I find myself constantly asking some students the same question: Can you please apply more ink / lead to the page? Until they do that, there is not much more to say. It is no accident that the most famous sports stars do goofy exercises like pushups even after they attain fame. There is very little for a teacher to say to most students.It is much more useful for me to listen to you than to speak to you, especially so early in the semester. The most important thing that anyone said to me on last Thursday was *My hand hurts*. That made me believe that the student (actually three different students said it) had finally put enough lead on the page, for then. Now my task is to exhort you to keep that up, a very simple task, simpler than continuing to listen to you, which remains my main task.

Next, there is the question of what *the other teachers do*. I really do appreciate it when students tell me what other teachers do. I also hope you appreciate that you should get a different perspective from each teacher. Your education should bring you into contact with methods you may not yet understand, methods you may find disagreeable. Yet the role of the student is to *suspend disbelief* and try something new, even if uncomfortable. Unfortunately, the tyranny of student evaluations prevents teachers from being too daring. I would prefer to have student evaluations conducted two to five years after the course is taken because I believe many students evaluate their comfort level right after they take a class. They evaluate their certainty about what they have learned. A contrasting view would be that, if you are so certain about it, you have not changed much, you have not learned much. You have simply filled in some cracks in the structure you already created. In fourteen weeks you can't do a complete renovation of your way of thinking and doing.


One of my own mentors said you can't effectively judge your own past for seven years (plus or minus). He wrote autobiographical books and plays and he claimed that, after more than seven years (plus or minus), memories get rusty and before seven years (plus or minus) you are too close to events to see how you have changed. So I ask you to suspend disbelief for a while and try something new and later see if you agree that you have changed for the better.

## Shopping Cart

Someone in this group asked whether they should change direction or scale back because I said that I thought it would be too expensive to put a device in each shopping cart. Here's what I said in reply.

I would like you to think about this in a different way. Instead of trying to decide what to do based on what I have said, try to find evidence that supports or refutes what I have
 said.

There is a major grocery store chain headquartered near here, Wegman's. They donate a lot of IT equipment to RIT so I know they are friendly to RIT. When I visit there, I often see the employees themselves shopping for groceries. I'll bet you could interview them to find out about the needs of shoppers that might be helped by having a device on the grocery cart or perhaps an app that might help.

I'll try to say more later but for now let me just add that the needs of the shoppers as perceived by the employees may differ from the needs of the shoppers as perceived by the shoppers and ALSO from the needs of the shoppers as EXPERIENCED by the shoppers. In other words, even the shoppers themselves may perceive differently from their experience.

A famous quote from Henry Ford, explaining why he did not listen to his customers was that, if he had, they would have just told him to invent a better horse and buggy.

# Day 09. Tuesday, 24 Feb

## Create a project website

RIT provides you with a place to put a website if you don't already have one. I can not find a formal channel through which you learn about it so here is what I know. I can access mine at [http://people.rit.edu/mjmics](http://people.rit.edu/mjmics) and you can access yours with a similar URL, substituting your username for mine. If you have not put anything there, you will see an error message. I created an `index.html` file containing the word *bla* and uploaded it to the site from a terminal, saying

```sh
sftp mjmics@gibson.rit.edu
cd www
put index.html
exit
```
\noindent
You can access it from a terminal by saying

```bash
ssh mjmics@gibson.rit.edu
chmod 755 www
cd www
chmod 755 index.html
exit
```

Again, you would substitute your username where I have entered mine above. One popular GUI for uploading your information is *FileZilla*. You can use it to graphically navigate to your `www` folder and put an \verb|index.html| file there. Where I used the terminal above, you can use menus in FileZilla or another GUI to do the same thing. What I did when I said `chmod 755 www` was to make the `www` publicly readable and executable but not publicly writable. Then I changed to that folder and made the file in it publicly readable and executable. You need to do that for every file you want to share, including your document and pictures. You can link them all in the \verb|index.html| file.

I was quite surprised to find that some students were unfamiliar with how to do this. You may be severely handicapped in your career if you do not know how to use a terminal to accomplish some basic tasks. You may not have time to learn a lot so it may help to use a combination of the terminal and GUI tools.

## Use all available resources

If you've overused the web for a decade or more you probably remember the meme involving Hitler getting bad news in the film *Die Untergang* (2004). People would subtitle the scene endlessly with bad news affecting different hobbies, occupations, sports, or celebrity foulups. Did you know that there were even versions for HCI? Yes, HCI is everywhere. And HCI people seemingly have time to throw up endless websites with internally conflicting advice, eternal truths, urban legends, and the occasional valuable piece of information. During your program here, you need to find a way to better cope with all the HCI information coming at you from every direction. You need to share with each other how you get information as well as how recall information when you need it. As you approach a difficult milestone, contextual inquiry, it will be tempting to keep gathering information right up to the last minute. Resist that temptation! You already know too much!

Making a deadline is a convergent process. You don't want to be open to new ideas. You want tunnelvision for the next couple of days. Any new information you receive has to be put somewhere you can find it after the deadline. Over half of your classmates probably don't have a good place to put new information right now. So put it anywhere and concentrate on processing the information you have right now.

## Milestone 2 may be delayed

It may make sense for us to delay the contextual inquiry deadline. We'll find out in class today by discussing where we stand. You may lack clients or interviews with clients as grist for your affinity diagrams. Let's divide into groups and hear a short description from each group about where you stand at this moment.

## Share interview techniques

You have to share your successful and unsuccessful interview techniques in a conversation. I can start the conversation with a few suggestions but you have to take from there. So here are a few commonly mentioned points about interviews.

The most successful interview has two interviewers. One takes notes and the other speaks. Don't divide the speaking. The one who takes notes should rarely speak and then only because the speaking interviewer has forgotten something. The speaking interviewer tries to maintain engagement with the subject. The speaking interviewer tries to keep the subject talking as much as possible and on-topic as much as possible. That job requires the full concentration of one person. That person should not try to do other things at the same time.

Avoid recording devices. If you do use a recorder, make it one that is very easy to operate and not intimidating and leave it on the table between you and the subject. Invite the subject to turn it off if they need to *go off the record*. You may want to turn it back on after the secrets have been shared. On the other hand, your experience may tell you that it has been inhibiting the subject or been the focus of the subject's attention. You may want to announce that we don't need it further and pocket it in that case. There is a balance, by the way, in the user interface of a recorder. It has to be able to tell you it is recording but it also has to fade into the background. Lots of recording devices, including one I often use, go too far one way or the other.

The most typical problem students have in interviews is that they fear silence. Can you allow enough silence to elapse to let your subject gather their thoughts? If not, what can you do?

Look puzzled. If there is too much eye contact, just write a question mark on your notepad or draw a simple shape like a circle or square and look puzzled again.

Look at artifacts. The three diagrams you generated in our previous class are artifacts that you can look at silently with your interview subject. Just don't say anything at all and look intently at each artifact.

Ask the same question over and over. If the subject is reluctant to speak, just ask them to *say more about that*.

Ask hypothetical questions. Activate the subject's imagination by asking them to place themselves into a situation and say what they would do.

Allow the initial speech, then stay on topic. Experience shows that subjects have rehearsed a certain speech about whatever is bothering them. They have to be allowed to declaim that speech. If not, they will keep losing track of your questions as they seek an opportunity to insert the speech. Once that is out of the way, let them refer back to it but do not allow them to repeat the whole speech or to give the certain speech about another issue. If you interview a subject about something they would like to be different, the interview may trigger associations with other things they would like to be different. You may feel the need to express empathy and tell analogous stories from your own experience. You should rehearse any such stories beforehand so you can abbreviate them as much as possible.

Overtly display respect and appreciation for the subject. I may have mentioned the robotics team of undocumented alien high-schoolers from Phoenix who defeated MIT in 2005. (There's a Wired profile of it that gets linked from various blogs every few months.) One of the key reasons they are thought to have defeated MIT was that, when they interviewed experts in underwater robotics, they treated the experts much better than did the haughty MIT team. One of the experts, interviewed by Wired later, said he gave them a lot more help than he gave the MIT team and that he began to think of himself as a member of their team. You can't buy that kind of help.

Don't bother to ask if a subject can think of anything else. Instead, stimulate them to think of something else. You can stimulate them by asking them about situations. When was the last time X happened? If they say something never happens, keep searching for that one time.

# Day 11. Tuesday, 03 March

The website picture has improved! In brief, I had received guidance prior to the semester beginning that I could assume you have web hosting available at RIT, and would know how to use it. Suffice it to say, there were issues. As a result, I have discovered more about the infrastructure here. There is a new resource being set up in IST for web hosting for faculty and students. This should replace some of what has been lost in the deemphasizing of some campus-wide resources. I struggled through a bit of it the other day and believe it is promising. I will try to share more with you as more information about it becomes available to me. I believe, for instance, that we may be able to all have accounts visible to each other on the same machine so that we can *look behind the scenes* at each other's websites. (If so, participation will doubtless be on an opt-in basis, not on an opt-out basis.)

The next milestone concerns personas and scenarios. There are two big issues to address as we prepare for this milestone. The first is class participation and the second is reading. The third thing to consider the next exercise.

## Class participation is uneven
Currently only five students contribute enough to class discussion to give me insight into their academic development.

At the end of every semester, students ask me to write recommendations for them. Sometimes, I have embarrassingly little insight into a given student's academic development. At that time, it is really too late for me to find out about them. It can be embarrassing to say that we have sat in the same room from January to May and I still know very little about someone's academic development.

Admittedly, there are some people who are not predisposed to speak and whose written work or sketches more than makes up for it. Even so, I wind up being the only recipient of your contributions unless others reflect on the exercise pdfs on myCourses. Your classmates really need your contributions. As graduate students, you should have more to contribute. Even if you are reluctant to speak, and are confident that the work you submit to me is exemplary, your classmates are your future peers. The people sitting around you will help you get jobs, complete jobs, win awards, get through hard times, and grow old with you. Don't abandon them in these first few years.

You may recall that I mentioned several pairs of famous people who knew each other as children or college classmates and grew famous together as partners, rivals, or even just as acquaintances. Bear in mind that, no matter how good or how bad you are at your work right now, there is someone sitting near you who can help you and who you can help. Together you may be able to make a bigger splash than any of you can do individually. Of course, you may say to yourself that you do speak to some colleague outside class and don't really need to say anything in class. That is just not true. You may have said things outside class to your partner that need to be said in class.

## Take my reading recommendations very seriously
I was concerned after you modeled some work that some of you did not read Holtzblatt. I mentioned this with respect to the sequence models. The initial sequence models did not seem to resemble those in Holtzblatt in any way.

For the personas and scenarios milestone, let me make the very strong suggestion that you use @Cooper2014. You can obtain this electronically from the RIT library, searching for *About face the essentials of interaction design*. Chapters 3 and 4 outline the processes. You should pay special attention to Figure 3-5, Overview of the persona creation process to develop personas. (We'll talk about Chapter 4 next time.) This figure outlines eight steps to take. When I look at the milestone output, I should believe that you really followed or at least considered these steps in some detail.

How should you read @Cooper2014? I'm glad you asked. This is a very good example of why you don't need slideshows. The book is organized in a way that brings out its main points. We'll talk more about this after Spring Break, but let's just briefly review some items that identify structure and guide your assimilation of the information therein.

- Table of contents
- Orange headings
- Black headings
- Boldface terms
- Italicized emphasis
- Figures with sequences
- Figures with comparisons
- Examples
- Justifications
- Answering objections
- References
- Order of presentation

Most of the items in the list are self-explanatory. The last one, though, needs a little explanation. The order in which Chapter 3 is presented could be called a series of steps, including think, do, and reflect. First, the authors present the idea of personas, then tell you how to do them, then reflect on some of the thoughts you might have as a result of experience with personas or with alternative methods. This organizing principle might remind you of the plan-do-check-act cycle that is a foundation of quality improvement work. You could think of learning a new approach to interaction design as an example of quality improvement work. If you do, then you might think about integrating aspects of the persona approach into your larger toolbox, the lifelong toolbox you will carry with you outside of graduate school.

![plan-do-check-act](planDoCheckAct.jpg)

One example of the plan-do-check-act cycle can be seen in this picture, sourced from a public-facing website at Cardiff University.

# Review exercises

Let's review the objectives of exercises we've done so far.

## 01drawingAFace
Show that you can improve your sketching by technique. Show that *I don't have talent* is not a valid reason to refrain from sketching.

## 02pickingUpAKey
Develop narrative progression using pictures. Use imagination to change the viewer's perspective. Use storytelling. Simplify pictures. Sharpen the focus of a message by simplifying pictures. Work within time and space limitations. Find a way to show sequence in a series of simple pictures. Show the order in which pictures should be viewed.

## 03widgetRedesign
Learn to identify affordance and the lack of affordance.
Take the environment around an interaction into account.
Work on your sense of which problems are worth solving.

## 04recordInteraction
Learn to describe interaction.
Notice how difficult it is to isolate the interaction from its surroundings.
Try to disambiguate what you are communicating in each picture.
Plan the narrative.

## 05smallInteraction
See how much difference a single constraint can make in a design.
Improve the clarity of a picture by removing some elements.
Consider the number of pictures required and the amount of information conveyed in each picture.
Plan your time.

## 06corpDirectory
Understand that the medium (a small square) is not suited to the message (a large outwardly fanning tree).
Learn some characteristics of one of the two most frequently occurring information structures (trees).
Think about users in identifiable groups.
Think about user characteristics such as the number of users, frequency of use, purpose of use, nearness to other users, and power and influence.

## 07modelWork
This exercise did not have an objective in the sequence of the other exercises. This exercise was simply meant to improve your milestone 2 preparation.

## 08elevator
Work on a problem for which the obvious solution model (existing elevators) is inappropriate or intractable.
Think about a completely unfamiliar situation and try to identify its salient characteristics.
Think abstractly.
Narrow your focus to a subset of possible users, situations, and relevant problems.

## Diverge then converge
For each exercise, you must diverge or your ideas will be boring. Then you must converge or you will not meet deadlines.
Another way to say this is that you must spend part of each exercise trying to play followed by some time trying to produce.

How do you know whether you have played and produced?
We spoke of the concept of flow and you know that you have that you are playing when you have achieved flow. That is an internal measure you may assess for yourself. An external measure might be a judgment of creativity. Your output is more likely to be assessed as creative if you have played but beware. Your output may be assessed as not creative for another reason. If you fail to converge, you will not have adequately conveyed your creativity. Thus you may find converge a necessary but not sufficient condition for others to appreciate your creativity.

Leonardo was a terrible example of failure to converge. He rarely finished his work and much of it only began to attain prominence centuries after his death. Mona Lisa, for instance, was not widely touted as the greatest example of oil painting until about the past hundred years.

It's easier to see the outcome of convergence than divergence since you have a series of sketches that people can or can't understand.
You have to ask yourself whether people get the message you conveyed.That is separate from whether or not you conveyed a good message. So your creativity may be judged by how good the message was. Your convergence can be defined as how well you conveyed the message you intended to convey.

## Allocate your time
In each exercise, you should try to work within a severe time constraint and prepare a presentable artifact in that time. You should improve your ability to complete each step so that you have something to show at the end. You have to get to know yourself well enough to know what you need to spend the most time doing. Do you struggle with the problem definition? Are you indecisive about which aspect to tackle? Do you struggle with rendering your ideas? Each exercise should contribute a little to your picture of what you need to do to grow.

## Tell a story
Every single exercise since the picking up a key exercise offers the opportunity to tell a story with your solution. Storytelling is one of the oldest and most defining human activities. You must be a good storyteller to be a good designer. People expect to experience stories and you can take advantage of our human predisposition to experiencing storytelling to communicate your design ideas.

Many, perhaps most, great stories are not told in linear time. Stories do not unfold stepwise, like appliance manuals. (Actually, Ikea does assembly manuals that approach storytelling.) You have to develop a way to tell story that takes the viewer's experience into account. This is often starting with a detail and expanding to a big picture or starting with a big picture and drilling down to a detail. It may start with a use case and end with an argument. However you plan a story, you must plan a story.

## Focus on affordance
Since the widget redesign exercise, every exercise has provided an opportunity to think about affordances in some way. Is there a precedent for affordances in a situation? Are users likely to be acculturated to any particular affordances? Are multiple affordances reinforcing or overwhelming? Are there signals that don't work as affordances because they take too long to mentally process? Are affordances bound by fashion?

## Identify interactions
You should be using the exercises to refine your picture of what constitutes interaction and what is outside the boundaries of interaction. How much of the user do we need to see? What aspects of the user do we need to know about? Does the user have arthrities? Can the user hear? Do we need to know that an ironing board is set up in the kitchen precariously close to the table where the user is wearing headphones and conducting an online conversation? Every sketch reveals something and hides something else. You must be conscious of both revealing and hiding details that matter or don't matter.

## Display information
Information comes in many forms and has many characteristics. You should be thinking, since the corporate directory exercise, about the characteristics of information. How is information best stored, transmitted, and processed? Is information hierarchical or tabular? Is information structured, semistructured, or unstructured? Is information personal or relevant to a group or to a community or to the public? What visible characteristics of information are most salient to consumers, color, position, texture, shape?

# Day 14. Thursday, March 12

Today, please discuss the following topics: Harrison Bergeron and the above review of exercises. You, the class, must take charge, and must make the discussion move forward. I, the teacher, will contribute as little as possible, preferrably nothing.

## Harrison Bergeron
In class, someone advanced the claim that we must design for the lowest common denominator if we design something that will be used by people of all levels of technological sophistication. I can think of many arguments against this claim.

Two of the arguments I can think of are advanced in the Kurt Vonnegut short story *Harrison Bergeron*, 1961. You should be aware when you consider it that it has been interpreted literally and as meaning the precise opposite of its literal meaning. In other words, it has been interpreted by some as warning against the dangers of catering to the least common denominator and by others as warning against the dangers of worrying about catering to the least common denominator. The former interpretation is favored by Fox News. The latter interpretation is favored by literary critics and the author of the story. I do say that in the hope of prejudicing you in favor of the latter interpretation but the fact that the story functions to support two opposing points of view serves to illustrate the fact that a device can serve two completely different groups of social commentators with two completely different kinds of analytical skills and abilities.

Please discuss the notion of a design target population and reaching them with respect to this least common denominator idea and alternatives. 
Please produce some written assertions in a myCourses discussion.
These may contradict each other but should come to some kind of resolution in a summary. When I say resolution, I don't mean that you must agree. That resolution could be that there are two (or n) points of view. In such a case, the summary will enumerate and briefly descrbe them. If you are in agreement, then describe that upon which you agree.

## The preceding exercise review
Please discuss the exercises with the view of making some assertions about what you have learned through or despite the exercises.
Please produce some written assertions in a myCourses discussion.
These may contradict each other but should come to some kind of resolution in a summary. When I say resolution, I don't mean that you must agree. That resolution could be that there are two (or n) points of view. In such a case, the summary will enumerate and briefly descrbe them. If you are in agreement, then describe that upon which you agree.

# Ambient Notification

\begin{center}
\includegraphics[
  width=0.89\linewidth]
{olio1.png}
\end{center}

These two graphics come from a recent article called ... Notification Hell,
[http://www.theverge.com/2015/3/26/8292213/olio-smartwatch-hands-on](http://www.theverge.com/2015/3/26/8292213/olio-smartwatch-hands-on).

It may be worthwhile to revisit your ambient notification exercise with this in mind. Also, you may want to consider the article, Tyranny of the Minimum Viable Product at
[https://medium.com/\@jonhpittman/the-tyranny-of-the-minimum-viable-product-fb25e2e57e6e](https://medium.com/\@jonhpittman/the-tyranny-of-the-minimum-viable-product-fb25e2e57e6e)
which describes a problem that startups in the Internet of Things seem to exhibit when they try to apply *design* to their efforts.

\begin{center}
\includegraphics[
  width=0.89\linewidth]
{olio2.png}
\end{center}

# Sketchbooks

I scored the sketchbooks very quickly on four measures and put the raw scores into myCourses because I felt it expedient even though I had not yet analyzed the scores.
This upset many students. I don't like to upset people but certain objectives for the course need to be promoted. I have asked people to use more pages, to date their sketches, to increase the amount of lead or ink they put on the page, and to increase the ratio of pictures to words. Scoring these measures is a way to promote these objectives.

## Page count
I counted the number of pages used in each sketchbook and divided that number by the number of pages used in the sketchbook with the most pages used. Following is a stem-and-leaf plot of those raw scores.

```
stem(p)
   4 | 30277
   6 | 00022494
   8 | 1133
  10 | 0
```
The entry in the last row signifies that one person received 100 percent. The next to last row signifies that two people received 81 percent and two people received 83 percent.

Later, upon analysis, I can refine these scores. For example, I can use a formula like

```
stem(log(p)/max(log(p))*10)
   6 | 3
   7 | 026688899
   8 | 147
   9 | 1122
  10 | 0
```
\noindent
to achieve a similar effect with a less draconian penalty.
Further analysis might result in the use of a different slope, for instance

```
stem(log(2*p)/max(log(2*p))*10)
   7 | 278
   8 | 113334458
   9 | 03344
  10 | 0
```
\noindent
essentially makes B the average score. Such analysis takes some time and thought. Most of the objections that have been raised are objections I have thought about already. Some, I plan to use to change the scores. Some are more questionable. Others seem to have been made prematurely. I have decades of teaching experience providing me with some insight into the difference between stated intentions and observed outcomes.
## Date count
I scored the dates in the same way as the pages. One student suggested that this unfairly penalizes students who wrote on fewer pages and therefore have fewer opportunities to label pages with dates. If that is true, there should be a strong correlation between the scores for pages and dates.

```
summary(lm(p~d))
...
Adjusted R-squared:  0.6006
...
summary(lm(log(p)~log(d)))
Adjusted R-squared:  0.3184
...
```
\noindent
The above fragments of regression output do not show a strong correlation between these two scores.  I believe that this is because some people did not take me seriously about the requirement of dating pages and some people did. I think the score for date count reveals whether or not a student took the requirement seriously.

Here, as in other cases, some students objected simply because of the low raw scores. That does not make sense to me. One student even suggested that they be allowed to retroactively go through the notebook and add correct dates! Instead, try to think about what makes sense. I want to attain an objective. I want a metric in place that promotes the objective. For most students, I can achieve that by applying a log to the raw results. For example,

```
stem(log(2*d)/max(log(2*d))*10)
  0 | 04
  0 | 66667788889999
  1 | 00
```
\noindent
makes B the average score. It *could* really drastically penalize the two students who took the date instruction least seriously.  I say *could* because I have not considered the weight of this raw component of the sketchbook score. In my mind, it needs enough weight to promote taking my requests seriously. I have repeated some of my requests numerous times to certain students with no effect.

## Whether perfect should be average
One approach to education is to provide students with a clear, simple list of instructions to follow. Those students who follow the instructions receive a perfect score and the others have only themselves to blame. They had the opportunity to achieve a perfect score because there were clear instructions. Only their own laziness or obstinacy is to blame for ratings below excellent.

The above approach leads to high satisfaction among current students. Students often feel as if they are in control of their education with this approach. They may say that it empowers them. Because young people often have little control over many aspects of their lives, the sense of control can feel like an education. Students often feel that, by taking responsibility for following clear instructions, they are learning a lot. They report favorable learning outcomes after taking courses that follow this approach and, increasingly, they are perceived as customers whose satisfaction is essential to the operation of colleges facing spiraling costs due to mushrooming administration.

As a result, this approach is spreading like a disease across all universities. Once a student has experienced this sense of power, they never want to return to the sense of uncertainty they may have experienced as an alternative. Once this approach is the norm in any department or college, it becomes irresistible for outliers.  Individual teachers may claim that you should use college as a place to experiment with new approaches and maintain an open mind to trying different things, but that argument falls on deaf ears if GPA is the only criteria for scholarship, internship, or employment selection. The very same sponsors and employers who bemoan the lack of imagination and inventiveness of recruits encourage this lack by using crude numbers for selection.

I (Mick) strongly believe in quantitative information. When people say that something is not quantifiable, I often find myself disagreeing. The problem is that quantification often requires more time, money, space, or other resources than are practically available. Grading is an example of poor quantification practices tyrannizing thoughtful people.

I need to balance several things in order to provide adequate grades. I need to compromise with the "perfect is average" environment but I also need to find a useful way to score that I can believe improves education rather than simply robbing me of my value as an educator. I need to reevaluate educational goals and techniques because the rest of the world has moved into a new era and the education establishment does not seem to be catching up.

Incredibly, students often complain that I change things and insist that my courses should be cut and dried without deviation from the beginning of one semester to the end. Then, if I want to try things differently, I should begin the next semester differently and remain consistent with the new thing throughout that semester. These same students often complain that education is stuck in the past, yet they contribute to it by their very insistence on a glacial pace of change.

## See what you made me do
You may be tempted to react to the scoring of dates by writing an absurd number of copies of the current date on every page or, perhaps, writing a single word on each page. Then you can point to the ridiculous looking outcome and say "See what you made me do!" I have encountered many varieties of the "See what you made me do!" approach made by students who see a fault in their teachers, peers, or the system at large. The best advice I can offer is to resist the temptation. You need an internal moral compass that you keep working on your whole life. You have to find the right thing to do in a situation and try to convince the authorities to rate you accordingly. You pay a great deal for tuition and you can never get full value by practicing suboptimal technique in order to highlight inadequacies in others.

![Windows Phone 7 HQ](wp7hq.jpg)

Michael Smuga, studio
manager, Windows Phone 7 Development HQ, is seen relaxing while 
the press photographs him to show that Microsoft is no
longer
uncool as part of a large publicity campaign prior to
the launch of WP7, circa 2010.  Note what appear to be hand-sketched
storyboards behind him and I dare you to tell me that
this is not an advertisement for doing sketchbooks in
this class!

# Bertin exercise critiques

Thanks to the two students who worked with me on this study of one student's solution to the Bertin exercise. This study is more detailed than what I expected you to do in class but serves to illustrate the process.

![bertin exercise example](bertinExerExmpl.jpg)

## The Invariant

The invariant should be reflected in the title of the information graphic. If it is not included, or if it can be improved, it is appropriate for the critique to include a suggestion. In this case, the invariant seems to me to be *Number of establishments by Size, County, and NAICS*. Both the content and the order of this invariant matter, as will become clear in the following paragraphs.

This invariant appropriately summarizes the information graphic.

Having critiqued the invariant and suggested a solution, I am in a position to answer the first of the three questions I ask you to consider for every exercise, whether the student has tackled a worthy problem. Certainly I believe that this is the case here because it is of interest to a great many people to summarize economic activity of a state by number of establishments, size of establishments, specific county of establishments, and kind of establishments. (The NAICS, which stands for North American Industry Classification System, is a standard for describing kinds of businesses). This is not a controversial claim because a great deal of policy and economic activity depends on such summaries.

## The components

The components are represented in the information graphic and one way to identify them is to see what is displayed. The $x$ and $y$ axes are frequently used to explore the most important components. Here, the $y$ axis displays the number of establishments, an integer ranging from 0 to 700. The $x$ axis displays bars representing combinations of counties and NAICS codes.

I have mentioned that each component should have a legend. The above components don't really have a complete legend, although Bertin would consider the axis labels to be part of a legend.

There is one legend. That legend depicts two categories of size, so size is the remaining component. We could make different claims about the characteristics of the retinal variables involved in this component and we will do so later.

For now, let us list the components along with their orders, lengths, and levels. Remember that order refers to raw numbers or percentages (usually based on population or area), length refers to the number of objects being represented, and level refers to nominal, ordinal, or quantitative measurements.

Number of establishments is an integer, evidently ranging from 1--700. Its order is raw, its length is either 700, the total number of establishments in a county/NAICS combination or the total number of establishments overall. Its level is quantitative because we can easily say that twenty establishments is twice as many as ten establishments. In other words, we can form a meaningful ratio between measures of the component.

Size has the order raw because it refers to number of employees rather than number of employees as a percentage of available working age population, for instance. Size has length 2 because we can only distinguish between establishments with fewer or more than twenty employees. Size is of ordinal level because we can say that an establishment in the 20 and over category is larger than an establishment in the under 20 category but we can't say how much larger given this information.

County is of raw order, of length either 7 (represented) or 36 (available in the entire state), and of level nominal because one county is not countier than another. Note that an attribute of county like name is ordinal in an alphabetical sense and an attribute of county like area is quantitative. All this component does, though, is to identify counties.

NAICS is a little trickier. I will call its order raw because of the way we use it here, but each code represents a location in a hierarchy of specialization so another interpretation might be arguable. Its length could be construed as the number of different codes represented in the graphic or in the state or in the entire catalog. Its level is also tricky because of the hierarchical ordering of the codes. I will call it nominal for our purposes because I have seen no evidence that it is meant to be used in another way.

To critique the components alone is simply to say whether they make sense as components of this graphic. More important is to critique their representation by retinal variables and to see if they are well matched to their retinal variables and whether better use could be made of the retinal variables *used up* by each component.

## Retinal Variables

Bertin describes the retinal variables in a dense, 438 page book. There is a lot to say. Nevertheless, we will consider the retinal variables depicted in the slideshow at a very basic level. The retinal variables include size, value, texture, color, orientation, and shape.

Three of the retinal variables here are described on the axes by bars. Bar height is very well matched to an integer ranging from 0 to 700, so I regard the use of the $y$ axis to describe number of firms as successful. There is no other component as well suited to representation by bar height in the data.

County and NAICS are described on the $x$ axis by the bar names. A tractable number of combinations has been shown. One shortcoming of this graphic is that there are not instructions to the assistant mentioned in the assignment spec. Recall that you were contributing a sketch and instructions to someone polishing the graphic. There is not enough to go on. This, among other issues, has led me to rethink the picture / word ratio constraint on sketchbooks. Instead, I would like to use picture amount and let words appear as needed without penalty.

One question about these two components, County, and NAICS, is whether they should be considered as one component or separately. That will remain an open question for now.

Finally, we come to the Size component. The representation of this component allows a number of interpretations.
We could refer to the choice of solid black and diagonal hatching as values, since one can be interpreted as black and the other as gray. We could also regard them as colors gray and black. We could also regard them as having orientation in the case of the hatching versus no orientation in the case of the black. Finally, we could consider them has having texture since we could call the black smooth and the hatching ridged.

One point Bertin makes about using more than one retinal variable to depict a component is that retinal variables may reinforce each other or be in conflict with each other. In the latter case, cognitive dissonance may be produced in the mind of the viewer. From Bertin's perspective, cognitive dissonance is always bad. Many people who produce information graphics seek to produce cognitive dissonance for reasons involving persuasion. For example, the information graphics produced by opponents of the health care plans of two recent US presidents have been designed explicitly to create cognitive dissonance in the minds of viewers. This usage stands outside Bertin's system which seeks only to support immediate answers to simple questions about information.

In this case, my reading is that the various retinal variables work together, reinforcing a consistent reading. It is not surprising that diagrams of this style may be seen in many publications. They serve an informative purpose.

# Visual Design

## Different perspectives drive different views

When we analyze what people see, we bring a perspective, in part based on where we are and what we do. Think about some bases for your perspective on the visible variables in presenting information, such as professional, cultural and biological.

\smallskip

\noindent \llap{``}When art critics get together they talk about Form and
Structure and Meaning. When artists get together they
talk about where you can buy cheap turpentine.''

\hfill --- Pablo
Picasso

\hfill quoted
by Steve McConnell,
\textit{Code Complete} (1993)

\smallskip

\noindent \llap{``}Modern philosophers have had little to say
about the nature of aesthetic interest; ... The
concentration has been on the philosophy of art, and in
particular on puzzles created by boring impostors like
Duchamp: is this signed urinal a work of art? etc.  This
makes for an exceedingly dull literature, devoted to
questions which can be answered in any way while leaving
everything important exactly as it is.''

\hfill
---Roger Scruton, \textit{Modern Philosophy} (1994), p. 589

## Gestalt principles
In 1923, Max Wertheimer published principles of visual grouping (in German) as follows. These principles were later widely translated and influenced people in a wide range of professions and cultures. The Gestalt psychologists themselves made extensive contacts among artists and scientists the world over. They were dispersed from Germany and never re-coalesced into a group in their lifetimes so the magnitude of their influence on others is not always clear in history books. In addition to the following short list, they formulated many other principles they shared with artists of the Bauhaus and famous scientists in various disciplines.

- proximity: proximate images form a group
- similarity: similar images form a group
- closure: perception completes images that appear to have missing parts
- symmetry: perception links unconnected symmetric images
- common fate: images perceived to have common fate (follow a path) form a group
- continuity: continuous images form a group
- prägnanz: images that seem to work well together form a group

## Dieter Rams

An industrial designer often cited as the
primary design influence on 
contemporary Apple products, Rams articulated the following
design principles, often quoted in popular media.

- Good design is innovative.
- Good design makes a product useful.
- Good design is aesthetic.
- Good design helps us to understand a product.
- Good design is unobtrusive.
- Good design is honest.
- Good design is durable.
- Good design is consequent to the last detail.
- Good design is concerned with the environment.
- Good design is as little design as possible.

## Edward Tufte
Formerly a public policy scholar, Tufte has carved out a
popular career publishing coffee-table quality books
about quantitative graphics. For years, he promoted a
principle called *data ink ratio maximization*. The
principle sought to evaluate graphics by comparing the
ink expended on portraying data and the ink expended on
other purposes, such as meaningless decoration. This
turned out to be a problematic principle. What do you
suppose could possibly go wrong with it?

More recently, Tufte has promoted the following list of
principles, found in the chapter
"Fundamental Principles of Analytic
Design" \textit{Beautiful Evidence}, pp 123--155.

- Comparisons--Show comparisons, contrasts, differences
- Causality, Mechanism, Structure, Explanation
- Multivariate Analysis---Show more than 1 or 2 variables
- Integration of Evidence---Integrate words, numbers, images,
      diagrams
- Documentation---label what data you have and measurements,
       etc.
- Content Counts Most of All---depend on quality, relevance,
       and integrity

Tufte's work is characterized in part on a reliance on
high-reso\-lution print media. His books are published by
a fine art press and he advocates against
powerlesspoint-type slide shows, claiming that their
information density is too low match the cognitive
capabilities of humans. He suggests instead that
speakers produce high-resolution pictures to be printed
and provided to audiences to accompany talks instead of
what he calls pee pee pfluff.

Tufte's advocacy began when slide shows were being
projected using lcd technology, capable of about
$640\times 480$ pixel resolution and a brightness of a
few hundred
lumens, displayed on makeshift screens
(often no more than white walls) at sizes of perhaps a
hundred inches diagonal. As I write in 2015, I have
recently read rumor of a new mainstream phone with a
3,820 $\times$ 2,160 pixel resolution on a
daylight-readable screen of about a 5.5 inch diagonal
(rumored specs of Samsung Galaxy Note 5). Do you think this rapid
advance in display technology affects or should affect
Tufte's advice?




# Information
Information can be controversial to define. Widespread agreement exists, though, about some properties and uses of information.

## Personal information systems

Extensive research over the past twenty years, some of
it by Tom Malone at MIT and Susan Dumais at Microsoft
Research, has explored how people organize personal
information.

One example that helps people understand the problem of
personal information is the knife analogy, described
below.

One important finding about personal information
management has been that people are prone to do one or
some combination of these two things: filing and piling.

After reviewing the following topics, conclude the
study of personal information systems by doing the
*share best practices* exercise.

## Knives in the home

Suppose you have just won a complete set of knives for
your home. Where should you put them? You could have a
single cabinet to store all knives, but it is more
likely that you will distribute the knives to different
rooms, placing them near where they will be used: steak
knives in a buffet in the dining room, cooking knives in
the kitchen, handyman knives in a garage workshop.

When you need a particular knife, it will be in the
context of a current task, such as preparing food,
setting a table, or cutting a length of rope for a
clothesline. In each room, there is some place where the 
tools appropriate to the tasks performed in that room 
are stored.

## Filing: using hierarchies to organize information

Filing refers to organizing items according to
categories or classifications or clusters.
(Researchers define these three words differently.)
When a filer looks for information, it is found in a
place where like information is found. That information 
may be in a nested structure containing more general 
information at the higher levels and more specific 
information at the lower levels.

For example, information relevant to your work as a
student may be kept in files on a usb drive in a folder 
called schoolwork. Within that folder may be a separate 
folder for each course, as well as a separate folder for 
administrative documents not related to any given 
course. There might be a folder for each term containing 
a schedule for that term, grades for that term, and 
more. On the other hand, you may divide such folders 
differently: into group work and individual work. Or you 
may organize according the types of files, with videos
in one folder, music in another, and text documents in 
another.

## Piling: using tags to organize information

Piling refers to dumping information where it is most 
convenient. The piler makes no effort to move 
information around. Instead, the piler usually uses tags 
of some kind to find information. The piler may create 
these tags or take advantage of existing tags.

For example, Mac users employ Spotlight, a local search 
engine to find files using (mostly) words in the files.  
Those words are automatically indexed by Spotlight into 
a tagging system, especially while the computer is 
otherwise idle. As another example, the IMDB has a file 
containing keywords for each movie recorded---if someone 
cares enough about that movie to type in keywords. You 
can search for a movie by entering any of these 
keywords.

What's problematic about such a system? One issue is 
that a given user does not necessarily know what 
keywords are available to describe a given concept. The 
IMDB tries to overcome this be presenting a display of 
all the keywords that appear in movies that share the 
keyword being searched. How else could you try to 
overcome this limitation?

Another limitation of tags is that words have different 
*senses* so that searches for words like net and rock 
return results that may not be of interest depending on 
whether the search is for tennis or the web or music or 
geology. How can you try to overcome this limitation?  
One way is to use context. For instance, your browser by 
default saves the most recent URL you visited as a 
*referrer* and makes it possible for the administrator 
of the next URL to identify it. If my referrer has the 
string *wimbledon* in it, am I more likely to be looking 
for tennis or the web?

A typical business use of tags can be found in Adwords, 
the main way Google earns revenue. An adword is a tag 
associated with an advertisement. A business can pay to 
be advertised when an adword appears in the Google 
search window.

## Exercise: share best practices

1. Form an ad hoc group of four (four is an ideal
   number---three or five if you must).

2. Share a google doc between the four group members and
the instructor.

3. Each member of the group writes three paragraphs
   describing your personal information process. The first
   paragraph describes what you do. The second paragraph
   describes what works well about it. The third
   paragraph describes what does not work well about it.

4. Discuss the resulting paragraphs

5. Write two total paragraphs as a group describing the
strengths of individual members you all agree should be
carried forward and the weaknesses of individual members
you all agree you do not want to include in your
personal information management process. These two paragraphs should constitute a summary of what you all agree on. If you feel that a point of disagreement merits sharing with the rest of the class, you may optionally add that as an additional paragraph.

Some valuable readings can be found at the following
URLs. These were all obtained by googling the expression
*pilers-vs-filers* and appeared in the first three pages
of results. These are replicated in the resources folder on
MyCourses. The names are the MyCourses files, while
the links are the google result links.

[FilersVsPilersForbes](http://www.forbes.com/sites/bwoo/2013/02/20/are-you-a-filer-or-piler/)

[FilersVsPilersEconomist](http://www.economist.com/node/1489224)

[Jones2011](http://books.google.com/books?id=byN4SPUt6RgC&pg=PA212&lpg=PA212&dq=filers+vs+pilers&source=bl&ots=d_4Bm_sAaG&sig=78Fkf46OjWKAbNb56L3sUKQfULY&hl=en&sa=X&ei=M5PVUu-eNoLmoAS-kYII&ved=0CEkQ6AEwBDgU#v=onepage&q=filers vs pilers&f=false)

Note that each of these readings has a different form of
credibility, to be discussed in a later section of the
course. When you use a search engine to discover
information about a topic, you must be sensitive to
issues related to the search engine and to the
information sources linked. Here, I will just give a
brief blurb about each source.

Forbes was a US magazine for decades before it created
an online presence. It cultivates an image as a maverick
business publication, espousing values favoring
considerable social and economic freedom for
individuals, and a blunt style, connecting business
success to individuals rather than organizations.

The Economist is a conservative British weekly magazine.
A policy advisor to US President Clinton once told me
that The Econ\-omist is the most widely read publicly
available weekly publication among presidents and prime
ministers of nations worldwide.

The Google Books result is a page from a book
 called *Personal Information
Management*, edited by William P Jones and Jaime Teevan.
This book is a collection of chapters by scholars who
write about information systems. This book
introduces the mainstream academic thinking about
personal information management. It introduces what
scholars who do studies about personal information
management have concluded over the past thirty years of
study.

# Descriptions of Information

People studied *information overload* long before the
Internet made it a tired phrase. In psychology classes
you may have seen videos of famous experiments such as
passing the basketball. In this experiment, a person
watches a group of people passing basketballs and is
asked to count the number of total passes and keep them
in mind. The person is told that accuracy is very
important. The real purpose of the basketball passing is
to overload the person with information. Meanwhile, a
person wearing a gorilla costume walks through the room.
After the exercise, the researchers ask the person if
anything unusual happened. The person invariably replies
that nothing unusual has happened. The researchers then
show the person a video of the preceding few minutes,
including the person in the gorilla costume. Invariably
the person is shocked. The person almost *never* accepts
that someone in a gorilla costume walked in front of
them until they see the video evidence. This
demonstrates the astounding power of information
overload to shut down our perceptions of our
environment.

Similar experiments abound. There is, for instance, one
experiment where a researcher with a map in hand walks up to
someone on a crowded London sidewalk and asks for
directions. While the bystander tries to think of the
best route, two uniformed workmen walk between the
researcher and the bystander, carrying a large heavy
mirror. Concealed behind the mirror is another
researcher of a different race and sex but carrying an
identical map in the same folded orientation. The
original researcher moves along with the two workmen who
speed past so that there is only a moment when the
bystander can't see the researcher. The new researcher,
of a different race and sex, tries to carry on the same
line of questioning as if nothing had happened. Video of
the encounters suggests that the bystander usually does
not realize the change because of the information
overload resulting from trying to visualize the landmark
under discussion and the route information.

Both these experiments and many similar ones are
described online under information overload or cognitive
overload or similar terms.

In addition to studying the effects of information,
there are many scientists studying information itself
and the characteristics that define information and
distinguish one kind of information from another.

## Unstructured information

The term unstructured information may be a bit 
misleading. It typically refers to information that is 
indeed structured but whose content does not follow very 
strict rules.
For example, a news article or a blog post could be 
considered unstructured information. An article usually 
has a title but not always. It does not follow a strict 
rule as to whether or not it is titled or subtitled. It 
may or may not have pictures. It may have varying 
numbers of paragraphs, tables, diagrams, comments from 
users, links to related articles, or other features. The 
key is that it is completely flexible about these things 
and the person who presents the article does not have to 
think about conveying the structure of the article to a 
computer program, only to a human reader. Human readers 
are much more forgiving of lapses in structure than are 
computer programs.

This lack of structure is really a matter of degree and 
is best understood by comparing it to the following 
terms.

## Semistructured information

Semistructured information re\-fers to labeled information 
such as is found in forms filled out by people. When you 
fill out a form, each place where you can insert 
information contains a label telling you what kind of 
information belongs there. There are some rules but it 
is often quite easy to break rules for completing forms.  
Some forms enforce rules by not allowing you to type in 
any information that violates the rules. A good example 
of this can be found in income tax forms online.

Yet most online forms allow the person filling them in 
some flexibility and may contain instructions that can 
be disobeyed. For instance, you may be transgendered and 
asked to fill in M or F in a box marked gender. You may 
be able to enter a T or leave the box blank, depending 
on how much time and money was spent on developing the 
form. If you do enter something unexpected, the person 
or program processing the form has to decide how to 
handle it.

It is a hallmark of semistructured information that some 
human intervention is required to process it because 
some entered information can not be anticipated.

## Structured information

Structured information obeys strict rules and can be 
processed in extremely large volumes at high speeds and 
can be aggregated easily to determine, for instance, how 
many orange shirts in size L were ordered on game days in 
the 2013 season. Structured information is often passed 
from one computer program to another. Systems that 
process structured information use various techniques to 
diminish the effects of human error, including bar code 
readers, credit card readers, qr code readers, nfc 
readers and similar devices to obtain information. When 
human input is needed, it is often restricted. For 
instance, when a fast-food cashier takes an order, they 
often press a touchscreen area with a picture of the 
item being ordered rather than trying to type a name or 
a price, both of which are supplied by a computer 
program reading the touchscreen.

Most structured information in and between large organizations is presented in one of two main ways, as relations or as hierarchies.

## Relational data

By far, the most prevalent form of data in large organizations 
today is relational data, stored in database products 
such as Oracle, SQL Server, and MySQL.

Relational data is presented in tables consisting of 
rows and columns.  The rows refer to entities and the 
columns refer to attributes of the entities. An example 
of an entity is a customer. An example of an attribute 
is a zip code for that customer.

A key characteristic of relational data is that the rows 
and columns of one table are usually linked to the rows 
and columns of many other tables. In order to speed 
processing of relational data, a given table should be 
long (many rows) and thin (few columns). So, rather than 
have a table that describes a customer, the information 
about a customer may be spread over many tables, each 
with only a few columns.

## Hierarchical data

The second most frequent way to present enterprise data is 
in a hierarchical format. XML and JSON are among the 
most common hierchical formats in general use.
To illustrate what the term *hierarchical* means, 
consider a waybill as an example.
One international waybill used by FedEx has four main 
headings and some required subheadings and optional 
subheadings. For instance, there can be an intermediate 
consignee in addition to an ultimate consignee.
The description of commodities to be shipped has a 
number of subheadings, not all of which are applicable 
to every kind of commodity. Hence, for each commodity 
there is a choice of entering number or unit in addition 
to quantity. Each commodity has a number, a description, 
a weight, and a value.

So an example hierarchy might look like this

\begin{verbatim}
 Sender
   Sender Name
   Sender Address
   Sender Account Number
 Recipient
   Recipient Name
   Recipient Address
 Commodities
   Commodity 1
     Quantity
     Unit / Number
     Weight
     Value
   Commodity 2
     Quantity
     Unit / Number
     Weight
     Value
 Authorization
\end{verbatim}

A key characteristic of this hierarchical form is that 
it can present exactly the same data as in the 
relational form above. In other words, the above 
hierarchy could be converted to tables of rows and 
columns. Many computer programs just translate between 
one form and the other, depending on immediate needs.

## Big data

The term *big data* refers to collections of data that 
can not be processed on a single computer. The 
traditional tools of computing are inappropriate for 
*big data* because they require that the data be 
available for processing on a computer.

A major breakthrough for everyday computing occurred 
when the founders of Google developed a way to process 
*big data* using large numbers of very inexpensive 
connected computers. The method they used has become the 
standard for working with *big data*. MapReduce was the 
name Google gave to its original framework and it has 
become a generic term, like Kleenex, to describe other 
examples of the framework, such as Hadoop, the most 
popular implementation.

The way in which these very inexpensive connected 
computers work together is in a kind of tree structure, 
where one computer at the top of the tree gives orders 
to other computers in the tree and receives results from 
them.

Two key characteristics of this approach are that no one 
computer in the tree has all the data and that no one 
computer is unique. These two characteristics enable
scalability and fault-tolerance.

## Memes

@Dawkins1976 coined the word *meme* in the following paragraphs, which follow a discussion of the primordial soup and of the gene as the prevalent replicator on Earth.

\begin{quotation}
The new soup is the soup of human culture. We need a name for the new replicator, a noun that conveys the idea of a unit of cultural transmission, or a unit of imitation. ‘Mimeme’ comes from a suitable Greek root, but I want a monosyllable that sounds a bit like ‘gene’. I hope my classicist friends will forgive me if I abbreviate mimeme to meme. If it is any consolation, it could alternatively be thought of as being related to ‘memory’, or to the French word même. It should be pronounced to rhyme with ‘cream’.

Examples of memes are tunes, ideas, catch-phrases, clothes fashions, ways of making pots or of building arches. Just as genes propagate themselves in the gene pool by leaping from body to body via sperms or eggs, so memes propagate themselves in the meme pool by leaping from brain to brain via a process which, in the broad sense, can be called imitation. If a scientist hears, or reads about, a good idea, he passes it on to his colleagues and students. He mentions it in his articles and his lectures. If the idea catchs on, it can be said to propagate itself, spreading from brain to brain. As my colleague N. K. Humphrey neatly summed up an earlier draft of this chapter: `$\ldots$ memes should be regarded as living structures, not just metaphorically but technically. When you plant a fertile meme in my mind you literally parasitize my brain, turning it into a vehicle for the meme’s propagation in just the way that a virus may parasitize the genetic mechanism of a host cell. And this isn’t just a way of talking—the meme for, say, “belief in life after death” is actually realized physically, millions of times over, as a structure in the nervous systems of individual men the world over.'
\end{quotation}

In the years since Dawkins coined the term, it has become popular to study the concept of memes and to track memes, thanks to the Web. Our awareness of memes as a force informs our interaction design in many ways. There can be no doubt that the most successful users of the web, such as Google and Facebook, maintain a keen sensitivity to memes. As a thought exercise, examine an electronic artifact, such as a website or smartphone app, and try to identify the presence and influence of any memes upon it. As a similar thought exercise, try to identify memes in your own work.

# Finding information

Nearly half a century ago, Nobel Prize winner
Herbert Simon is alleged (the origin of the quote has 
been the subject of some controversy) to have said that 
*in the future, attention will be our most precious 
resource*. He may have meant that so much information 
will be available that we will only be able to pay 
attention to a small fraction of it and that the problem 
of deciding what to pay attention to will become the 
prominent problem of the information-intensive era.

Relationships between businesses and between businesses 
and customers have been transformed by the ease with 
which information can be found online. This 
transformation is ongoing. As an example of current 
change, some retail stores in 2013 still forbid the use 
of smartphone cameras because they fear the use of 
search engines to make price comparisons. This is 
clearly not sustainable behavior. (To see why this is 
not sustainable, consider the point of view of the 
smartphone user making price comparisons. Is it more 
likely that the smartphone user will eliminate this 
particular store from the selection set or abandon the 
use of their smartphone?)
If behavior is not sustainable, then we have to ask 
whether a steady state will be achieved and, if so, how 
it will differ.

## Search engines

A person using a search engine reveals a great deal of 
personal information that has value for various stakeholders including business and government.
Some activists believe that individuals should be 
compensated for the personal information they share with 
search engines. They believe that the contribution made 
by users to search engines can be quantified. Others 
claim that users are compensated by search results and 
should quit complaining about search engines getting 
rich. But if the value of search results can be 
quantified and the value of user contributions can be 
quantified, policy makers may be convinced that 
consumers are being exploited and may seek to regulate 
search engines. This is one way the search engine 
industry may change in the near future.

Reading: Page and Brin, 1998. The
PageRank Citation Ranking:  Bringing Order to the Web.
[stanford IL pub](http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf)

Also, the Wikipedia entry on PageRank has some wonderful
graphics illustrating the basic concept.

## Information scent

The term *information scent* may be a little confusing 
because it is borrowed from anthropology. It refers to 
the expectation of finding information along a given 
path. The strongest scents represent some balance of the 
easiest catches and the most nutritious meals.

The root concept comes from our primitive ancestors 
foraging for food and using scent to choose paths. When 
the scent stops getting stronger, a given path is 
abandoned.

Similarly, psychologists have found that when the 
expectation of finding information stops growing along a 
given information path, the path is abandoned.

The omnipresence of Google as a way for products and services to be 
found has led their providers to focus on providing an 
appropriate information scent online. The result is that 
the web presence for successful enterprises fits into a 
predictable pattern where, to continue the food analogy, 
visitors can get a quick snack, the menu changes 
frequently and predictably, and the dishes are easy to 
find, understand, and digest.

Reading: Tracking the Scent of
Information, APA Monitor, V 43, N 3, P 44.
[Tracking the scent of information](http://www.apa.org/monitor/2012/03/information.aspx)

## Information credibility

Currently, information available online can come from 
obscured or relatively anonymous sources.

Currently, there are low barriers to presenting 
information online. For many reasons, information 
obtained online may not be credible. Using information 
obtained online requires consideration of credibility, a 
concept which has been defined differently by various
communities. Some of the concepts used in describing 
credibility include the following.

1. Technical knowledge, skill or expertise
2. Consistency of actions, values, meathods, 
   measures, principles, expectations, and 
   outcomes (definition of journalistic integrity 
   from Wikipedia)
3. Objectivity
4. Pecuniary Interest
5. Agreement with ideas and values held by the 
   recipient
6. Community membership
7. Precision (variance)
8. Accuracy (bias)
9. Falsifiability (using scientific method)

Reading: College Students' Credibility Judgments in the
Information-Seeking Process. Chapter 3 of *Digital
media, youth, and credibility*, 2011.

## Getting help

In a previous era, selection of computer applications 
was contingent in part on the availability of help for 
usage of the applications. Vendors providing 
applications had to determine optimal expenditure of 
resources on help facilities to be viable in the market.

Today, in contrast, the most prevalent forms of help for 
the use of computer applications are Youtube videos and 
user communities.  At this writing I am specifically 
referring to the Youtube service rather than videos 
services in general, based on a 2013 study of online 
video traffic.

Youtube has created a low-barrier marketplace for help, 
allowing individuals with relatively few resources to 
assess the best opportunities for profiting from the 
provision of help for computer applications. This means 
that institutional adopters of computer applications can 
use the level of available Youtube help as a proxy for 
the *health* of a given computer application, replacing 
possibly tedious and expensive primary research.

User communities spring up around successful computer 
applications and can be used as a cheap and convenient 
way to evaluate those applications in much the same way 
as Youtube videos. Unlike individual videos, user 
communities may transcend individual products or 
individual vendors. An online help community such as 
Stack Overflow thrives on a reputation that transcends 
that of any individual product. The relative attention 
Stack Overflow pays to a given product may serve as an 
index of that product's health.

## Exercise: comparing help for two browsers

Form an ad hoc group of four.
Identify two browsers, such as Chrome, Firefox, Safari, 
or others. Contrast the Youtube videos and user 
communities offering help for the two browsers.

Compare the health of the browsers.

Compare the communities supporting the two browsers and 
identify differences in focus, emphasis, direction, and 
mission.

# Networked information

The term *network* is used in two main ways in the 
computing world.  Both of these senses are critical for 
an understanding of the flow of information but 
they are very very different.

The first, and oldest, sense of the word is to describe 
the physical connections between computers. This 
includes the hardware and software that allows one 
computer to communicate with another computer and with 
larger groups of computers including the largest group 
of computers, the internet.

The second sense in which the word *network* is used 
comes from the emerging discipline of network science.  
This field of study has only been named in the past 
twenty-five years but draws on ideas dating back much 
further. It is relevant to us because it explains the 
behavior of all kinds of networks, including computer 
networks. Recent advances in network science have 
identified phenomena like *the long tail* and growth and 
decline of online communities such as Facebook and 
Myspace.

# Organized information

Designers use an almost folkloric understanding of how people organize information to design information artifacts to work with rather than against people. Some of the borrowings from other disciplines studying the organization of information include the following.

## Labeling
We can group information together under labels or without labels. The latter activity is usually called clustering while the former is often called categorization. If we have labels, the question arises as to where the labels come from and who gets to identify them.
Famously, John Dewey reserved many labels in his library classification system for items familiar to him and European men like him, but few labels for items that were familiar to the vast majority of humans. Card sorting is a common way to elicit labels.

## Grouping

When we group information together, we typically have a purpose.
For example,
some people studying animals have proposed labeling the classification of animals according to a food chain and features of animals such as their teeth and jaws that predispose them to eating similar things.

Psychologists who study grouping used to believe in the notion that people group things together by a process that can be approximated by counting similar attributes shared by different things.

More recently, psychologists led by Eleanor Rosch have claimed that people hold mental images of what they call prototypes of groups. Here the word prototype is NOT related to the sense in which we use it in this class. The prototype for grouping is a thing that best represents the group. For example, an early experiment found that, for North Americans, the robin is the prototype for birds. Rather than evaluating attributes of other things, the mental process to group things together as birds is to compare them to the mental picture of the robin.

## Flat and hierarchical grouping

We have already considered the problem of hierarchical groupings when we said that a file could only be placed in one location but that a file could have many tags. This same idea occurs in grouping of information except that one approach allows the item of information to be replicated in as many clusters as are appropriate. This concept of flat clustering is identical to tagging in practice. Hierarchical clustering requires that no piece of information be copied so that every clustered item is unique.

## Automatic and supervised grouping

If we accept labels, we need some authority to define which things belong with which labels. That authority is usually some kind of person or group of people. If we do not require labels, on the other hand, a machine may automatically group things together without human supervision.

Supervision in this case may be very limited. For example, a person can identify the meaning of *red* quite easily so that a machine can be trained to retrieve images with large patches of red. You can probably imagine a spectrum of supervision from easy and broad on the one hand to difficult and specialized on the other hand. At the opposite end of the spectrum from *red* might be a hard concept like *evidence*. It is much harder to tell a machine what constitutes *evidence* than to tell a machine what constitutes *red*.

A common approach to helping a machine to group things together is to provide a training set and a testing set, a set of things that have been grouped to train the machine and a set of unlabeled things to evaluate the outcome of the machine's training.

## Human computation
Historically it has been difficult to obtain judgments of humans to label enough things to help computers. Recently, under the banner of human computation, scientists have developed ways to turn small tasks that are difficult for computers into games that are fun to play. An example would be to recognize birds species in pictures. By carefully arranging for different people to try to label the same picture, it is possible to obtain useful labels. Pornographers also use the results of this research to defeat captchas, which are themselves outgrowths of this research. Visitors to pornographic sites or other sites with illicit content, are asked to solve captchas to obtain admittance. These captchas are ones that the host site's robots encountered while trying to harvest content from competitors or other gated communities.

While human computation was hailed as the solution to spam ten years ago, it has turned out to have some value and some unexpected consequences.

# Prototyping

Prototyping can be practiced in many different ways. This course requires you to have used an interface prototyping tool before you start. This is because you must construct prototypes of your projects as milestones 4 and 5. These prototypes are likely to look nothing like each other. That is because the first prototype should surface discussion of your idea such that you change your idea quite a bit. The power of prototyping is revealed in part in such changes. To see how prototyping fits, let's look at the larger picture of which it is a part.

## Iterative development

The iterative method for software development follows a simple cycle 
without a predetermined number of repetitions: design, 
build, evaluate. The following example
substitutes the word prototype for build and lists some
common techniques for each phase.

## Iterative model diagram

The diagram shows prototypes as arising from design activities. We can think of design as making choices and prototyping as the implementations of these choices. Hence, in this course, I ask you to work on this link in the process. In other courses, you will sharpen you evaluations of prototypes. Here we will do very little with the evaluate node in the iterative circle. Instead, you will primarily do design activities and instantiate them in prototypes.

\begin{center}
\tikzstyle{background rectangle}=[rounded corners,fill=yellow!10]
\definecolor{protocolor}{rgb}{0.9,0.50,0.55} 
\definecolor{designcolor}{rgb}{0.9,0.1,0.0} 
\definecolor{evalcolor}{rgb}{0.3,0.4,0.5} 
\definecolor{arrowcolor}{rgb}{0.7,0.8,0.9} 
\begin{tikzpicture}[show background rectangle] 
\node (p) at (0,2)
  [shape=ellipse,draw=none,fill=protocolor,text=white,scale=0.85]
  {\sf prototype};
\node (pa) at (-1.5,2.6)
  [shape=rectangle,draw=none,fill=protocolor!60,text=white,scale=0.5]
  {\sf lowfi, hifi};
\node (d) at (4,3)
  [shape=ellipse,draw=none,fill=designcolor,text=white,scale=0.85]
  {\sf design};
\node (da) at (4.7,4.3)
  [shape=rectangle,draw=none,fill=designcolor!60,text=white,text
  width=4cm,scale=0.5]
  {\sf contextual inquiry, personas, scenarios, sketching};
\node (e) at (2,0)
  [shape=ellipse,draw=none,fill=evalcolor,text=white,scale=0.85]
  {\sf evaluate};
\node (ea) at (4,-0.8)
  [shape=rectangle,draw=none,fill=evalcolor!60,text=white,text
  width=5cm,scale=0.5]
  {\sf heuristic evaluation, user testing};
\draw [->,very thick,arrowcolor] (d) to [bend right=45] (p);
\draw [->,very thick,arrowcolor] (p) to [bend right=45] (e);
\draw [->,very thick,arrowcolor] (e) to [bend right=45] (d);
\end{tikzpicture} 
\end{center}

## Expense of iterative development

This method is inherently more expensive than the 
waterfall method for a given size of computer program.  
That is often difficult for students to understand 
because the waterfall method is usually employed when 
larger computer programs are contemplated. Therefore it 
must seem that the average cost of a program developed 
via the waterfall method is more expensive than the 
average cost of a program developed via the iterative 
method. Such an intuition is good but it ignores the fact 
that people know the iterative method costs more per line 
of computer code, so they simply don't use it on large 
programs except under certain specific conditions.

## Lack of planning detail in iterative method

The expense of the iterative method involves several 
factors. One is that it is more flexible, not planned 
out in as much detail. It's easier to save money if you 
can plan each person's schedule six months in advance.  
In an iterative project there are always more meetings 
and these meetings are often spontaneous results of 
unanticipated discoveries.

## Extra products of the iterative method

Another aspect of the expense of the iterative method is 
that it produces many intermediate results that are not 
intended to be part of the final project. To illustrate, 
consider one of the cardinal rules of the iterative 
approach: that each cycle should occupy no more than *n* 
days. Typically, *n=5* so that the evaluation step 
occurs on a weekly basis. This means that something must 
be designed and built every week. The tools used to 
design and build things quickly typically lead to proof 
of concept prototypes that can not be directly used in a 
production version of a system. Often, these tools 
involve crayons, construction paper, and flippy movies 
and no computer-based artifacts at all. The purpose of 
these prototypes is to ensure that each member of the 
team has a mental model of the system that agrees with 
that of the mental model of other members, both customer 
and developer.

## Getting everyone on the same page

A simple way to phrase the foregoing is that much of the 
expenditure of the iterative method is to get everyone on 
the same page. This very regularly turns out to be a 
non-trivial task. A good project for students is 
sometimes to develop a paper prototype after talking to 
customers and then to *overhear* the customer reaction 
to the paper prototype when shown it by others. Although 
customers may not want to hurt the feelings of the 
students when face-to-face, student groups have found 
that they will typically unleash a firestorm of 
disapproval over the most surprising things when 
reacting to a third party.

## Fidelity of prototyping
Prototypes are often categorized according to how true they are to the finished product. A high-fidelity prototype looks more like the finished product while a low-fidelity prototype looks less like the finished product. It should be much faster to produce a low-fidelity prototype than to produce a high-fidelity prototype.

It is usually psychologically easier to criticize a low-fidelity prototype than to criticize a high-fidelity prototype. I have told students to draw a picture in ball-point pen on a torn-out piece of spiral binder paper to show a customer in order to free the customer from the need to accept undesirable work because it appears to have been so effortful.

It may be easier to alter a low-fidelity prototype during its use than to do the same for a high-fidelity prototype. If a participant suggests a change in an interface, you may be able to show the participant the effect of the change more immediately in a low-fidelity prototype.

## Paper prototyping

Paper prototyping enjoys a large following. Formerly it was much faster than any other method. Artists with paper-related skills enjoy it. The fact that it consists of many pieces of paper rather than a single digital file makes it easier for people to work on it at the same time.

@Sefelin2003 says that you might prefer a paper
prototype when
(a) available tools do not support the relevant
components / ideas,
(b) team members lack software skills $\Rightarrow$
risk of disenfranchisement,
or
(c) tests are likely to lead to drawings for discussion.

@Hendry2005 tells how you might evaluate a paper
prototype on the street instead of in the lab.

## Your second prototype

Milestone 5 for this course is to construct a second prototype (in Milestone 4 you constructed a first prototype).

# References
