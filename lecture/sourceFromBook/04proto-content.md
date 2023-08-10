
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

\begin{figure}
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
  \caption{the iterative development cycle}
  \end{center}
\end{figure}

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

## Evaluation in iterative development

\noindent \llap{``}I had a guaranteed military sale with ED 209 - renovation program, spare parts for twenty-five years ... Who cares if it worked or not?''

\hfill--Dick Jones, character in *Robocop* (1987)

Evaluation is very important but we are skipping it in this class except for a casual mention of heuristic evaluation and a brief discussion of data analysis in user studies. Evaluation is well covered in the HCI curriculum. This course focuses on the design phase.
The only evaluation we will do is on-the-spot critiquing, which is a small part of evaluation.

## Another perspective on iteration

Paul Boyd, VP of User Experience at Oracle Global Health Systems, came to campus early in 2019 and described his approach to design thinking. It resembles, but is a little more sophisticated than the picture of iterative design above. Figure \ref{fiListening} shows the process. The process starts with listening and resembles the traditional design thinking process, which includes five stages: empathize, define, ideate, prototype, and test.

\begin{figure}
  \begin{center}
    \includegraphics{fiListening.png}
  \caption{The listening, ideate, build cycle}
  \label{fiListening}
  \end{center}
\end{figure}

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

Milestone 5 for this course is to construct a second prototype (in Milestone 4 you constructed a first prototype). For this prototype, please do *not* polish your Milestone 4 prototype. As a learning experience, consider completely throwing away your previous prototype. Do not expect to receive a lot of credit for polishing the previous prototype, no matter how good it was. As a learning experience, it is more important for you to do the things that lead to the prototype than refining the prototype itself.

## Design as an input to a prototype

Design can be thought of as a two part process. The first part is a divergent process, wherein you generate alternatives. The second part is a convergent process, wherein you make choices that reflect external constraints. A prototype can be construed as the implementation of those choices. Keep in mind that the implementation of a choice is not the same thing as the choice itself. The implementation is even more constrained by technology than is the choice in many cases.

You can think of a prototype as one possible concrete expression of your design, a design already filtered through alternative generation, choices reflecting constraints, and implementation.

## Alternative generation
To begin your design, you can make sketches, whether concrete sketches on paper or sketches in your mind's eye. At this stage, you should be comfortable with sketching and should be able to sketch design ideas in your sketchbooks. Those sketches will be evaluated when I collect your sketchbooks. You should blend pictures and words this time.
Be careful not to rely on words if you feel weak at sketching. On the other hand, do not avoid words when they illuminate details that may be intrinsically hard to sketch, such as timing.

The National Science Foundation recently observed that there are insufficient computer-based tools available for the alternative generation phase and established an initiative to research creativity. I mention this because the literature that resulted from this initiative, as well as my discussions with some of the participants, awoke me to the problem that quite a bit of design software enforces its own look and feel. For this reason, I suggest that you begin your divergent process using paper or other non-software-based means. You may have noticed in class when we looked at prototypes that some of the prototypes had a very distinctive look, often an appealing look. Some of this may be connected to the tools used. I would like you to introduce prototyping tools as late in the process as you can because they are convergent rather than divergent. Their bread and butter is to get you from idea to product, not to broaden the scope of your ideas.

If software won't help with alternative generation, what will? The most reliable tool we have is to meet as a group and to share ideas without censorship. When we critique ideas, the first thing that may come to mind may be objections. When we generate ideas, we need to self-censor objections. The only things we might say that look like objections are occasional requests for clarification. Imagine, though, that you only have a few such requests in your clarification bank. If you ask for clarification too often, you will slow alternative generation down to a crawl.

I personally love to use image googling during alternative generation. This practice has been criticized by some with whom I have shared it, so it may not be for you. For me, it jogs my memory and reminds me of what I have seen before. It is rare that I pursue a completely unfamiliar image that appears in this process. It is more likely that, comparing images, I notice what it is that connects them in my mind. Consider the example of image googling the word *clustering*. I conclude that the image most closely associated with clustering is an unattractive picture of a scatterplot of red, green, and blue dots. This is not a new image to me but image googling helped me discover it as an alternative in introducing the clustering concept.

One issue in alternative generation is that it is difficult to quickly clarify a particular alternative to your colleagues. Rapid sketching helps but there is surely an art form to knowing how far to go with presenting one alternative before moving on to another. While you generate alternatives, you have to be sensitive to your coworkers, not to their judgment of your ideas, but to their understanding of your ideas.

A second issue is timing. Most design students, given a three-step project, will spend more than half their time on step one, then panic and underdo steps two and three. It is important to budget time for alternative generation. If you establish a clock in advance, it may free you to keep generating alternatives until the signal to stop, rather than constantly monitoring for a *good enough alternative* to run with further. You need to keep diverging until the end of the time for diverging, not latch on to one idea.

## Choices reflecting constraints
Charles Eames once said that design is all about constraints. The way he said it avoided saying that it was about balancing constraints, or compromising over constraints, or choosing which constraints to honor. By saying that it is about constraints, I think he acknowledges that great design may transcend constraints. Even so, it is the transcendence of the constraints that matters. The constraints that were transcended may not be apparent to an individual observer. For example, I once criticized a Disaster Response Workers prototype as being too desktoppy. The response was that the client requested it. That is a constraint. I still feel my critique was valid and that it is too desktoppy. While acknowledging that I may be wrong about that, I hoped the team would figure out a way to meet my constraint that it not look too desktoppy, while meeting the client's constraint that that they focus on the desktop. Notice that they could ignore my constraint, compromise to show they acknowledged it, or do some third creative thing that makes me feel one way about the solution and makes the client feel a different way about the solution. It is a hallmark of much successful design that it admits differing, even conflicting interpretations, but that these varying interpretations all include a wish to adopt the design.

Choice expresses your talent. You could say that your talent is revealed by your choices. There are analytical choices that may be arrived at by accounting practices or statistical practices or diplomacy. Those can be learned procedurally. What you must work on yourself is your insight. You must hone something within you that transcends that which is easily learned as procedure.

This is not to devalue accounting, statistics, or diplomacy. The big picture is made up of countless small parts and each learnable skill has a role to play in piecing together the big picture. For instance, Napoleon was often credited with a diabolical ability to foresee the future, but explained this as an outgrowth of his accounting ability. He could, for instance, tell off the top of his head how many horseshoe nails his army would require between Vienna and Austerlitz. With his encyclopedic knowledge of the details of the army, he could easily predict the details of the armies of his enemies, and know what choices faced them.

Napoleon is an easy example of how someone can assemble details into a clearer picture than anyone else, but you might be surprised to know that this characteristic is ascribed to many famous military leaders. Grant, Jackson, Patton, and Rommel are all examples of generals purported to have some kind of sixth sense which, upon inspection, appears to have been fed by encyclopedic knowledge of details.

Although the above examples are military, the lesson is not by any means confined to the military. Because I grew up in a military family I was exposed to many accounts of military success. Since then, though, I have observed the same phenomenon in art, science, and business. Talent can be cultivated through learnable skills but in some people, a point of transcendence is reached that is at least somewhat mysterious. You may find it worthwhile to strive for this level of transcendence for its own sake. All I can do is to urge you to try and to assure you that someone is likely to recognize when you have achieved it.

## Implementation
Implementation is what we will see when you complete the final milestone. There will doubtless be some confusion as to what you have done because we will be seeing evidence of divergence and convergence, not those processes themselves. The main thing that implementation adds is craftsmanship.

## Craftsmanship
Craftsmanship in constructing your prototype should clarify the choices you have made. Unfortunately, clarification of your choices is not the goal of Balsamiq, or Axure, or IndiegoStudio. The goal of these tools is get you from idea to completion as effortlessly as possible and perhaps to add some sparkle to your idea.

To decrease effort, the easiest thing for a toolmaker to do is to make some of your choices for you. This may lead to confusion about your ideas since we may not know which choices you have made and which choices the toolmaker has made for you. It may also distract us from thinking about the choices and redirect our attention to the sparkle.

Sparkle is certainly nice but it does not translate into successful design. If you review Dieter Rams's list of the elements of successful design, you will find evidence that dazzling presentation of design is not important to design.

Think of your your prototype as a vehicle for your ideas and think about evaluating it on that basis.

## Social presence
Often prototypes benefit from social presence indicators. You may especially want to emphasize social presence indicators that work when very small numbers of people are using your prototype.

You must also consider the problem of manipulation of social presence indicators. Astroturfing is a common online problem. In an age when gold farming is profitable and Amazon's Mechanical Turk has been studied from many angles, there is plenty of reason for a casual observer to question social presence indicators.

## Form factor
Some prototypes may benefit from being useful on different devices. You may benefit from thinking about how you can make platform hopping transparent.

## Project focus
In one past case, I questioned whether the focus of a prototype for a language learning game was language learning or game development. These are both gargantuan topics in their own right, so it may help to rank your goals to decide what is most important about your project in case resources such as time become an important constraint.
