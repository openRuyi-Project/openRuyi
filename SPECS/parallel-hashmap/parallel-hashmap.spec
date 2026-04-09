# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           parallel-hashmap
Version:        2.0.0
Release:        %autorelease
Summary:        Header-only hashmap and btree containers for C++
License:        Apache-2.0
URL:            https://greg7mdp.github.io/parallel-hashmap/
VCS:            git:https://github.com/greg7mdp/parallel-hashmap
#!RemoteAsset
Source0:        https://github.com/greg7mdp/parallel-hashmap/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    cmake

BuildOption(conf):  -DPHMAP_BUILD_TESTS=OFF
BuildOption(conf):  -DPHMAP_BUILD_EXAMPLES=OFF

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make

Provides:       %{name}-devel%{?_isa} = %{version}-%{release}

%description
The hashmaps and btree provided here are built upon those open
sourced by Google in the Abseil library. The hashmaps use closed
hashing, where values are stored directly into a memory array,
avoiding memory indirections. By using parallel SSE2 instructions,
these hashmaps are able to look up items by checking 16 slots in
parallel, allowing the implementation to remain fast even when the
table is filled up to 87.5%% capacity.

%files
%license LICENSE
%doc README.md
%{_includedir}/parallel_hashmap

%changelog
%autochangelog
