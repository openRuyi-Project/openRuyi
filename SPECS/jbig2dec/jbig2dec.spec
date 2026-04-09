# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jbig2dec
Version:        0.20
Release:        %autorelease
Summary:        A decoder implementation of the JBIG2 image compression format
License:        AGPL-3.0-or-later
URL:            https://jbig2dec.com
VCS:            git:https://github.com/ArtifexSoftware/jbig2dec/
#!RemoteAsset
Source0:        https://github.com/ArtifexSoftware/jbig2dec/releases/download/%{version}/jbig2dec-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  libtool
BuildRequires:  pkgconfig(libpng)
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
# for tests.
BuildRequires:  python

%description
jbig2dec is a decoder implementation of the JBIG2 image compression format.
This package contains the command-line tool.

%package        devel
Summary:        Development files for jbig2dec
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for jbig2dec.

%conf -p
autoreconf -fiv

%files
%doc CHANGES COPYING LICENSE README
%{_bindir}/jbig2dec
%{_mandir}/man1/jbig2dec.1*
%{_libdir}/libjbig2dec.so.0*

%files devel
%doc CHANGES COPYING LICENSE README
%{_includedir}/jbig2.h
%{_libdir}/libjbig2dec.so
%{_libdir}/pkgconfig/jbig2dec.pc

%changelog
%autochangelog
