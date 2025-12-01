# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test
Name:           libtomcrypt
Version:        1.18.2
Release:        %autorelease
Summary:        A comprehensive, portable cryptographic toolkit
License:        Unlicense OR WTFPL
URL:            http://www.libtom.net/
#!RemoteAsset
Source:         https://github.com/libtom/libtomcrypt/archive/v%{version}/libtomcrypt-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build): PREFIX="%{_prefix}"
BuildOption(build): INCPATH="%{_includedir}"
BuildOption(build): LIBPATH="%{_libdir}"
BuildOption(build): EXTRALIBS="-ltommath"
BuildOption(build): CFLAGS="%{optflags} -DLTM_DESC -DUSE_LTM"
BuildOption(build): -f makefile.shared library test

BuildOption(install): INSTALL_OPTS="-m 755"
BuildOption(install): INCPATH="%{_includedir}"
BuildOption(install): LIBPATH="%{_libdir}"
BuildOption(install): -f makefile.shared

BuildRequires:  libtommath-devel >= 1.0
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc

%description
A comprehensive, modular and portable cryptographic toolkit that provides
developers with a vast array of well known published block ciphers, one-way hash
functions, and a plethora of other routines.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

# No configure
%conf

%install -a
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
sed -i \
    -e 's|^prefix=.*|prefix=%{_prefix}|g' \
    -e 's|^libdir=.*|libdir=${prefix}/%{_lib}|g' \
    %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

# TODO: Fix test build.
%check

%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%{?autochangelog}
