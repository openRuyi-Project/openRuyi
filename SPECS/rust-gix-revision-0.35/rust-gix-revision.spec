# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-revision
%global full_version 0.35.0
%global pkgname gix-revision-0.35

Name:           rust-gix-revision-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "gix-revision"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:f651f2b1742f760bb8161d6743229206e962b73d9c33c41f4e4aefa6586cbd3d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-commitgraph-0.29/default) >= 0.29.0
Requires:       crate(gix-date-0.10/default) >= 0.10.7
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-object-0.50/default) >= 0.50.2
Requires:       crate(gix-revwalk-0.21/default) >= 0.21.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "gix-revision"

%package     -n %{name}+default
Summary:        The gitoxide project dealing with finding names for revisions and parsing specifications - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/describe)
Requires:       crate(%{pkgname}/merge-base)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gix-revision crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+describe
Summary:        The gitoxide project dealing with finding names for revisions and parsing specifications - feature "describe"
Requires:       crate(%{pkgname})
Requires:       crate(gix-hashtable-0.9/default) >= 0.9.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Provides:       crate(%{pkgname}/describe)

%description -n %{name}+describe
This metapackage enables feature "describe" for the Rust gix-revision crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        The gitoxide project dealing with finding names for revisions and parsing specifications - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-revision crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+merge-base
Summary:        The gitoxide project dealing with finding names for revisions and parsing specifications - feature "merge_base"
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Provides:       crate(%{pkgname}/merge-base)

%description -n %{name}+merge-base
This metapackage enables feature "merge_base" for the Rust gix-revision crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The gitoxide project dealing with finding names for revisions and parsing specifications - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(gix-hash-0.19/serde) >= 0.19.0
Requires:       crate(gix-object-0.50/serde) >= 0.50.2
Requires:       crate(serde-1.0/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-revision crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
