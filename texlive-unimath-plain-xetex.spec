Name:		texlive-unimath-plain-xetex
Version:	64951
Release:	1
Summary:	OpenType math support in (plain) XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unimath-plain-xetex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unimath-plain-xetex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unimath-plain-xetex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides OpenType math font support in plain TeX
format. It only works with the XeTeX engine.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xetex/unimath-plain-xetex
%doc %{_texmfdistdir}/doc/xetex/unimath-plain-xetex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
