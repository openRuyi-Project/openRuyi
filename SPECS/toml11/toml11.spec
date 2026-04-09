# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           toml11
Version:        4.4.0
Release:        %autorelease
Summary:        TOML for modern C++
License:        MIT
URL:            https://github.com/ToruNiina/toml11
#!RemoteAsset
Source0:        https://github.com/ToruNiina/toml11/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  gcc-c++
BuildRequires:  cmake


%description
@code{toml11} is a C++11 (or later) header-only toml parser/encoder
depending only on C++ standard library.

@itemize
@item It is compatible to the latest version of TOML v1.0.0.
@item It is one of the most TOML standard compliant libraries, tested with
a language agnostic test suite for TOML parsers.
@item It shows highly informative error messages.
@item It has configurable container.  You can use any random-access containers
and key-value maps as backend containers.
@item It optionally preserves comments without any overhead.
@item It has configurable serializer that supports comments, inline tables,
literal strings and multiline strings.
@item It supports user-defined type conversion from/into toml values.
@item It correctly handles UTF-8 sequences, with or without BOM.
@end itemize

%files
%license LICENSE
%doc README.md
%{_includedir}/toml.hpp
%{_includedir}/toml11/*.hpp
%{_includedir}/toml11/*/*.hpp
%{_libdir}/cmake/toml11/*.cmake

%changelog
%autochangelog
