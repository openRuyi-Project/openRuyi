# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tre
Version:        0.9.0
Release:        %autorelease
Summary:        POSIX-compatible regexp library with approximate matching
License:        BSD-3-Clause
URL:            https://laurikari.net/tre/
VCS:            git:https://github.com/laurikari/tre
#!RemoteAsset:  sha256:f57f5698cafdfe516d11fb0b71705916fe1162f14b08cf69d7cf86923b5a2477
Source:         https://github.com/laurikari/tre/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-shared

# Tests require locale en_US.ISO-8859-1.
BuildRequires:  glibc-locale

%description
TRE is a POSIX-compatible regexp matching library with approximate
(fuzzy) matching. This package contains the runtime library and the
agrep utility.

%package        devel
Summary:        Development files for the TRE regex library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config files, and documentation
needed to develop applications that use the TRE library.

%install -a
%find_lang %{name} --generate-subpackages

%files
%license LICENSE
%{_bindir}/agrep
%{_mandir}/man1/agrep.1*
%{_libdir}/libtre.so.5
%{_libdir}/libtre.so.5.*

%files devel
%doc doc/default.css doc/tre-api.html doc/tre-syntax.html
%{_includedir}/*
%{_libdir}/libtre.so
%{_libdir}/pkgconfig/tre.pc

%changelog
%autochangelog
