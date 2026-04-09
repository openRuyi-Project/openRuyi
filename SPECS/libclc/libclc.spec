# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libclc
Version:        21.1.7
Release:        %autorelease
Summary:        An open source implementation of the OpenCL 1.1 library requirements
License:        Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
URL:            https://libclc.llvm.org
VCS:            git:https://github.com/llvm/llvm-project
#!RemoteAsset
Source0:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/libclc-%{version}.src.tar.xz
BuildArch:      noarch
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_INSTALL_DATADIR=%{_datadir}
BuildOption(conf):  CFLAGS="%{build_cflags} -D__extern_always_inline=inline"

BuildRequires:  cmake
BuildRequires:  python3
BuildRequires:  pkgconfig(zlib)
BuildRequires:  clang-devel >= %{version}
BuildRequires:  llvm-devel >= %{version}
BuildRequires:  pkgconfig(libedit)
BuildRequires:  spirv-llvm-translator

%description
libclc is an open source implementation of the library requirements of the
OpenCL C programming language, as specified by the OpenCL 1.1 Specification.
It is intended to be used with the Clang compiler's OpenCL frontend.

%package        bc
Summary:        bc subset of %{name}
BuildArch:      noarch

%description    bc
The %{name}-spirv package contains the spirv*-mesa3d-.spv files only,
which are the subset required for upstream Mesa OpenCL support with RustiCL.

%files
%license LICENSE.TXT
%dir %{_datadir}/clc
%{_datadir}/clc/spirv-mesa3d-.spv
%{_datadir}/clc/spirv64-mesa3d-.spv
%{_datadir}/pkgconfig/libclc.pc

%files bc
%{_datadir}/clc/*.bc

%changelog
%autochangelog
