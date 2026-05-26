# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name built
%global full_version 0.8.0
%global pkgname built-0.8

Name:           rust-built-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "built"
License:        MIT
URL:            https://github.com/lukaslueg/built
#!RemoteAsset:  sha256:f4ad8f11f288f48ca24471bbd51ac257aaeaaa07adae295591266b792902ae64
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(built) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "built"

%package     -n %{name}+cargo-lock
Summary:        Provides a crate with information from the time it was built - feature "cargo-lock"
Requires:       crate(%{pkgname})
Requires:       crate(cargo-lock-10.0) >= 10.0.0
Provides:       crate(%{pkgname}/cargo-lock)

%description -n %{name}+cargo-lock
This metapackage enables feature "cargo-lock" for the Rust built crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Provides a crate with information from the time it was built - feature "chrono"
Requires:       crate(%{pkgname})
Requires:       crate(chrono-0.4/clock) >= 0.4.0
Provides:       crate(%{pkgname}/chrono)

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust built crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dependency-tree
Summary:        Provides a crate with information from the time it was built - feature "dependency-tree"
Requires:       crate(%{pkgname})
Requires:       crate(cargo-lock-10.0/dependency-tree) >= 10.0.0
Provides:       crate(%{pkgname}/dependency-tree)

%description -n %{name}+dependency-tree
This metapackage enables feature "dependency-tree" for the Rust built crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+git2
Summary:        Provides a crate with information from the time it was built - feature "git2"
Requires:       crate(%{pkgname})
Requires:       crate(git2-0.20) >= 0.20.0
Provides:       crate(%{pkgname}/git2)

%description -n %{name}+git2
This metapackage enables feature "git2" for the Rust built crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+semver
Summary:        Provides a crate with information from the time it was built - feature "semver"
Requires:       crate(%{pkgname})
Requires:       crate(semver-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/semver)

%description -n %{name}+semver
This metapackage enables feature "semver" for the Rust built crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
