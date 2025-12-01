# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# avoid bootstrapping problem
%bcond static 0
Name:           xz
Version:        5.8.1
Release:        %autorelease
Summary:        A Program for Compressing Files with the Lempel–Ziv–Markov algorithm
License:        0BSD AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://tukaani.org/xz/
#!RemoteAsset
Source0:        https://github.com/tukaani-project/xz/releases/download/v%{version}/xz-%{version}.tar.xz
#!RemoteAsset
Source1:        https://github.com/tukaani-project/xz/releases/download/v%{version}/xz-%{version}.tar.xz.sig
#!RemoteAsset
Source3:        https://tukaani.org/misc/lasse_collin_pubkey.txt#/xz.keyring
Source4:        xznew
Source5:        xznew.1
BuildRequires:  pkgconfig
Provides:       lzma = %{version}
Obsoletes:      lzma < %{version}

BuildSystem:    autotools
BuildOption(conf): --with-pic
BuildOption(conf): --docdir=%{_docdir}/%{name}
%if %{with static}
BuildOption(conf): --disable-shared
%else
BuildOption(conf): --disable-static
%endif
%description
The xz command is a program for compressing files.
* Average compression ratio of LZMA is about 30%% better than that of
  gzip, and 15%% better than that of bzip2.
* Decompression speed is only little slower than that of gzip, being
  two to five times faster than bzip2.
* In fast mode, compresses faster than bzip2 with a comparable
  compression ratio.
* Achieving the best compression ratios takes four to even twelve
  times longer than with bzip2. However, this does not affect
  decompressing speed.
* Very similar command line interface to what gzip and bzip2 have.

%package devel
Summary:        Development package for the LZMA library
License:        0BSD
Requires:       %{name} = %{version}
Provides:       lzma-devel = %{version}
Obsoletes:      lzma-devel < %{version}
Provides:       lzma-alpha-devel = %{version}
Obsoletes:      lzma-alpha-devel < %{version}

%description devel
This package contains the header files and libraries needed for
compiling programs using the LZMA library.

%if %{with static}
%package static
Summary:        Static version of LZMA library
License:        Public-Domain
Requires:       xz-devel = %{version}

%description static
Static library for the LZMA library
%endif

%build
export CFLAGS="%{optflags} -D_REENTRANT -pipe -fPIE"
export LDFLAGS="-Wl,-z,relro,-z,now -pie"
%make_build

%if %{with static}
cp ./src/liblzma/.libs/liblzma.a liblzma.a
%endif

%install -a
install -Dpm 0755 %{SOURCE4} %{buildroot}%{_bindir}/xznew
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_mandir}/man1/xznew.1
%if %{with static}
install -Dpm 0644 liblzma.a %{buildroot}%{_libdir}/
%endif
rm -vf %{buildroot}%{_docdir}/%{name}/{COPYING,COPYING.GPLv2}
%find_lang %{name} --all-name --with-man --generate-subpackages

%files
%license COPYING COPYING.GPLv2
%{_docdir}/%{name}
%{_bindir}/lzcat
%{_bindir}/lzcmp
%{_bindir}/lzdiff
%{_bindir}/lzegrep
%{_bindir}/lzfgrep
%{_bindir}/lzgrep
%{_bindir}/lzless
%{_bindir}/lzma
%{_bindir}/lzmadec
%{_bindir}/lzmainfo
%{_bindir}/lzmore
%{_bindir}/unlzma
%{_bindir}/unxz
%{_bindir}/xz
%{_bindir}/xzcat
%{_bindir}/xzcmp
%{_bindir}/xzdec
%{_bindir}/xzdiff
%{_bindir}/xzegrep
%{_bindir}/xzfgrep
%{_bindir}/xzgrep
%{_bindir}/xzless
%{_bindir}/xzmore
%{_bindir}/xznew
%{_mandir}/man1/lzcat.1*
%{_mandir}/man1/lzcmp.1*
%{_mandir}/man1/lzdiff.1*
%{_mandir}/man1/lzegrep.1*
%{_mandir}/man1/lzfgrep.1*
%{_mandir}/man1/lzgrep.1*
%{_mandir}/man1/lzless.1*
%{_mandir}/man1/lzma.1*
%{_mandir}/man1/lzmadec.1*
%{_mandir}/man1/lzmainfo.1*
%{_mandir}/man1/lzmore.1*
%{_mandir}/man1/unlzma.1*
%{_mandir}/man1/unxz.1*
%{_mandir}/man1/xz.1*
%{_mandir}/man1/xzcat.1*
%{_mandir}/man1/xzcmp.1*
%{_mandir}/man1/xzdec.1*
%{_mandir}/man1/xzdiff.1*
%{_mandir}/man1/xzegrep.1*
%{_mandir}/man1/xzfgrep.1*
%{_mandir}/man1/xzgrep.1*
%{_mandir}/man1/xzless.1*
%{_mandir}/man1/xzmore.1*
%{_mandir}/man1/xznew.1*
%{_libdir}/liblzma.so.5*

%files devel
%license COPYING COPYING.GPLv2
%{_includedir}/lzma.h
%dir %{_includedir}/lzma/
%{_includedir}/lzma/*
%{_libdir}/liblzma.so
%{_libdir}/pkgconfig/liblzma.pc

%if %{with static}
%files static
%license COPYING COPYING.GPLv2
%{_libdir}/liblzma.a
%endif

%changelog
%{?autochangelog}
