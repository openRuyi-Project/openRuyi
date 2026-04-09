# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           opus
Version:        1.5.2
Release:        %autorelease
Summary:        An audio codec for use in low-delay speech and audio communication
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://www.opus-codec.org/
VCS:            git:https://github.com/xiph/opus
#!RemoteAsset
Source0:        https://ftp.osuosl.org/pub/xiph/releases/opus/opus-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-custom-modes
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-hardening

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake

%description
The Opus codec is designed for interactive speech and audio transmission over
the Internet. It is designed by the IETF Codec Working Group and incorporates
technology from Skype's SILK codec and Xiph.Org's CELT codec.

%package        devel
Summary:        Development package for opus
Requires:       pkgconfig(ogg)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files for development with opus.

%conf -p
autoreconf -ivf

%files
%license COPYING
%{_libdir}/libopus.so.0*
%{_datadir}/doc/opus

%files devel
%doc README doc/html
%{_includedir}/opus
%{_libdir}/libopus.so
%{_libdir}/pkgconfig/opus.pc
%{_datadir}/aclocal/opus.m4
%{_mandir}/man3/opus_*.3*

%changelog
%autochangelog
