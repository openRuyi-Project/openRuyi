# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           twolame
Version:        0.4.0
Release:        %autorelease
Summary:        Optimized MPEG Audio Layer 2 encoding library
License:        LGPL-2.1-or-later
URL:            https://github.com/njh/twolame
#!RemoteAsset
Source:         http://downloads.sourceforge.net/twolame/twolame-%{version}.tar.gz
BuildSystem:    autotools

# the patch needs to change from .. to .
Patch0:         0001-fix-test-path-error.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-sndfile

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig(sndfile)

%description
TwoLAME is an optimized MPEG Audio Layer 2 (MP2) encoder. It serves as a
drop-in replacement for LAME (MP3 encoder) with a similar frontend and API.
This package contains the command line frontend.

%package        devel
Summary:        Development tools for TwoLAME applications
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and documentation needed to develop
applications with TwoLAME.

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc ChangeLog
%{_bindir}/twolame
%{_mandir}/man1/twolame.1*
%{_libdir}/libtwolame.so.*

%files devel
%{_docdir}/twolame
%{_libdir}/pkgconfig/twolame.pc
%{_libdir}/libtwolame.so
%{_includedir}/twolame.h

%changelog
%autochangelog
