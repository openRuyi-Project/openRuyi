# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wabt
Version:        1.0.39
Release:        %autorelease
Summary:        The WebAssembly Binary Toolkit
License:        Apache-2.0
URL:            https://github.com/WebAssembly/wabt
#!RemoteAsset
Source0:        https://github.com/WebAssembly/wabt/releases/download/%{version}/wabt-%{version}.tar.xz
BuildSystem:    cmake

# include cstdint.
Patch0:         0001-fix-test-include.patch
# disable some fail or timeout tests.
Patch1:         0002-exclude-some-tests.patch

BuildOption(conf):  -DBUILD_TESTS=ON
BuildOption(conf):  -DUSE_SYSTEM_GTEST=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)

%description
WABT (pronounced "wabbit") is a suite of tools for WebAssembly, intended for
use in toolchains or other systems that want to manipulate WebAssembly files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
Static libraries for %{name}.

%check
%cmake_build --target check

%files
%license LICENSE
%doc README.md
%{_bindir}/spectest-interp
%{_bindir}/wasm-decompile
%{_bindir}/wasm-interp
%{_bindir}/wasm-objdump
%{_bindir}/wasm-stats
%{_bindir}/wasm-strip
%{_bindir}/wasm-validate
%{_bindir}/wasm2c
%{_bindir}/wasm2wat
%{_bindir}/wast2json
%{_bindir}/wat-desugar
%{_bindir}/wat2wasm
%{_mandir}/man1/*.1*
%{_datadir}/wabt/

%files devel
%{_includedir}/wabt
%{_includedir}/wasm-rt.h
%{_includedir}/wasm-rt-exceptions.h
%{_libdir}/cmake/wabt/

%files static
%{_libdir}/libwabt.a
%{_libdir}/libwasm-rt-impl.a

%changelog
%autochangelog
