# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha1collisiondetection
%global full_version 0.3.4
%global pkgname sha1collisiondetection-0.3

Name:           rust-sha1collisiondetection-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "sha1collisiondetection"
License:        MIT
URL:            https://gitlab.com/sequoia-pgp/sha1collisiondetection
#!RemoteAsset:  sha256:1f606421e4a6012877e893c399822a4ed4b089164c5969424e1b9d1e66e6964b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(generic-array-0.12/default) >= 0.12.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "sha1collisiondetection"

%package     -n %{name}+clap
Summary:        SHA-1 hash function with collision detection and mitigation - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/derive) >= 4.0.0
Requires:       crate(clap-4/help) >= 4.0.0
Requires:       crate(clap-4/std) >= 4.0.0
Requires:       crate(clap-4/wrap-help) >= 4.0.0
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust sha1collisiondetection crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap-mangen
Summary:        SHA-1 hash function with collision detection and mitigation - feature "clap_mangen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-mangen-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/clap-mangen) = %{version}

%description -n %{name}+clap-mangen
This metapackage enables feature "clap_mangen" for the Rust sha1collisiondetection crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+const-oid
Summary:        SHA-1 hash function with collision detection and mitigation - feature "const-oid" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-oid-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/const-oid) = %{version}
Provides:       crate(%{pkgname}/oid) = %{version}

%description -n %{name}+const-oid
This metapackage enables feature "const-oid" for the Rust sha1collisiondetection crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "oid" feature.

%package     -n %{name}+default
Summary:        SHA-1 hash function with collision detection and mitigation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/digest-trait) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sha1collisiondetection crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        SHA-1 hash function with collision detection and mitigation - feature "digest" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/digest) = %{version}
Provides:       crate(%{pkgname}/digest-trait) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust sha1collisiondetection crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "digest-trait" feature.

%package     -n %{name}+std
Summary:        SHA-1 hash function with collision detection and mitigation - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/std) >= 0.10.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sha1collisiondetection crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
