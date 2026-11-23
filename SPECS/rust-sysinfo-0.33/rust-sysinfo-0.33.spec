# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sysinfo
%global full_version 0.33.1
%global pkgname sysinfo-0.33

Name:           rust-sysinfo-0.33
Version:        0.33.1
Release:        %autorelease
Summary:        Rust crate "sysinfo"
License:        MIT
URL:            https://github.com/GuillaumeGomez/sysinfo
#!RemoteAsset:  sha256:4fc858248ea01b66f19d8e8a6d55f41deaf91e9d495246fd01368d99935c6c01
Source:         https://static.crates.io/crates/sysinfo/0.33.1/download#/rust-sysinfo-0.33-0.33.1.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.164
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "sysinfo"

%package     -n %{name}+apple-sandbox
Summary:        Library to get system information such as processes, CPUs, disks, components and networks - feature "apple-sandbox" and 9 more
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/apple-app-store) = %{version}
Provides:       crate(%{pkgname}/apple-sandbox) = %{version}
Provides:       crate(%{pkgname}/component) = %{version}
Provides:       crate(%{pkgname}/disk) = %{version}
Provides:       crate(%{pkgname}/linux-netdevs) = %{version}
Provides:       crate(%{pkgname}/linux-tmpfs) = %{version}
Provides:       crate(%{pkgname}/network) = %{version}
Provides:       crate(%{pkgname}/unknown-ci) = %{version}
Provides:       crate(%{pkgname}/user) = %{version}
Provides:       crate(%{pkgname}/windows) = %{version}

%description -n %{name}+apple-sandbox
This metapackage enables feature "apple-sandbox" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "apple-app-store", "component", "disk", "linux-netdevs", "linux-tmpfs", "network", "unknown-ci", "user", and "windows" features.

%package     -n %{name}+c-interface
Summary:        Library to get system information such as processes, CPUs, disks, components and networks - feature "c-interface"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/component) = %{version}
Requires:       crate(%{pkgname}/default) = %{version}
Requires:       crate(%{pkgname}/disk) = %{version}
Requires:       crate(%{pkgname}/multithread) = %{version}
Requires:       crate(%{pkgname}/network) = %{version}
Requires:       crate(%{pkgname}/system) = %{version}
Requires:       crate(%{pkgname}/user) = %{version}
Requires:       crate(memchr-2/default) >= 2.5.0
Requires:       crate(rayon-1/default) >= 1.8.0
Provides:       crate(%{pkgname}/c-interface) = %{version}

%description -n %{name}+c-interface
This metapackage enables feature "c-interface" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Library to get system information such as processes, CPUs, disks, components and networks - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.164
Requires:       crate(libc-0.2/extra-traits) >= 0.2.164
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Library to get system information such as processes, CPUs, disks, components and networks - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/component) = %{version}
Requires:       crate(%{pkgname}/disk) = %{version}
Requires:       crate(%{pkgname}/multithread) = %{version}
Requires:       crate(%{pkgname}/network) = %{version}
Requires:       crate(%{pkgname}/system) = %{version}
Requires:       crate(%{pkgname}/user) = %{version}
Requires:       crate(memchr-2/default) >= 2.5.0
Requires:       crate(rayon-1/default) >= 1.8.0
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+multithread
Summary:        Library to get system information such as processes, CPUs, disks, components and networks - feature "multithread"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.8.0
Provides:       crate(%{pkgname}/multithread) = %{version}

%description -n %{name}+multithread
This metapackage enables feature "multithread" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Library to get system information such as processes, CPUs, disks, components and networks - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.190
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system
Summary:        Library to get system information such as processes, CPUs, disks, components and networks - feature "system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/default) >= 2.5.0
Provides:       crate(%{pkgname}/system) = %{version}

%description -n %{name}+system
This metapackage enables feature "system" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
