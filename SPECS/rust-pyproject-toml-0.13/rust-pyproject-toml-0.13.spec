# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyproject-toml
%global full_version 0.13.7
%global pkgname pyproject-toml-0.13

Name:           rust-pyproject-toml-0.13
Version:        0.13.7
Release:        %autorelease
Summary:        Rust crate "pyproject-toml"
License:        MIT
URL:            https://github.com/PyO3/pyproject-toml-rs.git
#!RemoteAsset:  sha256:f6d755483ad14b49e76713b52285235461a5b4f73f17612353e11a5de36a5fd2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indexmap-2/default) >= 2.6.0
Requires:       crate(indexmap-2/serde) >= 2.6.0
Requires:       crate(pep440-rs-0.7/default) >= 0.7.2
Requires:       crate(pep508-rs-0.9/default) >= 0.9.1
Requires:       crate(serde-1/default) >= 1.0.214
Requires:       crate(serde-1/derive) >= 1.0.214
Requires:       crate(thiserror-2/default) >= 2.0.12
Requires:       crate(toml-0.9/parse) >= 0.9.4
Requires:       crate(toml-0.9/serde) >= 0.9.4
Requires:       crate(toml-0.9/std) >= 0.9.4
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pyproject-toml"

%package     -n %{name}+glob
Summary:        Pyproject.toml parser in Rust - feature "glob" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glob-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}/glob) = %{version}
Provides:       crate(%{pkgname}/pep639-glob) = %{version}

%description -n %{name}+glob
This metapackage enables feature "glob" for the Rust pyproject-toml crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "pep639-glob" feature.

%package     -n %{name}+tracing
Summary:        Pyproject.toml parser in Rust - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pep440-rs-0.7/tracing) >= 0.7.2
Requires:       crate(pep508-rs-0.9/tracing) >= 0.9.1
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust pyproject-toml crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
