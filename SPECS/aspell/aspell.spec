# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           aspell
Version:        0.60.8.2
Release:        %autorelease
Summary:        Spell checker
License:        LGPL-2.0-or-later AND LGPL-2.1-only AND GPL-2.0-or-later AND BSD-2-Clause
URL:            https://github.com/GNUAspell/aspell
#!RemoteAsset:  sha256:57fe4863eae6048f72245a8575b44b718fb85ca14b9f8c0afc41b254dfd76919
Source:         https://ftpmirror.gnu.org/aspell/aspell-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-curses="-lncursesw"
BuildOption(conf):  --disable-rpath

# just for fix compile error.
# two patches is from opensuse.
Patch0:         0001-aspell-strict-aliasing.patch
Patch1:         0002-aspell-quotes.patch

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig
BuildRequires:  perl
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf

%description
GNU Aspell is a spell checker designed to eventually replace Ispell. It can
either be used as a library or as an independent spell checker. Its main
feature is that it does a much better job of coming up with possible
suggestions than just about any other spell checker out there for the
English language, including Ispell and Microsoft Word. It also has many
other technical enhancements over Ispell such as using shared memory for
dictionaries and intelligently handling personal dictionaries when more
than one Aspell process is open at once.

%package        devel
Summary:        Libraries and header files for Aspell development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The aspell-devel package includes libraries
and header files needed for Aspell development.

%conf -p
autoreconf -fiv
export CXXFLAGS="%{optflags} `ncursesw6-config --cflags`"
export LDFLAGS="`ncursesw6-config --libs`"

%install -a
ln -s ../%{_libdir}/aspell-0.60/ispell %{buildroot}%{_bindir}/ispell
ln -s ../%{_libdir}/aspell-0.60/spell %{buildroot}%{_bindir}/spell
# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc README TODO COPYING
%dir %{_libdir}/aspell-0.60
%{_bindir}/a*
%{_bindir}/ispell
%{_bindir}/pr*
%{_bindir}/run-with-aspell
%{_bindir}/spell
%{_bindir}/word-list-compress
%{_libdir}/lib*.so.*
%{_libdir}/aspell-0.60/*
%{_infodir}/aspell.*
%{_mandir}/man1/aspell.1.*
%{_mandir}/man1/run-with-aspell.1*
%{_mandir}/man1/word-list-compress.1*
%{_mandir}/man1/prezip-bin.1.*
%{_mandir}/man1/aspell-import.1.gz
%{_mandir}/man1/pspell-config.1*

%files devel
%dir %{_includedir}/pspell
%{_bindir}/pspell-config
%{_includedir}/aspell.h
%{_includedir}/pspell/pspell.h
%{_libdir}/lib*spell.so
%{_infodir}/aspell-dev.*

%changelog
%autochangelog
