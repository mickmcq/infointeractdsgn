% HCIN.620 Information and Interaction Design
% Course Notes
% Draft of \today

# Introduction

## Materials You Need

You need a notebook, pencil or pen, and a phone or small tablet with a camera in it.

## A. Notebook

The notebook should be approximately 5 $\times$ 8 in. This is so that I can more easily manage collecting them and returning them to you. I have had students insist that they need larger notebooks and it has been problematic. Please restrict yourself to this approximate dimension. The number of pages is not important. If you run out of pages, you can start a new notebook.

## B. Phone

You will need a phone, preferrably a smartphone running Android, iOS, or Windows. Any other OS needs consultation with the instructor. The phone should have a camera, capable of sending the most recent picture to an email address or other network destination. A small tablet *may* make an acceptable substitute for a phone but please see the instructor if you are considering such a substitution.

Please do not bring any laptops to class unless required for assistive technologies. If you normally require a laptop in class for any other reason, try to think of this class as an opportunity to try something different. If you must bring a laptop into the classroom, try to keep it in a covered container, like a beverage.

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




### Customers of IT


# Contextual Inquiry

Rapid Contextual Design : A How-to Guide to Key Techniques for User-Centered Design
by Burns Wendell, Jessamyn
Holtzblatt, Karen
Wood, Shelley

## User experience

User experience is often abbreviated UX.
Please read @Spinuzzi2000, wherein
Clay Spinuzzi
introduces three ways to study the user experience *in situ*.
@Spinuzzi2000 compares contextual inquiry with other
approaches, so you can see why we emphasize contextual
inquiry and what we might do instead (ethnography or
participatory design).  The key sentence in the article
suggests using contextual inquiry to make radical
changes in a short time frame. It relies on an
underlying work structure that reduces the amount of
time you have to spend to understand the workplace, so
it's not suitable for completely alien work processes.
Participatory design works well for incremental changes
and empowering users.
Ethnography works best if a great deal of time (both
client time and designer time) is available and a
detailed understanding is required.  The classic example
of this in information technology is Stephen Barley's
studies of technology adoption by radiologists. Barley
obtained an MD in the course of his study.

*Spinuzzi (2000) on contextual inquiry*

- radical changes
- reliance on underlying structure
- minimal client time

*Spinuzzi (2000) on ethnography*

- radical changes
- only choice in exotic workplace
- maximal client time

*Spinuzzi (2000) on participatory design*

- incremental changes
- empowers users
- maximal client time

The second required reading for this section, `08contextualDesign.pdf`,
describes the most commonly used of the above three methods.
It's the most common for a chain of reasons. First,
the reliance on an underlying work structure minimizes the
need for client time, always an attractive feature in a
resource-constrained workplace. Second, the direct manipulation of
the underlying work structure means that existing design
artifacts can be sidestepped and radical changes are 
possible without time-consuming study and modification of
existing design artifacts.

Because contextual inquiry and its umbrella, contextual
design, have been so successful and so inexpensive to
implement, you are more likely to participate in it in the
workplace than in any other design method.
One hallmark of contextual design you may experience is the
method's reliance on extremely large numbers of post-it
notes containing atomic observations about the subject work.
A team conducting a contextual inquiry typically immerses
itself in a mass of these post-it notes, following a
structured
method for grouping and regrouping the notes to make sense
of the subject work and to organize the observations of the
client participants to reveal the essential characteristics
that will inform the new design.
Beyer and Holtzblatt's picture of immersion follows.

\begin{center}
  \includegraphics[width=4.0in]{affinity.pdf}
\end{center}





# Personas
See @Pruitt2003.
See @Cooper2007.


# Scenarios

# Prototypes

# Iterative Development

- Design
- Prototype
- Evaluate

# Design

- Intuition
- Educate your Intuition
  - Empirical Evidence
  - Principles
  - Generating Alternatives: Divergent Thinking
  - Selecting From Alternatives: Convergent Thinking
- Design Patterns
- Iterative Development Revisited

# Design Guidelines from Vendors

Much of the design action in the world today is taking place in the battle between Android and iOS for market share and mind share. Some other firms, primarily Samsung and Microsoft, have published meaningful design guidelines. Most interaction designers today, whether or not they work in the mobile space, are familiar with the following three sets of guidelines.

[Android](https://developer.android.com/design/get­started/principles.html)

[iOS](https://developer.apple.com/library/ios/documentation/userexperience/conceptual/mobilehig/)

[Windows](http://msdn.microsoft.com/library/windows/apps/hh465424.aspx)

# Lessons from History

## People

- Individuals doing work
- Individuals making discretionary use of computers
- Workgroups
- Hierarchies
- Commuties of Practice
- Communities of Life

## Perspectives

- Human Factors
- MIS
- HCI

## HCI Tools through History

- Heuristic Evaluation

# Lessons from Psychology

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

## exercise: share best practices

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

5. Write two paragraphs as a group describing the
strengths of individual members you all agree should be
carried forward and the weaknesses of individual members
you all agree you do not want to include in your
personal information management process.

Some valuable readings can be found at the following
URLs. These were all obtained by googling the expression
*pilers-vs-filers* and appeared in the first three pages
of results. These are replicated in the resources folder on
MyCourses. The names are the MyCourses files, while
the links are the google result links.

[01pimFilersVsPilersForbes.pdf](http://www.forbes.com/sites/bwoo/2013/02/20/are-you-a-filer-or-piler/)

[01pimFilersVsPilersEconomist.pdf](http://www.economist.com/node/1489224)

[01pimJones2011.png](http://books.google.com/books?id=byN4SPUt6RgC&pg=PA212&lpg=PA212&dq=filers+vs+pilers&source=bl&ots=d_4Bm_sAaG&sig=78Fkf46OjWKAbNb56L3sUKQfULY&hl=en&sa=X&ei=M5PVUu-eNoLmoAS-kYII&ved=0CEkQ6AEwBDgU#v=onepage&q=filers vs pilers&f=false)

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
that The Economist is the most widely read publicly
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

# Information

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

Semistructured information refers to labeled information 
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

## Supply chain information

Supply chains typically have a channel captain, such as
Walmart in the retail world or General Motors in the US
automotive world. These channel captains can dictate the
flow of information through the supply chain. They
typically use formal documents structured as XML or some
conceptually similar format.

XML stands for eXtensible Markup Language and it
belongs to the same family as HTML and SGML, as well as
other such markup languages.

## Exercise: mit beer game

1. Form a group of four and create a google doc in which
you choose a role for each group member. The roles are
distributor, factory, retailer, and wholesaler. One
person must play each role. Share the
google doc with the instructor.

2. Play the MIT beer game
without prior knowledge of the game except as follows.
Take a snapshot of the graphics available to assess your
status after playing for half an hour.

3. Do the reading about the MIT beer game and play it
again for half an hour and take a corresponding snapshot
of the results.

4. Write three paragraphs in the google doc. First,
describe your experience running it without prior
knowledge (except for the following paragraph). Second,
describe your experience running it after learning about
it. Third, say what you think might be key issues in the
information flow through the supply chain that affect
your success.

Minimal description: The MIT beer game is an online
simulation of a supply chain. Each of six players
represents a role in the chain between raw materials and
thirsty customers. For you to succeed, you must all
succeed. You must work together to succeed. The game
occurs in rounds. Each member of the supply chain must
make a choice before a round can begin. The game
determines your performance in each round based on the
choices you make and your history of choices in previous
rounds and external factors such as demand fluctuations.
Before you learn about the game, try playing for half an
hour without resetting (each round builds on the success
or failure of previous rounds) just knowing this minimal
description.

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

## search engines

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

__Reading: 03findPageRank.pdf. Page and Brin, 1998. The
PageRank Citation Ranking:  Bringing Order to the Web.__
[stanford IL pub](http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf)

Also, the Wikipedia entry on PageRank has some wonderful
graphics illustrating the basic concept.

## information scent

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

Reading: 03findTrackingScent.pdf, Tracking the Scent of
Information, APA Monitor, V 43, N 3, P 44.
[Tracking the scent of information](http://www.apa.org/monitor/2012/03/information.aspx)

## information credibility

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

Reading: 03findStudentCredJudgment.pdf. College Students' Credibility Judgments in the
Information-Seeking Process. Chapter 3 of *Digital
media, youth, and credibility*, 2011.

## getting help

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

## exercise: comparing help for two browsers

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

# Developing information systems

Reading: `06projmgtintro.pdf` 12 pages; exam questions
from pages 5--10

Businesses spend billions of dollars developing 
information systems. Almost all of the knowledge used to 
do so has been developed in the past fifty years and is 
considered immature and unstable in comparison with 
other fields of study.

## representational state transfer

Representational state transfer is the approach to the 
architecture of the World Wide Web. It is the most 
fault-tolerant approach to system development in history 
and businesses are increasingly seeking opportunities to 
adopt it. It is not appropriate for certain business 
functions, however, and recent research indicates that 
many businesses experience failure with other approaches 
that they adopt because these approaches are marketed as 
representational state transfer. Hence, in 2014 it 
remains useful for general business professionals to 
understand enough about representational state transfer 
to be able to recognize prospects for its successful 
adoption in business and to distinguish between viable 
prospects and others.

## development methods

Business leaders widely believe that repeatable, tunable 
processes are critical to management. Repeatable methods 
for developing information systems have been tried and 
studied since the nineteen seventies and, while still an 
immature area, a few characteristics of development 
methods have emerged as promising amidst the instability 
of the development environment. Following are a few of 
these characteristics.

### waterfall model

Most business information systems courses teach two 
families of development methods. The older of these is 
the waterfall model. It is also called the SDLC, which 
stands for Systems Development Lifecycle Model. This 
model has the following two characteristics.

First, it occurs in clearly defined and scheduled 
stages. The stages are named, planned, and staffed in 
advance. They usually have the following names or a 
similar set of names: requirements gathering, analysis, 
design, implementation, maintenance, and sunset.

Second, each party to a given project signs a formal 
agreement at the end of each stage, indicating that the 
stage has been completed to their satisfaction. This 
aspect gives rise to the word *waterfall* because, once 
the agreement is signed, there is no option to return to 
a previous stage. The water has flowed from that shelf 
down to the next shelf and can not be put back. It is 
this characteristic that most certainly determines the 
circumstances under which the model will be used. The
stages are often listed to resemble a waterfall as
shown below.

\begin{figure*}
\begin{itemize}
\item []{\color[rgb]{0.3,0.4,0.5} Initiation}\ensuremath{\rightarrow}
  {\color{pink}Application Description}\ensuremath{\searrow}

\item
[]\ensuremath{\phantom{XX}\hookrightarrow}{\color[rgb]{0.3,0.4,0.5}Analysis}
  \ensuremath{\rightarrow}
  {\color{pink}RequirementsSpecification}\ensuremath{\searrow}

\item []\ensuremath{\phantom{XXXX}\hookrightarrow}
    {\color[rgb]{0.3,0.4,0.5}Design}\ensuremath{\rightarrow}
    {\color{pink} SystemDesign}\ensuremath{\searrow}

\item []\ensuremath{\phantom{XXXXXX}\hookrightarrow}
      {\color[rgb]{0.3,0.4,0.5}Implementation}\ensuremath{\rightarrow}
      {\color{pink} Product}
\end{itemize}
\end{figure*}

These characteristics mean that the waterfall model will 
only be used in circumstances where there is a clear
separation of customer and developer organizations. The 
developers report through a different command chain than 
do the customers of the project. This approach should be 
used when there is the likelihood of lawsuits following 
disagreements. It should be used in cases where there is 
no clear common single point of authority over the 
developer and customer organizations to mediate 
disputes. Finally, it is most often used when 
extraordinarly large sums of money are involved and 
there must be clear consequences for failure specified 
at the beginning of the project.

This approach generally seems counterintuitive to 
students and its failures are legion. The so-called 
Obamacare website may be a current example, depending on 
which account you believe.

It may surprise students to know that this was the very 
first and therefore longest-lived development method 
despite its abysmal record. It may make a worthwhile 
project for students to try to figure out why smart 
people keep selecting it. The reason may be that, 
increasingly, cooperation between autonomous, 
conflicting groups is necessary for progress. The 
likelihood of disagreement may rise when a group feels 
powerful enough to successfully challenge another group 
and this likelihood is then doubly likely to arise if 
both groups feel powerful enough to successfully 
challenge each other. Also, business disagreements are 
often settled by litigation and preparation for 
litigation may be more prudent than preparation for 
mutual success.

Last, and most obvious, is that every method 
developed since the waterfall model relies in part on 
trust between all parties and the absence of formal 
communication. Will the legal department recommend such 
an approach? This is a question asked at the start of
each large project when deciding on the best approach.

### iterative model

The second method for development usually taught is the 
iterative model. This model follows a simple cycle 
without a predetermined number of repetitions: design, 
build, evaluate. One example follows. This example
substitutes the word prototype for build and lists some
common techniques for each phase. Some of these are
described in more detail under the topic *user experience*.

\begin{figure*}
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
\end{figure*}

This method is inherently more expensive than the 
waterfall model for a given size of computer program.  
That is often difficult for students to understand 
because the waterfall model is usually employed when 
larger computer programs are contemplated. Therefore it 
must seem that the average cost of a program developed 
via the waterfall model is more expensive than the 
average cost of a program developed via the iterative 
model. Such an intuition is good but it ignores the fact 
that people know the iterative model costs more per line 
of computer code, so they simply don't use it on large 
programs except under certain specific conditions.

The expense of the iterative model involves several 
factors. One is that it is more flexible, not planned 
out in as much detail. It's easier to save money if you 
can plan each person's schedule six months in advance.  
In an iterative project there are always more meetings 
and these meetings are often spontaneous results of 
unanticipated discoveries.

Another aspect of the expense of the iterative model is 
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

A simple way to phrase the foregoing is that much of the 
expenditure of the iterative model is to get everyone on 
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

## project management

The Project Management Institute (PMI) has become the
world's most popular focal
point for best practices in project management. For
example, a recent
recruiter at UO identified the PMI as the source for
project management practices at DataLogic ADC, a Eugene
manufacturer of automatic data capture equipment.
Some universities devote entire departments or even, as
in the case of Stevens Institute of
Technology, entire business schools to PMI education.
PMI practices are inescapable in information systems
development.

The main reference guide to these practices is called
*The Project Management Body of Knowledge Guide*. The
required reading for this section is an excerpt from an
earlier edition of that guide, offering some general
definitions for project management. In addition, the
*Guide* lists all the non-controversial processes in
project management and provides lists of their inputs
and outputs. By *non-controversial* I mean all the
process that the project management profession agrees
upon as a baseline. Innumerable project management
consultants offer proprietary extensions to this body of
knowledge and these extensions are not covered in the
guide, nor are the basic processes covered in any great
depth. The *Guide* simply serves as a brief summary of
the current state of agreed best practice in the field.

The significance of project management for information
systems is that most information systems activities are
organized as projects. Productive organizations may be
managed as functional areas, operational areas, a matrix
of these kinds, or entirely as projects. This latter
category is extreme but it can be seen in the
organization of Hollywood movies and in the activities
of BP, one of the world's major oil companies.

I had the
good fortune to interview a vice president of BP in 2006
and learn that BP was then trying to discover best
practices from Hollywood blockbusters in order to reduce its
exposure to operational management by outsourcing as
much of each oil rig as possible and treating each oil
rig as if it were a Hollywood feature film. Each oil rig
is as large and complicated as a 70 story skyscraper,
although it is meant to be used for far less time and
for only one purpose.
Interestingly, BP had just experienced a catastrophic
oil spill (6,000 barrels) at the time and I could not
help but wonder how large a role exposure to litigation
may have motivated its project focus. Alert readers will
note that, just four years later, BP experienced a
vastly more important oil spill (5 million barrels),
known as the Deepwater Horizon oil spill.  That event
and its aftermath are far too complex to even summarize
here. I just want to note that the project management
approach to organization may be tied to other
considerations but that they feature prominently in
contexts other than information systems.

## swim lane diagrams

Swim lane diagrams are used as a project management tool
in IT. At a minimum, they portray roles, tasks, and handoffs.
The name \textit{swim lane} arises because they look
like a swimming pool divided into lanes with a start and
finish. Each role has a lane in the pool. Each task is
rectangle inside a lane. Each handoff is an arrow from
one lane to another.

Here is an example from
[processmodeling.info](http://www.processmodeling.info/posts/swimlane-lane-or-pool-learn-to-swim-first/)
containing additional symbols specific to Unified
Modeling Language.

\begin{center}
\includegraphics[
  width=0.79\linewidth]
{swimlanes001.jpg}
\end{center}

This diagram shows three roles: accounting, hiring
manager, and human resources, as well as five tasks:
create job requisition, conduct interviews, setup
payroll, and give first day briefing. The diagram has a
beginning and an end and is read from left to right. A
top to bottom version would work just as well but there
must always be the sense that the diagram shows some
process that has a definite start and stop and a sense
of time precedence among the tasks.

The swim lane diagram is one of many project management
tools. It's so successful that you can image google it
and find many versions of it. You may be subjected to
refinements of it in the workplace, but here let's just
consider what they all have in common.

\textit{How can you produce a swim lane diagram?}

The basic swim lane diagram should be easily understood
by any worker in one of the roles displayed. The diagram
may be drawn by asking someone in each role what they do
and where their handoffs are. To construct a swim lane
diagram, therefore, requires some skill in eliciting
information from people about what they do. People find
it notoriously difficult to describe what they do unless
they are doing it. Interviewing someone about their job
usually leaves critical gaps.

When visiting a worker to get help with a swim lane
diagram, it's a good idea to construct a diagram before
you visit them. It is easier to correct a wrong diagram
than to start from scratch. It also conveys to the
person that you have been trying and need their help,
rather than that you are trying to slough work off onto
them.

The diagram you present to someone should not look
polished. If possible, do it in ballpoint pen on cheap
notebook paper. The reason to do this is to make it
clear that you don't believe the diagram is finished. If
you produce a pretty diagram with fancy software and
print it in color, the worker you interview may be more
reluctant to change it than if it looks like something
you did not intend as a finished product. Decorations
are not helpful in eliciting information that would
cause the decorations to have to be redone.

There should be a lot of room on the page that you
present to a worker and you should hand them a pen or
pencil of a different color than what you've already
drawn so that afterward, you can distinguish between
what they've added and what you've added.

It may be better to visit alone or with another team
mate. If you're interviewing a less experienced worker,
they may be more intimidated by multiple visitors. On
the other hand, a more experienced worker may have so
much information to share that you need one team member to
talk to them while another takes notes.

Recording an interview may reduce the candor of the
worker being interviewed. If you must record, it's best
to put the recorder within easy reach of the worker and
invite them to turn it off if they want to say something
off the record. Be aware that, if they turn it off at
some point, they are unlikely to turn it back on for the
rest of the interview. I take it as a signal that the
recording makes them uncomfortable and I don't ask to
turn it back on later.

Be prepared with extra paper if the interviewee wants to
start over from scratch and be sure to have a camera or
time to copy in case they prefer to work on a
whiteboard.

One skill that's hard to teach is to know when to
interrupt. If you don't understand something, you should
ask about it as soon as possible but, if you disturb the
flow of the interviewee's thinking, you risk never
getting the info that would have flowed just after the
interruption. Before you interrupt, you should have a
good idea of how to proceed after the interruption is
finished.

One luxury you may not have is to revisit the same
worker after some other interviewee has modified what
they've said. I have had this experience where two
people involved in a single process have conflicting
views of their roles. This presents an opportunity for
process improvement that is beyond the scope of this
assignment but a likely application of this tool in the
workplace.

\textit{What makes a good swim lane diagram?}

Hanna Jung, a brilliant designer, shows an impressive example of
a swim lane diagram at
[tracking civic theater volunteers](http://www.hannajun.com/aa1.jpg)
where she also includes some additional symbols related
to \textit{pain points} in the process. Since I worked
with Hanna Jung in the past, I should add something you
can learn from her. Although she excels in many, many
ways, one thing that you can see within a few minutes of
watching her work is that
she begins solving problems as soon
as they present themselves and organizes her time and
that of others to maximize impact. I've met many
students who work hard, but can only think of two other
students out of a thousand who can do as much in as
little time as Hanna Jung. When others are still getting
started, she is close to finishing. And when she's
finished, she reviews her work and that of others to
decide whether to polish it or move on to the next
problem. She never wastes time overthinking a problem.

I believe that she achieves this success through
polishing her problem solving process. She determines
how much time is available to solve a problem and
divides the time into steps so that she won't get so
bogged down in one step and fail to make it to the end.
She writes or draws her initial plan clearly and invites
others to join her, thinking about what she knows of
their skills and how they could contribute. Then she
ruthlessly sticks to the plan, moving on to step two
even if she's not satisfied with step one. This way,
there's still time to go back to the beginning if there
has been a false start. If she goes back to the
beginning, she replans all the steps with the remaining
available time. All her planning seems to take less than
a couple of minutes for the length of assignments that
are given in school, but that is because she refines the
planning from course to course.

## exercise: diagram course registration

Please form a team and share a google doc among the team
members and the instructor to create a swim lane diagram 
for course registration.

You should be able to think of many of the tasks
involved since you are the primary customer in this
process. The other roles to consider may include the
registrar, departments that offer courses, instructors
of courses, counselors, building managers, and office
managing degree granting.

The main thing you should learn in the course of
creating this diagram is how to talk to people to refine
the diagram and make it a more realistic reflection of
an actual process.

The secondary thing to learn is how to make a diagram
that shows handoffs well enough to identify possible
problems in the process. Many, many problems in business
happen in collaborations where a "chain of command" can
not solve the problem because different groups are
involved.

# Information Architecture

# Pictures

- Color
- Aesthetics
- Beauty
- Arnheim

# Words

- Google
- IR
- NLP
- Typography

# Exercises

Throughout the semester, we'll do exercises to integrate
the ideas from lecture into your milestones or to
illustrate ideas you may use in other interface and
interaction design projects.

## Draw a face

Draw two horizontal lines to divide your notebook page into three parts, so each part is about 2 and half inches high.

Step 1 is to draw a human face in left-facing profile in the top third of the page. It is important to do this before looking at steps 2 and 3. Looking at those steps will affect how you do this step, so quit reading this now and draw the face!

Step 2 is to first make sure you have already drawn a face in left-facing profile before reading further. Quit reading! Draw that face in the upper third of your page. Are you sure you've drawn it? Really? Okay, then, step 2 is to draw another face in the middle third of the page but, this time, make one change. Carefully plan this head so that the eye is halfway between the top of the skull and the chin.

Step 3 is to draw a third human face in left-facing profile in the bottom third of the page. This time, use a dime and a half dollar as aids. (This exercise was conceived in an era when half dollar coins were common---your teacher can supply an appropriately sized disk as a substitute.)

## Describe an experience

Spend 25 minutes using an app and describing your experience

## Identify domains and skills

As a group, create an interface
to help you select project groups.  This interface
should help you understand each other's domains of
interest, as well as each other's skills.  Assume that
you want to form project teams with similar domains of
interest, but different skills.

As you work, think about how you approach this as a
design problem and how you cope with the constraints on
the problem.

As an example, last semester's students created a table
with one column for each domain (or, eventually, each
possible project), and rows for each identifiable skill.
Each student was free to enter his or her name into as
many cells as they wished.  When this table was printed,
one could develop a project group by drawing a squiggly
oval around the people interested in a domain, but with
different skills.

Last semester's solution had a lot of drawbacks, some of
which did not become apparent until many people
tried to use it.  One problem was that it became
difficult to identify exact rows and columns as it
expanded.  Another problem was that people wanted to
describe their skills or domains in greater detail than
was practical in the margins of a table.  For instance,
several people felt they had differing levels of skill
using Photoshop, so that a *Photoshop* row was
too generic to be useful.  A third problem was that some
skills were discovered to be universal, causing needless
clutter as everyone announced that they could do *xyz*.
A fourth problem was that students could not edit the
table at the same time and all the relevant information
was contained in the one table.  It was very useful to
have all the information at a glance, but very difficult
to manage all that information in one big object.

I can think of a design that might be better suited to
the wiki you have available, but I prefer that you
discover your own design.

## Widget redesign

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

Work in a small group to produce a poster as the focus
of your presentation.  The poster should include (1) a
rendering of the widget as you found it, (2) a rendering
of the widget as you redesigned it, (3) some text
explaining the problem, (4) some text explaining why the
redesign is a solution to that problem, (5) directions
for interacting with the redesigned widget, and (6) a
list of other real widgets that are similar due to
either human interaction or system input.

Critique the work of other students according to three
criteria, selection, solution, and craft.  Selection
means to critique the selection of the particular
widget.  Question whether it really is a widget and
whether it warrants redesign.  Solution means to
evaluate whether the redesign really does improve the
widget.  Craft means to critique the visual appeal of
the poster.  Question the poster as a communication
design.
(This exercise was developed by John Zimmerman at CMU.)

## Ambient notification

Work in pairs.  Don't repeat last week's pairs.
Develop an
ambient notification *device* to improve email.
Notification can be of anything related to email.
(This exercise was developed by John Zimmerman at CMU.)

## Thousand floor elevator

Design an elevator for a building with 1,000 floors.
This is a single elevator compartment that can travel to
any floor from ground to the top.  You must design a
system for selecting floors and for displaying selected
floors, as well as for displaying the current location
of the elevator.  You are free to imagine any
inhabitants of the building, any users of the elevator,
but not any extraordinary speed of the elevator.  In
other words, assume only current technology is available
to physically move the elevator compartment.  As
with the previous exercise, present this to the class
and receive critiques from other students.

As before, create a poster for your elevator.  The
poster should include (1) renderings of any displays and
controls, (2) some text describing what the displays
mean and how to operate the controls, 
(3) some text about the users of the elevator
and their destinations, (4) some text about any problems
related to the extremely large number of possible
destinations, and (5) some text about how you solve any
problems related to the very large number of possible
destinations.

As before, you will critique the work of other students.
Consider roughly the same three criteria, problem and
user
statement, solution, and craft.  Question whether
the poster really addresses problems with a 1,000
floor elevator and its users, whether the presentation
offers genuine solutions, and the craft of the poster.

## phone directory navigator

For this exercise, assume your design will be accessed
on a QVGA (320 $\times$ 240) phone.  There may be a
numeric keypad and a five way rocker button, but not
much else.

Design a system to navigate a corporate hierarchical
directory.  Plan it for Globocide Corp., which has
40,000 employees worldwide.  There are seven main
hierarchies of unequal depth and we'd like to be able to
traverse them.  We'd like to be able to find the path
from any given employee to the CEO.  We'd like to get a
picture of an employee's surroundings.  How dense is the
region around an employee?  How many are above or below
a given employee?  Who are the peers of an employee?
We'd also like to get a picture of a division in
comparison with its peers.  How many are in the
division?  How tall is its hierarchy?  How does its
shape differ from peer divisions?

Your design should be shown in a series of sketches that
work at QVGA resolution and show interactions and their
effects.

## business card calendar

This exercise comes from a blogger whose 48 year old
mother complained that she could not read the tiny
business card sized calendars given away by her bank or
other businesses.  The blogger noticed that the same
numbers were repeated 12 times on the card and proposed
a design challenge to improve this design for
readability and instant recognition.
Design a business-card sized calendar
      for a blogger's 48-yo mom.
It should be immediately understandable.
maximize type size or meaningful features.
It must span 1 year.
For any date number, be able identify which month,
weekday.
Minimize steps to know a date's data.
Holidays / special days should be easy to mark.
Be able to count days between nearby dates.

## affordance matrix

Before class, take pictures or collect
pictures of affordances on devices that afford pushing,
squeezing, or turning.  Arrange the best of these
pictures in a 3 $\times$ 3 (or 4) matrix, with pushing on
the first row, squeezing on the second row, and turning
on the third row.  Bring your matrix to class for
critiques as to how well these affordances suit the
named actions, how well you have documented the
affordances, and whether your matrix is pleasing to look
at. In class, form a group and develop a *best of*
matrix for your group, including only the very best of
your individual matrices.  This is part one of a two
part exercise, to be done with the same team throughout.

## affordance device

This is the second of a two-part exercise.
Work in the same group with which you developed the
affordance matrix.
Before class, create an
interactive object in the shape of a cube that invites
the user to push it, turn it, and squeeze it.  All three
of these should be interaction modalities for the
cube-based object.  develop the
physical object itself
during the week between classes and be ready to
share it with your classmates at the beginning of the
class listing this as the exercise.
During class, put the device into a central location and
take the device of another group.  You will introduce
that device to the class without any input from the
group that created it.

Your device should have
the general look and feel of a cube, even if you choose
to add or subtract from its shape so that it is not
*precisely* a cube.  People should think
*cube* when they see it.  The affordances
you choose should show what you learned in the
affordance matrix exercise.  The affordances may be
visual, aural, or tactile.  Although you have taken them
from instrumental examples, do not reproduce the actions
caused by the interactions.  This is probably obvious in
the case of a steering wheel, to which you do not need
to attach an actual automobile to demonstrate the effect
of steering (and which may complicate your
presentation!).  It may be less obvious in the case of a
switch, where you may want to include a light that acts
as an affordance but not a light that acts as
illumination (the purpose of the interaction).
Do not work on the
actions that will be accomplished by pushing, turning,
or squeezing it.

## revisit picking up a key

Earlier in the semester, you storyboarded a five
sentence story about picking up a key and using it to
open a door.  Using what you have learned since then,
improve upon that storyboard.  Work in pairs or trios
and either refine or replace the elements you used
before when you did the exercise alone.

## anti-affordance matrix

A 1 square kilometer toxic dump must be marked so it
will remain undisturbed for 10,000 years.
Create an *anti-affordance matrix* of 1 square
kilometer.
The components of the marking system should be robust
but have little intrinsic value (note that this does
*not*
mean that it will be cheap to implement) so that they will not be
destroyed or recycled.
Use
  a *Gestalt*, so more is received than sent, 
  use a *systems approach*, so
    elements of the communications system link to
    each other, index to each other, are
    co-presented and reciprocally reinforcing, and 
  use *Redundancy*, where some elements of the
    system can be degraded or lost without substantial
    damage to the system's capacity to communicate. 

## design notebook

Please keep a design notebook throughout the semester.
I prefer the 5$\times$8 Moleskine unruled sketchbook
with 100 pages, available at Borders and elsewhere, but
feel free to select anything similar in size and number
of pages.  Update the notebook every week with
drawings.
You should document examples
of good design as you encounter them.  You can't get a
perfect score on the design notebook without adding some
good design examples each week.  You should plan to
sketch for half an hour per day, three days per week
to make a difference in your drawing skill and to
receive full credit for the notebook.  There should be a
noticeable progression in the quality of your results as
the semester progresses, so there's no need to start as
a perfectionist.
This work is to help you express your
design ideas, not to identify the most talented artist.
Plan to turn in the notebook three times during the semester
and expect examples from it to be used for this class
and future classes, so don't include anything in it
you'd prefer to not share with the class.

Most students use pencil for the notebook, and the
characteristics of a pencil figure prominently in a few
exercises.  Many exercises can be done in pen and some
can benefit from color but, for the most part, departure
from pencil will be a distraction and a
waste of your time.  You can prevent your drawings from
smudging by applying spray fixative to them.  Many
artists use Krylon Workable Fixative, for about 7USD per
can.  The word *workable* in the name signifies
that you can apply a layer after your first layer of
pencil, then begin drawing over it again.  You can do
this repeatedly to prevent smudging drawings in
progress.  Googling the term fixative just now led me to
a lot of warnings about using it outdoors to avoid the
toxic effects.  As with any other chemical, you must
exercise appropriate caution and use sensible practices.

In addition to examples of good design you encounter,
please complete the following exercises, most of them from
*Making Comics* by the dates indicated.  Include
these in the design notebook and bring the design
notebook to class on these dates to facilitate
discussion.  For each exercise, please be sure to
include the italicized name in your notebook and the
date of your completion.  This will help you to revisit
the context of your sketches and measure
progress long after you've forgotten the details of
completing them.  It will be necessary for you to title
and date the exercises to receive full credit.
Please complete these by the indicated dates so that we
can discuss your experience.
Your classmates will depend on your contribution to the
discussion.  It's very important to your contribution
that you have actually completed the exercise, not just
conceptualized it.

## Waiting in Line

(not in *Making Comics*)
Create an approximately eight panel comic of a person
waiting in line and using mobile technology.  Connect
the mobile technology to what the person is waiting for
or to other people waiting along with the person.  We
should understand what the person is waiting for and
experience the entire wait from start to finish.

## Picking up a Key

Chapter 1.  On page 13 is a
five-sentence story, told in 8 panels.  The character is
supposed to be a man.  Change the character to a woman
or creature or a different man.  Change the last
sentence (about the lion) to a different ending.  Choose
your own number of panels, anywhere from 7 to 9 panels.
Tell the story your own way.

## Favorite Movie

Chapter 1, page 56,
exercise number 1: tell the story of a favorite movie in
pictures alone with no words.  A peer should be able to
tell us what happens in the movie without having seen
it.  Do not write the name of the movie on it!

## Packing

(not in *Making Comics*)
Create an approximately eight panel comic of a person
packing.  It could be a person packing for a daily
commute or for a vacation or business trip.  Do not
include any dialog.  We should be able to identify the
kind and duration of the trip and should be able to
learn a good deal about the person doing the packing.
We should experience the entire time of packing from
start to finish.

## Unoccupied Room

Chapter 1, page 57, exercise number 7: draw an
unoccupied room in enough detail that a peer can tell
ten meaningful things about the person who lives there.
Again, this exercise should be completed in a picture
alone with no words.  Except the date of completion and
the name of the exercise.

## Two Characters

Chapter 2, page
127, exercise number 1:  Create two characters, one with
five key life history aspects that are the same as your
own and one whose life history is different in every one
of the five aspects.  Include at least two sketches of
each character.

## Captions

Chapter 3, page
157, exercise number 1: Create a series of about eight
panels to illustrate the following paragraphs from the
novel __1984__ by George Orwell.  Select captions
from the following text.  Don't use all the text (!) and
don't use any text that is not in the following excerpt.
Do not try to reveal every detail in the following
excerpt---it's purposely long to promote some
flexibility and variety between the approaches of
different students.  Make choices that convey what is
happening in the scene.  This should require some design
compromise on your part.  You should choose what is
important and leave out what is not important.  This
exercise is largely about sharpening your ability to
choose what is important.  After you have completed the
eight panels, do the exercise again, using
*exactly* the same captions but a different
series of pictures.

*Begin excerpt from __1984__*

Outside, even through the shut window-pane, the world
looked cold. Down in the street little eddies of wind
were whirling dust and torn paper into spirals, and
though the sun was shining and the sky a harsh blue,
there seemed to be no colour in anything, except the
posters that were plastered everywhere. The
black-mous\-tachio'd face gazed down from every commanding
corner. There was one on the house-front immediately
opposite. `BIG BROTHER IS WATCHING YOU`, the caption said,
while the dark eyes looked deep into Winston's own. Down
at street level another poster, torn at one corner,
flapped fitfully in the wind, alternately covering and
uncovering the single word `INGSOC`. In the far distance a
helicopter skimmed down between the roofs, hovered for
an instant like a bluebottle, and darted away again with
a curving flight. It was the police patrol, snooping
into people's windows. The patrols did not matter,
however. Only the Thought Police mattered.

Behind Winston's back the voice from the telescreen was
still babbling away about pig-iron and the
overfulfilment of the Ninth Three-Year Plan. The
telescreen received and transmitted simultaneously. Any
sound that Winston made, above the level of a very low
whisper, would be picked up by it, moreover, so long as
he remained within the field of vision which the metal
plaque commanded, he could be seen as well as heard.
There was of course no way of knowing whether you were
being watched at any given moment. How often, or on what
system, the Thought Police plugged in on any individual
wire was guesswork. It was even conceivable that they
watched everybody all the time. But at any rate they
could plug in your wire whenever they wanted to. You had
to live--did live, from habit that became instinct--in
the assumption that every sound you made was overheard,
and, except in darkness, every movement scrutinized.

Winston kept his back turned to the telescreen. It was
safer; though, as he well knew, even a back can be
revealing. A kilometre away the Ministry of Truth, his
place of work, towered vast and white above the grimy
landscape.  This, he thought with a sort of vague
distaste--this was London, chief city of Airstrip One,
itself the third most populous of the provinces of
Oceania. He tried to squeeze out some childhood memory
that should tell him whether London had always been
quite like this. Were there always these vistas of
rotting nineteenth-century houses, their sides shored up
with baulks of timber, their windows patched with
cardboard and their roofs with corrugated iron, their
crazy garden walls sagging in all directions?  And the
bombed sites where the plaster dust swirled in the air
and the willow-herb straggled over the heaps of rubble;
and the places where the bombs had cleared a larger
patch and there had sprung up sordid colonies of wooden
dwellings like chicken-houses? But it was no use, he
could not remember: nothing remained of his childhood
except a series of bright-lit tableaux occurring against
no background and mostly unintelligible.

The Ministry of Truth---Minitrue, in Newspeak
$[$New\-speak
was the official language of Oceania. For an account of
its structure and etymology see Appendix.$]$---was
startlingly different from any other object in sight. It
was an enormous pyramidal structure of glittering white
concrete, soaring up, terrace after terrace, 300 metres
into the air. From where Winston stood it was just
possible to read, picked out on its white face in
elegant lettering, the three slogans of the Party:

~~~
              WAR IS PEACE
              FREEDOM IS SLAVERY
              IGNORANCE IS STRENGTH
~~~

The Ministry of Truth contained, it was said, three
thousand rooms above ground level, and corresponding
ramifications below. Scattered about London there were
just three other buildings of similar appearance and
size. So completely did they dwarf the surrounding
architecture that from the roof of Victory Mansions you
could see all four of them simultaneously. They were the
homes of the four Ministries between which the entire
apparatus of government was divided. The Ministry of
Truth, which concerned itself with news, entertainment,
education, and the fine arts. The Ministry of Peace,
which concerned itself with war. The Ministry of Love,
which maintained law and order. And the Ministry of
Plenty, which was responsible for economic affairs.
Their names, in Newspeak: Minitrue, Minipax, Miniluv,
and Miniplenty.

The Ministry of Love was the really frightening one.
There were no windows in it at all. Winston had never
been inside the Ministry of Love, nor within half a
kilometre of it. It was a place impossible to enter
except on official business, and then only by
penetrating through a maze of barbed-wire entanglements,
steel doors, and hidden machine-gun nests. Even the
streets leading up to its outer barriers were roamed by
gorilla-faced guards in black uniforms, armed with
jointed truncheons.

Winston turned round abruptly. He had set his features
into the expression of quiet optimism which it was
advisable to wear when facing the telescreen. He crossed
the room into the tiny kitchen. By leaving the Ministry
at this time of day he had sacrificed his lunch in the
canteen, and he was aware that there was no food in the
kitchen except a hunk of dark-coloured bread which had
got to be saved for tomorrow's breakfast. He took down
from the shelf a bottle of colourless liquid with a
plain white label marked `VICTORY GIN`. It gave off a
sickly, oily smell, as of Chinese rice-spirit. Winston
poured out nearly a teacupful, nerved himself for a
shock, and gulped it down like a dose of medicine.

Instantly his face turned scarlet and the water ran out
of his eyes. The stuff was like nitric acid, and
moreover, in swallowing it one had the sensation of
being hit on the back of the head with a rubber club.
The next moment, however, the burning in his belly died
down and the world began to look more cheerful. He took
a cigarette from a crumpled packet marked `VICTORY
CIGARETTES` and incautiously held it upright, whereupon
the tobacco fell out on to the floor. With the next he
was more successful.  He went back to the living-room
and sat down at a small table that stood to the left of
the telescreen. From the table drawer he took out a
penholder, a bottle of ink, and a thick, quarto-sized
blank book with a red back and a marbled cover.

*End excerpt from __1984__.*

## Extreme Emphasis

Chapter 3, page
157, exercise number 5: create about eight panels from
the Robin Williams monologue in the extreme-emphasis.mp4
video.  This is also available on Youtube under the
title, *Good Morning Vietnam - First Time on Air.*
Your goal is to letter the monologue in a way that
conveys the extremes of expression in the comedian's
voice and face.  The drawings and continuity are not the
issue here---any eight moments from the sequence will
do.

# Milestones
Together, the following milestones constitute a project that determines half of your grade.

1. Milestone 1, Feb 05, Project Focus
2. Milestone 2, Feb 26, Contextual Inquiry
3. Milestone 3, Mar 19, Personas
4. Milestone 4, Apr 23, Scenarios
5. Milestone 5, May 21, Prototype





The CTools site has a Wiki where I've listed some
Project Possibilities in a section of the same name.

The semester long project is the most important as well as the most
time-consuming part of this course.  Past project groups
claim to have spent up to 40 hours in meetings to plan
and organize their projects, with an enormous time
commitment of solitary work between meetings.

The outcome of this project should be a digital
prototype that can be shared, preferrably via the web.
There should be a web presentation even if the design
itself is of something that is not inherently web-based,
such as an intelligent wheelchair.  It should be
possible to communicate about the project outcome via
the web, both for the class and so that you can use the
project outcome in job searching.

Our competitors do this, and you can sometimes find
remarkable project websites associated with the top
schools.  Please be on the
lookout for similar material from other schools.

It would be best if you would not hand in any paper
related to your project, but use a website that develops
over the course of the semester and is used to document
each milestone.

Please *do not* present your milestones as a
slideshow.
Please see the file
`cog-style-ppt.pdf`
for reasons to reject the slideshow
format (e.g., low data-ink ratio, inherent ambiguity of
cryptic headings, cognitive dissonance introduced by
heavily nested festivals of bullet point levels, etc.).
Please use your project website to present your
milestones.

milestone 1. project focus

Establish a website that identifies your team, your
customer, the problem, and the general direction for
solution.  Be prepared for a critique of your milestone
similar to the widget redesign critique.  After you
present this milestone, you must summarize the critiques
by your classmates on your website.  You will need to do
this for every milestone, so develop a repeatable
process.

You can use @Holtzblatt2005, chapter 2, to help
you think about the scope of the project, its
stakeholders, and your general approach.
That text identifies examples of projects with a small,
tight scope that can be done rapidly, such as usability
fixes, market characterization for new system concepts,
website evaluation and redesign, next generation
systems, supporting a coherent task, and reporting.
There is also a discussion of stakeholders that can
inform you.  You should briefly identify your proposed
stakeholders and consider the following points about
them: goals, worries, ideas, how to involve them, how to
communicate progress, how to understand their way of
communicating, and how to communicate the design to
them.  You should include a set of covenants to govern
your group.  These must be agreed to by all members and
must specify grounds for expulsion from the group. Only
ten percent of all groups wind up having to enforce
these, but they may help stave off disaster,
so everyone should form covenants.

milestone 2. contextual inquiry
Conduct a contextual inquiry for your project.
See @Spinuzzi2000 and @Beyer1999.  You can
use
@Holtzblatt2005, chapters 3 through 
8 to complete this milestone.

Conduct a contextual inquiry on a workplace to which you
have access, using the techniques described
by Beyer and Holtzblatt.

Revising milestone 1.
Part of the purpose in looking at each other's websites
after Milestone 1 was for you to see that there are
things you could have done that you didn't do, or
perhaps things you did that you shouldn't have done.
Your milestone 1 website work is not done.  Milestone 1
was about specifying the broad outlines of your project:
scope, users, problem statement, solution statement.
Those broad outlines are likely to change.  There should
always be a place on your website where people can look
to find out *the big picture* so I'm not saying that you
should do away with that and replace it with a lot of
details, but be flexible about it and go back and change
a few words or diagrams or whatever that tell the big
picture as you go along.  Refer to that so that the big
picture directs you when you have to decide which
details are relevant.

Products.
You are likely to find that there are natural products
of a contextual inquiry that can be added to your
website.  Your website should help you as a team.
Typically a team has to come together to do some
activities, then go off individually to do others.  Your
website can be used to document the things you do as a
group so that individuals can use them, and to document
what individuals do that needs to be reported back to
the group.

Planning.
You will plan your interviews and the interpretation
session that follows and the construction of any
artifacts you develop like affinity diagrams.  This
planning can go on the website in the form of a schedule
or checklist that individuals can refer to.
@Holtzblatt2005 has several relevant checklists,
such as the CI process checklist (pp 80--81).

Interviews.
Individuals need to conduct their interviews so they
can be used in the interpretation session which,
according to @Holtzblatt2005, should
occur within 48hrs (p 101) after the interview.
Realistically, between now and Wednesday, you'll only
have time for one of these cycles.  By completing an
entire cycle, you'll have a blueprint you can refine for
future use.  One timesaving feature advocated in
@Holtzblatt2005 is to avoid discussing an
interview before an interpretation session (p 101).

Interpretation session.
You should have a lot of data after an interview and it
should be a challenge both to share it and to make sense
of it.  You should review, analyze, and capture key
issues in an interpretation session.  A natural product
of this activity is the affinity note, which becomes a
natural input into the next activity, constructing an
affinity diagram.  Chapters 6 and 7 of @Holtzblatt2005
give guidance on capturing sequence models,
artifact models, and physical models, and using them to
construct affinity diagrams.  These are
different for different projects, especially the
physical models, although the use of affinity notes are
likely to pervade all groups.

Affinity Diagram.
@Holtzblatt2005 gives very detailed
guidance about developing an affinity diagram from
affinity notes.  One thing that I would like to add is
that you can probably get a lot more done by using a
paper process than by using an online tool.  It's harder
to document a paper process on a website, though.  My
best suggestion is that you get two Elmer's display
boards, 36" $\times$ 48" \$3.60 in bulk, \$7.39 individually at
OfficeMax.

Use these and post-it notes and just bring the results
to class to present.
Last semester, the most productive groups found it
difficult to fit everything onto one of these boards.
Less productive groups found it quite easy and even had
space left over.  If you find that you have sparsely
populated one of these 3' $\times$ 4' boards, you
probably haven't dug deeply enough.  On the other hand,
adding more post-it notes until the thing is covered may
only mask the problem of not digging deeply enough,
rather than solve it.  One group last semester made the
unwise decision to omit pink and green labels altogether
so they could concentrate on boosting the number of
yellow post-it notes, having discovered that they could
not reach the minimum specified in
@Holtzblatt2005.  (The above color scheme is
clarified in detail in @Holtzblatt2005 ---
basically the above means that they did no grouping of
notes into themes at all).  As a result, they were
unprepared to say anything analytical about what they
had found, instead trapped at the individual anecdote
level.

There is a lot of software for doing affinity diagrams,
but the overhead is significant and it's harder for a
group of people to interact with tools that are
inherently meant for one person, one keyboard, one
mouse.  If you have a bunch of post-it pads and are
sitting around a posterboard display on a wall or a
conference table, you can generate a lot more material
faster.  By the way, you could just do stuff on a wall,
but then you have to figure out what to do with 500 --
1,000 post-it notes afterward.  The display board gives
you something you can fold up.  If you tie it tightly
enough or cover the surface with spray or tape or
staples, you may find that post-its will retain their
positioning.

milestone 3. personas & scenarios
See @Pruitt2003.
You can use @Cooper2007,
chapters 4 and 5 to complete the persona portion of this milestone.

You can use @Cooper2007,
chapters 6 and 7 to complete the scenario portion of this milestone.

Expect your scenarios to differ from those produced by other teams.
Most teams will provide context scenarios and will use
them to address questions such as the following.
(1) What is the setting in which the product will be
used?
(2) Will it be used for extended periods of time?
(3) Will the persona be subject to frequent
interruption?
(4) Are there multiple users of a single device?
(5) What other products is it used with?
(6) How much complexity is permissible, based on
persona skill and frequency of use?
(7) What primary activities does the persona need to
accomplish to meet his / her goals?
(8) How does the product relate to the user's higher
goals?
(9) What is the expected result of using the product?

Not every team will address all these questions, nor
will every team use context scenarios.  Most teams will
create scenarios of users successfully reaching goals,
rather than scenarios showing dysfunctional outcomes.
It's often the case that the most we can say about
dysfunctional scenarios is "Okay, don't do that then."
We usually prefer richer scenarios than would be
possible in a scenario that shows failure to meet goals.


milestone 4. lo-fi prototype
You can use @Holtzblatt2005, chapter 13, to
complete this milestone.
%Note that it may seem backward
%to create a lo-fi prototype before a scenario, but my
%experience has been that there is great educational
%value in creating a prototype early in the process,
%particularly for inexperienced students.  There is
%nothing to prevent you from doing some scenario work in
%preparing this milestone, but we need more iterations of
%a prototype than would be practical if we switched this
%milestone with the next one.

The lo-fi prototype is supposed to generate discussion
and to be something you can readily throw away and
rework.  If it is due shortly before the hi-fi
prototype, you  will be tempted to refine it rather than
rethink it.  There'll just be too much pressure from
that looming hi-fi prototype deadline.  I tried to put
lo-fi prototyping as early in the milestones as I could
and was even tempted to try to stick them in before
personas, but finally decided that that was just too
early.  The lo-fi prototype should generate discussion.
Expect to discuss them a lot!  Expect to rethink them
and make better scenarios because of having rethought
them.

milestone 5. hi-fi prototype
The outcome of this milestone should be something viable
for user testing.  You should not have to modify this
so you can use it for testing.  Therefore, the
definition of hi-fi may be relaxed.  This may well be a
mid-fi prototype.  The goal is to prepare something you
can use to gain relevant knowledge about the design from
users.

final project presentation
The thrust of this presentation will be to have
conducted user testing on your hi-fi prototype and to be
able to report on that testing.  You should
*briefly* summarize your project and spend at
least two-thirds of your time discussing user testing
and its impact on your design.
You will have to have conducted user testing for this
presentation to be successful.
You will have to connect that testing to your design and
tell how your design should change based on that testing
for this presentation to be successful.




# Resources

Blogs and bloggers exemplify resources that are
underdocumented in the academic literature.  Many
designers look to *A List Apart* or
*Alertbox* for ideas and inspiration.  A very
long list of "celebrities" maintain an online presence
with a remarkable influence on contemporary designers.
They include
Aza Raskin,
Jesse James Garrett,
Mimi Ito,
danah boyd,
Jacob Nielsen,
and many more.

Plenty of online tools are part of a typical designer's
workday, such as
kuler.
Some platform specific tools like Axure have big
followings.

I use Wikipedia as a reference for many topics.  For
instance, the Wikipedia entry on HSV color space
provides a good introduction to some important terms
about color.  Wikipedia urls typically have a format so
that if I refer to the entry on HSV color space, you may
assume that the url (for the English language version) is
[http://en.wikipedia.org/wiki/HSV_color_space](http://en.wikipedia.org/wiki/HSV_color_space).
Wikipedia remains controversial among many academicians.

A valuable resource for HCI literature can be found at
[hcibib](http://www.hcibib.org).  You
may find it helpful for much of your work.

# References
