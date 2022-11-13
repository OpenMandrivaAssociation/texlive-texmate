Name:		texlive-texmate
Version:	15878
Release:	1
Summary:	Comprehensive chess annotation in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texmate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texmate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texmate.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texmate.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXmate formats chess games from very simple ascii input. The
clean "1. e4 e5; 2. Nf3 Nc6; 3. Bb5 a6" will produce the same
results as the sloppier "1 e4 e5; Nf3 Nc6 3.. Bb5 a6". The
resulting format is fully customizable. There are 4 levels of
commentary: 1 is the main game, 2-3 are commentaries. Each has
its fonts, punctuation marks, etc., and these are also
customizable. The package includes a tool for the creation of
diagrams. The package works in conjunction with skak to produce
diagrams of the current position automatically. For chess
fonts, the package uses the chessfss system.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/texmate/texmate.sty
%doc %{_texmfdistdir}/doc/latex/texmate/README
%doc %{_texmfdistdir}/doc/latex/texmate/texmate2manual.pdf
%doc %{_texmfdistdir}/doc/latex/texmate/texmate2manual.tex
#- source
%doc %{_texmfdistdir}/source/latex/texmate/texmate.dtx
%doc %{_texmfdistdir}/source/latex/texmate/texmate.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
