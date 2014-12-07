# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/texmate
# catalog-date 2006-09-21 21:05:13 +0200
# catalog-license lppl
# catalog-version 2
Name:		texlive-texmate
Version:	2
Release:	9
Summary:	Comprehensive chess annotation in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texmate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texmate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texmate.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texmate.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2-2
+ Revision: 756742
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2-1
+ Revision: 719707
- texlive-texmate
- texlive-texmate
- texlive-texmate

