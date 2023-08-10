rerun    = "Rerun to get cross-references right"
basename = book
latex    = lualatex
option   = -jobname $(basename) '\input{preamble-basic.tex}'

all : $(basename).tex
	perl -i -pe 's/\\section\{/\\mysection{/' $(basename).tex
	perl -i -pe 's/\\subsection\{/\\mysubsection{/' $(basename).tex
	$(latex) $(option) || true
	grep -q $(rerun) $(basename).log \
	     && $(latex) $(option) \
	     || true

$(basename).tex : $(basename)-content.md
	pandoc                           \
	  -t latex                       \
	  --filter pandoc-include        \
		--citeproc                     \
	  --bibliography $(basename).bib \
	  --template pandocNotes         \
	     $(basename)-content.md      \
	  -o $(basename).tex

$(basename)-content.md : 0*.md 1*.md
	cat                           \
	  00intro-content.md          \
	  01bkgrndRad-content.md      \
	  02audience-content.md       \
	  03contextInquiry-content.md \
	  04proto-content.md          \
	  05personalinfo-content.md   \
	  06infoStruct-content.md     \
	  07findingInfo-content.md    \
	  08visInfo-content.md        \
	  09milestones-content.md     \
	  10exercises-content.md      \
	  11references-content.md     \
	  > $(basename)-content.md

clean :
	rm $(basename)-content.md *.log *.aux *.out *~ *-tmp1.tex *-tmp2.tex *-content.tex
