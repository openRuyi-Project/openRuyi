# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           csmith
Version:        2.3.0
Release:        %autorelease
Summary:        Tool to generate random C programs for compiler testing
License:        BSD
URL:            https://github.com/csmith-project/csmith
#!RemoteAsset:  sha256:9d024a6b202f6a1b9e01351218a85888c06b67b837fe4c6f8ef5bd522fae098c
Source:         https://github.com/csmith-project/csmith/archive/csmith-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  m4
BuildRequires:  autoconf
BuildRequires:  perl-devel
BuildRequires:  perl-macros

%description
Csmith is a tool that can generate random C programs that statically and
dynamically conform to the C99 standard. It is useful for stress-testing
compilers, static analyzers, and other tools that process C code.

%package        devel
Summary:        Header files and libraries for Csmith development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains the header files and libraries for
developing applications that use %{name}.

%conf -p
sed -i 's:/lib:/%{_lib}:' runtime/CMakeLists.txt

%install -a
find %{buildroot} -name *.a  -exec rm -f {} \;
rm -v %{buildroot}%{_bindir}/compiler_test.in

%files
%doc AUTHORS ChangeLog README TODO
%doc doc/probabilities.txt scripts/compiler_test.in
%license COPYING
%{_bindir}/compiler_test.pl
%{_bindir}/csmith
%{_bindir}/launchn.pl
%{_libdir}/libcsmith.so.0*
%{_datarootdir}/doc/csmith/probabilities.txt

%files devel
%{_includedir}/*
%{_libdir}/libcsmith.so

%changelog
%autochangelog
