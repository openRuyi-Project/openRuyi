# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cli11
Version:        2.6.2
Release:        %autorelease
Summary:        Command line parser for C++11
License:        BSD-3-Clause
URL:            https://cliutils.github.io/CLI11/book/
VCS:            git:https://github.com/CLIUtils/CLI11.git
#!RemoteAsset:  sha256:c6ea6b2e5608b3ea8617999bd5f47420c71b2ebdb8dc4767c1034d1da5785711
Source0:        https://github.com/CLIUtils/CLI11/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCLI11_BUILD_DOCS=OFF
BuildOption(conf):  -DCLI11_BUILD_EXAMPLES=OFF
BuildOption(conf):  -DCLI11_BUILD_TESTS=ON
BuildOption(conf):  -DCLI11_SINGLE_FILE=ON
BuildOption(conf):  -DCLI11_FULL_INSTALL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  pkgconfig(catch2)

%description
CLI11 is a command line parser for C++11 and beyond that provides a rich
feature set with a simple and intuitive interface.

%package        devel
Summary:        Development files for %{name}

%description    devel
Development files for CLI11.

%files devel
%doc README.md
%license LICENSE
%{_includedir}/CLI/
%{_includedir}/CLI11.hpp
%{_datadir}/cmake/CLI11/
%{_datadir}/pkgconfig/CLI11.pc

%changelog
%autochangelog
