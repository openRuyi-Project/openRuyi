# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mold
Version:        2.41.0
Release:        %autorelease
Summary:        A Modern Linker
License:        MIT AND (Apache-2.0 OR MIT)
URL:            https://github.com/rui314/mold
#!RemoteAsset:  sha256:0a61abac85d818437b425df856822e9d6e9982baeae5a93bcb02fe6c0060c61a
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# Allow building against the system-provided `xxhash.h`
Patch0:         0001-Use-system-compatible-include-path-for-xxhash.h.patch

BuildOption(conf):  -DMOLD_USE_SYSTEM_MIMALLOC=ON

BuildRequires:  pkgconfig(libblake3)
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(mimalloc)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(tbb)

Requires(post): update-alternatives
Requires(preun): update-alternatives

%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times faster than the LLVM lld linker.
mold is designed to increase developer productivity by reducing
build time, especially in rapid debug-edit-rebuild cycles.

%post
if [ "$1" = 1 ]; then
  update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.mold 100
fi

%postun
if [ "$1" = 0 ]; then
  update-alternatives --remove ld %{_bindir}/ld.mold
fi

%files
%license %{_docdir}/mold/LICENSE
%ghost %{_bindir}/ld
%{_bindir}/mold
%{_bindir}/ld.mold
%{_libdir}/mold/mold-wrapper.so
%{_libexecdir}/mold/ld
%{_mandir}/man1/ld.mold.1*
%{_mandir}/man1/mold.1*

%changelog
%autochangelog
