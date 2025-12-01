# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           icu4c
Version:        77.1
Release:        %autorelease
Summary:        International Components for Unicode
License:        Unicode-3.0
URL:            https://icu.unicode.org/
#!RemoteAsset
Source0:        https://github.com/unicode-org/icu/releases/download/release-77-1/%{name}-77_1-src.tgz
#!RemoteAsset
Source1:        https://github.com/unicode-org/icu/releases/download/release-77-1/%{name}-77_1-docs.zip
BuildSystem:    autotools
Patch0:         0001-icu-fix-install-mode-files.patch
Patch1:         0002-icu-error-reporting.patch
Patch2:         0003-icu-avoid-x87-excess-precision.patch
Patch3:         0004-locale.patch
Patch4:         0005-nan-undefined-conversion.patch

BuildOption(conf): --disable-static
BuildOption(conf): --enable-shared
BuildOption(conf): --disable-samples
BuildOption(conf): --with-data-packaging=archive

BuildOption(build): -C source
BuildOption(install): -C source

BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  python3
BuildRequires:  unzip
Provides:       bundled(tzdata) = 2024b
Provides:       icu
Requires:       tzdata

%description
ICU is a set of C and C++ libraries that provide extensive Unicode and locale
support. This package contains the runtime libraries, data files, and command-line
tools for ICU.

%package devel
Summary:        Development files for the ICU library
Requires:       %{name} = %{version}

%description devel
This package contains the headers, symbolic links, and other files needed to
develop applications that use the ICU libraries.

%prep -a
mkdir html
cd html
unzip %SOURCE1

%conf
cd source
mkdir -p data/out/tmp
export CXXFLAGS="%{optflags} -DICU_DATA_DIR='\"%{_datadir}/icu/%{version}\"' -fexcess-precision=fast"
export CFLAGS="$CXXFLAGS"
%configure

%build -a
cd source/data/
%ifarch %armb hppa mips mips64 ppc ppc64 %sparc s390 s390x m68k
  cp in/icudt77l.dat out/
%else
  LD_LIBRARY_PATH="../lib:../stubdata:../tools/ctestfw:$LD_LIBRARY_PATH" \
  ../bin/icupkg -tb in/icudt77l.dat out/icudt77b.dat
%endif


%install -a
install -d -m 755 %{buildroot}%{_datadir}/icu/%{version}
install -m 644 source/data/out/icudt*.dat %{buildroot}%{_datadir}/icu/%{version}/
install -d -m 755 %{buildroot}%{_docdir}/%{name}
cp -a html/* %{buildroot}%{_docdir}/%{name}/
cp -a license.html readme.html %{buildroot}%{_docdir}/%{name}/
find %{buildroot} -type f -name "*.la" -delete
chmod a+rx %{buildroot}%{_libdir}/lib*.so.*
rm -f %{buildroot}%{_libdir}/icu/%{version}/{Makefile.inc,pkgdata.inc}

%files
%license license.html
%doc readme.html
%_bindir/*
%_sbindir/*
%_mandir/man*/*
%dir %_datadir/icu
%dir %_datadir/icu/%{version}
%_datadir/icu/%{version}/*
%_libdir/libicu*.so.*

%files devel
%_libdir/libicu*.so
%_includedir/unicode/
%dir %_libdir/icu/
%dir %_libdir/icu/%{version}/
%_libdir/pkgconfig/icu-*.pc
%_bindir/icu-config
%dir %_datadir/icu/
%dir %_datadir/icu/%{version}/
%_datadir/icu/%{version}/config/
%doc %{_docdir}/%{name}/
%{_libdir}/icu/Makefile.inc
%{_libdir}/icu/pkgdata.inc
%{_libdir}/icu/current

%changelog
%{?autochangelog}
