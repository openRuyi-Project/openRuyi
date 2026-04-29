# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yoke
%global full_version 0.8.2
%global pkgname yoke-0.8

Name:           rust-yoke-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "yoke"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:abe8c5fda708d9ca3df187cae8bfb9ceda00dd96231bed36e445a1a48e66f9ca
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(stable-deref-trait-1.0) >= 1.2.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/serde)

%description
Source code for takopackized Rust crate "yoke"

%package     -n %{name}+alloc
Summary:        Abstraction allowing borrowed data to be carried along with the backing data it borrows from - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(stable-deref-trait-1.0/alloc) >= 1.2.1
Requires:       crate(zerofrom-0.1/alloc) >= 0.1.7
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust yoke crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Abstraction allowing borrowed data to be carried along with the backing data it borrows from - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/zerofrom)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust yoke crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Abstraction allowing borrowed data to be carried along with the backing data it borrows from - feature "derive"
Requires:       crate(%{pkgname})
Requires:       crate(yoke-derive-0.8) >= 0.8.2
Requires:       crate(zerofrom-0.1/derive) >= 0.1.7
Provides:       crate(%{pkgname}/derive)

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust yoke crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerofrom
Summary:        Abstraction allowing borrowed data to be carried along with the backing data it borrows from - feature "zerofrom"
Requires:       crate(%{pkgname})
Requires:       crate(zerofrom-0.1) >= 0.1.7
Provides:       crate(%{pkgname}/zerofrom)

%description -n %{name}+zerofrom
This metapackage enables feature "zerofrom" for the Rust yoke crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
