%global tl_name texmate
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2
Release:	%{tl_revision}.1
Summary:	Comprehensive chess annotation in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/texmate
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texmate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texmate.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texmate.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeXmate formats chess games from very simple ascii input. The clean "1.
e4 e5; 2. Nf3 Nc6; 3. Bb5 a6" will produce the same results as the
sloppier "1 e4 e5; Nf3 Nc6 3.. Bb5 a6". The resulting format is fully
customizable. There are 4 levels of commentary: 1 is the main game, 2-3
are commentaries. Each has its fonts, punctuation marks, etc., and these
are also customizable. The package includes a tool for the creation of
diagrams. The package works in conjunction with skak to produce diagrams
of the current position automatically. For chess fonts, the package uses
the chessfss system.

