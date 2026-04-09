# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dlpack
Version:        1.3
Release:        %autorelease
Summary:        DLPack: Open In Memory Tensor Structure
License:        Apache-2.0
URL:            https://github.com/dmlc/dlpack
#!RemoteAsset
Source0:        https://github.com/dmlc/dlpack/archive/v%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
DLPack is an open in-memory tensor structure to for sharing tensor among frameworks. DLPack enables:
 * Easier sharing of operators between deep learning frameworks.
 * Easier wrapping of vendor level operator implementations, allowing collaboration when introducing new devices/ops.
 * Quick swapping of backend implementations, like different version of BLAS
 * For final users, this could bring more operators, and possibility of mixing usage between frameworks.

%files
%dir %{_includedir}/dlpack
%{_includedir}/dlpack/*
%dir %{_libdir}/cmake/dlpack/
%{_libdir}/cmake/dlpack/*.cmake

%changelog
%autochangelog
