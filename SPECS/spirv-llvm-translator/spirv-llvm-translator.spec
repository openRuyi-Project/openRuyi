# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           spirv-llvm-translator
Version:        21.1.3
Release:        %autorelease
Summary:        LLVM to SPIRV Translator
License:        NCSA
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
#!RemoteAsset
Source0:        https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DLLVM_BUILD_TOOLS=ON
BuildOption(conf):  -DCMAKE_INSTALL_RPATH:BOOL=";"
BuildOption(conf):  -DLLVM_DIR="%{_libdir}/cmake/llvm"
BuildOption(conf):  -DLLVM_EXTERNAL_PROJECTS="SPIRV-Headers"
BuildOption(conf):  -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR="%{_includedir}/spirv"
BuildOption(conf):  -DLLVM_LIBDIR_SUFFIX=64

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig(SPIRV-Headers)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libffi)

%description
Khronos LLVM to SPIRV Translator. This is a library to be used by Mesa
for OpenCL support. It translates LLVM IR to Khronos SPIR-V.

%package        devel
Summary:        Development files for LLVM to SPIRV Translator
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for LLVM to SPIRV Translator.

%files
%doc README.md
%license LICENSE.TXT
%{_libdir}/libLLVMSPIRVLib.so.*
%{_bindir}/llvm-spirv

%files devel
%{_includedir}/LLVMSPIRVLib/
%{_libdir}/libLLVMSPIRVLib.so
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc

%changelog
%autochangelog
