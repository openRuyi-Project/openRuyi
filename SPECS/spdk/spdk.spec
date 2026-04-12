# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           spdk
Version:        25.09
Release:        %autorelease
Summary:        Set of libraries and utilities for high performance user-mode storage
License:        BSD-3-Clause AND BSD-2-Clause
URL:            http://spdk.io
VCS:            git:https://github.com/spdk/spdk
#!RemoteAsset:  sha256:f2abbd321a8140c908d6a197e2f6e263e6ae3a42beb6e4aee2b1c62def1afd25
Source0:        https://github.com/spdk/spdk/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

# Warning: This patch seems abandoned
# https://github.com/spdk/spdk/issues/2736
# https://review.spdk.io/c/spdk/spdk/+/14996
# We're using the patch based on the Alpine one (which looks somehow similar), refreshed to v25.09
# https://gitlab.alpinelinux.org/alpine/aports/-/blob/master/community/spdk/isal.patch
Patch0:         2001-with-system-isal.patch

BuildOption(install):  libdir=%{_libdir}

BuildRequires:  make
BuildRequires:  pkgconfig(libdpdk)
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libaio)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  fuse3
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-pip
BuildRequires:  python-setuptools
BuildRequires:  python-wheel
BuildRequires:  python-hatchling
BuildRequires:  util-linux-devel
BuildRequires:  patchelf
BuildRequires:  pkgconfig(libisal)
BuildRequires:  pkgconfig(libisal_crypto)
BuildRequires:  pkgconfig(libibverbs)
BuildRequires:  pkgconfig(librdmacm)
BuildRequires:  pkgconfig(libiscsi)

Requires:       dpdk
Requires:       numactl
Requires:       openssl
Requires:       libaio
Requires:       libuuid
Requires:       fuse3

%description
The Storage Performance Development Kit provides a set of tools
and libraries for writing high performance, scalable, user-mode storage
applications.

%package        devel
Summary:        Storage Performance Development Kit development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel
This package contains the headers and other files needed for
developing applications with the Storage Performance Development Kit.

%package        static
Summary:        Storage Performance Development Kit static libraries
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
This package contains the static libraries for the Storage Performance
Development Kit.

%package        tools
Summary:        Storage Performance Development Kit tools files
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    tools
%{summary}

# not utilize a standard configure script.
%conf
export LD=ld.bfd
export CC="gcc -fuse-ld=bfd"
export CXX="g++ -fuse-ld=bfd"

./configure --prefix=%{_usr} \
    --libdir=%{_libdir} \
    --with-dpdk \
    --with-rdma \
    --with-iscsi-initiator \
    --disable-examples \
    --disable-tests \
    --disable-unit-tests \
    --with-shared \
    --with-system-isal

%install -p
find . -name "*.mk" -o -name "Makefile" | xargs sed -i 's/pip install/pip install --no-build-isolation/g'

%install -a

# Create self-contained spdk-setup script (similar to PKGBUILD approach)
echo '#!/usr/bin/env bash' > %{buildroot}%{_bindir}/spdk-setup
cat scripts/common.sh scripts/setup.sh >> %{buildroot}%{_bindir}/spdk-setup
sed -ri '/^rootdir/d;/^source/d;s,\$rootdir,%{_usr},' %{buildroot}%{_bindir}/spdk-setup
chmod +x %{buildroot}%{_bindir}/spdk-setup

# Install bash completion
install -Dm644 scripts/bash-completion/spdk %{buildroot}%{_datadir}/bash-completion/completions/spdk

# Install license
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

# Install tools
mkdir -p %{buildroot}%{_datadir}/%{name}
find scripts -type f -regextype egrep -regex '.*(spdkcli|rpc).*[.]py' \
    -exec cp --parents -t %{buildroot}%{_datadir}/%{name} {} ";"

# no tests
%check

%files
%license %{_datadir}/licenses/%{name}/LICENSE
%{_bindir}/spdk-setup
%{python_sitelib}/spdk*/*
%{_bindir}/nvmf_tgt
%{_bindir}/iscsi_tgt
%{_bindir}/vhost
%{_bindir}/spdk_*
%{_libdir}/*.so.*
%{_datadir}/bash-completion/completions/spdk

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%{_libdir}/*.so

%files static
%{_libdir}/*.a

%files tools
%{_datadir}/%{name}/scripts
%{_bindir}/spdk-cli
%{_bindir}/spdk-mcp
%{_bindir}/spdk-rpc
%{_bindir}/spdk-sma

%changelog
%autochangelog
