# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           hunspell
Version:        1.7.3
Release:        %autorelease
Summary:        A spell checker and morphological analyzer library
License:        LGPL-2.1-or-later
URL:            https://github.com/hunspell/hunspell
#!RemoteAsset:  sha256:433274dac0619cb00c2e18b43a3dd3a9d50da5b5613fa9b5c21781e35dd76bc1
Source0:        %{url}/releases/download/v%{version}/hunspell-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --enable-nls
BuildOption(conf):  --with-ui
BuildOption(conf):  --with-readline

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  bison
BuildRequires:  libstdc++-devel
BuildRequires:  gettext-devel
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)

%description
Hunspell is a spell checker and morphological analyzer library and
program designed for languages with rich morphology and complex word
compounding or character encoding. Hunspell interfaces: Ispell-like
terminal interface using Curses library, Ispell pipe interface,
LibreOffice or OpenOffice.org UNO module.

%package        devel
Requires:       hunspell%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Summary:        Files for developing with hunspell

%description    devel
Includes and definitions for developing with hunspell.

%conf -p
autoreconf -fiv

%install -a
rm -f %{buildroot}%{_bindir}/example
%find_lang %{name} --generate-subpackages

%files
%license COPYING license.hunspell license.myspell
%doc README AUTHORS THANKS
%attr(755,root,root) %{_bindir}/hunspell
%{_bindir}/analyze
%{_bindir}/chmorph
%{_bindir}/munch
%{_bindir}/unmunch
%{_bindir}/hunzip
%{_bindir}/hzip
%{_bindir}/affixcompress
%{_bindir}/ispellaff2myspell
%{_bindir}/makealias
%{_bindir}/wordforms
%{_bindir}/wordlist2hunspell
%{_libdir}/libhunspell-*.so.*
%dir %{_mandir}/hu
%dir %{_mandir}/hu/man1
%{_mandir}/man1/hunspell.1*
%{_mandir}/man1/hunzip.1.*
%{_mandir}/man1/hzip.1*
%lang(hu) %{_mandir}/hu/man1/hunspell.1*

%files devel
%{_libdir}/libhunspell-*.so
#{_libdir}/libhunspell.so
%{_mandir}/man3/hunspell.3*
%{_mandir}/man5/hunspell.5*
%{_includedir}/hunspell
%{_libdir}/pkgconfig/hunspell.pc

%changelog
%autochangelog
