# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsndfile
Version:        1.2.2
Release:        %autorelease
Summary:        Library for reading and writing sound files
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
URL:            https://github.com/libsndfile/libsndfile
#!RemoteAsset
Source0:        https://github.com/libsndfile/libsndfile/releases/download/%{version}/libsndfile-%{version}.tar.xz
BuildSystem:    autotools

# Replace custom bool with stdbool.h
Patch0:         0001-libsndfile-1.2.2-stdbool.patch

BuildOption(conf):  --disable-dependency-tracking
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-sqlite
BuildOption(conf):  --enable-alsa
BuildOption(conf):  --enable-largefile
BuildOption(conf):  --enable-mpeg

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  pkgconfig(opus)
BuildRequires:  lame-devel

%description
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface.

%package        devel
Summary:        Development files for libsndfile
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Development files for libsndfile.

%conf -p
autoreconf -fiv

%check
LD_LIBRARY_PATH=$PWD/src/.libs make check

%files
%license COPYING
%doc AUTHORS README
%{_libdir}/libsndfile.so.1*
%{_bindir}/sndfile-*
%{_mandir}/man1/sndfile-*.1*

%files devel
%doc ChangeLog
%doc %{_docdir}/libsndfile
%{_includedir}/sndfile.h
%{_includedir}/sndfile.hh
%{_libdir}/libsndfile.so
%{_libdir}/pkgconfig/sndfile.pc

%changelog
%autochangelog
