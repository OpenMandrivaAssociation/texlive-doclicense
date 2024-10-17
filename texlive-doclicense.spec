Name:		texlive-doclicense
Version:	68441
Release:	1
Summary:	Support for putting documents under a license
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/doclicense
License:	cc0 lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doclicense.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doclicense.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doclicense.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to put your document under a license
and include a link to read about the license or include an icon
or image of the license. Currently, only Creative Commons is
supported, but this package is designed to handle all kinds of
licenses.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/doclicense
%{_texmfdistdir}/tex/latex/doclicense
%doc %{_texmfdistdir}/doc/latex/doclicense

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
