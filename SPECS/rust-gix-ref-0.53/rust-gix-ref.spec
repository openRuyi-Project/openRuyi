# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-ref
%global full_version 0.53.1
%global pkgname gix-ref-0.53

Name:           rust-gix-ref-0.53
Version:        0.53.1
Release:        %autorelease
Summary:        Rust crate "gix-ref"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:b966f578079a42f4a51413b17bce476544cca1cf605753466669082f94721758
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gix-actor-0.35/default) >= 0.35.6
Requires:       crate(gix-features-0.43/default) >= 0.43.1
Requires:       crate(gix-features-0.43/walkdir) >= 0.43.1
Requires:       crate(gix-fs-0.16/default) >= 0.16.1
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-lock-18.0/default) >= 18.0.0
Requires:       crate(gix-object-0.50/default) >= 0.50.2
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-tempfile-18.0) >= 18.0.0
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(gix-validate-0.10/default) >= 0.10.1
Requires:       crate(memmap2-0.9/default) >= 0.9.10
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(winnow-0.7/default) >= 0.7.15
Requires:       crate(winnow-0.7/simd) >= 0.7.15
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-ref"

%package     -n %{name}+document-features
Summary:        Handle git references - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-ref crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Handle git references - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(gix-actor-0.35/serde) >= 0.35.6
Requires:       crate(gix-hash-0.19/serde) >= 0.19.0
Requires:       crate(gix-object-0.50/serde) >= 0.50.2
Requires:       crate(serde-1.0/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-ref crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
