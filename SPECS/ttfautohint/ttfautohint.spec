# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ttfautohint
Version:        1.8.4
Release:        %autorelease
Summary:        Automated hinting utility for TrueType fonts
License:        FTL OR GPL-2.0-only
URL:            http://www.freetype.org/ttfautohint
VCS:            git:https://repo.or.cz/ttfautohint.git
#!RemoteAsset:  sha256:8a876117fa6ebfd2ffe1b3682a9a98c802c0f47189f57d3db4b99774206832e1
Source0:        http://download.savannah.gnu.org/releases/freetype/ttfautohint-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --without-doc
BuildOption(conf):  --without-qt

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)

%description
This is a utility which takes a TrueType font as the input, removes its
bytecode instructions (if any), and returns a new font where all glyphs
are bytecode hinted using the information given by FreeType's autohinting
module.

%package        devel
Summary:        Development files for %{name}-libs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for libttfautohint.

%prep -a
echo %{version} > VERSION

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc AUTHORS NEWS README THANKS TODO *.TXT
%doc doc/img
%doc doc/ttfautohint.{html,pdf,txt}
%{_bindir}/ttfautohint
%{_libdir}/libttfautohint.so.*

%files devel
%license COPYING
%{_includedir}/ttfautohint*.h
%{_libdir}/libttfautohint.so
%{_libdir}/pkgconfig/ttfautohint.pc

%changelog
%{?autochangelog}
