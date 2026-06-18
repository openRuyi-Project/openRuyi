# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           spirv-llvm-translator
Version:        22.1.3
Release:        %autorelease
Summary:        LLVM to SPIRV Translator
License:        NCSA
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
#!RemoteAsset:  sha256:8d3d5c31c1ff355dbbf87046f1b94cd1ab5390439a817679ec71484df74cac18
Source0:        https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

# This change is not applicable in the SPIRV-Headers vulkan-sdk-1.4.350.0 version.
Patch2000:      2000-Revert-Remove-internal-values-for-SPV_INTEL_predicat.patch

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
BuildRequires:  (cmake(LLVM) >= 22 with cmake(LLVM) < 23)
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
