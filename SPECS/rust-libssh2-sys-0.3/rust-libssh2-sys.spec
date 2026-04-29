# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.58
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(libz-sys-1.0/libc) >= 1.1.25
Requires:       crate(openssl-sys-0.9/default) >= 0.9.112
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Requires:       crate(vcpkg-0.2/default) >= 0.2.15
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "libssh2-sys"

%package     -n %{name}+openssl-sys
Summary:        Native bindings to the libssh2 library - feature "openssl-sys" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/default) >= 0.9.112
Provides:       crate(%{pkgname}/openssl-on-win32)
Provides:       crate(%{pkgname}/openssl-sys)

%description -n %{name}+openssl-sys
This metapackage enables feature "openssl-sys" for the Rust libssh2-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "openssl-on-win32" feature.

%package     -n %{name}+vendored-openssl
Summary:        Native bindings to the libssh2 library - feature "vendored-openssl"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/vendored) >= 0.9.112
Provides:       crate(%{pkgname}/vendored-openssl)

%description -n %{name}+vendored-openssl
This metapackage enables feature "vendored-openssl" for the Rust libssh2-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng-compat
Summary:        Native bindings to the libssh2 library - feature "zlib-ng-compat"
Requires:       crate(%{pkgname})
Requires:       crate(libz-sys-1.0/libc) >= 1.1.25
Requires:       crate(libz-sys-1.0/zlib-ng) >= 1.1.25
Provides:       crate(%{pkgname}/zlib-ng-compat)

%description -n %{name}+zlib-ng-compat
This metapackage enables feature "zlib-ng-compat" for the Rust libssh2-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
