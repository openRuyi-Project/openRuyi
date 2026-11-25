# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name netdev
%global full_version 0.46.3
%global pkgname netdev-0.46

Name:           rust-netdev-0.46
Version:        0.46.3
Release:        %autorelease
Summary:        Rust crate "netdev"
License:        MIT
URL:            https://github.com/shellrow/netdev
#!RemoteAsset:  sha256:c3c52c2584961c68f5a6e3356797344061f818c93b8acc9cd6d7e284795e563e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(block2-0.6/default) >= 0.6.0
Requires:       crate(dispatch2-0.3/default) >= 0.3.0
Requires:       crate(dlopen2-0.8) >= 0.8.2
Requires:       crate(ipnet-2/default) >= 2.12.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(mac-addr-0.3/default) >= 0.3.0
Requires:       crate(netlink-packet-core-0.9/default) >= 0.9.0
Requires:       crate(netlink-packet-route-0.33/default) >= 0.33.0
Requires:       crate(netlink-sys-0.9/default) >= 0.9.0
Requires:       crate(objc2-core-foundation-0.3/default) >= 0.3.0
Requires:       crate(objc2-system-configuration-0.3/scnetworkconfiguration) >= 0.3.0
Requires:       crate(once-cell-1/default) >= 1.0.0
Requires:       crate(plist-1/default) >= 1.10.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-networkmanagement-iphelper) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-networkmanagement-ndis) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-libraryloader) >= 0.61.0

# Cargo resolves the jni-sys alias of the Android dependency offline.
Requires:       crate(jni-sys-0.4/default) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/gateway) = %{version}

%description
Source code for takopackized Rust crate "netdev"

%package     -n %{name}+android-extra
Summary:        Cross-platform library for enumerating network interfaces with metadata - feature "android-extra"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jni-0.21/default) >= 0.21.1
Requires:       crate(ndk-context-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}/android-extra) = %{version}

%description -n %{name}+android-extra
This metapackage enables feature "android-extra" for the Rust netdev crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+apple-system-configuration-extra
Summary:        Cross-platform library for enumerating network interfaces with metadata - feature "apple-system-configuration-extra"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-system-configuration-0.3/scdynamicstore) >= 0.3.0
Requires:       crate(objc2-system-configuration-0.3/scdynamicstorekey) >= 0.3.0
Requires:       crate(objc2-system-configuration-0.3/scnetworkconfiguration) >= 0.3.0
Requires:       crate(objc2-system-configuration-0.3/scpreferences) >= 0.3.0
Requires:       crate(objc2-system-configuration-0.3/scschemadefinitions) >= 0.3.0
Provides:       crate(%{pkgname}/apple-system-configuration-extra) = %{version}

%description -n %{name}+apple-system-configuration-extra
This metapackage enables feature "apple-system-configuration-extra" for the Rust netdev crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+apple-wifi-extra
Summary:        Cross-platform library for enumerating network interfaces with metadata - feature "apple-wifi-extra"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-0.6/default) >= 0.6.0
Requires:       crate(objc2-core-wlan-0.3/default) >= 0.3.0
Requires:       crate(objc2-foundation-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/apple-wifi-extra) = %{version}

%description -n %{name}+apple-wifi-extra
This metapackage enables feature "apple-wifi-extra" for the Rust netdev crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Cross-platform library for enumerating network interfaces with metadata - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/android-extra) = %{version}
Requires:       crate(%{pkgname}/apple-system-configuration-extra) = %{version}
Requires:       crate(%{pkgname}/gateway) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust netdev crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Cross-platform library for enumerating network interfaces with metadata - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipnet-2/serde) >= 2.12.0
Requires:       crate(mac-addr-0.3/serde) >= 0.3.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust netdev crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
