# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           speexdsp
Version:        1.2.1
Release:        %autorelease
Summary:        A patent-free, Open Source/Free Software DSP library
License:        BSD-3-Clause
URL:            http://www.speex.org/
VCS:            git:https://gitlab.xiph.org/xiph/speexdsp.git
#!RemoteAsset
Source0:        https://downloads.xiph.org/releases/speex/speexdsp-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-neon
BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gdb

%description
Speex is a patent-free audio codec designed especially for voice (unlike
Vorbis which targets general audio) signals and providing good narrowband
and wideband quality. This project aims to be complementary to the Vorbis
codec.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%files
%license COPYING
%doc AUTHORS TODO ChangeLog README NEWS doc/manual.pdf
%dir %{_docdir}/speexdsp
%{_libdir}/libspeexdsp.so.*

%files devel
%{_includedir}/speex/
%{_libdir}/pkgconfig/speexdsp.pc
%{_libdir}/libspeexdsp.so

%changelog
%{?autochangelog}
