# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit       c14da81424f5d3c4205dc58f87edff68d83e656d
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

Name:           mmtests
Version:        2.0~rc1+git20260312.%{shortcommit}
Release:        %autorelease
Summary:        Configurable test framework
License:        GPL-2.0-only
URL:            https://github.com/gormanm/mmtests
#!RemoteAsset:  sha256:8aaf9b69e74087f7f3a501dda3c65e3e7805e932358c848ef0ad2d638bd5669f
Source:         https://github.com/gormanm/mmtests/archive/%{commit}/mmtests-%{commit}.tar.gz

# Adapt MMTests to openRuyi
Patch2000:      2000-openRuyi.patch

BuildRequires:  python3
BuildRequires:  python3-rpm-macros

# dependencies documented in run-mmtests.sh
Requires:       autoconf
Requires:       automake
Requires:       libtool
Requires:       make
Requires:       patch
Requires:       bc
Requires:       binutils-devel
Requires:       bzip2
Requires:       coreutils
Requires:       /usr/bin/cpupower
Requires:       e2fsprogs
Requires:       expect
Requires:       expect-devel
Requires:       gawk
Requires:       gcc
Requires:       gzip
Requires:       hdparm
Requires:       hostname
Requires:       hwloc
Requires:       iproute2
Requires:       nmap
Requires:       numactl
Requires:       perl(File::Slurp)
Requires:       perl(Time::HiRes)
Requires:       psmisc
Requires:       tcl
Requires:       time
Requires:       util-linux
Requires:       wget
Requires:       which
Requires:       xfsprogs
Requires:       xfsprogs-devel
Requires:       xz
Requires:       btrfs-progs
Requires:       numad
Requires:       tuned
Requires:       perl(Try::Tiny)
Requires:       perl(JSON)
Requires:       perl(GD)
# Requires:       linux-tools

# dependencies documented in README.md
Recommends:     perl(List::BinarySearch)
Recommends:     perl(Math::Gradient)
# Recommends:     R

%description
MMTests is a configurable test suite that runs a number of common workloads
of interest to developers. It is possible to add monitors for the workload
and it provides reporting tools for comparing different test runs.

%prep
%autosetup -p1 -n %{name}-%{commit}

# No configure
%conf

%build
# No Build

%install
install -d %{buildroot}%{_libexecdir}/MMTests
cp -pr \
  bin bin-virt configs drivers monitors shellpack_src shellpacks \
  config host_config *.sh %{buildroot}%{_libexecdir}/MMTests

%files
%license COPYING
%doc README.md docs
%{_libexecdir}/MMTests

%changelog
%autochangelog
