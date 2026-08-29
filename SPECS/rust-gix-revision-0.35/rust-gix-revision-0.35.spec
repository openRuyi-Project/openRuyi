# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(gix-commitgraph-0.29/default) >= 0.29.0
Requires:       crate(gix-date-0.10/default) >= 0.10.3
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-object-0.50/default) >= 0.50.0
Requires:       crate(gix-revwalk-0.21/default) >= 0.21.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "gix-revision"

%package     -n %{name}+default
Summary:        The gitoxide project dealing with finding names for revisions and parsing specifications - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/describe) = %{version}
Requires:       crate(%{pkgname}/merge-base) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gix-revision crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+describe
Summary:        The gitoxide project dealing with finding names for revisions and parsing specifications - feature "describe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-hashtable-0.9/default) >= 0.9.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.13
Provides:       crate(%{pkgname}/describe) = %{version}

%description -n %{name}+describe
This metapackage enables feature "describe" for the Rust gix-revision crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        The gitoxide project dealing with finding names for revisions and parsing specifications - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-revision crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+merge-base
Summary:        The gitoxide project dealing with finding names for revisions and parsing specifications - feature "merge_base"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.13
Provides:       crate(%{pkgname}/merge-base) = %{version}

%description -n %{name}+merge-base
This metapackage enables feature "merge_base" for the Rust gix-revision crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The gitoxide project dealing with finding names for revisions and parsing specifications - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-hash-0.19/serde) >= 0.19.0
Requires:       crate(gix-object-0.50/serde) >= 0.50.0
Requires:       crate(serde-1/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-revision crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
