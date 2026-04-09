# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cppunit
Version:        1.15.1
Release:        %autorelease
Summary:        C++ port of JUnit testing framework
License:        LGPL-2.1-or-later
URL:            https://www.freedesktop.org/wiki/Software/cppunit/
VCS:            git:https://anongit.freedesktop.org/git/libreoffice/cppunit.git
#!RemoteAsset
Source:         http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --disable-doxygen

BuildRequires:  gcc-c++

%description
CppUnit is the C++ port of the famous JUnit framework for unit testing.
Test output can be in XML for automatic testing and GUI based for supervised tests.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries, header files, and examples for developing
applications that use the CppUnit framework.

%files
%license COPYING AUTHORS
%doc NEWS README THANKS TODO BUGS
%doc %{_docdir}/%{name}
%{_bindir}/DllPlugInTester
%{_libdir}/lib*.so*

%files devel
%{_includedir}/cppunit
%{_libdir}/libcppunit.so
%{_libdir}/pkgconfig/cppunit.pc

%changelog
%autochangelog
