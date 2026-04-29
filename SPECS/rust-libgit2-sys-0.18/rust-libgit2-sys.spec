# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libgit2-sys
%global full_version 0.18.3+1.9.2
%global pkgname libgit2-sys-0.18

Name:           rust-libgit2-sys-0.18
Version:        0.18.3
Release:        %autorelease
Summary:        Rust crate "libgit2-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/git2-rs
#!RemoteAsset:  sha256:c9b3acc4b91781bb0b3386669d325163746af5f6e4f73e6d2d630e09a35f3487
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.58
Requires:       crate(cc-1.0/parallel) >= 1.2.58
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(libz-sys-1.0/libc) >= 1.1.25
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/vendored)

%description
Source code for takopackized Rust crate "libgit2-sys"

%package     -n %{name}+libssh2-sys
Summary:        Native bindings to the libgit2 library - feature "libssh2-sys" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(libssh2-sys-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}/libssh2-sys)
Provides:       crate(%{pkgname}/ssh)

%description -n %{name}+libssh2-sys
This metapackage enables feature "libssh2-sys" for the Rust libgit2-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ssh" feature.

%package     -n %{name}+openssl-sys
Summary:        Native bindings to the libgit2 library - feature "openssl-sys" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/default) >= 0.9.112
Provides:       crate(%{pkgname}/https)
Provides:       crate(%{pkgname}/openssl-sys)

%description -n %{name}+openssl-sys
This metapackage enables feature "openssl-sys" for the Rust libgit2-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "https" feature.

%package     -n %{name}+vendored-openssl
Summary:        Native bindings to the libgit2 library - feature "vendored-openssl"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/vendored) >= 0.9.112
Provides:       crate(%{pkgname}/vendored-openssl)

%description -n %{name}+vendored-openssl
This metapackage enables feature "vendored-openssl" for the Rust libgit2-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng-compat
Summary:        Native bindings to the libgit2 library - feature "zlib-ng-compat"
Requires:       crate(%{pkgname})
Requires:       crate(libssh2-sys-0.3/zlib-ng-compat) >= 0.3.1
Requires:       crate(libz-sys-1.0/libc) >= 1.1.25
Requires:       crate(libz-sys-1.0/zlib-ng) >= 1.1.25
Provides:       crate(%{pkgname}/zlib-ng-compat)

%description -n %{name}+zlib-ng-compat
This metapackage enables feature "zlib-ng-compat" for the Rust libgit2-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
