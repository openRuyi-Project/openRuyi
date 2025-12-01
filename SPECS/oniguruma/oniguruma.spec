# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           oniguruma
Version:        6.9.10
Release:        %autorelease
Summary:        Regular expressions library
License:        BSD-2-Clause
URL:            https://github.com/kkos/oniguruma/
#!RemoteAsset
Source0:    https://github.com/kkos/oniguruma/releases/download/v%{version}/onig-%{version}.tar.gz

BuildSystem:    autotools

BuildOption(conf): --disable-silent-rules
BuildOption(conf): --disable-static

BuildRequires:      gcc
# autoreconf needs these
BuildRequires:  autoconf automake libtool

%description
Oniguruma is a regular expressions library that supports various character
encodings for each regular expression object.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
This package contains the header files, documentation, and other development
files for the oniguruma library.


%prep -a
%{__sed} -i.multilib -e 's|-L@libdir@||' onig-config.in

%conf -p
autoreconf -fiv

%install -a
find %{buildroot} -type f \( -name "*.la" -o -name "*.a" \) -delete -print

%files
%doc        AUTHORS
%license    COPYING
%lang(ja)   %doc    README_japanese index_ja.html
%{_libdir}/libonig.so.5*

%files          devel
%lang(ja)   %doc    doc/*.ja
%doc HISTORY README.md index.html doc/API doc/CALLOUTS.API doc/CALLOUTS.BUILTIN doc/FAQ doc/RE
%{_bindir}/onig-config
%{_includedir}/onig*.h
%{_libdir}/libonig.so
%{_libdir}/pkgconfig/oniguruma.pc

%changelog
%{?autochangelog}
