%global tl_name doclicense
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.3.0
Release:	%{tl_revision}.1
Summary:	Support for putting documents under a license
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/doclicense
License:	cc0 lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/doclicense.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/doclicense.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/doclicense.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to put your document under a license and include
a link to read about the license or include an icon or image of the
license. Currently, only Creative Commons is supported, but this package
is designed to handle all kinds of licenses.

