# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name keyring
%global full_version 3.6.3
%global pkgname keyring-3

Name:           rust-keyring-3
Version:        3.6.3
Release:        %autorelease
Summary:        Rust crate "keyring"
License:        MIT OR Apache-2.0
URL:            https://github.com/hwchen/keyring-rs
#!RemoteAsset:  sha256:eebcc3aff044e5944a8fbaf69eb277d11986064cba30c468730e8b9909fb551c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.22
Requires:       crate(zeroize-1/default) >= 1.8.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "keyring"

%package     -n %{name}+apple-native
Summary:        Cross-platform library for managing passwords/credentials - feature "apple-native"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(security-framework-2/default) >= 2.0.0
Requires:       crate(security-framework-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/apple-native) = %{version}

%description -n %{name}+apple-native
This metapackage enables feature "apple-native" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-io
Summary:        Cross-platform library for managing passwords/credentials - feature "async-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zbus-4/async-io) >= 4.0.0
Provides:       crate(%{pkgname}/async-io) = %{version}

%description -n %{name}+async-io
This metapackage enables feature "async-io" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-secret-service
Summary:        Cross-platform library for managing passwords/credentials - feature "async-secret-service"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(secret-service-4/default) >= 4.0.0
Requires:       crate(zbus-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/async-secret-service) = %{version}

%description -n %{name}+async-secret-service
This metapackage enables feature "async-secret-service" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-openssl
Summary:        Cross-platform library for managing passwords/credentials - feature "crypto-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dbus-secret-service-4.0.0-rc.1/crypto-openssl) >= 4.0.0-rc.1
Requires:       crate(dbus-secret-service-4.0.0-rc.2/crypto-openssl) >= 4.0.0-rc.2
Requires:       crate(dbus-secret-service-4/crypto-openssl) >= 4.0.1
Requires:       crate(secret-service-4/crypto-openssl) >= 4.0.0
Provides:       crate(%{pkgname}/crypto-openssl) = %{version}

%description -n %{name}+crypto-openssl
This metapackage enables feature "crypto-openssl" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-rust
Summary:        Cross-platform library for managing passwords/credentials - feature "crypto-rust"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dbus-secret-service-4.0.0-rc.1/crypto-rust) >= 4.0.0-rc.1
Requires:       crate(dbus-secret-service-4.0.0-rc.2/crypto-rust) >= 4.0.0-rc.2
Requires:       crate(dbus-secret-service-4/crypto-rust) >= 4.0.1
Requires:       crate(secret-service-4/crypto-rust) >= 4.0.0
Provides:       crate(%{pkgname}/crypto-rust) = %{version}

%description -n %{name}+crypto-rust
This metapackage enables feature "crypto-rust" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+linux-native
Summary:        Cross-platform library for managing passwords/credentials - feature "linux-native"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(linux-keyutils-0.2/default) >= 0.2.0
Requires:       crate(linux-keyutils-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/linux-native) = %{version}

%description -n %{name}+linux-native
This metapackage enables feature "linux-native" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+linux-native-async-persistent
Summary:        Cross-platform library for managing passwords/credentials - feature "linux-native-async-persistent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-secret-service) = %{version}
Requires:       crate(%{pkgname}/linux-native) = %{version}
Provides:       crate(%{pkgname}/linux-native-async-persistent) = %{version}

%description -n %{name}+linux-native-async-persistent
This metapackage enables feature "linux-native-async-persistent" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+linux-native-sync-persistent
Summary:        Cross-platform library for managing passwords/credentials - feature "linux-native-sync-persistent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/linux-native) = %{version}
Requires:       crate(%{pkgname}/sync-secret-service) = %{version}
Provides:       crate(%{pkgname}/linux-native-sync-persistent) = %{version}

%description -n %{name}+linux-native-sync-persistent
This metapackage enables feature "linux-native-sync-persistent" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl
Summary:        Cross-platform library for managing passwords/credentials - feature "openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-0.10/default) >= 0.10.66
Provides:       crate(%{pkgname}/openssl) = %{version}

%description -n %{name}+openssl
This metapackage enables feature "openssl" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sync-secret-service
Summary:        Cross-platform library for managing passwords/credentials - feature "sync-secret-service"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dbus-secret-service-4.0.0-rc.1/default) >= 4.0.0-rc.1
Requires:       crate(dbus-secret-service-4.0.0-rc.2/default) >= 4.0.0-rc.2
Requires:       crate(dbus-secret-service-4/default) >= 4.0.1
Provides:       crate(%{pkgname}/sync-secret-service) = %{version}

%description -n %{name}+sync-secret-service
This metapackage enables feature "sync-secret-service" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Cross-platform library for managing passwords/credentials - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zbus-4/tokio) >= 4.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored
Summary:        Cross-platform library for managing passwords/credentials - feature "vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dbus-secret-service-4.0.0-rc.1/vendored) >= 4.0.0-rc.1
Requires:       crate(dbus-secret-service-4.0.0-rc.2/vendored) >= 4.0.0-rc.2
Requires:       crate(dbus-secret-service-4/vendored) >= 4.0.1
Requires:       crate(openssl-0.10/vendored) >= 0.10.66
Provides:       crate(%{pkgname}/vendored) = %{version}

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows-native
Summary:        Cross-platform library for managing passwords/credentials - feature "windows-native"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(byteorder-1/default) >= 1.2.0
Requires:       crate(windows-sys-0.60/default) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-foundation) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-security-credentials) >= 0.60.0
Provides:       crate(%{pkgname}/windows-native) = %{version}

%description -n %{name}+windows-native
This metapackage enables feature "windows-native" for the Rust keyring crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
