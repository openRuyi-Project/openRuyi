# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-config
%global full_version 0.46.0
%global pkgname gix-config-0.46

Name:           rust-gix-config-0.46
Version:        0.46.0
Release:        %autorelease
Summary:        Rust crate "gix-config"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:5dfb898c5b695fd4acfc3c0ab638525a65545d47706064dcf7b5ead6cdb136c0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-config-value-0.15/default) >= 0.15.3
Requires:       crate(gix-features-0.43/default) >= 0.43.1
Requires:       crate(gix-glob-0.21/default) >= 0.21.0
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-ref-0.53/default) >= 0.53.1
Requires:       crate(gix-sec-0.12/default) >= 0.12.2
Requires:       crate(memchr-2.0/default) >= 2.8.0
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(unicode-bom-2.0/default) >= 2.0.3
Requires:       crate(winnow-0.7/default) >= 0.7.15
Requires:       crate(winnow-0.7/simd) >= 0.7.15
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-config"

%package     -n %{name}+document-features
Summary:        Git-config file parser and editor from the gitoxide project - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-config crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Git-config file parser and editor from the gitoxide project - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(bstr-1.0/serde) >= 1.12.1
Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-config-value-0.15/serde) >= 0.15.3
Requires:       crate(gix-glob-0.21/serde) >= 0.21.0
Requires:       crate(gix-ref-0.53/serde) >= 0.53.1
Requires:       crate(gix-sec-0.12/serde) >= 0.12.2
Requires:       crate(serde-1.0/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-config crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
