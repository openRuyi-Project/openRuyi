# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sysinfo
%global full_version 0.38.4
%global pkgname sysinfo-0.38

Name:           rust-sysinfo-0.38
Version:        0.38.4
Release:        %autorelease
Summary:        Rust crate "sysinfo"
License:        MIT
URL:            https://github.com/GuillaumeGomez/sysinfo
#!RemoteAsset:  sha256:92ab6a2f8bfe508deb3c6406578252e491d299cbbf3bc0529ecc3313aee4a52f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.173
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/apple-app-store) = %{version}
Provides:       crate(%{pkgname}/apple-sandbox) = %{version}
Provides:       crate(%{pkgname}/linux-netdevs) = %{version}
Provides:       crate(%{pkgname}/linux-tmpfs) = %{version}
Provides:       crate(%{pkgname}/unknown-ci) = %{version}

%description
Source code for takopackized Rust crate "sysinfo"

%package     -n %{name}+component
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "component"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/objc2-io-kit) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfbase) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfnumber) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfstring) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/std) >= 0.3.2
Requires:       crate(objc2-io-kit-0.3/hidsystem) >= 0.3.2
Requires:       crate(objc2-io-kit-0.3/libc) >= 0.3.2
Requires:       crate(objc2-io-kit-0.3/std) >= 0.3.2
Requires:       crate(windows-0.62/win32-foundation) >= 0.62.0
Requires:       crate(windows-0.62/win32-security) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-com) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-ole) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-rpc) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-variant) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-wmi) >= 0.62.0
Provides:       crate(%{pkgname}/component) = %{version}

%description -n %{name}+component
This metapackage enables feature "component" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/extra-traits) >= 0.2.173
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "default" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/component) = %{version}
Requires:       crate(%{pkgname}/disk) = %{version}
Requires:       crate(%{pkgname}/network) = %{version}
Requires:       crate(%{pkgname}/system) = %{version}
Requires:       crate(%{pkgname}/user) = %{version}
Provides:       crate(%{pkgname}/c-interface) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "c-interface" feature.

%package     -n %{name}+disk
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "disk"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/objc2-io-kit) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfbase) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfnumber) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfstring) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/std) >= 0.3.2
Requires:       crate(windows-0.62/win32-foundation) >= 0.62.0
Requires:       crate(windows-0.62/win32-security) >= 0.62.0
Requires:       crate(windows-0.62/win32-storage-filesystem) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-io) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-ioctl) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-systemservices) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-windowsprogramming) >= 0.62.0
Provides:       crate(%{pkgname}/disk) = %{version}

%description -n %{name}+disk
This metapackage enables feature "disk" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+multithread
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "multithread"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.8.0
Provides:       crate(%{pkgname}/multithread) = %{version}

%description -n %{name}+multithread
This metapackage enables feature "multithread" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+network
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "network"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-0.62/win32-foundation) >= 0.62.0
Requires:       crate(windows-0.62/win32-networking-winsock) >= 0.62.0
Requires:       crate(windows-0.62/win32-networkmanagement-iphelper) >= 0.62.0
Requires:       crate(windows-0.62/win32-networkmanagement-ndis) >= 0.62.0
Provides:       crate(%{pkgname}/network) = %{version}

%description -n %{name}+network
This metapackage enables feature "network" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-foundation
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "objc2-core-foundation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/std) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-foundation) = %{version}

%description -n %{name}+objc2-core-foundation
This metapackage enables feature "objc2-core-foundation" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-io-kit
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "objc2-io-kit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-io-kit-0.3/libc) >= 0.3.2
Requires:       crate(objc2-io-kit-0.3/std) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-io-kit) = %{version}

%description -n %{name}+objc2-io-kit
This metapackage enables feature "objc2-io-kit" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.190
Requires:       crate(serde-1/derive) >= 1.0.190
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/objc2-io-kit) = %{version}
Requires:       crate(memchr-2/default) >= 2.5.0
Requires:       crate(ntapi-0.4/default) >= 0.4.0
Requires:       crate(objc2-core-foundation-0.3/cfbase) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfstring) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/std) >= 0.3.2
Requires:       crate(windows-0.62/wdk-system-systeminformation) >= 0.62.0
Requires:       crate(windows-0.62/wdk-system-systemservices) >= 0.62.0
Requires:       crate(windows-0.62/wdk-system-threading) >= 0.62.0
Requires:       crate(windows-0.62/win32-foundation) >= 0.62.0
Requires:       crate(windows-0.62/win32-security-authorization) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-diagnostics-debug) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-diagnostics-toolhelp) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-kernel) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-memory) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-performance) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-power) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-processstatus) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-registry) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-remotedesktop) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-systeminformation) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-systemservices) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-threading) >= 0.62.0
Requires:       crate(windows-0.62/win32-ui-shell) >= 0.62.0
Provides:       crate(%{pkgname}/system) = %{version}

%description -n %{name}+system
This metapackage enables feature "system" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+user
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "user"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-0.62/win32-foundation) >= 0.62.0
Requires:       crate(windows-0.62/win32-networkmanagement-netmanagement) >= 0.62.0
Requires:       crate(windows-0.62/win32-security) >= 0.62.0
Requires:       crate(windows-0.62/win32-security-authentication-identity) >= 0.62.0
Requires:       crate(windows-0.62/win32-security-authorization) >= 0.62.0
Provides:       crate(%{pkgname}/user) = %{version}

%description -n %{name}+user
This metapackage enables feature "user" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows
Summary:        Get system information such as processes, CPUs, disks, components and networks - feature "windows"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-0.62/default) >= 0.62.0
Provides:       crate(%{pkgname}/windows) = %{version}

%description -n %{name}+windows
This metapackage enables feature "windows" for the Rust sysinfo crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
