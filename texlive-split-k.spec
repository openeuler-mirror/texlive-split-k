%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-k
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1460:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harvard.tar.xz
Source1461:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harvard.doc.tar.xz
Source1463:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harvmac.tar.xz
Source1464:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harvmac.doc.tar.xz
Source1465:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/historische-zeitschrift.tar.xz
Source1466:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/historische-zeitschrift.doc.tar.xz
Source1570:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hook-pre-commit-pkg.doc.tar.xz
Source1709:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hatching.tar.xz
Source1710:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hatching.doc.tar.xz
Source1895:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hacm.tar.xz
Source1896:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hacm.doc.tar.xz
Source1897:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hands.tar.xz
Source1898:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/heuristica.tar.xz
Source1899:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/heuristica.doc.tar.xz
Source1900:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hfbright.tar.xz
Source1901:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hfbright.doc.tar.xz
Source1902:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hfoldsty.tar.xz
Source1903:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hfoldsty.doc.tar.xz
Source2131:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/helvetic.tar.xz
Source2220:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hanoi.tar.xz
Source2221:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/havannah.tar.xz
Source2222:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/havannah.doc.tar.xz
Source2224:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hexgame.tar.xz
Source2225:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hexgame.doc.tar.xz
Source2226:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/horoscop.tar.xz
Source2227:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/horoscop.doc.tar.xz
Source2618:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/happy4th.doc.tar.xz
Source2667:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hrlatex.tar.xz
Source2668:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hrlatex.doc.tar.xz
Source2760:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hausarbeit-jura.tar.xz
Source2761:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hausarbeit-jura.doc.tar.xz
Source3176:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harveyballs.tar.xz
Source3177:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harveyballs.doc.tar.xz
Source3178:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/here.tar.xz
Source3179:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/here.doc.tar.xz
Source3180:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hf-tikz.tar.xz
Source3181:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hf-tikz.doc.tar.xz
Source3183:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hobby.tar.xz
Source3184:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hobby.doc.tar.xz
Source3186:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hvfloat.tar.xz
Source3187:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hvfloat.doc.tar.xz
Source4231:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/handout.tar.xz
Source4232:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/handout.doc.tar.xz
Source4233:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hang.tar.xz
Source4234:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hang.doc.tar.xz
Source4235:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hanging.tar.xz
Source4236:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hanging.doc.tar.xz
Source4238:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hardwrap.tar.xz
Source4239:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hardwrap.doc.tar.xz
Source4241:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harnon-cv.tar.xz
Source4242:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harnon-cv.doc.tar.xz
Source4243:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harpoon.tar.xz
Source4244:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harpoon.doc.tar.xz
Source4245:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hc.tar.xz
Source4246:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hc.doc.tar.xz
Source4248:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/he-she.tar.xz
Source4249:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/he-she.doc.tar.xz
Source4250:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hhtensor.tar.xz
Source4251:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hhtensor.doc.tar.xz
Source4253:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/histogr.tar.xz
Source4254:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/histogr.doc.tar.xz
Source4256:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hitec.tar.xz
Source4257:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hitec.doc.tar.xz
Source4258:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hletter.tar.xz
Source4259:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hletter.doc.tar.xz
Source4260:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hpsdiss.tar.xz
Source4261:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hpsdiss.doc.tar.xz
Source4263:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hrefhide.tar.xz
Source4264:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hrefhide.doc.tar.xz
Source4266:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hvindex.tar.xz
Source4267:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hvindex.doc.tar.xz
Source6035:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harmony.tar.xz
Source6036:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/harmony.doc.tar.xz
Source6397:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/har2nat.tar.xz
Source6398:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/har2nat.doc.tar.xz
Source6399:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hobete.tar.xz
Source6400:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hobete.doc.tar.xz
Source6677:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hep.tar.xz
Source6678:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hep.doc.tar.xz
Source6679:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hepnames.tar.xz
Source6680:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hepnames.doc.tar.xz
Source6681:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hepparticles.tar.xz
Source6682:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hepparticles.doc.tar.xz
Source6683:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hepthesis.tar.xz
Source6684:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hepthesis.doc.tar.xz
Source6685:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hepunits.tar.xz
Source6686:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hepunits.doc.tar.xz
Source7371:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/h2020proposal.tar.xz
Source7372:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/h2020proposal.doc.tar.xz
Source7771:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/halloweenmath.tar.xz
Source7772:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/halloweenmath.doc.tar.xz
Source7773:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hackthefootline.tar.xz
Source7774:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hackthefootline.doc.tar.xz
Source7775:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hecthese.tar.xz
Source7776:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hecthese.doc.tar.xz
Source7777:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hithesis.tar.xz
Source7778:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hithesis.doc.tar.xz
Source7779:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hustthesis.tar.xz
Source7780:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hustthesis.doc.tar.xz
Source8038:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hlist.doc.tar.xz 
Source8039:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hlist.tar.xz
Source8168:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hagenberg-thesis.tar.xz
Source8169:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hagenberg-thesis.doc.tar.xz
Source8170:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/handin.tar.xz
Source8171:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/handin.doc.tar.xz
Source8172:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hulipsum.tar.xz
Source8173:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/hulipsum.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-harvard
Provides:       tex-harvard = %{tl_version}
License:        LPPL
Summary:        Harvard citation package for use with LaTeX 2e
Version:        svn15878.2.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(harvard.sty) = %{tl_version}

%description -n texlive-harvard
This is a re-implementation, for LaTeX 2e, of the original
Harvard package. The bundle contains the LaTeX package, several
BibTeX styles, and a 'Perl package' for use with LaTeX2HTML.
Harvard is an author-year citation style (all but the first
author are suppressed in second and subsequent citations of the
same entry); the package defines several variant styles:
apsr.bst for the American Political Science Review; agsm.bst
for Australian Government publications; dcu.bst from the Design
Computing Unit of the University of Sydney; kluwer.bstwhich
aims at the format preferred in Kluwer publications;
nederlands.bst which deals with sorting Dutch names with
prefixes (such as van) according to Dutch rules, together with
several styles whose authors offer no description of their
behaviour.

%package -n texlive-harvard-doc
Summary:        Documentation for harvard
Version:        svn15878.2.0.5

Provides:       tex-harvard-doc
AutoReqProv:    No

%description -n texlive-harvard-doc
Documentation for harvard

%package -n texlive-harvmac
Provides:       tex-harvmac = %{tl_version}
License:        CC-BY
Summary:        Macros for scientific articles
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(harvmac.tex) = %{tl_version}

%description -n texlive-harvmac
Known as 'Harvard macros', since written at that University.

%package -n texlive-harvmac-doc
Summary:        Documentation for harvmac
Version:        svn15878.0

Provides:       tex-harvmac-doc
AutoReqProv:    No

%description -n texlive-harvmac-doc
Documentation for harvmac

%package -n texlive-historische-zeitschrift
Provides:       tex-historische-zeitschrift = %{tl_version}
License:        LPPL
Summary:        Biblatex style for the journal 'Historische Zeitschrift'
Version:        svn42635
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(historische-zeitschrift.bbx) = %{tl_version}
Provides:       tex(historische-zeitschrift.cbx) = %{tl_version}

%description -n texlive-historische-zeitschrift
The package provides citations according with the house style
of the 'Historische Zeitschrift', a German historical journal.
The scheme is a fullcite for the first citation and 'Author,
Shorttitle (as note N, P)' for later citations (P being the
page number). For further details, see the description of the
house style at the journal's site. The package depends on
biblatex (version 0.8 or higher) as well as etoolbox (version
1.5 or higher).

%package -n texlive-historische-zeitschrift-doc
Summary:        Documentation for historische-zeitschrift
Version:        svn42635
Provides:       tex-historische-zeitschrift-doc
AutoReqProv:    No

%description -n texlive-historische-zeitschrift-doc
Documentation for historische-zeitschrift

%package -n texlive-hatching
Provides:       tex-hatching = %{tl_version}
License:        Public Domain
Summary:        MetaPost macros for hatching interior of closed paths
Version:        svn23818.0.11

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-hatching
The file hatching.mp contains a set of MetaPost macros for
hatching interior of closed paths. Examples of usage are
included.

%package -n texlive-hatching-doc
Summary:        Documentation for hatching
Version:        svn23818.0.11

Provides:       tex-hatching-doc
AutoReqProv:    No

%description -n texlive-hatching-doc
Documentation for hatching

%package -n texlive-hacm
Provides:       tex-hacm = %{tl_version}
License:        LPPL 1.3
Summary:        Font support for the Arka language
Version:        svn27671.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(hacm.map) = %{tl_version}, tex(alblant.tfm) = %{tl_version}
Provides:       tex(defans.tfm) = %{tl_version}, tex(fenlil.tfm) = %{tl_version}
Provides:       tex(fialis.tfm) = %{tl_version}, tex(inje.tfm) = %{tl_version}
Provides:       tex(kardinal.tfm) = %{tl_version}, tex(lantia.tfm) = %{tl_version}
Provides:       tex(nalnia.tfm) = %{tl_version}, tex(olivia.tfm) = %{tl_version}
Provides:       tex(ralblant.tfm) = %{tl_version}, tex(rdefans.tfm) = %{tl_version}
Provides:       tex(rfenlil.tfm) = %{tl_version}, tex(rfialis.tfm) = %{tl_version}
Provides:       tex(rinje.tfm) = %{tl_version}, tex(rkardinal.tfm) = %{tl_version}
Provides:       tex(rlantia.tfm) = %{tl_version}, tex(rnalnia.tfm) = %{tl_version}
Provides:       tex(rolivia.tfm) = %{tl_version}, tex(alblant.pfb) = %{tl_version}
Provides:       tex(defans.pfb) = %{tl_version}, tex(fenlil.pfb) = %{tl_version}
Provides:       tex(fialis.pfb) = %{tl_version}, tex(inje.pfb) = %{tl_version}
Provides:       tex(kardinal.pfb) = %{tl_version}, tex(lantia.pfb) = %{tl_version}
Provides:       tex(nalnia.pfb) = %{tl_version}, tex(olivia.pfb) = %{tl_version}
Provides:       tex(alblant.vf) = %{tl_version}, tex(defans.vf) = %{tl_version}
Provides:       tex(fenlil.vf) = %{tl_version}, tex(fialis.vf) = %{tl_version}
Provides:       tex(inje.vf) = %{tl_version}, tex(kardinal.vf) = %{tl_version}
Provides:       tex(lantia.vf) = %{tl_version}, tex(nalnia.vf) = %{tl_version}
Provides:       tex(olivia.vf) = %{tl_version}, tex(hacm.sty) = %{tl_version}
Provides:       tex(ot1halb.fd) = %{tl_version}, tex(ot1hdef.fd) = %{tl_version}
Provides:       tex(ot1hfen.fd) = %{tl_version}, tex(ot1hfia.fd) = %{tl_version}
Provides:       tex(ot1hinj.fd) = %{tl_version}, tex(ot1hkar.fd) = %{tl_version}
Provides:       tex(ot1hlan.fd) = %{tl_version}

%description -n texlive-hacm
The package supports typesetting hacm, the alphabet of the
constructed language Arka. The bundle provides nine official
fonts, in Adobe Type 1 format.

%package -n texlive-hacm-doc
Summary:        Documentation for hacm
Version:        svn27671.0.1

Provides:       tex-hacm-doc
AutoReqProv:    No

%description -n texlive-hacm-doc
Documentation for hacm

%package -n texlive-hands
Provides:       tex-hands = %{tl_version}
License:        Public Domain
Summary:        Pointing hand font
Version:        svn13293.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(hands.tfm) = %{tl_version}

%description -n texlive-hands
Provides right- and left-pointing hands in both black-on-white
and white-on-black realisation. The font is distributed as
Metafont source.

%package -n texlive-heuristica
Provides:       tex-heuristica = %{tl_version}
License:        OFL
Summary:        Fonts extending Utopia, with LaTeX support files
Version:        svn43507
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(fontenc.sty)
Requires:       tex(textcomp.sty), tex(mweights.sty), tex(etoolbox.sty), tex(fontaxes.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(zut_5b7xz5.enc) = %{tl_version}, tex(zut_bavnqe.enc) = %{tl_version}
Provides:       tex(zut_ckaykl.enc) = %{tl_version}, tex(zut_cq6rqq.enc) = %{tl_version}
Provides:       tex(zut_cvig5d.enc) = %{tl_version}, tex(zut_d3dvo4.enc) = %{tl_version}
Provides:       tex(zut_dcwkkw.enc) = %{tl_version}, tex(zut_dhvb6d.enc) = %{tl_version}
Provides:       tex(zut_dvh2xl.enc) = %{tl_version}, tex(zut_e7tlds.enc) = %{tl_version}
Provides:       tex(zut_edf5gu.enc) = %{tl_version}, tex(zut_etrbro.enc) = %{tl_version}
Provides:       tex(zut_evgarn.enc) = %{tl_version}, tex(zut_f5n2rf.enc) = %{tl_version}
Provides:       tex(zut_fc3mov.enc) = %{tl_version}, tex(zut_flhghs.enc) = %{tl_version}
Provides:       tex(zut_g4w54e.enc) = %{tl_version}, tex(zut_geqeyh.enc) = %{tl_version}
Provides:       tex(zut_hbxdik.enc) = %{tl_version}, tex(zut_hln2hy.enc) = %{tl_version}
Provides:       tex(zut_hvy566.enc) = %{tl_version}, tex(zut_ijw3px.enc) = %{tl_version}
Provides:       tex(zut_it5nv3.enc) = %{tl_version}, tex(zut_j3hjx2.enc) = %{tl_version}
Provides:       tex(zut_k42udk.enc) = %{tl_version}, tex(zut_n2gc2n.enc) = %{tl_version}
Provides:       tex(zut_nvi5ys.enc) = %{tl_version}, tex(zut_qy67bk.enc) = %{tl_version}
Provides:       tex(zut_rhmrtx.enc) = %{tl_version}, tex(zut_rutxxy.enc) = %{tl_version}
Provides:       tex(zut_tfeu3y.enc) = %{tl_version}, tex(zut_thxlbm.enc) = %{tl_version}
Provides:       tex(zut_tsvs4d.enc) = %{tl_version}, tex(zut_u7pc6m.enc) = %{tl_version}
Provides:       tex(zut_ul3ofd.enc) = %{tl_version}, tex(zut_v7it2w.enc) = %{tl_version}
Provides:       tex(zut_vaioc2.enc) = %{tl_version}, tex(zut_vtjod4.enc) = %{tl_version}
Provides:       tex(zut_ysltpx.enc) = %{tl_version}, tex(zut_zk7stm.enc) = %{tl_version}
Provides:       tex(zut_zl5g24.enc) = %{tl_version}, tex(Heuristica.map) = %{tl_version}
Provides:       tex(Heuristica-Bold.otf) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic.otf) = %{tl_version}
Provides:       tex(Heuristica-Italic.otf) = %{tl_version}
Provides:       tex(Heuristica-Regular.otf) = %{tl_version}
Provides:       tex(Heuristica-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-inf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-inf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-inf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-sup-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-sup-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tosf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tosf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-inf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-inf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-inf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-sup-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-sup-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tosf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tosf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-inf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-inf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-inf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-sup-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-sup-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tosf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tosf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-inf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-inf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-inf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-sup-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-sup-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-t2b.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-t2c.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Heuristica-Bold.pfb) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Heuristica-Italic.pfb) = %{tl_version}
Provides:       tex(Heuristica-Regular.pfb) = %{tl_version}
Provides:       tex(Heuristica-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Heuristica-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Heuristica-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Heuristica-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Heuristica-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(Heuristica-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Heuristica-Inf.fd) = %{tl_version}
Provides:       tex(LY1Heuristica-Sup.fd) = %{tl_version}
Provides:       tex(LY1Heuristica-TLF.fd) = %{tl_version}
Provides:       tex(LY1Heuristica-TOsF.fd) = %{tl_version}
Provides:       tex(T1Heuristica-Inf.fd) = %{tl_version}
Provides:       tex(T1Heuristica-Sup.fd) = %{tl_version}
Provides:       tex(T1Heuristica-TLF.fd) = %{tl_version}
Provides:       tex(T1Heuristica-TOsF.fd) = %{tl_version}
Provides:       tex(T2AHeuristica-Inf.fd) = %{tl_version}
Provides:       tex(T2AHeuristica-Sup.fd) = %{tl_version}
Provides:       tex(T2AHeuristica-TLF.fd) = %{tl_version}
Provides:       tex(T2AHeuristica-TOsF.fd) = %{tl_version}
Provides:       tex(T2BHeuristica-Inf.fd) = %{tl_version}
Provides:       tex(T2BHeuristica-Sup.fd) = %{tl_version}
Provides:       tex(T2BHeuristica-TLF.fd) = %{tl_version}
Provides:       tex(T2BHeuristica-TOsF.fd) = %{tl_version}
Provides:       tex(T2CHeuristica-Inf.fd) = %{tl_version}
Provides:       tex(T2CHeuristica-Sup.fd) = %{tl_version}
Provides:       tex(T2CHeuristica-TLF.fd) = %{tl_version}
Provides:       tex(T2CHeuristica-TOsF.fd) = %{tl_version}
Provides:       tex(TS1Heuristica-TLF.fd) = %{tl_version}
Provides:       tex(TS1Heuristica-TOsF.fd) = %{tl_version}
Provides:       tex(heuristica.sty) = %{tl_version}

%description -n texlive-heuristica
The fonts extend the utopia set with Cyrillic glyphs,
additional figure styles, ligatures and Small Caps in Regular
style only. Macro support, and maths fonts that match the
Utopia family, are provided by the Fourier and the Mathdesign
font packages.

%package -n texlive-heuristica-doc
Summary:        Documentation for heuristica
Version:        svn43507
Provides:       tex-heuristica-doc
AutoReqProv:    No

%description -n texlive-heuristica-doc
Documentation for heuristica

%package -n texlive-hfbright
Provides:       tex-hfbright = %{tl_version}
License:        LPPL
Summary:        The hfbright fonts
Version:        svn29349.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(hfmital.enc) = %{tl_version}, tex(hfmsa.enc) = %{tl_version}
Provides:       tex(hfmsb.enc) = %{tl_version}, tex(hfmsym.enc) = %{tl_version}
Provides:       tex(hfot1.enc) = %{tl_version}, tex(hfbright.map) = %{tl_version}
Provides:       tex(hfbr10.pfb) = %{tl_version}, tex(hfbr17.pfb) = %{tl_version}
Provides:       tex(hfbr8.pfb) = %{tl_version}, tex(hfbr9.pfb) = %{tl_version}
Provides:       tex(hfbras10.pfb) = %{tl_version}, tex(hfbras8.pfb) = %{tl_version}
Provides:       tex(hfbras9.pfb) = %{tl_version}, tex(hfbrbs10.pfb) = %{tl_version}
Provides:       tex(hfbrbs8.pfb) = %{tl_version}, tex(hfbrbs9.pfb) = %{tl_version}
Provides:       tex(hfbrbx10.pfb) = %{tl_version}, tex(hfbrmb10.pfb) = %{tl_version}
Provides:       tex(hfbrmi10.pfb) = %{tl_version}, tex(hfbrmi8.pfb) = %{tl_version}
Provides:       tex(hfbrmi9.pfb) = %{tl_version}, tex(hfbrsl10.pfb) = %{tl_version}
Provides:       tex(hfbrsl17.pfb) = %{tl_version}, tex(hfbrsl8.pfb) = %{tl_version}
Provides:       tex(hfbrsl9.pfb) = %{tl_version}, tex(hfbrsy10.pfb) = %{tl_version}
Provides:       tex(hfbrsy8.pfb) = %{tl_version}, tex(hfbrsy9.pfb) = %{tl_version}
Provides:       tex(hfsltl10.pfb) = %{tl_version}, tex(hftl10.pfb) = %{tl_version}

%description -n texlive-hfbright
These are Adobe Type 1 versions of the OT1-encoded and maths
parts of the Computer Modern Bright fonts.

%package -n texlive-hfbright-doc
Summary:        Documentation for hfbright
Version:        svn29349.0

Provides:       tex-hfbright-doc
AutoReqProv:    No

%description -n texlive-hfbright-doc
Documentation for hfbright

%package -n texlive-hfoldsty
Provides:       tex-hfoldsty = %{tl_version}
License:        GPL+
Summary:        Old style numerals with EC fonts
Version:        svn29349.1.15

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontenc.sty), tex(fix-cm.sty), tex(ifthen.sty)
Provides:       tex(hfobi0500.tfm) = %{tl_version}, tex(hfobi0600.tfm) = %{tl_version}
Provides:       tex(hfobi0700.tfm) = %{tl_version}, tex(hfobi0800.tfm) = %{tl_version}
Provides:       tex(hfobi0900.tfm) = %{tl_version}, tex(hfobi1000.tfm) = %{tl_version}
Provides:       tex(hfobi1095.tfm) = %{tl_version}, tex(hfobi1200.tfm) = %{tl_version}
Provides:       tex(hfobi1440.tfm) = %{tl_version}, tex(hfobi1728.tfm) = %{tl_version}
Provides:       tex(hfobi2074.tfm) = %{tl_version}, tex(hfobi2488.tfm) = %{tl_version}
Provides:       tex(hfobi2986.tfm) = %{tl_version}, tex(hfobi3583.tfm) = %{tl_version}
Provides:       tex(hfobl0500.tfm) = %{tl_version}, tex(hfobl0600.tfm) = %{tl_version}
Provides:       tex(hfobl0700.tfm) = %{tl_version}, tex(hfobl0800.tfm) = %{tl_version}
Provides:       tex(hfobl0900.tfm) = %{tl_version}, tex(hfobl1000.tfm) = %{tl_version}
Provides:       tex(hfobl1095.tfm) = %{tl_version}, tex(hfobl1200.tfm) = %{tl_version}
Provides:       tex(hfobl1440.tfm) = %{tl_version}, tex(hfobl1728.tfm) = %{tl_version}
Provides:       tex(hfobl2074.tfm) = %{tl_version}, tex(hfobl2488.tfm) = %{tl_version}
Provides:       tex(hfobl2986.tfm) = %{tl_version}, tex(hfobl3583.tfm) = %{tl_version}
Provides:       tex(hfobx0500.tfm) = %{tl_version}, tex(hfobx0600.tfm) = %{tl_version}
Provides:       tex(hfobx0700.tfm) = %{tl_version}, tex(hfobx0800.tfm) = %{tl_version}
Provides:       tex(hfobx0900.tfm) = %{tl_version}, tex(hfobx1000.tfm) = %{tl_version}
Provides:       tex(hfobx1095.tfm) = %{tl_version}, tex(hfobx1200.tfm) = %{tl_version}
Provides:       tex(hfobx1440.tfm) = %{tl_version}, tex(hfobx1728.tfm) = %{tl_version}
Provides:       tex(hfobx2074.tfm) = %{tl_version}, tex(hfobx2488.tfm) = %{tl_version}
Provides:       tex(hfobx2986.tfm) = %{tl_version}, tex(hfobx3583.tfm) = %{tl_version}
Provides:       tex(hfocc0500.tfm) = %{tl_version}, tex(hfocc0600.tfm) = %{tl_version}
Provides:       tex(hfocc0700.tfm) = %{tl_version}, tex(hfocc0800.tfm) = %{tl_version}
Provides:       tex(hfocc0900.tfm) = %{tl_version}, tex(hfocc1000.tfm) = %{tl_version}
Provides:       tex(hfocc1095.tfm) = %{tl_version}, tex(hfocc1200.tfm) = %{tl_version}
Provides:       tex(hfocc1440.tfm) = %{tl_version}, tex(hfocc1728.tfm) = %{tl_version}
Provides:       tex(hfocc2074.tfm) = %{tl_version}, tex(hfocc2488.tfm) = %{tl_version}
Provides:       tex(hfocc2986.tfm) = %{tl_version}, tex(hfocc3583.tfm) = %{tl_version}
Provides:       tex(hfodh0500.tfm) = %{tl_version}, tex(hfodh0600.tfm) = %{tl_version}
Provides:       tex(hfodh0700.tfm) = %{tl_version}, tex(hfodh0800.tfm) = %{tl_version}
Provides:       tex(hfodh0900.tfm) = %{tl_version}, tex(hfodh1000.tfm) = %{tl_version}
Provides:       tex(hfodh1095.tfm) = %{tl_version}, tex(hfodh1200.tfm) = %{tl_version}
Provides:       tex(hfodh1440.tfm) = %{tl_version}, tex(hfodh1728.tfm) = %{tl_version}
Provides:       tex(hfodh2074.tfm) = %{tl_version}, tex(hfodh2488.tfm) = %{tl_version}
Provides:       tex(hfodh2986.tfm) = %{tl_version}, tex(hfodh3583.tfm) = %{tl_version}
Provides:       tex(hfoit0600.tfm) = %{tl_version}, tex(hfoit0700.tfm) = %{tl_version}
Provides:       tex(hfoit0800.tfm) = %{tl_version}, tex(hfoit0900.tfm) = %{tl_version}
Provides:       tex(hfoit1000.tfm) = %{tl_version}, tex(hfoit1095.tfm) = %{tl_version}
Provides:       tex(hfoit1200.tfm) = %{tl_version}, tex(hfoit1440.tfm) = %{tl_version}
Provides:       tex(hfoit1728.tfm) = %{tl_version}, tex(hfoit2074.tfm) = %{tl_version}
Provides:       tex(hfoit2488.tfm) = %{tl_version}, tex(hfoit2986.tfm) = %{tl_version}
Provides:       tex(hfoit3583.tfm) = %{tl_version}, tex(hfooc0500.tfm) = %{tl_version}
Provides:       tex(hfooc0600.tfm) = %{tl_version}, tex(hfooc0700.tfm) = %{tl_version}
Provides:       tex(hfooc0800.tfm) = %{tl_version}, tex(hfooc0900.tfm) = %{tl_version}
Provides:       tex(hfooc1000.tfm) = %{tl_version}, tex(hfooc1095.tfm) = %{tl_version}
Provides:       tex(hfooc1200.tfm) = %{tl_version}, tex(hfooc1440.tfm) = %{tl_version}
Provides:       tex(hfooc1728.tfm) = %{tl_version}, tex(hfooc2074.tfm) = %{tl_version}
Provides:       tex(hfooc2488.tfm) = %{tl_version}, tex(hfooc2986.tfm) = %{tl_version}
Provides:       tex(hfooc3583.tfm) = %{tl_version}, tex(hforb0500.tfm) = %{tl_version}
Provides:       tex(hforb0600.tfm) = %{tl_version}, tex(hforb0700.tfm) = %{tl_version}
Provides:       tex(hforb0800.tfm) = %{tl_version}, tex(hforb0900.tfm) = %{tl_version}
Provides:       tex(hforb1000.tfm) = %{tl_version}, tex(hforb1095.tfm) = %{tl_version}
Provides:       tex(hforb1200.tfm) = %{tl_version}, tex(hforb1440.tfm) = %{tl_version}
Provides:       tex(hforb1728.tfm) = %{tl_version}, tex(hforb2074.tfm) = %{tl_version}
Provides:       tex(hforb2488.tfm) = %{tl_version}, tex(hforb2986.tfm) = %{tl_version}
Provides:       tex(hforb3583.tfm) = %{tl_version}, tex(hform0500.tfm) = %{tl_version}
Provides:       tex(hform0600.tfm) = %{tl_version}, tex(hform0700.tfm) = %{tl_version}
Provides:       tex(hform0800.tfm) = %{tl_version}, tex(hform0900.tfm) = %{tl_version}
Provides:       tex(hform1000.tfm) = %{tl_version}, tex(hform1095.tfm) = %{tl_version}
Provides:       tex(hform1200.tfm) = %{tl_version}, tex(hform1440.tfm) = %{tl_version}
Provides:       tex(hform1728.tfm) = %{tl_version}, tex(hform2074.tfm) = %{tl_version}
Provides:       tex(hform2488.tfm) = %{tl_version}, tex(hform2986.tfm) = %{tl_version}
Provides:       tex(hform3583.tfm) = %{tl_version}, tex(hfosc0500.tfm) = %{tl_version}
Provides:       tex(hfosc0600.tfm) = %{tl_version}, tex(hfosc0700.tfm) = %{tl_version}
Provides:       tex(hfosc0800.tfm) = %{tl_version}, tex(hfosc0900.tfm) = %{tl_version}
Provides:       tex(hfosc1000.tfm) = %{tl_version}, tex(hfosc1095.tfm) = %{tl_version}
Provides:       tex(hfosc1200.tfm) = %{tl_version}, tex(hfosc1440.tfm) = %{tl_version}
Provides:       tex(hfosc1728.tfm) = %{tl_version}, tex(hfosc2074.tfm) = %{tl_version}
Provides:       tex(hfosc2488.tfm) = %{tl_version}, tex(hfosc2986.tfm) = %{tl_version}
Provides:       tex(hfosc3583.tfm) = %{tl_version}, tex(hfosi0500.tfm) = %{tl_version}
Provides:       tex(hfosi0600.tfm) = %{tl_version}, tex(hfosi0700.tfm) = %{tl_version}
Provides:       tex(hfosi0800.tfm) = %{tl_version}, tex(hfosi0900.tfm) = %{tl_version}
Provides:       tex(hfosi1000.tfm) = %{tl_version}, tex(hfosi1095.tfm) = %{tl_version}
Provides:       tex(hfosi1200.tfm) = %{tl_version}, tex(hfosi1440.tfm) = %{tl_version}
Provides:       tex(hfosi1728.tfm) = %{tl_version}, tex(hfosi2074.tfm) = %{tl_version}
Provides:       tex(hfosi2488.tfm) = %{tl_version}, tex(hfosi2986.tfm) = %{tl_version}
Provides:       tex(hfosi3583.tfm) = %{tl_version}, tex(hfosl0500.tfm) = %{tl_version}
Provides:       tex(hfosl0600.tfm) = %{tl_version}, tex(hfosl0700.tfm) = %{tl_version}
Provides:       tex(hfosl0800.tfm) = %{tl_version}, tex(hfosl0900.tfm) = %{tl_version}
Provides:       tex(hfosl1000.tfm) = %{tl_version}, tex(hfosl1095.tfm) = %{tl_version}
Provides:       tex(hfosl1200.tfm) = %{tl_version}, tex(hfosl1440.tfm) = %{tl_version}
Provides:       tex(hfosl1728.tfm) = %{tl_version}, tex(hfosl2074.tfm) = %{tl_version}
Provides:       tex(hfosl2488.tfm) = %{tl_version}, tex(hfosl2986.tfm) = %{tl_version}
Provides:       tex(hfosl3583.tfm) = %{tl_version}, tex(hfoso0500.tfm) = %{tl_version}
Provides:       tex(hfoso0600.tfm) = %{tl_version}, tex(hfoso0700.tfm) = %{tl_version}
Provides:       tex(hfoso0800.tfm) = %{tl_version}, tex(hfoso0900.tfm) = %{tl_version}
Provides:       tex(hfoso1000.tfm) = %{tl_version}, tex(hfoso1095.tfm) = %{tl_version}
Provides:       tex(hfoso1200.tfm) = %{tl_version}, tex(hfoso1440.tfm) = %{tl_version}
Provides:       tex(hfoso1728.tfm) = %{tl_version}, tex(hfoso2074.tfm) = %{tl_version}
Provides:       tex(hfoso2488.tfm) = %{tl_version}, tex(hfoso2986.tfm) = %{tl_version}
Provides:       tex(hfoso3583.tfm) = %{tl_version}, tex(hfoss0500.tfm) = %{tl_version}
Provides:       tex(hfoss0600.tfm) = %{tl_version}, tex(hfoss0700.tfm) = %{tl_version}
Provides:       tex(hfoss0800.tfm) = %{tl_version}, tex(hfoss0900.tfm) = %{tl_version}
Provides:       tex(hfoss1000.tfm) = %{tl_version}, tex(hfoss1095.tfm) = %{tl_version}
Provides:       tex(hfoss1200.tfm) = %{tl_version}, tex(hfoss1440.tfm) = %{tl_version}
Provides:       tex(hfoss1728.tfm) = %{tl_version}, tex(hfoss2074.tfm) = %{tl_version}
Provides:       tex(hfoss2488.tfm) = %{tl_version}, tex(hfoss2986.tfm) = %{tl_version}
Provides:       tex(hfoss3583.tfm) = %{tl_version}, tex(hfost0600.tfm) = %{tl_version}
Provides:       tex(hfost0700.tfm) = %{tl_version}, tex(hfost0800.tfm) = %{tl_version}
Provides:       tex(hfost0900.tfm) = %{tl_version}, tex(hfost1000.tfm) = %{tl_version}
Provides:       tex(hfost1095.tfm) = %{tl_version}, tex(hfost1200.tfm) = %{tl_version}
Provides:       tex(hfost1440.tfm) = %{tl_version}, tex(hfost1728.tfm) = %{tl_version}
Provides:       tex(hfost2074.tfm) = %{tl_version}, tex(hfost2488.tfm) = %{tl_version}
Provides:       tex(hfost2986.tfm) = %{tl_version}, tex(hfost3583.tfm) = %{tl_version}
Provides:       tex(hfosx0500.tfm) = %{tl_version}, tex(hfosx0600.tfm) = %{tl_version}
Provides:       tex(hfosx0700.tfm) = %{tl_version}, tex(hfosx0800.tfm) = %{tl_version}
Provides:       tex(hfosx0900.tfm) = %{tl_version}, tex(hfosx1000.tfm) = %{tl_version}
Provides:       tex(hfosx1095.tfm) = %{tl_version}, tex(hfosx1200.tfm) = %{tl_version}
Provides:       tex(hfosx1440.tfm) = %{tl_version}, tex(hfosx1728.tfm) = %{tl_version}
Provides:       tex(hfosx2074.tfm) = %{tl_version}, tex(hfosx2488.tfm) = %{tl_version}
Provides:       tex(hfosx2986.tfm) = %{tl_version}, tex(hfosx3583.tfm) = %{tl_version}
Provides:       tex(hfotc0600.tfm) = %{tl_version}, tex(hfotc0700.tfm) = %{tl_version}
Provides:       tex(hfotc0800.tfm) = %{tl_version}, tex(hfotc0900.tfm) = %{tl_version}
Provides:       tex(hfotc1000.tfm) = %{tl_version}, tex(hfotc1095.tfm) = %{tl_version}
Provides:       tex(hfotc1200.tfm) = %{tl_version}, tex(hfotc1440.tfm) = %{tl_version}
Provides:       tex(hfotc1728.tfm) = %{tl_version}, tex(hfotc2074.tfm) = %{tl_version}
Provides:       tex(hfotc2488.tfm) = %{tl_version}, tex(hfotc2986.tfm) = %{tl_version}
Provides:       tex(hfotc3583.tfm) = %{tl_version}, tex(hfoti0500.tfm) = %{tl_version}
Provides:       tex(hfoti0600.tfm) = %{tl_version}, tex(hfoti0700.tfm) = %{tl_version}
Provides:       tex(hfoti0800.tfm) = %{tl_version}, tex(hfoti0900.tfm) = %{tl_version}
Provides:       tex(hfoti1000.tfm) = %{tl_version}, tex(hfoti1095.tfm) = %{tl_version}
Provides:       tex(hfoti1200.tfm) = %{tl_version}, tex(hfoti1440.tfm) = %{tl_version}
Provides:       tex(hfoti1728.tfm) = %{tl_version}, tex(hfoti2074.tfm) = %{tl_version}
Provides:       tex(hfoti2488.tfm) = %{tl_version}, tex(hfoti2986.tfm) = %{tl_version}
Provides:       tex(hfoti3583.tfm) = %{tl_version}, tex(hfott0600.tfm) = %{tl_version}
Provides:       tex(hfott0700.tfm) = %{tl_version}, tex(hfott0800.tfm) = %{tl_version}
Provides:       tex(hfott0900.tfm) = %{tl_version}, tex(hfott1000.tfm) = %{tl_version}
Provides:       tex(hfott1095.tfm) = %{tl_version}, tex(hfott1200.tfm) = %{tl_version}
Provides:       tex(hfott1440.tfm) = %{tl_version}, tex(hfott1728.tfm) = %{tl_version}
Provides:       tex(hfott2074.tfm) = %{tl_version}, tex(hfott2488.tfm) = %{tl_version}
Provides:       tex(hfott2986.tfm) = %{tl_version}, tex(hfott3583.tfm) = %{tl_version}
Provides:       tex(hfoui0500.tfm) = %{tl_version}, tex(hfoui0600.tfm) = %{tl_version}
Provides:       tex(hfoui0700.tfm) = %{tl_version}, tex(hfoui0800.tfm) = %{tl_version}
Provides:       tex(hfoui0900.tfm) = %{tl_version}, tex(hfoui1000.tfm) = %{tl_version}
Provides:       tex(hfoui1095.tfm) = %{tl_version}, tex(hfoui1200.tfm) = %{tl_version}
Provides:       tex(hfoui1440.tfm) = %{tl_version}, tex(hfoui1728.tfm) = %{tl_version}
Provides:       tex(hfoui2074.tfm) = %{tl_version}, tex(hfoui2488.tfm) = %{tl_version}
Provides:       tex(hfoui2986.tfm) = %{tl_version}, tex(hfoui3583.tfm) = %{tl_version}
Provides:       tex(hfovi0600.tfm) = %{tl_version}, tex(hfovi0700.tfm) = %{tl_version}
Provides:       tex(hfovi0800.tfm) = %{tl_version}, tex(hfovi0900.tfm) = %{tl_version}
Provides:       tex(hfovi1000.tfm) = %{tl_version}, tex(hfovi1095.tfm) = %{tl_version}
Provides:       tex(hfovi1200.tfm) = %{tl_version}, tex(hfovi1440.tfm) = %{tl_version}
Provides:       tex(hfovi1728.tfm) = %{tl_version}, tex(hfovi2074.tfm) = %{tl_version}
Provides:       tex(hfovi2488.tfm) = %{tl_version}, tex(hfovi2986.tfm) = %{tl_version}
Provides:       tex(hfovi3583.tfm) = %{tl_version}, tex(hfovt0600.tfm) = %{tl_version}
Provides:       tex(hfovt0700.tfm) = %{tl_version}, tex(hfovt0800.tfm) = %{tl_version}
Provides:       tex(hfovt0900.tfm) = %{tl_version}, tex(hfovt1000.tfm) = %{tl_version}
Provides:       tex(hfovt1095.tfm) = %{tl_version}, tex(hfovt1200.tfm) = %{tl_version}
Provides:       tex(hfovt1440.tfm) = %{tl_version}, tex(hfovt1728.tfm) = %{tl_version}
Provides:       tex(hfovt2074.tfm) = %{tl_version}, tex(hfovt2488.tfm) = %{tl_version}
Provides:       tex(hfovt2986.tfm) = %{tl_version}, tex(hfovt3583.tfm) = %{tl_version}
Provides:       tex(hfoxc0500.tfm) = %{tl_version}, tex(hfoxc0600.tfm) = %{tl_version}
Provides:       tex(hfoxc0700.tfm) = %{tl_version}, tex(hfoxc0800.tfm) = %{tl_version}
Provides:       tex(hfoxc0900.tfm) = %{tl_version}, tex(hfoxc1000.tfm) = %{tl_version}
Provides:       tex(hfoxc1095.tfm) = %{tl_version}, tex(hfoxc1200.tfm) = %{tl_version}
Provides:       tex(hfoxc1440.tfm) = %{tl_version}, tex(hfoxc1728.tfm) = %{tl_version}
Provides:       tex(hfoxc2074.tfm) = %{tl_version}, tex(hfoxc2488.tfm) = %{tl_version}
Provides:       tex(hfoxc2986.tfm) = %{tl_version}, tex(hfoxc3583.tfm) = %{tl_version}
Provides:       tex(hfobi0500.vf) = %{tl_version}, tex(hfobi0600.vf) = %{tl_version}
Provides:       tex(hfobi0700.vf) = %{tl_version}, tex(hfobi0800.vf) = %{tl_version}
Provides:       tex(hfobi0900.vf) = %{tl_version}, tex(hfobi1000.vf) = %{tl_version}
Provides:       tex(hfobi1095.vf) = %{tl_version}, tex(hfobi1200.vf) = %{tl_version}
Provides:       tex(hfobi1440.vf) = %{tl_version}, tex(hfobi1728.vf) = %{tl_version}
Provides:       tex(hfobi2074.vf) = %{tl_version}, tex(hfobi2488.vf) = %{tl_version}
Provides:       tex(hfobi2986.vf) = %{tl_version}, tex(hfobi3583.vf) = %{tl_version}
Provides:       tex(hfobl0500.vf) = %{tl_version}, tex(hfobl0600.vf) = %{tl_version}
Provides:       tex(hfobl0700.vf) = %{tl_version}, tex(hfobl0800.vf) = %{tl_version}
Provides:       tex(hfobl0900.vf) = %{tl_version}, tex(hfobl1000.vf) = %{tl_version}
Provides:       tex(hfobl1095.vf) = %{tl_version}, tex(hfobl1200.vf) = %{tl_version}
Provides:       tex(hfobl1440.vf) = %{tl_version}, tex(hfobl1728.vf) = %{tl_version}
Provides:       tex(hfobl2074.vf) = %{tl_version}, tex(hfobl2488.vf) = %{tl_version}
Provides:       tex(hfobl2986.vf) = %{tl_version}, tex(hfobl3583.vf) = %{tl_version}
Provides:       tex(hfobx0500.vf) = %{tl_version}, tex(hfobx0600.vf) = %{tl_version}
Provides:       tex(hfobx0700.vf) = %{tl_version}, tex(hfobx0800.vf) = %{tl_version}
Provides:       tex(hfobx0900.vf) = %{tl_version}, tex(hfobx1000.vf) = %{tl_version}
Provides:       tex(hfobx1095.vf) = %{tl_version}, tex(hfobx1200.vf) = %{tl_version}
Provides:       tex(hfobx1440.vf) = %{tl_version}, tex(hfobx1728.vf) = %{tl_version}
Provides:       tex(hfobx2074.vf) = %{tl_version}, tex(hfobx2488.vf) = %{tl_version}
Provides:       tex(hfobx2986.vf) = %{tl_version}, tex(hfobx3583.vf) = %{tl_version}
Provides:       tex(hfocc0500.vf) = %{tl_version}, tex(hfocc0600.vf) = %{tl_version}
Provides:       tex(hfocc0700.vf) = %{tl_version}, tex(hfocc0800.vf) = %{tl_version}
Provides:       tex(hfocc0900.vf) = %{tl_version}, tex(hfocc1000.vf) = %{tl_version}
Provides:       tex(hfocc1095.vf) = %{tl_version}, tex(hfocc1200.vf) = %{tl_version}
Provides:       tex(hfocc1440.vf) = %{tl_version}, tex(hfocc1728.vf) = %{tl_version}
Provides:       tex(hfocc2074.vf) = %{tl_version}, tex(hfocc2488.vf) = %{tl_version}
Provides:       tex(hfocc2986.vf) = %{tl_version}, tex(hfocc3583.vf) = %{tl_version}
Provides:       tex(hfodh0500.vf) = %{tl_version}, tex(hfodh0600.vf) = %{tl_version}
Provides:       tex(hfodh0700.vf) = %{tl_version}, tex(hfodh0800.vf) = %{tl_version}
Provides:       tex(hfodh0900.vf) = %{tl_version}, tex(hfodh1000.vf) = %{tl_version}
Provides:       tex(hfodh1095.vf) = %{tl_version}, tex(hfodh1200.vf) = %{tl_version}
Provides:       tex(hfodh1440.vf) = %{tl_version}, tex(hfodh1728.vf) = %{tl_version}
Provides:       tex(hfodh2074.vf) = %{tl_version}, tex(hfodh2488.vf) = %{tl_version}
Provides:       tex(hfodh2986.vf) = %{tl_version}, tex(hfodh3583.vf) = %{tl_version}
Provides:       tex(hfoit0600.vf) = %{tl_version}, tex(hfoit0700.vf) = %{tl_version}
Provides:       tex(hfoit0800.vf) = %{tl_version}, tex(hfoit0900.vf) = %{tl_version}
Provides:       tex(hfoit1000.vf) = %{tl_version}, tex(hfoit1095.vf) = %{tl_version}
Provides:       tex(hfoit1200.vf) = %{tl_version}, tex(hfoit1440.vf) = %{tl_version}
Provides:       tex(hfoit1728.vf) = %{tl_version}, tex(hfoit2074.vf) = %{tl_version}
Provides:       tex(hfoit2488.vf) = %{tl_version}, tex(hfoit2986.vf) = %{tl_version}
Provides:       tex(hfoit3583.vf) = %{tl_version}, tex(hfooc0500.vf) = %{tl_version}
Provides:       tex(hfooc0600.vf) = %{tl_version}, tex(hfooc0700.vf) = %{tl_version}
Provides:       tex(hfooc0800.vf) = %{tl_version}, tex(hfooc0900.vf) = %{tl_version}
Provides:       tex(hfooc1000.vf) = %{tl_version}, tex(hfooc1095.vf) = %{tl_version}
Provides:       tex(hfooc1200.vf) = %{tl_version}, tex(hfooc1440.vf) = %{tl_version}
Provides:       tex(hfooc1728.vf) = %{tl_version}, tex(hfooc2074.vf) = %{tl_version}
Provides:       tex(hfooc2488.vf) = %{tl_version}, tex(hfooc2986.vf) = %{tl_version}
Provides:       tex(hfooc3583.vf) = %{tl_version}, tex(hforb0500.vf) = %{tl_version}
Provides:       tex(hforb0600.vf) = %{tl_version}, tex(hforb0700.vf) = %{tl_version}
Provides:       tex(hforb0800.vf) = %{tl_version}, tex(hforb0900.vf) = %{tl_version}
Provides:       tex(hforb1000.vf) = %{tl_version}, tex(hforb1095.vf) = %{tl_version}
Provides:       tex(hforb1200.vf) = %{tl_version}, tex(hforb1440.vf) = %{tl_version}
Provides:       tex(hforb1728.vf) = %{tl_version}, tex(hforb2074.vf) = %{tl_version}
Provides:       tex(hforb2488.vf) = %{tl_version}, tex(hforb2986.vf) = %{tl_version}
Provides:       tex(hforb3583.vf) = %{tl_version}, tex(hform0500.vf) = %{tl_version}
Provides:       tex(hform0600.vf) = %{tl_version}, tex(hform0700.vf) = %{tl_version}
Provides:       tex(hform0800.vf) = %{tl_version}, tex(hform0900.vf) = %{tl_version}
Provides:       tex(hform1000.vf) = %{tl_version}, tex(hform1095.vf) = %{tl_version}
Provides:       tex(hform1200.vf) = %{tl_version}, tex(hform1440.vf) = %{tl_version}
Provides:       tex(hform1728.vf) = %{tl_version}, tex(hform2074.vf) = %{tl_version}
Provides:       tex(hform2488.vf) = %{tl_version}, tex(hform2986.vf) = %{tl_version}
Provides:       tex(hform3583.vf) = %{tl_version}, tex(hfosc0500.vf) = %{tl_version}
Provides:       tex(hfosc0600.vf) = %{tl_version}, tex(hfosc0700.vf) = %{tl_version}
Provides:       tex(hfosc0800.vf) = %{tl_version}, tex(hfosc0900.vf) = %{tl_version}
Provides:       tex(hfosc1000.vf) = %{tl_version}, tex(hfosc1095.vf) = %{tl_version}
Provides:       tex(hfosc1200.vf) = %{tl_version}, tex(hfosc1440.vf) = %{tl_version}
Provides:       tex(hfosc1728.vf) = %{tl_version}, tex(hfosc2074.vf) = %{tl_version}
Provides:       tex(hfosc2488.vf) = %{tl_version}, tex(hfosc2986.vf) = %{tl_version}
Provides:       tex(hfosc3583.vf) = %{tl_version}, tex(hfosi0500.vf) = %{tl_version}
Provides:       tex(hfosi0600.vf) = %{tl_version}, tex(hfosi0700.vf) = %{tl_version}
Provides:       tex(hfosi0800.vf) = %{tl_version}, tex(hfosi0900.vf) = %{tl_version}
Provides:       tex(hfosi1000.vf) = %{tl_version}, tex(hfosi1095.vf) = %{tl_version}
Provides:       tex(hfosi1200.vf) = %{tl_version}, tex(hfosi1440.vf) = %{tl_version}
Provides:       tex(hfosi1728.vf) = %{tl_version}, tex(hfosi2074.vf) = %{tl_version}
Provides:       tex(hfosi2488.vf) = %{tl_version}, tex(hfosi2986.vf) = %{tl_version}
Provides:       tex(hfosi3583.vf) = %{tl_version}, tex(hfosl0500.vf) = %{tl_version}
Provides:       tex(hfosl0600.vf) = %{tl_version}, tex(hfosl0700.vf) = %{tl_version}
Provides:       tex(hfosl0800.vf) = %{tl_version}, tex(hfosl0900.vf) = %{tl_version}
Provides:       tex(hfosl1000.vf) = %{tl_version}, tex(hfosl1095.vf) = %{tl_version}
Provides:       tex(hfosl1200.vf) = %{tl_version}, tex(hfosl1440.vf) = %{tl_version}
Provides:       tex(hfosl1728.vf) = %{tl_version}, tex(hfosl2074.vf) = %{tl_version}
Provides:       tex(hfosl2488.vf) = %{tl_version}, tex(hfosl2986.vf) = %{tl_version}
Provides:       tex(hfosl3583.vf) = %{tl_version}, tex(hfoso0500.vf) = %{tl_version}
Provides:       tex(hfoso0600.vf) = %{tl_version}, tex(hfoso0700.vf) = %{tl_version}
Provides:       tex(hfoso0800.vf) = %{tl_version}, tex(hfoso0900.vf) = %{tl_version}
Provides:       tex(hfoso1000.vf) = %{tl_version}, tex(hfoso1095.vf) = %{tl_version}
Provides:       tex(hfoso1200.vf) = %{tl_version}, tex(hfoso1440.vf) = %{tl_version}
Provides:       tex(hfoso1728.vf) = %{tl_version}, tex(hfoso2074.vf) = %{tl_version}
Provides:       tex(hfoso2488.vf) = %{tl_version}, tex(hfoso2986.vf) = %{tl_version}
Provides:       tex(hfoso3583.vf) = %{tl_version}, tex(hfoss0500.vf) = %{tl_version}
Provides:       tex(hfoss0600.vf) = %{tl_version}, tex(hfoss0700.vf) = %{tl_version}
Provides:       tex(hfoss0800.vf) = %{tl_version}, tex(hfoss0900.vf) = %{tl_version}
Provides:       tex(hfoss1000.vf) = %{tl_version}, tex(hfoss1095.vf) = %{tl_version}
Provides:       tex(hfoss1200.vf) = %{tl_version}, tex(hfoss1440.vf) = %{tl_version}
Provides:       tex(hfoss1728.vf) = %{tl_version}, tex(hfoss2074.vf) = %{tl_version}
Provides:       tex(hfoss2488.vf) = %{tl_version}, tex(hfoss2986.vf) = %{tl_version}
Provides:       tex(hfoss3583.vf) = %{tl_version}, tex(hfost0600.vf) = %{tl_version}
Provides:       tex(hfost0700.vf) = %{tl_version}, tex(hfost0800.vf) = %{tl_version}
Provides:       tex(hfost0900.vf) = %{tl_version}, tex(hfost1000.vf) = %{tl_version}
Provides:       tex(hfost1095.vf) = %{tl_version}, tex(hfost1200.vf) = %{tl_version}
Provides:       tex(hfost1440.vf) = %{tl_version}, tex(hfost1728.vf) = %{tl_version}
Provides:       tex(hfost2074.vf) = %{tl_version}, tex(hfost2488.vf) = %{tl_version}
Provides:       tex(hfost2986.vf) = %{tl_version}, tex(hfost3583.vf) = %{tl_version}
Provides:       tex(hfosx0500.vf) = %{tl_version}, tex(hfosx0600.vf) = %{tl_version}
Provides:       tex(hfosx0700.vf) = %{tl_version}, tex(hfosx0800.vf) = %{tl_version}
Provides:       tex(hfosx0900.vf) = %{tl_version}, tex(hfosx1000.vf) = %{tl_version}
Provides:       tex(hfosx1095.vf) = %{tl_version}, tex(hfosx1200.vf) = %{tl_version}
Provides:       tex(hfosx1440.vf) = %{tl_version}, tex(hfosx1728.vf) = %{tl_version}
Provides:       tex(hfosx2074.vf) = %{tl_version}, tex(hfosx2488.vf) = %{tl_version}
Provides:       tex(hfosx2986.vf) = %{tl_version}, tex(hfosx3583.vf) = %{tl_version}
Provides:       tex(hfotc0600.vf) = %{tl_version}, tex(hfotc0700.vf) = %{tl_version}
Provides:       tex(hfotc0800.vf) = %{tl_version}, tex(hfotc0900.vf) = %{tl_version}
Provides:       tex(hfotc1000.vf) = %{tl_version}, tex(hfotc1095.vf) = %{tl_version}
Provides:       tex(hfotc1200.vf) = %{tl_version}, tex(hfotc1440.vf) = %{tl_version}
Provides:       tex(hfotc1728.vf) = %{tl_version}, tex(hfotc2074.vf) = %{tl_version}
Provides:       tex(hfotc2488.vf) = %{tl_version}, tex(hfotc2986.vf) = %{tl_version}
Provides:       tex(hfotc3583.vf) = %{tl_version}, tex(hfoti0500.vf) = %{tl_version}
Provides:       tex(hfoti0600.vf) = %{tl_version}, tex(hfoti0700.vf) = %{tl_version}
Provides:       tex(hfoti0800.vf) = %{tl_version}, tex(hfoti0900.vf) = %{tl_version}
Provides:       tex(hfoti1000.vf) = %{tl_version}, tex(hfoti1095.vf) = %{tl_version}
Provides:       tex(hfoti1200.vf) = %{tl_version}, tex(hfoti1440.vf) = %{tl_version}
Provides:       tex(hfoti1728.vf) = %{tl_version}, tex(hfoti2074.vf) = %{tl_version}
Provides:       tex(hfoti2488.vf) = %{tl_version}, tex(hfoti2986.vf) = %{tl_version}
Provides:       tex(hfoti3583.vf) = %{tl_version}, tex(hfott0600.vf) = %{tl_version}
Provides:       tex(hfott0700.vf) = %{tl_version}, tex(hfott0800.vf) = %{tl_version}
Provides:       tex(hfott0900.vf) = %{tl_version}, tex(hfott1000.vf) = %{tl_version}
Provides:       tex(hfott1095.vf) = %{tl_version}, tex(hfott1200.vf) = %{tl_version}
Provides:       tex(hfott1440.vf) = %{tl_version}, tex(hfott1728.vf) = %{tl_version}
Provides:       tex(hfott2074.vf) = %{tl_version}, tex(hfott2488.vf) = %{tl_version}
Provides:       tex(hfott2986.vf) = %{tl_version}, tex(hfott3583.vf) = %{tl_version}
Provides:       tex(hfoui0500.vf) = %{tl_version}, tex(hfoui0600.vf) = %{tl_version}
Provides:       tex(hfoui0700.vf) = %{tl_version}, tex(hfoui0800.vf) = %{tl_version}
Provides:       tex(hfoui0900.vf) = %{tl_version}, tex(hfoui1000.vf) = %{tl_version}
Provides:       tex(hfoui1095.vf) = %{tl_version}, tex(hfoui1200.vf) = %{tl_version}
Provides:       tex(hfoui1440.vf) = %{tl_version}, tex(hfoui1728.vf) = %{tl_version}
Provides:       tex(hfoui2074.vf) = %{tl_version}, tex(hfoui2488.vf) = %{tl_version}
Provides:       tex(hfoui2986.vf) = %{tl_version}, tex(hfoui3583.vf) = %{tl_version}
Provides:       tex(hfovi0600.vf) = %{tl_version}, tex(hfovi0700.vf) = %{tl_version}
Provides:       tex(hfovi0800.vf) = %{tl_version}, tex(hfovi0900.vf) = %{tl_version}
Provides:       tex(hfovi1000.vf) = %{tl_version}, tex(hfovi1095.vf) = %{tl_version}
Provides:       tex(hfovi1200.vf) = %{tl_version}, tex(hfovi1440.vf) = %{tl_version}
Provides:       tex(hfovi1728.vf) = %{tl_version}, tex(hfovi2074.vf) = %{tl_version}
Provides:       tex(hfovi2488.vf) = %{tl_version}, tex(hfovi2986.vf) = %{tl_version}
Provides:       tex(hfovi3583.vf) = %{tl_version}, tex(hfovt0600.vf) = %{tl_version}
Provides:       tex(hfovt0700.vf) = %{tl_version}, tex(hfovt0800.vf) = %{tl_version}
Provides:       tex(hfovt0900.vf) = %{tl_version}, tex(hfovt1000.vf) = %{tl_version}
Provides:       tex(hfovt1095.vf) = %{tl_version}, tex(hfovt1200.vf) = %{tl_version}
Provides:       tex(hfovt1440.vf) = %{tl_version}, tex(hfovt1728.vf) = %{tl_version}
Provides:       tex(hfovt2074.vf) = %{tl_version}, tex(hfovt2488.vf) = %{tl_version}
Provides:       tex(hfovt2986.vf) = %{tl_version}, tex(hfovt3583.vf) = %{tl_version}
Provides:       tex(hfoxc0500.vf) = %{tl_version}, tex(hfoxc0600.vf) = %{tl_version}
Provides:       tex(hfoxc0700.vf) = %{tl_version}, tex(hfoxc0800.vf) = %{tl_version}
Provides:       tex(hfoxc0900.vf) = %{tl_version}, tex(hfoxc1000.vf) = %{tl_version}
Provides:       tex(hfoxc1095.vf) = %{tl_version}, tex(hfoxc1200.vf) = %{tl_version}
Provides:       tex(hfoxc1440.vf) = %{tl_version}, tex(hfoxc1728.vf) = %{tl_version}
Provides:       tex(hfoxc2074.vf) = %{tl_version}, tex(hfoxc2488.vf) = %{tl_version}
Provides:       tex(hfoxc2986.vf) = %{tl_version}, tex(hfoxc3583.vf) = %{tl_version}
Provides:       tex(hfoldsty.sty) = %{tl_version}, tex(omlhfor.fd) = %{tl_version}
Provides:       tex(omshfor.fd) = %{tl_version}, tex(t1hfodh.fd) = %{tl_version}
Provides:       tex(t1hfor.fd) = %{tl_version}, tex(t1hfoss.fd) = %{tl_version}
Provides:       tex(t1hfott.fd) = %{tl_version}, tex(t1hfovt.fd) = %{tl_version}
Provides:       tex(ts1hfor.fd) = %{tl_version}, tex(ts1hfoss.fd) = %{tl_version}
Provides:       tex(ts1hfott.fd) = %{tl_version}, tex(ts1hfovtt.fd) = %{tl_version}

%description -n texlive-hfoldsty
The hfoldsty package provides virtual fonts for using oldstyle
(0123456789) figures with the European Computer Modern fonts.
It does a similar job as the eco package by Sebastian Kirsch
but includes a couple of improvements, i.e., better kerning
with guillemets, and support for character protruding using the
pdfcprot package.

%package -n texlive-hfoldsty-doc
Summary:        Documentation for hfoldsty
Version:        svn29349.1.15

Provides:       tex-hfoldsty-doc
AutoReqProv:    No

%description -n texlive-hfoldsty-doc
Documentation for hfoldsty

%package -n texlive-helvetic
Provides:       tex-helvetic = %{tl_version}
License:        GPL+
Summary:        URW "Base 35" font pack for LaTeX
Version:        svn31835.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(uhv.map) = %{tl_version}, tex(phvb.tfm) = %{tl_version}
Provides:       tex(phvb7t.tfm) = %{tl_version}, tex(phvb7tn.tfm) = %{tl_version}
Provides:       tex(phvb8c.tfm) = %{tl_version}, tex(phvb8cn.tfm) = %{tl_version}
Provides:       tex(phvb8r.tfm) = %{tl_version}, tex(phvb8rn.tfm) = %{tl_version}
Provides:       tex(phvb8t.tfm) = %{tl_version}, tex(phvb8tn.tfm) = %{tl_version}
Provides:       tex(phvbc.tfm) = %{tl_version}, tex(phvbc7t.tfm) = %{tl_version}
Provides:       tex(phvbc7tn.tfm) = %{tl_version}, tex(phvbc8t.tfm) = %{tl_version}
Provides:       tex(phvbc8tn.tfm) = %{tl_version}, tex(phvbo.tfm) = %{tl_version}
Provides:       tex(phvbo7t.tfm) = %{tl_version}, tex(phvbo7tn.tfm) = %{tl_version}
Provides:       tex(phvbo8c.tfm) = %{tl_version}, tex(phvbo8cn.tfm) = %{tl_version}
Provides:       tex(phvbo8r.tfm) = %{tl_version}, tex(phvbo8rn.tfm) = %{tl_version}
Provides:       tex(phvbo8t.tfm) = %{tl_version}, tex(phvbo8tn.tfm) = %{tl_version}
Provides:       tex(phvbon.tfm) = %{tl_version}, tex(phvbrn.tfm) = %{tl_version}
Provides:       tex(phvr.tfm) = %{tl_version}, tex(phvr7t.tfm) = %{tl_version}
Provides:       tex(phvr7tn.tfm) = %{tl_version}, tex(phvr8c.tfm) = %{tl_version}
Provides:       tex(phvr8cn.tfm) = %{tl_version}, tex(phvr8r.tfm) = %{tl_version}
Provides:       tex(phvr8rn.tfm) = %{tl_version}, tex(phvr8t.tfm) = %{tl_version}
Provides:       tex(phvr8tn.tfm) = %{tl_version}, tex(phvrc.tfm) = %{tl_version}
Provides:       tex(phvrc7t.tfm) = %{tl_version}, tex(phvrc7tn.tfm) = %{tl_version}
Provides:       tex(phvrc8t.tfm) = %{tl_version}, tex(phvrc8tn.tfm) = %{tl_version}
Provides:       tex(phvro.tfm) = %{tl_version}, tex(phvro7t.tfm) = %{tl_version}
Provides:       tex(phvro7tn.tfm) = %{tl_version}, tex(phvro8c.tfm) = %{tl_version}
Provides:       tex(phvro8cn.tfm) = %{tl_version}, tex(phvro8r.tfm) = %{tl_version}
Provides:       tex(phvro8rn.tfm) = %{tl_version}, tex(phvro8t.tfm) = %{tl_version}
Provides:       tex(phvro8tn.tfm) = %{tl_version}, tex(phvron.tfm) = %{tl_version}
Provides:       tex(phvrrn.tfm) = %{tl_version}, tex(arb10u.tfm) = %{tl_version}
Provides:       tex(arb2n.tfm) = %{tl_version}, tex(arb7j.tfm) = %{tl_version}
Provides:       tex(arb8u.tfm) = %{tl_version}, tex(arb9t.tfm) = %{tl_version}
Provides:       tex(ari10u.tfm) = %{tl_version}, tex(ari2n.tfm) = %{tl_version}
Provides:       tex(ari7j.tfm) = %{tl_version}, tex(ari8u.tfm) = %{tl_version}
Provides:       tex(ari9t.tfm) = %{tl_version}, tex(arj10u.tfm) = %{tl_version}
Provides:       tex(arj2n.tfm) = %{tl_version}, tex(arj7j.tfm) = %{tl_version}
Provides:       tex(arj8u.tfm) = %{tl_version}, tex(arj9t.tfm) = %{tl_version}
Provides:       tex(arr10u.tfm) = %{tl_version}, tex(arr2n.tfm) = %{tl_version}
Provides:       tex(arr7j.tfm) = %{tl_version}, tex(arr8u.tfm) = %{tl_version}
Provides:       tex(arr9t.tfm) = %{tl_version}, tex(mhvb.tfm) = %{tl_version}
Provides:       tex(mhvb8t.tfm) = %{tl_version}, tex(mhvbi.tfm) = %{tl_version}
Provides:       tex(mhvbi8t.tfm) = %{tl_version}, tex(mhvr.tfm) = %{tl_version}
Provides:       tex(mhvr8t.tfm) = %{tl_version}, tex(mhvri.tfm) = %{tl_version}
Provides:       tex(mhvri8t.tfm) = %{tl_version}, tex(uhvb7t.tfm) = %{tl_version}
Provides:       tex(uhvb7tn.tfm) = %{tl_version}, tex(uhvb8c.tfm) = %{tl_version}
Provides:       tex(uhvb8cn.tfm) = %{tl_version}, tex(uhvb8r.tfm) = %{tl_version}
Provides:       tex(uhvb8rn.tfm) = %{tl_version}, tex(uhvb8t.tfm) = %{tl_version}
Provides:       tex(uhvb8tn.tfm) = %{tl_version}, tex(uhvbc7t.tfm) = %{tl_version}
Provides:       tex(uhvbc7tn.tfm) = %{tl_version}, tex(uhvbc8t.tfm) = %{tl_version}
Provides:       tex(uhvbc8tn.tfm) = %{tl_version}, tex(uhvbi7t.tfm) = %{tl_version}
Provides:       tex(uhvbi8c.tfm) = %{tl_version}, tex(uhvbi8r.tfm) = %{tl_version}
Provides:       tex(uhvbi8t.tfm) = %{tl_version}, tex(uhvbo7t.tfm) = %{tl_version}
Provides:       tex(uhvbo7tn.tfm) = %{tl_version}, tex(uhvbo8c.tfm) = %{tl_version}
Provides:       tex(uhvbo8cn.tfm) = %{tl_version}, tex(uhvbo8r.tfm) = %{tl_version}
Provides:       tex(uhvbo8rn.tfm) = %{tl_version}, tex(uhvbo8t.tfm) = %{tl_version}
Provides:       tex(uhvbo8tn.tfm) = %{tl_version}, tex(uhvr7t.tfm) = %{tl_version}
Provides:       tex(uhvr7tn.tfm) = %{tl_version}, tex(uhvr8c.tfm) = %{tl_version}
Provides:       tex(uhvr8cn.tfm) = %{tl_version}, tex(uhvr8r.tfm) = %{tl_version}
Provides:       tex(uhvr8rn.tfm) = %{tl_version}, tex(uhvr8t.tfm) = %{tl_version}
Provides:       tex(uhvr8tn.tfm) = %{tl_version}, tex(uhvrc7t.tfm) = %{tl_version}
Provides:       tex(uhvrc7tn.tfm) = %{tl_version}, tex(uhvrc8t.tfm) = %{tl_version}
Provides:       tex(uhvrc8tn.tfm) = %{tl_version}, tex(uhvri7t.tfm) = %{tl_version}
Provides:       tex(uhvri7tn.tfm) = %{tl_version}, tex(uhvri8c.tfm) = %{tl_version}
Provides:       tex(uhvri8cn.tfm) = %{tl_version}, tex(uhvri8r.tfm) = %{tl_version}
Provides:       tex(uhvri8rn.tfm) = %{tl_version}, tex(uhvri8t.tfm) = %{tl_version}
Provides:       tex(uhvri8tn.tfm) = %{tl_version}, tex(uhvro7t.tfm) = %{tl_version}
Provides:       tex(uhvro7tn.tfm) = %{tl_version}, tex(uhvro8c.tfm) = %{tl_version}
Provides:       tex(uhvro8cn.tfm) = %{tl_version}, tex(uhvro8r.tfm) = %{tl_version}
Provides:       tex(uhvro8rn.tfm) = %{tl_version}, tex(uhvro8t.tfm) = %{tl_version}
Provides:       tex(uhvro8tn.tfm) = %{tl_version}, tex(uhvb8a.pfb) = %{tl_version}
Provides:       tex(uhvb8ac.pfb) = %{tl_version}, tex(uhvbo8a.pfb) = %{tl_version}
Provides:       tex(uhvbo8ac.pfb) = %{tl_version}, tex(uhvr8a-105.pfb) = %{tl_version}
Provides:       tex(uhvr8a.pfb) = %{tl_version}, tex(uhvr8ac.pfb) = %{tl_version}
Provides:       tex(uhvro8a-105.pfb) = %{tl_version}, tex(uhvro8a.pfb) = %{tl_version}
Provides:       tex(uhvro8ac.pfb) = %{tl_version}, tex(phvb.vf) = %{tl_version}
Provides:       tex(phvb7t.vf) = %{tl_version}, tex(phvb7tn.vf) = %{tl_version}
Provides:       tex(phvb8c.vf) = %{tl_version}, tex(phvb8cn.vf) = %{tl_version}
Provides:       tex(phvb8t.vf) = %{tl_version}, tex(phvb8tn.vf) = %{tl_version}
Provides:       tex(phvbc.vf) = %{tl_version}, tex(phvbc7t.vf) = %{tl_version}
Provides:       tex(phvbc7tn.vf) = %{tl_version}, tex(phvbc8t.vf) = %{tl_version}
Provides:       tex(phvbc8tn.vf) = %{tl_version}, tex(phvbo.vf) = %{tl_version}
Provides:       tex(phvbo7t.vf) = %{tl_version}, tex(phvbo7tn.vf) = %{tl_version}
Provides:       tex(phvbo8c.vf) = %{tl_version}, tex(phvbo8cn.vf) = %{tl_version}
Provides:       tex(phvbo8t.vf) = %{tl_version}, tex(phvbo8tn.vf) = %{tl_version}
Provides:       tex(phvbon.vf) = %{tl_version}, tex(phvbrn.vf) = %{tl_version}
Provides:       tex(phvr.vf) = %{tl_version}, tex(phvr7t.vf) = %{tl_version}
Provides:       tex(phvr7tn.vf) = %{tl_version}, tex(phvr8c.vf) = %{tl_version}
Provides:       tex(phvr8cn.vf) = %{tl_version}, tex(phvr8t.vf) = %{tl_version}
Provides:       tex(phvr8tn.vf) = %{tl_version}, tex(phvrc.vf) = %{tl_version}
Provides:       tex(phvrc7t.vf) = %{tl_version}, tex(phvrc7tn.vf) = %{tl_version}
Provides:       tex(phvrc8t.vf) = %{tl_version}, tex(phvrc8tn.vf) = %{tl_version}
Provides:       tex(phvro.vf) = %{tl_version}, tex(phvro7t.vf) = %{tl_version}
Provides:       tex(phvro7tn.vf) = %{tl_version}, tex(phvro8c.vf) = %{tl_version}
Provides:       tex(phvro8cn.vf) = %{tl_version}, tex(phvro8t.vf) = %{tl_version}
Provides:       tex(phvro8tn.vf) = %{tl_version}, tex(phvron.vf) = %{tl_version}
Provides:       tex(phvrrn.vf) = %{tl_version}, tex(mhvb.vf) = %{tl_version}
Provides:       tex(mhvb8t.vf) = %{tl_version}, tex(mhvbi.vf) = %{tl_version}
Provides:       tex(mhvbi8t.vf) = %{tl_version}, tex(mhvr.vf) = %{tl_version}
Provides:       tex(mhvr8t.vf) = %{tl_version}, tex(mhvri.vf) = %{tl_version}
Provides:       tex(mhvri8t.vf) = %{tl_version}, tex(uhvb7t.vf) = %{tl_version}
Provides:       tex(uhvb7tn.vf) = %{tl_version}, tex(uhvb8c.vf) = %{tl_version}
Provides:       tex(uhvb8cn.vf) = %{tl_version}, tex(uhvb8t.vf) = %{tl_version}
Provides:       tex(uhvb8tn.vf) = %{tl_version}, tex(uhvbc7t.vf) = %{tl_version}
Provides:       tex(uhvbc7tn.vf) = %{tl_version}, tex(uhvbc8t.vf) = %{tl_version}
Provides:       tex(uhvbc8tn.vf) = %{tl_version}, tex(uhvbi7t.vf) = %{tl_version}
Provides:       tex(uhvbi8c.vf) = %{tl_version}, tex(uhvbi8t.vf) = %{tl_version}
Provides:       tex(uhvbo7t.vf) = %{tl_version}, tex(uhvbo7tn.vf) = %{tl_version}
Provides:       tex(uhvbo8c.vf) = %{tl_version}, tex(uhvbo8cn.vf) = %{tl_version}
Provides:       tex(uhvbo8t.vf) = %{tl_version}, tex(uhvbo8tn.vf) = %{tl_version}
Provides:       tex(uhvr7t.vf) = %{tl_version}, tex(uhvr7tn.vf) = %{tl_version}
Provides:       tex(uhvr8c.vf) = %{tl_version}, tex(uhvr8cn.vf) = %{tl_version}
Provides:       tex(uhvr8t.vf) = %{tl_version}, tex(uhvr8tn.vf) = %{tl_version}
Provides:       tex(uhvrc7t.vf) = %{tl_version}, tex(uhvrc7tn.vf) = %{tl_version}
Provides:       tex(uhvrc8t.vf) = %{tl_version}, tex(uhvrc8tn.vf) = %{tl_version}
Provides:       tex(uhvri7t.vf) = %{tl_version}, tex(uhvri7tn.vf) = %{tl_version}
Provides:       tex(uhvri8c.vf) = %{tl_version}, tex(uhvri8cn.vf) = %{tl_version}
Provides:       tex(uhvri8t.vf) = %{tl_version}, tex(uhvri8tn.vf) = %{tl_version}
Provides:       tex(uhvro7t.vf) = %{tl_version}, tex(uhvro7tn.vf) = %{tl_version}
Provides:       tex(uhvro8c.vf) = %{tl_version}, tex(uhvro8cn.vf) = %{tl_version}
Provides:       tex(uhvro8t.vf) = %{tl_version}, tex(uhvro8tn.vf) = %{tl_version}
Provides:       tex(8ruhv.fd) = %{tl_version}, tex(omluhv.fd) = %{tl_version}
Provides:       tex(omsuhv.fd) = %{tl_version}, tex(ot1uhv.fd) = %{tl_version}
Provides:       tex(t1uhv.fd) = %{tl_version}, tex(ts1uhv.fd) = %{tl_version}

%description -n texlive-helvetic
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-hanoi
Provides:       tex-hanoi = %{tl_version}
License:        Public Domain
Summary:        Tower of Hanoi in TeX
Version:        svn25019.20120101

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(hanoi.tex) = %{tl_version}

%description -n texlive-hanoi
The Plain TeX program (typed in the shape of the towers of
Hanoi) serves both as a game and as a TeX programming exercise.
As a game it will solve the towers with (up to) 15 discs (with
15 discs, 32767 moves are needed).

%package -n texlive-havannah
Provides:       tex-havannah = %{tl_version}
License:        LPPL 1.2
Summary:        Diagrams of board positions in the games of Havannah and Hex
Version:        svn36348.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty)
Provides:       tex(havannah.sty) = %{tl_version}

%description -n texlive-havannah
This package defines macros for typesetting diagrams of board
positions in the games of Havannah and Hex.

%package -n texlive-havannah-doc
Summary:        Documentation for havannah
Version:        svn36348.0

Provides:       tex-havannah-doc
AutoReqProv:    No

%description -n texlive-havannah-doc
Documentation for havannah

%package -n texlive-hexgame
Provides:       tex-hexgame = %{tl_version}
License:        LPPL
Summary:        Provide an environment to draw a hexgame-board
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstcol.sty), tex(pst-poly.sty), tex(calc.sty), tex(ifthen.sty)
Provides:       tex(hexgame.sty) = %{tl_version}

%description -n texlive-hexgame
Hex is a mathematical game invented by the Danish mathematician
Piet Hein and independently by the mathematician John Nash.
This package defines an environment that enables the user to
draw such a game in a trivial way.

%package -n texlive-hexgame-doc
Summary:        Documentation for hexgame
Version:        svn15878.1.0

Provides:       tex-hexgame-doc
AutoReqProv:    No

%description -n texlive-hexgame-doc
Documentation for hexgame

%package -n texlive-horoscop
Provides:       tex-horoscop = %{tl_version}
License:        Public Domain
Summary:        Generate astrological charts in LaTeX
Version:        svn30530.0.92

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(wasysym.sty), tex(marvosym.sty), tex(starfont.sty), tex(pict2e.sty)
Requires:       tex(trig.sty)
Provides:       tex(horoscop.sty) = %{tl_version}

%description -n texlive-horoscop
The horoscop package provides a unified interface for
astrological font packages; typesetting with pict2e of standard
wheel charts and some variations, in PostScript- and PDF-
generating TeX engines; and access to external calculation
software (Astrolog and Swiss Ephemeris) for computing object
positions.

%package -n texlive-hook-pre-commit-pkg-doc
Summary:        Documentation for hook-pre-commit-pkg
Version:        svn41378

Provides:       tex-hook-pre-commit-pkg-doc
AutoReqProv:    No

%description -n texlive-hook-pre-commit-pkg-doc
Documentation for hook-pre-commit-pkg

%package -n texlive-horoscop-doc
Summary:        Documentation for horoscop
Version:        svn30530.0.92

Provides:       tex-horoscop-doc
AutoReqProv:    No

%description -n texlive-horoscop-doc
Documentation for horoscop

%package -n texlive-happy4th-doc
Summary:        Documentation for happy4th
Version:        svn25020.20120102

Provides:       tex-happy4th-doc
AutoReqProv:    No

%description -n texlive-happy4th-doc
Documentation for happy4th

%package -n texlive-hrlatex
Provides:       tex-hrlatex = %{tl_version}
License:        LPPL
Summary:        LaTeX support for Croatian documents
Version:        svn18020.0.23

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(txfonts.sty), tex(amsmath.sty), tex(amsthm.sty)
Requires:       tex(amssymb.sty), tex(graphicx.sty), tex(optional.sty), tex(calc.sty)
Requires:       tex(ifthen.sty), tex(framed.sty), tex(multicol.sty), tex(enumerate.sty)
Requires:       tex(paralist.sty), tex(xcolor.sty), tex(cancel.sty), tex(hyperref.sty)
Requires:       tex(inputenc.sty), tex(fontenc.sty), tex(babel.sty), tex(amsopn.sty)
Provides:       tex(fsbispit.cls) = %{tl_version}, tex(fsbmath.sty) = %{tl_version}
Provides:       tex(hrlatex.sty) = %{tl_version}

%description -n texlive-hrlatex
This package simplifies creation of new documents for the
(average) Croatian user. As an example, a class file hrdipl.cls
(designed for the graduation thesis at the University of
Zagreb) and sample thesis documents are included.

%package -n texlive-hrlatex-doc
Summary:        Documentation for hrlatex
Version:        svn18020.0.23

Provides:       tex-hrlatex-doc
AutoReqProv:    No

%description -n texlive-hrlatex-doc
Documentation for hrlatex

%package -n texlive-hausarbeit-jura
Provides:       tex-hausarbeit-jura = %{tl_version}
License:        LPPL 1.3
Summary:        Class for writing "juristiche Hausarbeiten" at German Universities
Version:        svn42054
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(ifluatex.sty), tex(ifxetex.sty), tex(inputenc.sty)
Requires:       tex(fontenc.sty), tex(babel.sty), tex(textcomp.sty), tex(eurosym.sty)
Requires:       tex(indentfirst.sty), tex(geometry.sty), tex(csquotes.sty), tex(jurabib.sty)
Provides:       tex(hausarbeit-jura.cls) = %{tl_version}

%description -n texlive-hausarbeit-jura
The class was developed for use by students writing legal
essays ("juristische Hausarbeit") at German Universities. It is
based on jurabook and jurabib and makes it easy for LaTeX
beginners to get a correct and nicely formatted paper.

%package -n texlive-hausarbeit-jura-doc
Summary:        Documentation for hausarbeit-jura
Version:        svn42054
Provides:       tex-hausarbeit-jura-doc
AutoReqProv:    No

%description -n texlive-hausarbeit-jura-doc
Documentation for hausarbeit-jura


%package -n texlive-harveyballs
Provides:       tex-harveyballs = %{tl_version}
License:        GPLv3+
Summary:        Create Harvey Balls using TikZ
Version:        svn32003.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty)
Provides:       tex(harveyballs.sty) = %{tl_version}

%description -n texlive-harveyballs
The package provides 5 commands (giving symbols that indicate
values from "none" to "full").

%package -n texlive-harveyballs-doc
Summary:        Documentation for harveyballs
Version:        svn32003.1.1

Provides:       tex-harveyballs-doc
AutoReqProv:    No

%description -n texlive-harveyballs-doc
Documentation for harveyballs

%package -n texlive-here
Provides:       tex-here = %{tl_version}
License:        Public Domain
Summary:        Emulation of obsolete package for "here" floats
Version:        svn16135.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(float.sty)
Provides:       tex(here.sty) = %{tl_version}

%description -n texlive-here
Provides the H option for floats in LaTeX to signify that the
environment is not really a float (and should therefore be
placed "here" and not float at all). The package emulates an
older package of the same name, which has long been suppressed
by its author. The job is done by nothing more than loading the
float package, which has long provided the option in an
acceptable framework.

%package -n texlive-here-doc
Summary:        Documentation for here
Version:        svn16135.0

Provides:       tex-here-doc
AutoReqProv:    No

%description -n texlive-here-doc
Documentation for here

%package -n texlive-hf-tikz
Provides:       tex-hf-tikz = %{tl_version}
License:        LPPL 1.3
Summary:        A simple way to highlight formulas and formula parts
Version:        svn34733.0.3a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(xparse.sty), tex(etoolbox.sty)
Provides:       tex(hf-tikz.sty) = %{tl_version}

%description -n texlive-hf-tikz
The package provides a way to highlight formulas and formula
parts in both documents and presentations, us TikZ.

%package -n texlive-hf-tikz-doc
Summary:        Documentation for hf-tikz
Version:        svn34733.0.3a

Provides:       tex-hf-tikz-doc
AutoReqProv:    No

%description -n texlive-hf-tikz-doc
Documentation for hf-tikz

%package -n texlive-hobby
Provides:       tex-hobby = %{tl_version}
License:        LPPL 1.3
Summary:        An implementation of Hobby's algorithm for PGF/TikZ
Version:        svn44474
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty)
Provides:       tex(hobby.code.tex) = %{tl_version}, tex(pgflibraryhobby.code.tex) = %{tl_version}
Provides:       tex(pml3array.sty) = %{tl_version}, tex(tikzlibraryhobby.code.tex) = %{tl_version}

%description -n texlive-hobby
This package defines a path generation function for PGF/TikZ
which implements Hobby's algorithm for a path built out of
Bezier curves which passes through a given set of points. The
path thus generated may by used as a TikZ 'to path'. The
implementation is in LaTeX3.

%package -n texlive-hobby-doc
Summary:        Documentation for hobby
Version:        svn44474
Provides:       tex-hobby-doc
AutoReqProv:    No

%description -n texlive-hobby-doc
Documentation for hobby

%package -n texlive-hvfloat
Provides:       tex-hvfloat = %{tl_version}
License:        LPPL
Summary:        Rotating caption and object of floats independently
Version:        svn46124
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphicx.sty), tex(keyval.sty), tex(caption.sty)
Provides:       tex(hvfloat.sty) = %{tl_version}

%description -n texlive-hvfloat
This package defines a macro to place objects (tables and
figures) and their captions in different positions with
different rotating angles within a float. All objects and
captions can be framed. The main command is \hvFloat{float
type}{floating object}{caption}{label}; a simple example is
\hvFloat{figure}{\includegraphics{rose}}{Caption}{fig:0}.
Options are provided to place captions to the right or left,
and rotated. Setting nonFloat=true results in placing the float
here.

%package -n texlive-hvfloat-doc
Summary:        Documentation for hvfloat
Version:        svn46124
Provides:       tex-hvfloat-doc
AutoReqProv:    No

%description -n texlive-hvfloat-doc
Documentation for hvfloat

%package -n texlive-handout
Provides:       tex-handout = %{tl_version}
License:        LPPL 1.3
Summary:        Create handout for auditors of a talk
Version:        svn43962
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(kvoptions.sty), tex(etoolbox.sty)
Provides:       tex(handout.sty) = %{tl_version}

%description -n texlive-handout
In some fields of scholarship, a beamer does not offer good
support when giving a talk in a proceeding. For example, in
classical philology, the main sources are text, and it will be
better to distribute a handout to the audience with extracts of
the texts about which we will talk. The package supports
preparation of such handouts when writing the talk.

%package -n texlive-handout-doc
Summary:        Documentation for handout
Version:        svn43962
Provides:       tex-handout-doc
AutoReqProv:    No

%description -n texlive-handout-doc
Documentation for handout

%package -n texlive-hang
Provides:       tex-hang = %{tl_version}
License:        LPPL 1.3
Summary:        Environments for hanging paragraphs and list items
Version:        svn43280
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(hang.sty) = %{tl_version}

%description -n texlive-hang
This package provides environments for hanging paragraphs and
list items. In addition, it defines environments for labeled
paragraphs and list items.

%package -n texlive-hang-doc
Summary:        Documentation for hang
Version:        svn43280
Provides:       tex-hang-doc
AutoReqProv:    No

%description -n texlive-hang-doc
Documentation for hang

%package -n texlive-hanging
Provides:       tex-hanging = %{tl_version}
License:        LPPL 1.3
Summary:        Hanging paragraphs
Version:        svn15878.1.2b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(hanging.sty) = %{tl_version}

%description -n texlive-hanging
The hanging package facilitates the typesetting of hanging
paragraphs. The package also enables typesetting with hanging
punctuation, by making punctuation characters active. This
facility is best suppressed (it can interfere with other
packages) -- there are package options for suppressing each
individual punctuation character. 'Real' attempts at hanging
punction should nowadays use the microtype package, which takes
advantage of the support offered in recent versions of pdfTeX.

%package -n texlive-hanging-doc
Summary:        Documentation for hanging
Version:        svn15878.1.2b

Provides:       tex-hanging-doc
AutoReqProv:    No

%description -n texlive-hanging-doc
Documentation for hanging

%package -n texlive-hardwrap
Provides:       tex-hardwrap = %{tl_version}
License:        LPPL 1.3
Summary:        Hard wrap text to a certain character length
Version:        svn21396.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifplatform.sty), tex(pdftexcmds.sty)
Requires:       tex(ifxetex.sty)
Provides:       tex(hardwrap.sty) = %{tl_version}

%description -n texlive-hardwrap
The package facilitates wrapping text to a specific character
width, breaking lines by words rather than, as done by TeX, by
characters. The primary use for these facilities is to aid the
generation of messages sent to the log file or console output
to display messages to the user. Package authors may also find
this useful when writing out arbitary text to an external file.

%package -n texlive-hardwrap-doc
Summary:        Documentation for hardwrap
Version:        svn21396.0.2

Provides:       tex-hardwrap-doc
AutoReqProv:    No

%description -n texlive-hardwrap-doc
Documentation for hardwrap

%package -n texlive-harnon-cv
Provides:       tex-harnon-cv = %{tl_version}
License:        Public Domain
Summary:        A CV document class with a vertical timeline for experience
Version:        svn26543.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(harnon-cv.cls) = %{tl_version}

%description -n texlive-harnon-cv
The class offers another modern, neat, design, and provides a
simple means of adding an 'experience timeline'.

%package -n texlive-harnon-cv-doc
Summary:        Documentation for harnon-cv
Version:        svn26543.1.0

Provides:       tex-harnon-cv-doc
AutoReqProv:    No

%description -n texlive-harnon-cv-doc
Documentation for harnon-cv

%package -n texlive-harpoon
Provides:       tex-harpoon = %{tl_version}
License:        Public Domain
Summary:        Extra harpoons, using the graphics package
Version:        svn21327.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty)
Provides:       tex(harpoon.sty) = %{tl_version}

%description -n texlive-harpoon
Provides over- and under-harpoon symbol commands; the harpoons
may point in either direction, with the hook pointing up or
down. The covered object is provided as an argument to the
commands, so that they have the look of accent commands.

%package -n texlive-harpoon-doc
Summary:        Documentation for harpoon
Version:        svn21327.1.0

Provides:       tex-harpoon-doc
AutoReqProv:    No

%description -n texlive-harpoon-doc
Documentation for harpoon

%package -n texlive-hc
Provides:       tex-hc = %{tl_version}
License:        GPLv2+
Summary:        Replacement for the LaTeX classes
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(natbib.sty), tex(fontenc.sty), tex(inputenc.sty), tex(ifthen.sty)
Requires:       tex(babel.sty), tex(xspace.sty), tex(palatino.sty), tex(mathpple.sty)
Requires:       tex(pifont.sty), tex(fancyref.sty), tex(truncate.sty), tex(typearea.sty)
Requires:       tex(multicol.sty), tex(hyperref.sty), tex(fancybox.sty)
Provides:       tex(hcart.cls) = %{tl_version}, tex(hcletter.cls) = %{tl_version}
Provides:       tex(hcreport.cls) = %{tl_version}, tex(hcslides.cls) = %{tl_version}

%description -n texlive-hc
A set of replacements for the default LaTeX classes, based upon
the Koma-Script bundle and the seminar class. Includes hcart,
hcreport, hcletter, and hcslides.

%package -n texlive-hc-doc
Summary:        Documentation for hc
Version:        svn15878.0

Provides:       tex-hc-doc
AutoReqProv:    No

%description -n texlive-hc-doc
Documentation for hc

%package -n texlive-he-she
Provides:       tex-he-she = %{tl_version}
License:        LPPL 1.3
Summary:        Alternating pronouns to aid gender-neutral writing
Version:        svn41359

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty), tex(everyhook.sty)
Provides:       tex(he-she.sty) = %{tl_version}

%description -n texlive-he-she
The package implements a version of semi-automatic pronoun
switching for writing gender-neutral (and possibly annoying)
prose. It has upper- and lowercase versions of switching
pronouns for all case forms, plus anaphoric versions that
reflect the current gender choice.

%package -n texlive-he-she-doc
Summary:        Documentation for he-she
Version:        svn41359

Provides:       tex-he-she-doc
AutoReqProv:    No

%description -n texlive-he-she-doc
Documentation for he-she

%package -n texlive-hhtensor
Provides:       tex-hhtensor = %{tl_version}
License:        LPPL
Summary:        Print vectors, matrices, and tensors
Version:        svn24981.0.61

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ushort.sty), tex(amsmath.sty)
Provides:       tex(hhtensor.sty) = %{tl_version}

%description -n texlive-hhtensor
This package provides commands for vectors, matrices, and
tensors with different styles -- arrows (as the LaTeX default),
underlined, and bold).

%package -n texlive-hhtensor-doc
Summary:        Documentation for hhtensor
Version:        svn24981.0.61

Provides:       tex-hhtensor-doc
AutoReqProv:    No

%description -n texlive-hhtensor-doc
Documentation for hhtensor

%package -n texlive-histogr
Provides:       tex-histogr = %{tl_version}
License:        LPPL 1.3
Summary:        Draw histograms with the LaTeX picture environment
Version:        svn15878.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(histogr.sty) = %{tl_version}

%description -n texlive-histogr
This is a collection pf macros to draw histogram bars inside a
LaTeX picture-environment.

%package -n texlive-histogr-doc
Summary:        Documentation for histogr
Version:        svn15878.1.01

Provides:       tex-histogr-doc
AutoReqProv:    No

%description -n texlive-histogr-doc
Documentation for histogr

%package -n texlive-hitec
Provides:       tex-hitec = %{tl_version}
License:        LPPL
Summary:        Class for documentation
Version:        svn15878.0.0_beta_

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(hitec.cls) = %{tl_version}

%description -n texlive-hitec
An article-based class designed for use for documentation in
high-technology companies.

%package -n texlive-hitec-doc
Summary:        Documentation for hitec
Version:        svn15878.0.0_beta_

Provides:       tex-hitec-doc
AutoReqProv:    No

%description -n texlive-hitec-doc
Documentation for hitec

%package -n texlive-hletter
Provides:       tex-hletter = %{tl_version}
License:        LPPL 1.2
Summary:        Flexible letter typesetting with flexible page headings
Version:        svn30002.4.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(graphicx.sty), tex(babel.sty)
Provides:       tex(hdefine.clo) = %{tl_version}, tex(hhead.sty) = %{tl_version}
Provides:       tex(hlete.clo) = %{tl_version}, tex(hletf.clo) = %{tl_version}
Provides:       tex(hletg.clo) = %{tl_version}, tex(hletter.cls) = %{tl_version}
Provides:       tex(hsetup.sty) = %{tl_version}, tex(mergeh.sty) = %{tl_version}

%description -n texlive-hletter
The package permits the user to specify easily, with the aid of
self defined key-words, letters (with a logo and private) and
headings. The heading may include a footer and the letter
provides commands to include a scanned signature and two
signees. The package works with the merge package.

%package -n texlive-hletter-doc
Summary:        Documentation for hletter
Version:        svn30002.4.2

Provides:       tex-hletter-doc
AutoReqProv:    No

%description -n texlive-hletter-doc
Documentation for hletter

%package -n texlive-hpsdiss
Provides:       tex-hpsdiss = %{tl_version}
License:        GPL+
Summary:        A dissertation class
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(calc.sty), tex(ragged2e.sty), tex(rotating.sty)
Requires:       tex(mparhack.sty), tex(graphicx.sty), tex(colordvi.sty)
Provides:       tex(hpsdiss.cls) = %{tl_version}

%description -n texlive-hpsdiss
The class was developed to typeset a dissertation at ETH
Zurich. The requirements were to use A5 paper and 10pt type. A
sample of the output is shown in the PDF documentation link.

%package -n texlive-hpsdiss-doc
Summary:        Documentation for hpsdiss
Version:        svn15878.1.0

Provides:       tex-hpsdiss-doc
AutoReqProv:    No

%description -n texlive-hpsdiss-doc
Documentation for hpsdiss

%package -n texlive-hrefhide
Provides:       tex-hrefhide = %{tl_version}
License:        LPPL 1.3
Summary:        Suppress hyper links when printing
Version:        svn22255.1.0f

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xcolor.sty), tex(hyperref.sty), tex(kvoptions.sty)
Provides:       tex(hrefhide.sty) = %{tl_version}

%description -n texlive-hrefhide
This package provides the command \hrefdisplayonly (which
provides a substitute for \href). While the (hyperlinked) text
appears like an ordinary \href in the compiled PDF file, the
same text will be "hidden" when printing the text. (Hiding is
actually achieved by making the text the same colour as the
background, thus preserving the layout of the rest of the
text.)

%package -n texlive-hrefhide-doc
Summary:        Documentation for hrefhide
Version:        svn22255.1.0f

Provides:       tex-hrefhide-doc
AutoReqProv:    No

%description -n texlive-hrefhide-doc
Documentation for hrefhide

%package -n texlive-hvindex
Provides:       tex-hvindex = %{tl_version}
License:        LPPL
Summary:        Support for indexing
Version:        svn46051
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(makeidx.sty)
Provides:       tex(hvindex.sty) = %{tl_version}

%description -n texlive-hvindex
The package simplifies the indexing of words using the \index
command of makeidx. With the package, to index a word in a
text, you only have to type it once; the package makes sure it
is both typeset and indexed.

%package -n texlive-hvindex-doc
Summary:        Documentation for hvindex
Version:        svn46051
Provides:       tex-hvindex-doc
AutoReqProv:    No

%description -n texlive-hvindex-doc
Documentation for hvindex

%package -n texlive-har2nat
Provides:       tex-har2nat = %{tl_version}
License:        LPPL
Summary:        Replace the harvard package with natbib
Version:        svn17356.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(suffix.sty), tex(natbib.sty)
Provides:       tex(har2nat.sty) = %{tl_version}

%description -n texlive-har2nat
This small package allows a LaTeX document containing the
citation commands provided by the Harvard package to be
compiled using the natbib package. Migration from harvard to
natbib thus can be achieved simply by replacing
\usepackage{harvard} with \usepackage{natbib}
\usepackage{har2nat} It is important that har2nat be loaded
after natbib, since it modifies natbib commands.

%package -n texlive-har2nat-doc
Summary:        Documentation for har2nat
Version:        svn17356.1.0

Provides:       tex-har2nat-doc
AutoReqProv:    No

%description -n texlive-har2nat-doc
Documentation for har2nat

%package -n texlive-hobete
Provides:       tex-hobete = %{tl_version}
License:        LPPL
Summary:        Unofficial beamer theme for the University of Hohenheim
Version:        svn27036.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(l3keys2e.sty), tex(xfrac.sty), tex(xparse.sty)
Requires:       tex(tikz.sty)
Provides:       tex(beamercolorthemehohenheim.sty) = %{tl_version}
Provides:       tex(beamerouterthemehohenheim.sty) = %{tl_version}
Provides:       tex(beamerouterthemehohenheimposter.sty) = %{tl_version}
Provides:       tex(beamerthemehohenheim.sty) = %{tl_version}
Provides:       tex(hobete.sty) = %{tl_version}

%description -n texlive-hobete
The package provides a beamer theme which features the Ci
colors of the University of Hohenheim. Please note that this is
not an official Theme, and that there will be no support for
it, from the University. Furthermore there is NO relationship
between the University and this theme.

%package -n texlive-hobete-doc
Summary:        Documentation for hobete
Version:        svn27036.0

Provides:       tex-hobete-doc
AutoReqProv:    No

%description -n texlive-hobete-doc
Documentation for hobete

%package -n texlive-hep
Provides:       tex-hep = %{tl_version}
License:        LPPL
Summary:        A "convenience wrapper" for High Energy Physics packages
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(url.sty), tex(cite.sty), tex(hyperref.sty), tex(amsmath.sty)
Requires:       tex(braket.sty), tex(cancel.sty), tex(slashed.sty), tex(hepnicenames.sty)
Requires:       tex(hepunits.sty), tex(feynmf.sty), tex(booktabs.sty), tex(setspace.sty)
Requires:       tex(fancyhdr.sty), tex(tocbibind.sty), tex(morefloats.sty), tex(afterpage.sty)
Requires:       tex(ccaption.sty), tex(subfigure.sty), tex(caption.sty)
Provides:       tex(hep.sty) = %{tl_version}

%description -n texlive-hep
Loads the author's hepunits and hepnicenames packages, and a
selection of others that are useful in High Energy Physics
papers, etc.

%package -n texlive-hep-doc
Summary:        Documentation for hep
Version:        svn15878.1.0

Provides:       tex-hep-doc
AutoReqProv:    No

%description -n texlive-hep-doc
Documentation for hep

%package -n texlive-hepnames
Provides:       tex-hepnames = %{tl_version}
License:        LPPL
Summary:        Pre-defined high energy particle names
Version:        svn35722.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(heppennames.sty), tex(hepparticles.sty)
Requires:       tex(xspace.sty), tex(amsmath.sty)
Provides:       tex(hepnames.sty) = %{tl_version}, tex(hepnicenames.sty) = %{tl_version}
Provides:       tex(heppennames.sty) = %{tl_version}

%description -n texlive-hepnames
Hepnames provides a pair of LaTeX packages, heppennames and
hepnicenames, providing a large set of pre-defined high energy
physics particle names built with the hepparticles package. The
packages are based on pennames.sty by Michel Goosens and Eric
van Herwijnen. Heppennames re-implements the particle names in
pennames.sty, with some additions and alterations and greater
flexibility and robustness due to the hepparticles structures,
which were written for this purpose. Hepnicenames provides the
main non-resonant particle names from heppennames with more
"friendly" names.

%package -n texlive-hepnames-doc
Summary:        Documentation for hepnames
Version:        svn35722.2.0

Provides:       tex-hepnames-doc
AutoReqProv:    No

%description -n texlive-hepnames-doc
Documentation for hepnames

%package -n texlive-hepparticles
Provides:       tex-hepparticles = %{tl_version}
License:        LPPL
Summary:        Macros for typesetting high energy physics particle names
Version:        svn35723.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(subdepth.sty), tex(amsmath.sty)
Provides:       tex(hepparticles.sty) = %{tl_version}

%description -n texlive-hepparticles
HEPparticles is a set of macros for typesetting high energy
particle names, to meet the following criteria: 1. The main
particle name is a Roman or Greek symbol, to be typeset in
upright font in normal contexts. 2. Additionally a superscript
and/or subscript may follow the main symbol. 3. Particle
resonances may also have a resonance specifier which is typeset
in parentheses following the main symbol. In general the
parentheses may also be followed by sub- and superscripts. 4.
The particle names are expected to be used both in and out of
mathematical contexts. 5. If the surrounding text is bold or
italic then the particle name should adapt to that context as
best as possible (this may not be possible for Greek symbols).
A consequence of point 5 is that the well-known problems with
boldness of particle names in section titles, headers and
tables of contents automatically disappear if these macros are
used.

%package -n texlive-hepparticles-doc
Summary:        Documentation for hepparticles
Version:        svn35723.2.0

Provides:       tex-hepparticles-doc
AutoReqProv:    No

%description -n texlive-hepparticles-doc
Documentation for hepparticles

%package -n texlive-hepthesis
Provides:       tex-hepthesis = %{tl_version}
License:        LPPL
Summary:        A class for academic reports, especially PhD theses
Version:        svn46054
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(a4wide.sty), tex(fontenc.sty), tex(etoolbox.sty), tex(microtype.sty)
Requires:       tex(changepage.sty), tex(varwidth.sty), tex(amsmath.sty), tex(makeidx.sty)
Requires:       tex(titling.sty), tex(booktabs.sty), tex(hep.sty), tex(lineno.sty)
Requires:       tex(draftcopy.sty), tex(setspace.sty), tex(fancyhdr.sty), tex(tocbibind.sty)
Requires:       tex(comment.sty), tex(rotating.sty), tex(caption.sty), tex(afterpage.sty)
Requires:       tex(csquotes.sty), tex(hyperref.sty)
Provides:       tex(hepthesis.cls) = %{tl_version}

%description -n texlive-hepthesis
Hepthesis is a LaTeX class for typesetting large academic
reports, in particular PhD theses. It was originally developed
for typesetting the author's high-energy physics PhD thesis and
includes some features specifically tailored to such an
application. In particular, hepthesis offers: Attractive
semantic environments for various rubric sections; Extensive
options for draft production, screen viewing and binding-ready
output; Helpful extensions of existing environments, including
equation and tabular; and Support for quotations at the start
of the thesis and each chapter. The class is based on scrbook,
from the KOMA-Script bundle.

%package -n texlive-hepthesis-doc
Summary:        Documentation for hepthesis
Version:        svn46054
Provides:       tex-hepthesis-doc
AutoReqProv:    No

%description -n texlive-hepthesis-doc
Documentation for hepthesis

%package -n texlive-hepunits
Provides:       tex-hepunits = %{tl_version}
License:        LPPL
Summary:        A set of units useful in high energy physics applications
Version:        svn15878.1.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(xspace.sty), tex(SIunits.sty)
Provides:       tex(hepunits.sty) = %{tl_version}

%description -n texlive-hepunits
Hepunits is a LaTeX package built on the SIunits package which
adds a collection of useful HEP units to the existing SIunits
set. These include the energy units \MeV, \GeV, \TeV and the
derived momentum and mass units \MeVoverc, \MeVovercsq and so
on.

%package -n texlive-hepunits-doc
Summary:        Documentation for hepunits
Version:        svn15878.1.1.1

Provides:       tex-hepunits-doc
AutoReqProv:    No

%description -n texlive-hepunits-doc
Documentation for hepunits

%package -n texlive-h2020proposal-doc
Provides:       tex-h2020proposal-doc = %{tl_version}
License:        GPLv3+
Summary:        doc files of h2020proposal
Version:        svn38428

AutoReqProv:    No

%description -n texlive-h2020proposal-doc
Documentation for h2020proposal

%package -n texlive-h2020proposal
Provides:       tex-h2020proposal = %{tl_version}
License:        GPLv3+
Summary:        LaTeX class and template for EU H2020 RIA proposal
Version:        svn38428

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(h2020proposal.cls) = %{tl_version}

%description -n texlive-h2020proposal
This package consists of a class file as well as FET and ICT
proposal templates for writing EU H2020 RIA proposals and
generating automatically the many cross-referenced tables that
are required.

%package -n texlive-hackthefootline
Summary:        Footline selection for LaTeX beamer's standard themes
Version:        svn46494
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(hackthefootline.sty) = %{tl_version}

%description -n texlive-hackthefootline
This package provides arbitrary footline selection for LaTeX
beamer's standard themes. It makes use of the following other
LaTeX packages: appendixnumberbeamer, calc, etoolbox, and
numprint.

%package -n texlive-halloweenmath
Summary:        Scary and creepy math symbols with AMS-LaTeX integration
Version:        svn44043
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(halloweenmath.sty) = %{tl_version}

%description -n texlive-halloweenmath
The package defines a handful of commands for typesetting
mathematical symbols of various kinds, ranging from 'large'
operators to extensible arrow-like relations and growing arrow-
like math accents that all draw from the classic Halloween-
related iconography (pumpkins, witches, ghosts, cats, and so
on) while being, at the same time, seamlessly integrated within
the rest of the mathematics produced by (AmS-)LaTeX.

%package -n texlive-hecthese
Summary:        A class for dissertations and theses at HEC Montreal
Version:        svn47473
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(hecthese.cls) = %{tl_version}

%description -n texlive-hecthese
This package provides the hecthese class, a class based on
memoir and compatible with LaTeX. Using this class,
postgraduate students at HEC Montreal will be able to write
their dissertation or thesis while complying with all the
presentation standards required by the University. This class
is meant to be as flexible as possible; in particular, there
are very few hardcoded features except those that take care of
the document's layout. Dissertations and theses at HEC Montreal
can be written on a per-chapter or per-article basis. Documents
that are written on a per-article basis require a bibliography
for each of the included articles and a general bibliography
for the entire document. The hecthese class takes care of these
requirements. The class depends on babel, color, enumitem,
fontawesome, framed, numprint, url, and hyperref.

%package -n texlive-hithesis
Summary:        Harbin Institute of Technology Thesis Template
Version:        svn46564
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ctex-fontset-siyuan.def) = %{tl_version}
Provides:       tex(hithesis.cfg) = %{tl_version}, tex(hithesis.cls) = %{tl_version}
Provides:       tex(hithesis.sty) = %{tl_version}

%description -n texlive-hithesis
hithesis is a LaTeX thesis template package for Harbin
Institute of Technolog supporting bachelor, master, doctor
dissertations.

%package -n texlive-hustthesis
Summary:        Unofficial thesis template for Huazhong University
Version:        svn42547
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(hustthesis.cls) = %{tl_version}

%description -n texlive-hustthesis
The package provides an Unofficial Thesis Template in LaTeX for
Huazhong University of Science and Technology.

%package -n texlive-hlist
Summary:        Horizontal and columned lists
Version:        svn44983
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(simplekv.sty)
Provides:       tex(hlist.sty) = %{tl_version}, tex(hlist.tex) = %{tl_version}

%description -n texlive-hlist
This plain TeX and LaTeX package provides the "hlist"
environment in which \hitem starts a horizontal and columned
item. It depends upon the simplekv package.

%package -n texlive-hagenberg-thesis
Summary:        A Collection of LaTeX classes, style files, and example documents for academic manuscripts
Version:        svn45629
License:        CC-BY
Requires:       texlive-base texlive-kpathsea
Provides:       tex(hgb.sty) = %{tl_version}, tex(hgbabbrev.sty) = %{tl_version}
Provides:       tex(hgbarticle.cls) = %{tl_version}, tex(hgbbib.sty) = %{tl_version}
Provides:       tex(hgbheadings.sty) = %{tl_version}, tex(hgblistings.sty) = %{tl_version}
Provides:       tex(hgbmath.sty) = %{tl_version}, tex(hgbreport.cls) = %{tl_version}
Provides:       tex(hgbthesis.cls) = %{tl_version}

%description -n texlive-hagenberg-thesis
This bundle contains a collection of modern LaTeX classes,
style files, and example documents for authoring Bachelor,
Master, or Diploma theses and related academic manuscripts in
English and German. Includes a comprehensive tutorial (in
German) with detailed instructions and authoring guidelines.

%package -n texlive-handin
Summary:        Light weight template for creating school submissions using LaTeX
Version:        svn48255
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(handin.sty) = %{tl_version}

%description -n texlive-handin
This package is for students creating school submissions using
LaTeX. It is especially suitable for math, physics, statistics
and the like. It can easily be used for creating exercises,
too.

%package -n texlive-harmony
Provides:       tex-harmony = %{tl_version}
License:        LPPL
Summary:        Typeset harmony symbols, etc., for musicology
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(amssymb.sty)
Provides:       tex(harmony.sty) = %{tl_version}

%description -n texlive-harmony
The package harmony.sty uses the packages ifthen and amssymb
from the amsfonts bundle, together with the LaTeX font
lcirclew10 and the font musix13 from musixtex.

%package -n texlive-harmony-doc
Summary:        Documentation for harmony
Version:        svn15878.0

Provides:       tex-harmony-doc
AutoReqProv:    No

%description -n texlive-harmony-doc
Documentation for harmony

%package -n texlive-hulipsum
Summary:        Hungarian dummy text (Lorum ipse)
Version:        svn46803
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(hulipsum.sty) = %{tl_version}

%description -n texlive-hulipsum
Lorem ipsum is an improper Latin filler dummy text, cf. the
lipsum package. It is commonly used for demonstrating the
textual elements of a document template. Lorum ipse is a
Hungarian variation of Lorem ipsum. (Lorum is a Hungarian card
game, and ipse is a Hungarian slang word meaning bloke.) With
this package you can typeset 150 paragraphs of Lorum ipse. All
paragraphs are taken with permission from
http://www.lorumipse.hu. Thanks to Lorum Ipse Lab (Viktor Nagy
and David Takacs) for their work.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/heuristica"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-harvard
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bib/harvard/
%{_texdir}/texmf-dist/bibtex/bst/harvard/
%{_texdir}/texmf-dist/tex/latex/harvard/

%files -n texlive-harvard-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/harvard/

%files -n texlive-harvmac
%{_texdir}/texmf-dist/tex/plain/harvmac/

%files -n texlive-harvmac-doc
%{_texdir}/texmf-dist/doc/plain/harvmac/

%files -n texlive-historische-zeitschrift
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/historische-zeitschrift/

%files -n texlive-historische-zeitschrift-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/historische-zeitschrift/

%files -n texlive-hook-pre-commit-pkg-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/support/hook-pre-commit-pkg/

%files -n texlive-hatching
%license pd.txt
%{_texdir}/texmf-dist/metapost/hatching/

%files -n texlive-hatching-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/metapost/hatching/

%files -n texlive-hacm
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/map/dvips/hacm/
%{_texdir}/texmf-dist/fonts/tfm/public/hacm/
%{_texdir}/texmf-dist/fonts/type1/public/hacm/
%{_texdir}/texmf-dist/fonts/vf/public/hacm/
%{_texdir}/texmf-dist/tex/latex/hacm/

%files -n texlive-hacm-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/hacm/

%files -n texlive-hands
%license pd.txt
%{_texdir}/texmf-dist/fonts/source/public/hands/
%{_texdir}/texmf-dist/fonts/tfm/public/hands/

%files -n texlive-heuristica
%license ofl.txt
%{_datadir}/fonts/heuristica
%{_texdir}/texmf-dist/fonts/enc/dvips/heuristica/
%{_texdir}/texmf-dist/fonts/map/dvips/heuristica/
%{_texdir}/texmf-dist/fonts/opentype/public/heuristica/
%{_texdir}/texmf-dist/fonts/tfm/public/heuristica/
%{_texdir}/texmf-dist/fonts/type1/public/heuristica/
%{_texdir}/texmf-dist/fonts/vf/public/heuristica/
%{_texdir}/texmf-dist/tex/latex/heuristica/

%files -n texlive-heuristica-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/heuristica/

%files -n texlive-hfbright
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/hfbright/
%{_texdir}/texmf-dist/fonts/enc/dvips/hfbright/
%{_texdir}/texmf-dist/fonts/map/dvips/hfbright/
%{_texdir}/texmf-dist/fonts/type1/public/hfbright/

%files -n texlive-hfbright-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/hfbright/

%files -n texlive-hfoldsty
%license gpl.txt
%{_texdir}/texmf-dist/fonts/tfm/public/hfoldsty/
%{_texdir}/texmf-dist/fonts/vf/public/hfoldsty/
%{_texdir}/texmf-dist/tex/latex/hfoldsty/

%files -n texlive-hfoldsty-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/hfoldsty/

%files -n texlive-helvetic
%license gpl.txt
%{_texdir}/texmf-dist/dvips/helvetic/
%{_texdir}/texmf-dist/fonts/afm/adobe/helvetic/
%{_texdir}/texmf-dist/fonts/afm/urw/helvetic/
%{_texdir}/texmf-dist/fonts/map/dvips/helvetic/
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/
%{_texdir}/texmf-dist/fonts/vf/monotype/helvetic/
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/
%{_texdir}/texmf-dist/tex/latex/helvetic/

%files -n texlive-hanoi
%license pd.txt
%{_texdir}/texmf-dist/tex/plain/hanoi/

%files -n texlive-havannah
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/havannah/

%files -n texlive-havannah-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/havannah/

%files -n texlive-hexgame
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hexgame/

%files -n texlive-hexgame-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hexgame/

%files -n texlive-horoscop
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/horoscop/

%files -n texlive-horoscop-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/horoscop/


%files -n texlive-happy4th-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/plain/happy4th/

%files -n texlive-hrlatex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hrlatex/

%files -n texlive-hrlatex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hrlatex/

%files -n texlive-hausarbeit-jura
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/hausarbeit-jura/

%files -n texlive-hausarbeit-jura-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/hausarbeit-jura/

%files -n texlive-harveyballs
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/harveyballs/

%files -n texlive-harveyballs-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/harveyballs/

%files -n texlive-here
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/here/

%files -n texlive-here-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/here/

%files -n texlive-hf-tikz
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/hf-tikz/

%files -n texlive-hf-tikz-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/hf-tikz/

%files -n texlive-hobby
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/hobby/

%files -n texlive-hobby-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/hobby/

%files -n texlive-hvfloat
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hvfloat/

%files -n texlive-hvfloat-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hvfloat/

%files -n texlive-handout
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/handout/

%files -n texlive-handout-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/handout/

%files -n texlive-hang
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/hang/

%files -n texlive-hang-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/hang/

%files -n texlive-hanging
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/hanging/

%files -n texlive-hanging-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/hanging/

%files -n texlive-hardwrap
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/hardwrap/

%files -n texlive-hardwrap-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/hardwrap/

%files -n texlive-harnon-cv
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/harnon-cv/

%files -n texlive-harnon-cv-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/harnon-cv/

%files -n texlive-harpoon
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/harpoon/

%files -n texlive-harpoon-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/harpoon/

%files -n texlive-hc
%{_texdir}/texmf-dist/bibtex/bst/hc/
%{_texdir}/texmf-dist/tex/latex/hc/

%files -n texlive-hc-doc
%{_texdir}/texmf-dist/doc/latex/hc/

%files -n texlive-he-she
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/he-she/

%files -n texlive-he-she-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/he-she/

%files -n texlive-hhtensor
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hhtensor/

%files -n texlive-hhtensor-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hhtensor/

%files -n texlive-histogr
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/histogr/

%files -n texlive-histogr-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/histogr/

%files -n texlive-hitec
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hitec/

%files -n texlive-hitec-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hitec/

%files -n texlive-hletter
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/hletter/

%files -n texlive-hletter-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/hletter/

%files -n texlive-hpsdiss
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/hpsdiss/

%files -n texlive-hpsdiss-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/hpsdiss/

%files -n texlive-hrefhide
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/hrefhide/

%files -n texlive-hrefhide-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/hrefhide/

%files -n texlive-hvindex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hvindex/

%files -n texlive-hvindex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hvindex/

%files -n texlive-harmony
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/harmony/

%files -n texlive-harmony-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/harmony/

%files -n texlive-har2nat
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/har2nat/

%files -n texlive-har2nat-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/har2nat/

%files -n texlive-hobete
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hobete/

%files -n texlive-hobete-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hobete/

%files -n texlive-hep
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hep/

%files -n texlive-hep-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hep/

%files -n texlive-hepnames
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hepnames/

%files -n texlive-hepnames-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hepnames/

%files -n texlive-hepparticles
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hepparticles/

%files -n texlive-hepparticles-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hepparticles/

%files -n texlive-hepthesis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hepthesis/

%files -n texlive-hepthesis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hepthesis/

%files -n texlive-hepunits
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/hepunits/

%files -n texlive-hepunits-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/hepunits/

%files -n texlive-h2020proposal-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/h2020proposal/

%files -n texlive-h2020proposal
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/h2020proposal/

%files -n texlive-hackthefootline
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/hackthefootline/
%{_texdir}/texmf-dist/tex/latex/hackthefootline/

%files -n texlive-halloweenmath
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/halloweenmath/
%{_texdir}/texmf-dist/tex/latex/halloweenmath/

%files -n texlive-hecthese
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/hecthese/
%{_texdir}/texmf-dist/tex/latex/hecthese/

%files -n texlive-hithesis
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/hithesis/
%{_texdir}/texmf-dist/bibtex/bst/hithesis/
%{_texdir}/texmf-dist/makeindex/hithesis/
%{_texdir}/texmf-dist/tex/latex/hithesis/

%files -n texlive-hustthesis
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/hustthesis/
%{_texdir}/texmf-dist/bibtex/bst/hustthesis/
%{_texdir}/texmf-dist/tex/latex/hustthesis/

%files -n texlive-hlist
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/generic/hlist/
%{_texdir}/texmf-dist/tex/generic/hlist/

%files -n texlive-hagenberg-thesis
%{_texdir}/texmf-dist/tex/latex/hagenberg-thesis/
%doc %{_texdir}/texmf-dist/doc/latex/hagenberg-thesis/

%files -n texlive-handin
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/handin/
%doc %{_texdir}/texmf-dist/doc/latex/handin/

%files -n texlive-hulipsum
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/hulipsum/
%doc %{_texdir}/texmf-dist/doc/latex/hulipsum/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
