# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-credentials
%global full_version 0.30.0
%global pkgname gix-credentials-0.30

Name:           rust-gix-credentials-0.30
Version:        0.30.0
Release:        %autorelease
Summary:        Rust crate "gix-credentials"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:0039dd3ac606dd80b16353a41b61fc237ca5cb8b612f67a9f880adfad4be4e05
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-command-0.6/default) >= 0.6.5
Requires:       crate(gix-config-value-0.15/default) >= 0.15.3
Requires:       crate(gix-date-0.10/default) >= 0.10.7
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-prompt-0.11/default) >= 0.11.2
Requires:       crate(gix-sec-0.12/default) >= 0.12.2
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(gix-url-0.32/default) >= 0.32.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-credentials"

%package     -n %{name}+document-features
Summary:        The gitoxide project to interact with git credentials helpers - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-credentials crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The gitoxide project to interact with git credentials helpers - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(bstr-1.0/serde) >= 1.12.1
Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-sec-0.12/serde) >= 0.12.2
Requires:       crate(serde-1.0/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-credentials crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
