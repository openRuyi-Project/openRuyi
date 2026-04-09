# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstreamname rocminfo
%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global pkg_desc ROCm system info utility

Name:           rocminfo
Version:        %{rocm_version}
Release:        %autorelease
Summary:        %{pkg_desc}
License:        NCSA
URL:            https://github.com/ROCm/rocminfo
#!RemoteAsset
Source0:        %{url}/archive/refs/tags/rocm-%{version}.tar.gz
BuildSystem:    cmake

Patch0:         0001-adjust-CMAKE_CXX_FLAGS.patch

BuildOption(conf):  -DROCM_DIR=%{_prefix}

BuildRequires:  make
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  pkgconfig(python3)
BuildRequires:  cmake(hsa-runtime64) >= 1.0

# rocminfo calls lsmod to check the kernel mode driver status
Requires:       kmod

%description
%{pkg_desc}

%prep -a
sed -i -e 's@/usr/bin/env python3@/usr/bin/python3@' rocm_agent_enumerator

%install -a
chmod 755 %{buildroot}%{_bindir}/*

%files
%doc README.md
%license License.txt
%{_bindir}/rocm_agent_enumerator
%{_bindir}/rocminfo
#Duplicated files:
%exclude %{_docdir}/*/License.txt

%changelog
%autochangelog
