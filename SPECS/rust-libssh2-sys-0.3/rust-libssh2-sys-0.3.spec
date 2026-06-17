# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libssh2-sys
%global full_version 0.3.1
%global pkgname libssh2-sys-0.3

Name:           rust-libssh2-sys-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "libssh2-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/ssh2-rs
#!RemoteAsset:  sha256:220e4f05ad4a218192533b300327f5150e809b54c4ec83b5a1d91833601811b9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.25
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(libz-sys-1/libc) >= 1.1.0
Requires:       crate(openssl-sys-0.9/default) >= 0.9.35
Requires:       crate(pkg-config-0.3) >= 0.3.11
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "libssh2-sys"

%package     -n %{name}+openssl-sys
Summary:        Native bindings to the libssh2 library - feature "openssl-sys" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-sys-0.9/default) >= 0.9.35
Provides:       crate(%{pkgname}/openssl-on-win32) = %{version}
Provides:       crate(%{pkgname}/openssl-sys) = %{version}

%description -n %{name}+openssl-sys
This metapackage enables feature "openssl-sys" for the Rust libssh2-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "openssl-on-win32" feature.

%package     -n %{name}+vendored-openssl
Summary:        Native bindings to the libssh2 library - feature "vendored-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-sys-0.9/vendored) >= 0.9.35
Provides:       crate(%{pkgname}/vendored-openssl) = %{version}

%description -n %{name}+vendored-openssl
This metapackage enables feature "vendored-openssl" for the Rust libssh2-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng-compat
Summary:        Native bindings to the libssh2 library - feature "zlib-ng-compat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libz-sys-1/libc) >= 1.1.0
Requires:       crate(libz-sys-1/zlib-ng) >= 1.1.0
Provides:       crate(%{pkgname}/zlib-ng-compat) = %{version}

%description -n %{name}+zlib-ng-compat
This metapackage enables feature "zlib-ng-compat" for the Rust libssh2-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
