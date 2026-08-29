# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit      e0f63b6580cc9f1c50d18928a4273106dc3a6c41
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           yarpgen
Version:        0+git20260624.%{shortcommit}
Release:        %autorelease
Summary:        Yet Another Random Program Generator
License:        Apache-2.0 AND BSL-1.0
URL:            https://github.com/intel/yarpgen
#!RemoteAsset:  sha256:0700e50b5070b87bf9b9b09d6f1228f1756a7e79fc9db61313e61270298b0b75
Source:         https://github.com/intel/yarpgen/archive/%{commit}/yarpgen-%{commit}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  m4

%description
yarpgen is a random program generator, which produces correct runnable C/C++ and DPC++(this work is in an early stage) programs. The generator is specifically designed to trigger compiler optimization bugs and is intended for compiler testing.

%install
# Use our own install step
install -Dp -m0755 scripts/yarpgen %{buildroot}%{_bindir}/yarpgen

%check
# no tests

%files
%doc README.md SECURITY.md bugs.rst
%license LICENSE.txt
%{_bindir}/yarpgen

%changelog
%autochangelog
