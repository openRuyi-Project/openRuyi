# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           audiofile
Version:        0.3.6
Release:        %autorelease
Summary:        Library for accessing various audio file formats
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://github.com/mpruett/audiofile/
#!RemoteAsset
Source:         http://audiofile.68k.org/audiofile-%{version}.tar.gz
BuildSystem:    autotools

# fix CVE-2015-7747
Patch0:         0001-audiofile-0.3.6-CVE-2015-7747.patch
# Fixes integer underflow for signed minimum values.
Patch1:         0002-audiofile-0.3.6-left-shift-neg.patch
# Patch changes test data arrays from char to signed char and corrects numeric literals for clarity.
Patch2:         0003-audiofile-0.3.6-narrowing.patch
# Patch adds overflow checks and safety handling to prevent crashes and invalid memory use.
Patch3:         0004-audiofile-0.3.6-pull42.patch
# Patch clamps ADPCM index values to valid range to prevent out-of-bounds errors.
Patch4:         0005-audiofile-0.3.6-pull43.patch
# Patch adds safety checks to prevent division by zero and unsupported codec configurations.
Patch5:         0006-audiofile-0.3.6-pull44.patch
Patch6:         0007-822b732fd31ffcb78f6920001e9b1fbd815fa712.patch
# Patch sets output chunk frame count to 0 on short reads to prevent invalid data processing.
Patch7:         0008-941774c8c0e79007196d7f1e7afdc97689f869b3.patch
# Patch prevents NULL dereference by checking module initialization failure.
Patch8:         0009-fde6d79fb8363c4a329a184ef0b107156602b225.patch
# ensures proper type conversion for unsigned array initialization.
Patch9:         0010-integer-overflow.patch
# fix CVE-2022-24599
Patch10:        0011-audiofile-0.3.6-CVE-2022-24599.patch

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --enable-static

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(alsa-topology)
BuildRequires:  pkgconfig(flac)
BuildRequires:  make

%description
The Audio File library is an implementation of the Audio File Library
from SGI, which provides an API for accessing audio file formats like
AIFF/AIFF-C, WAVE, and NeXT/Sun .snd/.au files.

%package        devel
Summary:        Development files for Audio File applications
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The audiofile-devel package contains libraries, include files, and
other resources you can use to develop Audio File applications.

%install -a
# build for tests only.
rm -f %{buildroot}%{_libdir}/*.a

%files
%license COPYING COPYING.GPL
%doc ACKNOWLEDGEMENTS AUTHORS NEWS NOTES README TODO
%{_bindir}/sfconvert
%{_bindir}/sfinfo
%{_libdir}/libaudiofile.so.1*
%{_mandir}/man1/*

%files devel
%doc ChangeLog docs/*.3.txt
%{_libdir}/libaudiofile.so
%{_libdir}/pkgconfig/audiofile.pc
%{_includedir}/*
%{_mandir}/man3/*

%changelog
%autochangelog
