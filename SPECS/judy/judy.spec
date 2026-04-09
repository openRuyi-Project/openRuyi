# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           judy
Version:        1.0.5
Release:        %autorelease
Summary:        A general purpose dynamic array implemented as a C callable library
License:        LGPL-2.1-or-later
URL:            https://judy.sourceforge.net/
VCS:            svn:https://svn.code.sf.net/p/judy/code/trunk
#!RemoteAsset
Source0:        https://sourceforge.net/projects/judy/files/judy/Judy-%{version}/Judy-%{version}.tar.gz
BuildSystem:    autotools

# use shared library to test
Patch0:         0001-Judy-test-shared.patch
# remove the build timestamp from the generated documentation header
# to ensure reproducible builds
Patch1:         0002-fix-reproducible-builds.patch

BuildOption(conf):  --disable-static
# fail to compile properly with parallel make
# https://sourceforge.net/p/judy/bugs/22/
BuildOption(build):  -j1

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Judy is a C library that provides a state-of-the-art core technology that
implements a sparse dynamic array. Judy arrays are declared simply with a null
pointer. A Judy array consumes memory only when it is populated, yet can grow
to take advantage of all available memory if desired. Judy's key benefits are
scalability, high performance, and memory efficiency. A Judy array is
extensible and can scale up to a very large number of elements, bounded only by
machine memory. Since Judy is designed as an unbounded array, the size of a
Judy array is not pre-allocated but grows and shrinks dynamically with the
array population.

%package        devel
Summary:        Development libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the development libraries and header files for %{name}.

%files
%license COPYING
%doc AUTHORS ChangeLog README examples/
%{_libdir}/libJudy.so.1*

%files devel
%doc doc
%{_includedir}/Judy.h
%{_libdir}/libJudy.so
%{_mandir}/man3/J*

%changelog
%autochangelog
