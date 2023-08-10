
# Milestones
Together, the following milestones constitute a project that determines half of your grade.

1. Milestone 1, Project Focus
2. Milestone 2, Contextual Inquiry
3. Milestone 3, Personas
4. Milestone 4, Lo-fi Prototype
5. Milestone 5, Hi-fi Prototype

The semester long project is the most important as well as the most
time-consuming part of this course.  Past project groups
claim to have spent up to 40 hours in meetings to plan
and organize their projects, with an enormous time
commitment of solitary work between meetings.

The outcome of this project should be a digital
prototype that can be shared, preferably via the web.
There should be a web presentation even if the design
itself is of something that is not inherently web-based,
such as an intelligent wheelchair.  It should be
possible to communicate about the project outcome via
the web, both for the class and so that you can use the
project outcome in job searching.

Our competitors do this, and you can sometimes find
remarkable project websites associated with the top
schools.  Be on the
lookout for similar material from other schools.

It would be best if you would not hand in any paper
related to your project, but use a website that develops
over the course of the semester and is used to document
each milestone.

Please *do not* present your milestones as a
slide show.
Please see the introduction and the file
`cog-style-ppt.pdf`
for reasons to reject the slide show
format (e.g., low data-ink ratio, inherent ambiguity of
cryptic headings, cognitive dissonance introduced by
heavily nested festivals of bullet point levels, etc.).
Please use your project website to present your
milestones.

## Create a project website

*Important note! Since writing the following section, I have been informed that the facility described has deprecated in favor of a new system of which I have no details. I'm leaving this as a placeholder but will probably have to change some details early in the semester.*

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

## Diverge, then converge

You must do two things to develop a creative project and meet deadlines. You must first diverge, then converge. Divergence is fun and, in my experience, people spend too much time on it, then go into a frenzy of convergence. You must decide in advance what fraction of your time is spent on each process and be decisive about switching from one mode to the other when your time comes.

The same is true for gathering ideas and implementing them.
If you've overused the web for a decade or more you probably remember the meme involving Hitler getting bad news in the film *Die Untergang* (2004). People would subtitle the scene endlessly with bad news affecting different hobbies, occupations, sports, or celebrity foulups. 

Did you know that there were even versions for HCI? Yes, HCI is everywhere. And HCI people seemingly have time to throw up endless websites with internally conflicting advice, eternal truths, urban legends, and the occasional valuable piece of information. During your program here, you need to find a way to better cope with all the HCI information coming at you from every direction. You need to share with each other how you get information as well as how recall information when you need it. As you approach a difficult milestone like contextual inquiry, it will be tempting to keep gathering information right up to the last minute. Resist that temptation! You already know too much!

Making a deadline is a convergent process. You don't want to be open to new ideas. You want tunnel vision near a deadline. Any new information you receive has to be put somewhere you can find it after the deadline. Over half of your classmates probably don't have a good place to put new information right now. So put it anywhere and concentrate on processing the information you have right now.

## Milestone 1. project focus

Establish a website that identifies your team, your
customer, the problem, and the general direction for
solution.  (*Onsite version of the course only: Be prepared for a critique of your milestone
similar to the widget redesign critique.  After you
present this milestone, you must summarize the critiques
by your classmates on your website.  You will need to do
this for every milestone, so develop a repeatable
process.*)

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

## Milestone 2. contextual inquiry
Conduct a contextual inquiry for your project
on a workplace to which you
have access.
You can
use
@Holtzblatt2005, chapters 3 through 
8 to complete this milestone.
Also see @Spinuzzi2000 and @Beyer1999.

### Revising milestone 1
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

### Products
You are likely to find that there are natural products
of a contextual inquiry that can be added to your
website.  Your website should help you as a team.
Typically a team has to come together to do some
activities, then go off individually to do others.  Your
website can be used to document the things you do as a
group so that individuals can use them, and to document
what individuals do that needs to be reported back to
the group.

### Planning
You will plan your interviews and the interpretation
session that follows and the construction of any
artifacts you develop like affinity diagrams.  This
planning can go on the website in the form of a schedule
or checklist that individuals can refer to.
@Holtzblatt2005 has several relevant checklists,
such as the CI process checklist (pp 80--81).

### Interviews
Individuals need to conduct their interviews so they
can be used in the interpretation session which,
according to @Holtzblatt2005, should
occur within 48hrs (p 101) after the interview.
Realistically, between now and your deadline, you'll only
have time for one of these cycles.  By completing an
entire cycle, you'll have a blueprint you can refine for
future use.  One timesaving feature advocated in
@Holtzblatt2005 is to avoid discussing an
interview before an interpretation session (p 101).

### Interpretation session
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

### Affinity Diagram
@Holtzblatt2005 gives very detailed
guidance in Chapter 8 about developing an affinity diagram from
affinity notes. I won't reproduce that guidance here but I will give a brief overview. Beware trying to use this overview as anything more than an introduction. Your diagramming session could easily drag on for eight hours if it is to succeed. You really need more detailed guidance to complete it. The following paragraphs give an overview of these steps:

1. Add 500 post-it notes to the wall
2. Add the bottom level of labels above the post-it notes
3. Add the temporary top level of labels and reorganize all the notes and labels to fit them.
4. Remove the temporary top level labels.
5. Add the middle level of labels.
6. Add the top level of labels.

Note that there are four *levels* of post-it notes. The lowest level is the atomic observation, referred to as an affinity note by Holtzblatt. These each simply copy one thing a participant said. For example, a participant might say "I hate the menu system because it's so hard to navigate." The other three kinds of post-it notes are the affinity labels, as Holtzblatt calls them. There are top, mid, and bottom level labels. For example, a bottom level label for the above note could be "challenges navigating the menus", while a higher level might be "menus" or "navigation".

The overview of the process is that you use post-it notes grouped together on a wall, preferrably on enough wax butcher paper taped to the wall so that a group of four can comfortably navigate and fill it with about 125 groups of 4 notes. Holtzblatt suggests starting with about 500 yellow post-it notes that represent atomic items (step 1). These are the affinity notes mentioned in the description of the Interpretation session. Your group should stop when you can no longer keep track of the groups of these yellow notes.

Next (steps 2 through 6), @Holtzblatt2005 describes a process of labeling these roughly 500 notes with three layers of notes of different colors. I find the colors confusing so my brief overview will simply refer to the bottom level, the middle level, and the top level. You start with the bottom level but, confusingly, you next proceed to the top level as a rough cut. Then you remove this temporary top level, build the middle level and finally the actual top level.

Although the labels are also post-it notes, albeit colored differently, be aware that @Holtzblatt2005 distinguishes between them and the yellow atomic affinity notes by using the term *labels* to describe the post-it notes at these three levels.

The general guidance for these labels is to write them in the first person, to reveal concrete detail, to use words that mean the same to everyone, to let the meaning emerge from the groups (instead of predefining), and to reorganize hard-to-label groups rather than continue wrestling with unsatisfying label wording.

As I mentioned above, the bottom level of labels is begun (step 2) when the people can no longer keep track of the groups of affinity notes without any labels. The labels at the bottom level should have design relevance and highlight distinctions rather than bringing groups together.

The next step (step 3) is to build a temporary top level, largely because this will help you move the affinity notes around into positions closer to their final positions. There should be only half a dozen or so of these temporary top level labels. Once everything has been moved around then remove the temporary top level (step 4).

The next step (step 5) is to build the middle level of labels. These labels should highlight high level work concepts, such as steps in work, communication strategies in work, tool use, and organizational structure.

The final step (step 6) of the affinity diagram is to add the top level, the level that describes the key issues. These key issues will inform the behavior patterns that will be the basis for the next milestone. Any break in the chain from interviews to these key issues jeopardizes the next milestone and, ultimately the entire project.

Keep in mind that these affinity labels are written in the first person and represent things an archetypal user might say. They certainly don't need to be things actually said in an interview but they do need to be things someone might say. That way, they can be a concrete basis for a persona. See Figure \ref{fiAffinityExample.png} for a fragment of an excellent set of affinity labels.

\pic[height=4.5in,width=4.25in]{fiAffinityExample.png}{Part of an excellent set of affinity labels}

### Affinity diagram details

One thing that I would like to add is that you can probably get a lot more done by using a paper process than by using an online tool.  It's harder to document a paper process on a website, though.  My best suggestion is that you get four Elmer's display boards, 36" $\times$ 48" \$3.60 in bulk, \$7.39 individually at an office supply store. You should be able to fit 150 3" $\times$ 3" post-it notes on each board. It will be even easier if you have neat handwriting and use smaller post-it notes.

Use these boards and post-it notes and just bring the results to class to present. One previous semester, the most productive groups found it difficult to fit everything onto one of these boards. Less productive groups found it quite easy and even had space left over.  If you find that you have sparsely populated one of these 36" $\times$ 48" boards, you probably haven't dug deeply enough.  On the other hand, adding more post-it notes until the thing is covered may only mask the problem of not digging deeply enough, rather than solve it.  One previous group made the unwise decision to omit pink and green labels altogether so they could concentrate on boosting the number of yellow post-it notes, having discovered that they could not reach the 500 minimum specified in @Holtzblatt2005.  (The above color scheme is clarified in detail in @Holtzblatt2005 --- basically the above means that they did no grouping of notes into themes at all).  As a result, they were unprepared to say anything analytical about what they had found, instead trapped at the individual anecdote level.

There is a lot of software for doing affinity diagrams, but the overhead is significant and it's harder for a group of people to interact with tools that are inherently meant for one person, one keyboard, one mouse.  If you have a bunch of post-it pads and are sitting around a posterboard display on a wall or a conference table, you can generate a lot more material faster.  By the way, you could just do stuff on a wall as @Holtzblatt2005 recommends, but then you have to figure out what to do with 500 -- 1,000 post-it notes afterward.  The display board gives you something you can fold up.  If you tie it tightly enough or cover the surface with fixative spray or tape or staples, you may find that post-its will retain their positioning.

### Miro
One final addition to this section is that I have actually had good luck with a software package called Miro, formerly known as Realtime Boards. This is web-based collaborative diagramming software that all members of the group can access at once from their own machines. I like it because of that and because it looks good on my thirty inch monitor when I'm grading assignments. Although I am generally against software for affinity diagramming, this is a wonderful exception to the rule. And it is free for students!
(N.B. After I wrote this, Figma was updated to include much of the functionality of Miro, so feel free to use it instead.)

## Milestone 3. personas

See @Pruitt2003.
Use @Cooper2014, chapter 3 to complete the persona milestone. The first author of that book, Alan Cooper co-originated the persona concept, so you should regard that as basic required HCI reading anyway.

The persona process involves fewer steps than does the contextual inquiry, so I won't give an overview here. Let me just remind you that each persona's behavior patterns are selected because of the key issues at the top of the affinity diagram. @Cooper2014 describes various ways to research the persona but the way you have done it in this project is through the contextual inquiry.

You must generate a primary persona. These are the focus of your prototype and any scenarios that the prototype will satisfy. You should also develop at least two secondary personas, especially if your contextual inquiry has led you to a complicated picture of goals and means. 

Finally, you may benefit from inclusion of one or more anti-personas. These personas define behavior patterns you have explicitly determined to be out-of-scope for your project. I mention this because *overly broad scope* is one of the most severe afflictions to beset student projects. You should welcome anti-personas as a tool you can use to eject aspects of the project that will dilute your focus, sap your energy, and make your direction waver.

Personas sometimes benefit from *dashboard* displays, displays that were once fashionable in data analytics for their resemblance to instrumention of cars or planes. The point of the resemblance is what matters. Dashboards are meant to be instantly readable. It may be easy to create meters along several behavioral axes showing, at a glance, the difference between personas. This is optional but it has clearly helped some groups.

## Milestone 4. lo-fi prototype
You can use @Holtzblatt2005, chapter 13, to
complete this milestone.
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
and make better designs because of having rethought
them.

The lo-fi prototype should show the basic layout of screens but not typography and colors. There should be some indication of the flow of the application, at least a diagram showing the flow from one screen to another. An alternative approach is to put all your screens on a canvas using Miro, an online collaborative drawing tool. Then you can draw arrows from one screen to another. You may be able to do the same using Figma or other software. If you make the prototype using paper or cardstock, you can make a cardboard "window" to place over the active screen, hiding any callouts or arrows or headings around the screen and focusing a participant's attention on just that screen. In this case you might make the prototype on a 24" $\times$ 36" foldable posterboard with attached index cards for the individual screens. Then you could lay the posterboard on a large conference table for an interactive evaluation with a live participant.

## Milestone 5. hi-fi prototype
The outcome of this milestone should be something viable
for user testing.  You should not have to modify this
so you can use it for testing.  Therefore, the
definition of hi-fi may be relaxed.  This may well be a
mid-fi prototype.  The goal is to prepare something you
can use to gain relevant knowledge about the design from
users.

You need to show the flow of your application rather than just showing individual screens. You may achieve this with a narrated video or other means you negotiate with the instructor.

The video of your hifi prototype should be a walkthrough of your site or app. It should show the paths that a user takes through the application or site. There should be some narration of the tasks that the user is thinking of while the user achieves their goals using the prototype. It should be clear throughout what the user is doing and why they are doing it. You should state the purpose of the app or site at the beginning, along with the name of the project. This should be followed by each task or path in turn. At the end, there should be some indication that we've reached the end, rather than leaving us to wonder if some of the video was cut off.

## Final project presentation
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

No slideshow is needed for this presentation but you should add a short page to your website telling what you've done to test your prototype.

For the online version of the course, the in-person presentation may not be possible. Therefore you must do one of two things. Either report on user testing via an appointment with the instructor in the instructor's office or via a Bluejeans / Zoom teleconference.

The final presentation is not graded but you can not receive a grade for the course if you do not complete it. It is your responsibility to schedule it with the instructor in the online version of the course.

## Milestone critiques

Someone in a group working on a shopping cart device asked whether they should change direction or scale back because I said that I thought it would be too expensive to put a device in each shopping cart. Here's what I said in reply.

I would like you to think about this in a different way. Instead of trying to decide what to do based on what I have said, try to find evidence that supports or refutes what I have
 said.

There is a major grocery store chain headquartered near here, Wegman's. They donate a lot of IT equipment to RIT so I know they are friendly to RIT. When I visit there, I often see the employees themselves shopping for groceries. I'll bet you could interview them to find out about the needs of shoppers that might be helped by having a device on the grocery cart or perhaps an app that might help.

I'll try to say more later but for now let me just add that the needs of the shoppers as perceived by the employees may differ from the needs of the shoppers as perceived by the shoppers and ALSO from the needs of the shoppers as EXPERIENCED by the shoppers. In other words, even the shoppers themselves may perceive differently from their experience.

A famous quote from Henry Ford, explaining why he did not listen to his customers was that, if he had, they would have just told him to invent a better horse and buggy.


## Project management
Many teachers agree that no project management skills are required to work on a project with a group of four or fewer people. This is a major reason teachers who are not teaching project management advocate groups of four or fewer for class projects. Nevertheless, many students are unaware of or don't believe this claim, and ask about project management. There are two things I can share about project management without diverting much attention from our purpose. One is the individual interactions between team members. I will discuss that later. For now, I would like to make a few remarks about the practice of project management in the IT workplace.

The Project Management Institute (PMI) has become the
most popular focal
point worldwide for best practices in project management. For
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

An alternative to thinking with a project management focus is to think with a *devops* focus. *Devops* is a contraction of development and operations and is popular in organizations whose primary product is software. Thinking from a *devops* perspective is often seen as contradictory to project management thinking because *devops* preaches continuous improvement of processes rather than seeing the delivery of software as primarily the product of a lifecycle. While an organization practicing *devops* will typically have projects and project managers, they are not the primary concern. The primary concerns are
(1) the flow of work from development to operations to customers,
(2) the flow of feedback from customers to operations to developers, and
(3) a culture that fosters innovation, trust, and continuous improvement. Additionally, *devops* is concerned with reducing work in process and unplanned work. You can read more about *devops* in books with either *devops* in the title or titled with the related term *release engineering*.

