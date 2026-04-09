# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           safeint
Version:        3.0.28a
Release:        %autorelease
Summary:        Class library for C++ that manages integer overflows
License:        MIT
URL:            https://github.com/dcleblanc/SafeInt
#!RemoteAsset
Source0:        %{url}/archive/%{version}/SafeInt-%{version}.tar.gz
BuildSystem:    cmake

# Remove GCC 98 test compilation target from CMakeLists
Patch0:         0001-gcc98_test_rm.patch
# Fix GCC 14 compilation by removing obsolete SafeIntGccCompileOnly exception handler
Patch1:         0002-gcc14_test_fix.patch
# Move C++17 template class and includes from function scope to file scope (GCC 15+ compatibility)
Patch2:         0003-move-cpp17-code-to-file-scope.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
An integer overflow library that was originally created in Microsoft
Office in 2003, and later was made open source on CodePlex using the MS-PL
license. After CodePlex was deprecated, the project was moved to github
and the license was changed to the MIT license.

An header-only package.

%install
install -d %{buildroot}%{_includedir}/SafeInt
install -D -p SafeInt.hpp -t %{buildroot}%{_includedir}/SafeInt/
install -D -p safe_math.h -t %{buildroot}%{_includedir}/SafeInt/
install -D -p safe_math_impl.h -t %{buildroot}%{_includedir}/SafeInt/

%files
%license LICENSE
%doc README.md
%dir %{_includedir}/SafeInt
%{_includedir}/SafeInt/SafeInt.hpp
%{_includedir}/SafeInt/safe_math.h
%{_includedir}/SafeInt/safe_math_impl.h

%changelog
%autochangelog
