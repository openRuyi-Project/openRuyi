# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           magic_enum
Version:        0.9.7
Release:        %autorelease
Summary:        Static reflection for enums for modern C++
License:        MIT
URL:            https://github.com/Neargye/magic_enum
#!RemoteAsset
Source0:        https://github.com/Neargye/magic_enum/releases/download/v%{version}/magic_enum-v%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(catch2)

%description
Magic Enum is a header-only C++17 library that provides static reflection for
enums, working with any enum type without any macro or boilerplate code.

%install -a
rm -f %{buildroot}%{_datadir}/%{name}/package.xml

%files
%license LICENSE
%doc README.md doc
%{_includedir}/magic_enum/magic_enum*.hpp
%{_datadir}/cmake/magic_enum/
%{_datadir}/pkgconfig/magic_enum.pc

%changelog
%autochangelog
