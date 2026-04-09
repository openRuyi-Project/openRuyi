# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           doctest
Version:        2.4.12
Release:        %autorelease
Summary:        C++ test framework
License:        MIT
URL:            https://github.com/doctest/doctest
#!RemoteAsset
Source0:        https://github.com/doctest/doctest/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
doctest is a single-header testing framework for C++11 and later.  It
has been designed to be fast, light and unintrusive.

%files
%license LICENSE.txt
%doc README.md
%{_includedir}/doctest/*.h
%{_includedir}/doctest/extensions/*.h
%{_libdir}/cmake/doctest/*.cmake

%changelog
%autochangelog
