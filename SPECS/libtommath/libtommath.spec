# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           libtommath
Version:        1.3.0
Release:        %autorelease
Summary:        A portable number theoretic multiple-precision integer library
License:        Unlicense
URL:            http://www.libtom.net/
VCS:            git:https://github.com/libtom/libtommath
#!RemoteAsset
Source:         https://github.com/libtom/libtommath/archive/refs/tags/v%{version}.tar.gz

BuildSystem:    autotools

BuildOption(build):  CFLAGS="%{optflags} -I./"
BuildOption(build):  -f makefile.shared
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  LIBPATH=%{_libdir}
BuildOption(install):  -f makefile.shared

BuildRequires:  make
BuildRequires:  libtool

%description
A free open source portable number theoretic multiple-precision integer library
written entirely in C, designed with a simple API and efficient routines.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use libtommath.

%prep -a
# Fix permissions on installed library
sed -i -e 's/644 $(LIBNAME)/755 $(LIBNAME)/g' makefile.shared
# Fix pkgconfig path
sed -i \
    -e 's|^prefix=.*|prefix=%{_prefix}|g' \
    -e 's|^libdir=.*|libdir=%{_libdir}|g' \
    %{name}.pc.in

# No configure
%conf

%install -a
find %{buildroot} -name '*.a' -delete

%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libtommath.pc

%changelog
%{?autochangelog}
