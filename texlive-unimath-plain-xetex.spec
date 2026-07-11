%global tl_name unimath-plain-xetex
%global tl_revision 72498

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2c
Release:	%{tl_revision}.1
Summary:	OpenType math support in (plain) XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/plain/unimath-plain-xetex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unimath-plain-xetex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unimath-plain-xetex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides OpenType math font support in plain TeX format. It
only works with the XeTeX engine.

