# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           icu4c
Version:        79.1
Release:        %autorelease
Summary:        International Components for Unicode
License:        Unicode-3.0
URL:            https://icu.unicode.org/
VCS:            git:https://github.com/unicode-org/icu
#!RemoteAsset:  sha256:06fa63ecb521048f8082f12ad988f6b678d90cbd88aafce24cbc94902b191d99
Source0:        https://github.com/unicode-org/icu/releases/download/release-%{version}/%{name}-%{version}-sources.tgz
#!RemoteAsset:  sha256:1939663d6a0a4a6523c69ea655438bd3fbce3186358279d4717d4c06fe697182
Source1:        https://github.com/unicode-org/icu/releases/download/release-%{version}/%{name}-%{version}-docs.zip
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-samples
BuildOption(build):  -C source
BuildOption(install):  -C source
BuildOption(check):  -C source

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(python3)
BuildRequires:  unzip

Provides:       bundled(tzdata) = 2026e
Provides:       icu

Requires:       tzdata

%patchlist
# Honor DESTDIR for unpacked ICU data; https://api.opensuse.org/public/source/openSUSE:Factory/icu/icu-fix-install-mode-files.diff?rev=95.
2000-icu-fix-install-mode-files.patch
# Include errno details in ICU data-tool errors; https://api.opensuse.org/public/source/openSUSE:Factory/icu/icu-error-reporting.diff?rev=95.
2001-icu-error-reporting.patch
# Avoid excess x87 precision in tests; https://api.opensuse.org/public/source/openSUSE:Factory/icu/icu-avoid-x87-excess-precision.diff?rev=95.
2002-icu-avoid-x87-excess-precision.patch
# Honor empty POSIX locale variables; https://api.opensuse.org/public/source/openSUSE:Factory/icu/locale.diff?rev=95.
2003-locale.patch
# Avoid non-finite integer conversion; https://github.com/unicode-org/icu/commit/29f1188d191a7a75ac7ffa4bfa390f625da39c53.
2004-nan-undefined-conversion.patch

%description
ICU is a set of C and C++ libraries that provide extensive Unicode and locale
support. This package contains the runtime libraries, data files, and command-line
tools for ICU.

%package        devel
Summary:        Development files for the ICU library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the headers, symbolic links, and other files needed to
develop applications that use the ICU libraries.

%package        doc
Summary:        API documentation for ICU
BuildArch:      noarch

%description    doc
API reference for the ICU libraries.

%prep -a
mkdir html
cd html
unzip %SOURCE1

%conf -p
cd source
mkdir -p data/out/tmp
export CXXFLAGS="%{optflags} -DICU_DATA_DIR='\"%{_datadir}/icu/%{version}\"' -fexcess-precision=fast"
export CFLAGS="$CXXFLAGS"

%install -a
chmod a+rx %{buildroot}%{_libdir}/lib*.so.*

%files
%doc readme.html
%license license.html
%{_bindir}/*
%exclude %{_bindir}/icu-config
%{_mandir}/man*/*
%dir %{_datadir}/icu
%dir %{_datadir}/icu/%{version}
%{_datadir}/icu/%{version}/*
%exclude %{_datadir}/icu/%{version}/config/
%{_libdir}/libicu*.so.*

%files devel
%{_libdir}/libicu*.so
%{_includedir}/unicode/
%dir %{_libdir}/icu/
%dir %{_libdir}/icu/%{version}/
%{_libdir}/icu/%{version}/Makefile.inc
%{_libdir}/icu/%{version}/pkgdata.inc
%{_libdir}/pkgconfig/icu-i18n.pc
%{_libdir}/pkgconfig/icu-io.pc
%{_libdir}/pkgconfig/icu-uc.pc
%_bindir/icu-config
%dir %{_datadir}/icu/
%dir %{_datadir}/icu/%{version}/
%{_datadir}/icu/%{version}/config/
%{_libdir}/icu/Makefile.inc
%{_libdir}/icu/pkgdata.inc
%{_libdir}/icu/current

%files doc
%doc html

%changelog
%autochangelog
