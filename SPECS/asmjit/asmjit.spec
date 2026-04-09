# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit      f64c90818ff2ef87ec4f73f44d0a7e73fbff3229
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           asmjit
Version:        0+git20260104.%{shortcommit}
Release:        %autorelease
Summary:        A lightweight library suitable for low-latency machine code generation
License:        Zlib
URL:            https://asmjit.com
VCS:            git:https://github.com/asmjit/asmjit
#!RemoteAsset
Source0:        https://github.com/asmjit/asmjit/archive/%{commit}/asmjit-%{commit}.tar.gz
BuildSystem:    cmake

BuildOption(conf): -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
BuildOption(conf): -DASMJIT_STATIC=0
BuildOption(conf): -DASMJIT_TEST=1

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
AsmJit is a lightweight library suitable for low-latency machine code
generation written in C++. It can generate machine code for X86, X86_64, and
AArch64 architectures. It has a type-safe API that allows C++ compiler to do
semantic checks at compile-time even before the assembled code is generated
or executed.}

%package        devel
Summary:        Headers and libraries for asmjit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and libraries for asmjit

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libasmjit.so

%files          devel
%doc README.md
%{_includedir}/asmjit/
%{_libdir}/cmake/asmjit/

%changelog
%autochangelog
